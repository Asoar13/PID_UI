
from PySide6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from collections import deque

class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("实时 PID 曲线")
        self.resize(600, 400)
        self.layout = QVBoxLayout(self)

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.showGrid(x=True, y=True)
        self.layout.addWidget(self.plot_widget)

        self.time_counter = 0
        self.time_data = deque(maxlen=200)
        self.target_data = deque(maxlen=200)
        self.current_data = deque(maxlen=200)

        self.curve_target = self.plot_widget.plot(pen=pg.mkPen('r', width=2), name="目标值")
        self.curve_current = self.plot_widget.plot(pen=pg.mkPen('b', width=2), name="实际值")

    def receive_data(self, target, current):
        self.time_counter += 1
        self.time_data.append(self.time_counter)
        self.target_data.append(target)
        self.current_data.append(current)

        if self.time_counter > 200:
            self.plot_widget.setXRange(self.time_counter - 200, self.time_counter, padding=0)
        else:
            self.plot_widget.setXRange(0, 200, padding=0)

        self.curve_target.setData(self.time_data, self.target_data)
        self.curve_current.setData(self.time_data, self.current_data)