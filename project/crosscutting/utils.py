import logging
import os


def create_folder(folder_name: str) -> None:
    """Based on the folder name create the folder if doesn't exist.

    Args:
    ----
        folder_name (str): Folder name to create.
    """
    if not folder_name:
        logging.error("The folder name must be passed as an argument")
        raise TypeError

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
