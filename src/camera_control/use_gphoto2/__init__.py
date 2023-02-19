from enum import Enum
import gphoto2 as gp

from initialize_camera import initialize_camera
from capture import capture_preview, capture_jpeg, capture_raw, capture_jpeg_raw
from save_image import save_image

GP_ERROR = Enum("GP_ERROR", [])


class cameraControl:
    _gp_file = None
    _gp_type = None

    def __init__(self) -> None:
        self.cam = gp.Camera()

    def initialize_camera(self): initialize_camera(self)

    def capture_preview(self): capture_preview(self)
    def capture_jpeg(self): capture_jpeg(self)
    def capture_raw(self): capture_raw(self)
    def capture_jpeg_raw(self): capture_jpeg_raw(self)

    def save_image(self, fp): save_image(self, fp)
