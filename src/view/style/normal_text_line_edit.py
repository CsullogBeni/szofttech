from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont

class NormalTextLineEdit(QLineEdit):
    """
    Subclass of QLineEdit, that sets the text and the font style as needed.
    """
    def __init__(self, default_text: str = '', font_size: int = 12, max_width: int = 1100, arg_id: str = '',
                 arg_default: str = ''):
        super(NormalTextLineEdit, self).__init__()
        self.setText(default_text)
        self.setMaximumWidth(max_width)
        tool_tip = arg_id
        if arg_default:
            tool_tip += ('\nDefault: ' + str(arg_default))
        self.setToolTip(tool_tip)
        self.setFont(QFont('MS shell Dlg 2', font_size))