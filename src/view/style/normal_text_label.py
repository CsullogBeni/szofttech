from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class NormalTextLabel(QLabel):
    """
    Subclass of QLabel, that sets the text and the font style.
    """

    def __init__(self, text: str = '', font_size: int = 12):
        super(NormalTextLabel, self).__init__()
        self.setText(text)
        self.setFont(QFont('MS shell Dlg 2', font_size))
