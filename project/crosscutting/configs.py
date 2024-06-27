from pydantic import BaseModel

from project.crosscutting.config_helper import main_settings

settings = main_settings()


class VideoConfig(BaseModel):
    output_folder: str
    extract_output_folder: str
    resize_output_folder: str
    frame_rate: int


class Config:
    Video = VideoConfig(**settings["Video"]) if "Video" in settings else None
