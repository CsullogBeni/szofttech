from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont

class TitleTextLabel(QLabel):
    """
    It is a subclass of QLabel, that sets the text and the font style to represent a title.
    """
    def __init__(self, text: str = '', font_size: int = 12):
        super(TitleTextLabel, self).__init__()
        self.setText(text)
        self.setFont(QFont('MS shell Dlg 2', font_size))