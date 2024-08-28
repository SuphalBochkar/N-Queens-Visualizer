import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
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

        self.setWindowTitle("N-Queen Visualizer Input")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label1 = QLabel("Enter the number of queens:")
        layout.addWidget(self.label1)

        self.numQueensInput = QLineEdit()
        layout.addWidget(self.numQueensInput)

        self.label2 = QLabel("Select the speed (ms):")
        layout.addWidget(self.label2)

        self.speedSlider = QSlider(Qt.Horizontal)
        self.speedSlider.setMinimum(10)
        self.speedSlider.setMaximum(200)
        self.speedSlider.setValue(100)
        layout.addWidget(self.speedSlider)

        self.speedLabel = QLabel("100 ms")
        layout.addWidget(self.speedLabel)

        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.startVisualization)
        layout.addWidget(self.startButton)

        self.setLayout(layout)

        self.speedSlider.valueChanged.connect(self.updateSpeedLabel)

    def updateSpeedLabel(self, value):
        self.speedLabel.setText(f"{value} ms")

    def startVisualization(self):
        self.numQueens = int(self.numQueensInput.text())
        self.speed = self.speedSlider.value()
        self.close()
        run_visualization(self.numQueens, self.speed)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    input_window = InputWindow()
    input_window.show()
    sys.exit(app.exec_())
