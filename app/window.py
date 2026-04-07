from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QMainWindow, QWidget, QPushButton, QLineEdit, 
    QComboBox, QVBoxLayout, QHBoxLayout, QLabel)
from PyQt6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pathwise")
        self.setFixedSize(QSize(1280, 720))

        # --- Grid Panel (Left) ---
        self.gridPanel = QWidget()
        self.gridPanel.setFixedSize(QSize(980, 720))
        self.gridPanel.setAutoFillBackground(True)
        palette = self.gridPanel.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#CCCCCC"))

        # --- Config Panel (Right) ---
        self.configPanel = QWidget()
        self.configPanel.setFixedSize(QSize(300, 720))
        self.configPanel.setAutoFillBackground(True)
        palette = self.configPanel.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#646464"))
        self.configPanel.setPalette(palette)

        # --- Widgets inside config panel ---
        self.headerText = QLabel("Pathwise by TacticalNeko")

        self.generateButton = QPushButton("Generate")
        self.generateButton.setFixedSize(QSize(200, 40))
        self.generateButton.setStyleSheet("""
            QPushButton {
                background-color: #66FF00;
                color: #000000;
                border-radius: 10px;
                border: 2px solid #000000;
            }

            QPushButton:pressed {
                background-color: #22FFDD;
                }
            """)  

        self.gridSize = QLineEdit()
        self.gridSize.setPlaceholderText("Enter value...")
        self.gridSize.setFixedSize(QSize(200, 40))

        self.algorithmDropdown = QComboBox()
        self.algorithmDropdown.addItems(["A*", "Dijkstra", "BFS", "DFS"])
        self.algorithmDropdown.setFixedSize(QSize(200, 40))
                                   

        # --- Config panel layout ---
        configLayout = QVBoxLayout()
        configLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        configLayout.setSpacing(20)
        configLayout.addWidget(self.headerText)
        configLayout.addWidget(self.generateButton)
        configLayout.addWidget(self.gridSize)
        configLayout.addWidget(self.algorithmDropdown)
        self.configPanel.setLayout(configLayout)

        # --- Main layout ---
        mainLayout = QHBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.gridPanel)
        mainLayout.addWidget(self.configPanel)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)