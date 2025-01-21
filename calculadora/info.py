from  PySide6.QtWidgets import QLabel
from variables import SMALL_FONT_SIZE
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)


    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
       