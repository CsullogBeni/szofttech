from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class NormalTextLabel(QLabel):
    def __init__(self, text: str = '', font_size: int = 12):
        super(NormalTextLabel, self).__init__()
        self.setText(text)
        self.setFont(QFont('TBD', font_size))
