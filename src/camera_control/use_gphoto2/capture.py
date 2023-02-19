def _set_format(self, _format):
    pass


def _capture(self, _format):
    try:
        if (_format == "PREV"):
            pass
        if (_format == "JPEG"):
            self._gp_file = self.cam.capture(gp.GP_CAPTURE_IMAGE)
            self._gp_type = gp.GP_CAPTURE_IMAGE
        elif (_format == "RAW"):
            pass  # TODO
    except Exception() as e:
        pass


def capture_jpeg(self):
    self._capture("JPEG")


def capture_preview(self):
    return self._capture("PREV")


def capture_raw(self):
    pass


def capture_jpeg_raw(self):
    pass
