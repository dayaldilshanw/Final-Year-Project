import sys
import time
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class RealTimeDataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Real-Time Data Display")
        self.setGeometry(100, 100, 400, 150)

        self.layout = QVBoxLayout()

        self.temperature_label = QLabel("Temperature: N/A")
        self.humidity_label = QLabel("Humidity: N/A")

        self.layout.addWidget(self.temperature_label)
        self.layout.addWidget(self.humidity_label)

        self.setLayout(self.layout)

    def update_realtime_data(self):
        while True:
            # Replace these lines with your actual data retrieval logic
            temperature = random.uniform(20, 30)
            humidity = random.uniform(40, 60)

            self.temperature_label.setText(f"Temperature: {temperature:.2f} °C")
            self.humidity_label.setText(f"Humidity: {humidity:.2f} %")

            # Sleep for a short interval to simulate real-time updates
            time.sleep(2)

def main():
    app = QApplication(sys.argv)
    window = RealTimeDataApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
