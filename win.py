
from PySide6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from collections import deque
import ui_plot

class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("实时 PID 曲线")
        self.resize(600, 400)
        
        # 类成员变量
        self.ui = ui_plot.Ui_plot_ui()  # 曲线窗口UI
        self.ui.setupUi(self)
        self.plot_widget = self.ui.curve_plot

        self.plot_widget.setBackground('w')
        self.plot_widget.showGrid(x=True, y=True)

        self.time_counter = 0
        self.time_data = deque(maxlen=200)
        self.target_data = deque(maxlen=200)
        self.current_data = deque(maxlen=200)

        self.curve_target = self.plot_widget.plot(pen=pg.mkPen('r', width=2), name="目标值")
        self.curve_current = self.plot_widget.plot(pen=pg.mkPen('b', width=2), name="实际值")

    def receive_data(self, target, current, info_str, err_str):
        self.time_counter += 1
        self.time_data.append(self.time_counter)
        self.target_data.append(target)
        self.current_data.append(current)

        if self.time_counter > 200:
            self.plot_widget.setXRange(self.time_counter - 200, self.time_counter, padding=0)
        else:
            self.plot_widget.setXRange(0, 200, padding=0)

        # 更新曲线
        self.curve_target.setData(self.time_data, self.target_data)
        self.curve_current.setData(self.time_data, self.current_data)
        
        # 更新信息
        self.ui.label_out.setText(info_str)
        self.ui.label_err.setText(err_str)
        
        