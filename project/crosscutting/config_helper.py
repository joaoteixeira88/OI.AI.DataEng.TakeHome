from __future__ import annotations

import json
import logging
import os
from typing import Any, Iterable

MAIN_SETTINGS_PATH = os.getenv("MAIN_SETTINGS")


class ApplicationSettings:
    """
    A class which models this project's settings as an object,
    We can access the nested settings via attributes or and we can also
    iterate over this object's keys.
    """

    @staticmethod
    def create(dictionary: dict) -> ApplicationSettings:
        """
        A factory function which creates an instance of this class
        from a provided dictionary. Works for nested dictionaries.

        Args:
            dictionary: dict The dictionary to
            transform into ApplicationSettings
        Returns:
            ApplicationSettings An ApplicationSettings object.
        """
        # the object_hook will build a ApplicationSettings object as it is
        # transversing every leaf dictionary of the file.
        return json.loads(json.dumps(dictionary), object_hook=ApplicationSettings)

    def __init__(self, dictionary: dict):
        self.__dict__.update(dictionary)

    def keys(self) -> Iterable:
        """A function which returns the settings keys
        Returns:
            dict_keys object
        """
        return self.__dict__.keys()

    def __contains__(self, key: str):
        """
        Defines behavior for membership tests using in and not in.
        Returns:
            bool Wether key is in this object or not.
        """
        return key in self.__dict__

    def __iter__(self):
        """
        Returns an iterator which iterates over the settings keys
        Returns
            Iterator A generator object which iterates over the keys
        """
        yield from self.keys()

    def __getitem__(self, key: str):
        """
        Whenever we access an item with the `self[key]` notation,
        this is called.
        """
        return self.__dict__[key]

    def __getattr__(self, key: str):
        """
        Whenever we access an item with the `self.key` notation,
        this is called.
        """
        return self.__dict__[key]

    def __setitem__(self, key: str, value: Any):
        """
        Whenever we set an item with the `self[key] = ...` notation,
        this is called.
        """
        self.__dict__[key] = value

    def __setattr__(self, key: str, value: Any):
        """
        Whenever we set an item with the `self.key = ...` notation,
        this is called.
        """
        self.__dict__[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        A function which behaves as a normal dictionary
        get function.
        Args:
            key: str The key to get.
            default: Any The default value if key does not exist
        Returns:
            The value
        """
        return self[key] if key in self else default


def override_dict(first: dict, second: dict) -> None:
    """
    A function which takes a dictionary and merge_updates it
    over the second one. It modifies the first dictionary,
    IT DOES NOT RETURN A NEW ONE!
    Usage:
    ```
        first = {"a": {"b": 4, "c": 5}, "f": {"k": 3}}
        second = {"d": 6, "a": {"c": 8, "e": 9}, "j": 9}
        override_dict(first, second)
        assert first["a"]["c"] == second["a"]["c"]
        assert "j" in first
        assert "d" in first
    ```
    Args:
        first: dict The dictionary to override
        second: dict The dictionary which we
        wish to use to override the first one
    Returns
        None
    """
    for key, value_second in second.items():
        if key in first:
            value_first = first[key]
            if isinstance(value_first, type(value_second)):
                if isinstance(value_first, dict):
                    # if both are dictionaries we make a recursive call
                    override_dict(first[key], value_second)
                elif isinstance(value_first, (tuple, list)):
                    # we append if they are tuples or lists
                    first[key] = value_first + value_second
                else:
                    # if they are not "dict" types then we override
                    first[key] = value_second
            else:
                # we cannot merge different types so we override
                first[key] = value_second
        else:
            # we add a fresh new entry
            first[key] = value_second


def main_settings() -> ApplicationSettings:
    """
    A function which builds an ApplicationSettings object representing
    the current environment's application settings as an object.
    Returns:
        ApplicationSettings
    """
    if not MAIN_SETTINGS_PATH:
        raise ValueError("MAIN_SETTINGS ENV must exist.")

    with open(MAIN_SETTINGS_PATH, mode="r", encoding="utf-8") as file:
        main_data = json.load(file) or {}

    if os.path.exists(MAIN_SETTINGS_PATH):
        # the file is not mandatory. It is injected in the K8s environment
        # through the deployment process.
        with open(MAIN_SETTINGS_PATH, mode="r", encoding="utf-8") as file:
            override_data = json.load(file) or {}
        override_dict(main_data, override_data)
    else:
        logging.warning(
            "%s does not exist. Ignore this if it's not "
            "running in validation or rollout",
            MAIN_SETTINGS_PATH,
        )

    return ApplicationSettings.create(dictionary=main_data)
