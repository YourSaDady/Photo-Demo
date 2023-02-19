from camera_control import cameraControl
from user_interface import UI
from file_operation import photo_automation_module as PAM

"""
NOTE:   Modules should not import and directly call each other
        Instead use callback functions
"""

ui = UI()
ui.initialize_window()

# TODO: register callbacl

"""
TODO:   file automation: implement the following:
        - open(dir: string)->bool:  open and parse the context folder and return success
        - get_curr()->str:          return the file path of current pointer
        - prev()->bool:             modify the pointer to the previous file and return success
        - next()->bool:             modify the pointer to the next file and return success
        - head():                   modify the pointer to the head (one next to the newest one)
"""

ui.run()
