from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont

class NormalTextComboBox(QComboBox):
    """
    Subclass of QComboBox, that sets the text and the font style as needed.
    """
    def __init__(self, choices: list = None, arg_id: str = '', default: str = None, font_size: int = 12):
        super(NormalTextComboBox, self).__init__()