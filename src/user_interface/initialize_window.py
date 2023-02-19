import tkinter as tk
import tkinter.filedialog as filedialog
from ui_component import ui_select


def _update_preview(self):
    frame = self.callback_CAM_PREV()
    pass


def _select_context(self):
    self.context_folder = filedialog.askdirectory(
        parent=self.window, initialdir=self.context_folder, title="Context Folder")


def _with_draw(self):
    self.callback_FILE_PREV()

    fn = self.callback_FILE_CURR()
    if (ui_select(self, "Delete file " + fn + " ?", ["OK", "Cancel"])) == 0:
        self.callback_FILE_DEL(fn)
    else:
        self.callback_FILE_NEXT()


def initialize_window(self):
    self.window = tk.Tk()

    # preview callback
    self.window.after(100, lambda: _update_preview(self))

    # Open_context
    self.btn_contex_select = tk.Button(
        self.window, text="Open Context", command=lambda: _select_context(self))

    # Take photo
    self.btn_shoot = tk.Button(
        self.window, text="Shoot", command=self.callback_CAM_CAP)
    # TODO: key binding

    # save
    self.btn_save = tk.Button(self.window, text="Confirm", command=lambda: self.callback_CAM_SAVE(
        self.callback_FILE_CURR()
    ))
    self.callback_FILE_NEXT()

    # withdraw
    self.btn_withdraw = tk.Button(
        self.window, text="Withdraw", command=lambda: _with_draw(self))
