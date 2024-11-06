from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont

class NormalTextComboBox(QComboBox):
    """
    Subclass of QComboBox, that sets the text and the font style as needed.
    """
    def __init__(self, choices: list = None, arg_id: str = '', default: str = None, font_size: int = 12):
        super(NormalTextComboBox, self).__init__()
        if choices is None:
            choices = []
        self.addItem("")
        tool_tip = None
        if arg_id and default:
            tool_tip = arg_id + '\nDefault: ' + str(default)
        elif arg_id:
            tool_tip = arg_id
        for choice in choices:
            self.addItem(str(choice))
            if arg_id:
                tool_tip += f"\n{str(choice)}"
        if arg_id:
            self.setToolTip(tool_tip)
        self.setFont(QFont('MS shell Dlg 2', font_size))