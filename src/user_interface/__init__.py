from initialize_window import initialize_window


class UI:
    window = None  # TODO: Last opened dir

    # capture preview image     arg: None;      return: preview (PIL Image object)
    callback_CAM_PREV = None

    # capture image;            arg: None;      return: success / fail
    callback_CAM_CAP = None

    # save captured image;      arg: path;      return: success / fail
    callback_CAM_SAVE = None

    # file engine go to next;   arg: None;      return: None
    callback_FILE_NEXT = None

    # file engine go to prev;   arg: NOne;      return: None
    callback_FILE_PREV = None

    # get current file name;    arg: None;      return: absolute file path
    callback_FILE_CURR = None

    # delete file;              arg: file path; return: success / fail
    callback_FILE_DEL = None

    context_folder = None

    prev_frame = None

    def __init__(self) -> None:
        pass

    def register_callback(self, condition, function):
        if condition in self.callback_list:
            self.callback_list[condition] = function
        else:
            raise Exception()

    def initialize_window(self): initialize_window(self)

    def run(self): window.mainloop()
