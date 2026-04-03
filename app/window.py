from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QHBoxLayout # 
from PyQt6.QtGui import QColor, QPalette

# Reusable widget that renders as a solid colour block.
# QWidget doesn't fill its background by default, hence the palette workaround.
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pathwise")
        self.setFixedSize(QSize(1280, 720))

        layout = QHBoxLayout() # Tells the layout to be horizontal.

        self.gridPanel = Color("#CCCCCC")
        self.gridPanel.setFixedSize(QSize(980, 720))

        self.configPanel = Color("#646464")
        self.configPanel.setFixedSize(QSize(300, 720))

        layout.addWidget(self.gridPanel)
        layout.addWidget(self.configPanel)
    
        # QMainWindow won't accept a layout directly, needs a container widget.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)