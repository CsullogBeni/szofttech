from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class NormalTextButton(QPushButton):
    """
    Subclass of QPushButton, that sets the font, text and tool tip.
    """
    def __init__(self, text: str = '', tool_tip: str = None, font_size: int = 10):
        super(NormalTextButton, self).__init__()
        self.setText(text)
        if tool_tip:
            self.setToolTip(tool_tip)
        self.setFont(QFont('MS shell Dlg 2', font_size))
