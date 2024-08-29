import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSlider,
)
from PyQt5.QtCore import Qt
from visualizer import run_visualization


class InputWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("N-Queens Application")
        self.setGeometry(700, 400, 500, 300)

        # Create a main layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # Title label
        titleLabel = QLabel("N-Queens Problem Visualizer")
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setStyleSheet(
            "font-size: 18px; font-weight: bold; margin-bottom: 10px;"
        )
        mainLayout.addWidget(titleLabel)

        # Input for number of queens
        inputLayout = QHBoxLayout()
        queensLabel = QLabel("Number of Queens:")
        queensLabel.setStyleSheet("font-size: 14px;")
        inputLayout.addWidget(queensLabel)

        self.numQueensInput = QLineEdit()
        self.numQueensInput.setPlaceholderText("Enter a number")
        self.numQueensInput.setFixedWidth(200)
        self.numQueensInput.setStyleSheet("padding: 5px; font-size: 14px;")
        inputLayout.addWidget(self.numQueensInput)
        mainLayout.addLayout(inputLayout)

        # Speed slider for visualization speed
        speedLayout = QHBoxLayout()
        speedLabel = QLabel("Visualization Speed:")
        speedLabel.setStyleSheet("font-size: 14px;")
        speedLayout.addWidget(speedLabel)

        self.speedSlider = QSlider(Qt.Horizontal)
        self.speedSlider.setMinimum(10)
        self.speedSlider.setMaximum(200)
        self.speedSlider.setValue(100)
        self.speedSlider.setStyleSheet("padding: 5px;")
        speedLayout.addWidget(self.speedSlider)

        self.speedDisplayLabel = QLabel("100 ms")
        self.speedDisplayLabel.setStyleSheet("font-size: 14px; margin-left: 10px;")
        speedLayout.addWidget(self.speedDisplayLabel)
        mainLayout.addLayout(speedLayout)

        # Start button for visualization
        self.startButton = QPushButton("Start Visualization")
        self.startButton.setStyleSheet(
            "font-size: 16px; padding: 10px; background-color: #4CAF50; color: white;"
        )
        self.startButton.clicked.connect(self.startVisualization)
        mainLayout.addWidget(self.startButton)

        # Set main layout
        self.setLayout(mainLayout)

        # Connect slider value change to label update
        self.speedSlider.valueChanged.connect(self.updateSpeedLabel)

    def updateSpeedLabel(self):
        value = self.speedSlider.value()
        self.speedDisplayLabel.setText(f"{value} ms")

    def startVisualization(self):
        self.numQueens = int(self.numQueensInput.text())
        self.speed = self.speedSlider.value()
        self.close()
        run_visualization(self.numQueens, self.speed)
