import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
import uart
import win
import time
import ui_main

""" 
接收格式： (target,current)
发送格式： (t:_,p:_,i:_,d:_)
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("串口 PID 调参上位机")
        self.resize(300, 200)
        self.layout = QVBoxLayout(self)

        # 内部变量初始化
        self.plot_window = None 
        self.serial_thread = None
        self.last_time = time.time() # 计时
        self.receive_cnt = 0         # 接收累计计数（用来算频率）
        self.COUNT_PERIOD_CNT = 100  # 到达数目就计算此段时间的接收频率
        self.ui = ui_main.Ui_Form()
        self.ui.setupUi(self)
        self.auto_send_flag = False # 自动发送参数标志位

        # 绑定事件 展示图
        self.ui.btn_show_curve.clicked.connect(self.show_plot_window)
        # 连接串口
        self.ui.btn_connect.clicked.connect(self.start_serial)
        # 更新参数，发送
        self.ui.btn_click_update.clicked.connect(self.send_new_param)
        # 更新参数，自动，发送
        self.ui.btn_auto_update.clicked.connect(self.set_btn_auto_update)
        # PID改变参数
        self.btn_event_bind()
        # slider与lienEdit改变参数
        self.ui.slider_target.valueChanged.connect(self.slider_set_line_edit)
        self.ui.le_target.textChanged.connect(self.line_edit_set_slider)
        
    # 加减按键的绑定
    def btn_event_bind(self):
        self.ui.btn_kp_add.clicked.connect(lambda : self.custom_line_edit_calc(self.ui.le_kp,  self.ui.le_kp_jump, 1))
        self.ui.btn_ki_add.clicked.connect(lambda : self.custom_line_edit_calc(self.ui.le_ki,  self.ui.le_ki_jump, 1))
        self.ui.btn_kd_add.clicked.connect(lambda : self.custom_line_edit_calc(self.ui.le_kd,  self.ui.le_kd_jump, 1))
        self.ui.btn_kp_sub.clicked.connect(lambda : self.custom_line_edit_calc(self.ui.le_kp,  self.ui.le_kp_jump, -1))
        self.ui.btn_ki_sub.clicked.connect(lambda : self.custom_line_edit_calc(self.ui.le_ki,  self.ui.le_ki_jump, -1))
        self.ui.btn_kd_sub.clicked.connect(lambda : self.custom_line_edit_calc(self.ui.le_kd,  self.ui.le_kd_jump, -1))
    # 用正负数表示加减
    def custom_line_edit_calc(self, le_num1:QLineEdit, le_num2:QLineEdit, sign):
        try:
            num1 = float(le_num1.text())
            num2 = float(le_num2.text())
            final_num = 0.0
            if(sign > 0): final_num = num1 + num2
            else: final_num = num1 - num2
            le_num1.setText(f"{final_num:.2f}")
            self.auto_update_by_flag()
        except Exception as e:
            print(f"值更新错误：{e}")
            
    # 输入条控制滑条
    def line_edit_set_slider(self, text):
        self.ui.slider_target.blockSignals(True)
        try:
            if text == '': return   # 检查
            value = int(text)
            if(value > self.ui.slider_target.maximum()) : value = self.ui.slider_target.maximum()
            if(value < self.ui.slider_target.minimum()) : value = self.ui.slider_target.minimum()
            self.ui.slider_target.setValue(value)
            self.auto_update_by_flag()
        except Exception as e:
            print(f"值更新错误：{e}")
        self.ui.slider_target.blockSignals(False)
    # 滑条控制输入条
    def slider_set_line_edit(self, value):
        self.ui.le_target.blockSignals(True)
        self.ui.le_target.setText(str(value))
        self.ui.le_target.blockSignals(False)
        self.auto_update_by_flag()

    # 反转flag和禁用状态
    def set_btn_auto_update(self):
        if self.auto_send_flag:
            self.auto_send_flag = False
            self.ui.btn_click_update.setEnabled(True)
            self.ui.btn_click_update.setText("手动更新")
        else:
            self.auto_send_flag = True
            self.ui.btn_click_update.setEnabled(False)
            self.ui.btn_click_update.setText("实时更新中")

    # 显示曲线
    def show_plot_window(self):
        # 检查
        if self.plot_window is None:
            self.plot_window = win.PlotWindow()
        # 显示被隐藏的窗口
        self.plot_window.show()
        self.plot_window.activateWindow()

    # 打开串口
    def start_serial(self):
        # 检查
        if self.serial_thread is not None and self.serial_thread.isRunning():
            return 
        port = self.ui.le_port.text()
        baudrate = int(self.ui.le_baud.text())

        # 创建串口线程
        self.serial_thread = uart.SerialThread(port, baudrate)
        
        # 绑定线程的信号到处理函数
        self.serial_thread.error_signal.connect(self.handle_serial_error)
        
        # 窗口画线
        self.serial_thread.data_received_signal.connect(self.plot_receive_data)
        self.last_time = time.time()
        
        # 也接一个到主界面的状态栏更新一下
        self.serial_thread.data_received_signal.connect(lambda data_str: self.ui.label_cur_status.setText(f"状态: 接收中 ({data_str})"))

        # 3. 启动线程
        self.serial_thread.start()
        self.ui.label_cur_status.setText(f"状态: 已连接 {port}")

    # 关闭串口
    def stop_serial(self):
        if self.serial_thread is not None:
            self.serial_thread.stop()
            self.serial_thread = None # 丢弃
            self.ui.label_cur_status.setText("状态: 已断开")

    # 串口线程的错误显示
    def handle_serial_error(self, err_msg):
        self.ui.label_cur_status.setText(err_msg)
        print(f"错误：{err_msg}")
        self.stop_serial()
        
    # 曲线窗口接收到数据
    def plot_receive_data(self, data_str:str):
        try:
            # 计算时差
            self.receive_cnt += 1
            if self.receive_cnt >= self.COUNT_PERIOD_CNT:
                cur_time = time.time()
                gap = (cur_time - self.last_time) *1000
                print(f"间隔: {cur_time:.2f}s - {self.last_time:.2f}s = {gap:.2f}ms, 频率: {self.COUNT_PERIOD_CNT/(gap/1000):.2f} Hz")
                self.last_time = cur_time
                self.receive_cnt = 0
            
            # 做图
            if self.plot_window is None:
                return
            tar, cur = map(int, data_str.strip("()").split(","))
            self.plot_window.receive_data(tar, cur)
        except Exception as e:
            print(f"接收解析错误：{e}")
    
    # 发送更新参数
    def auto_update_by_flag(self):
        if self.auto_send_flag:
            self.send_new_param()
    def send_new_param(self):
        # 取值
        target = self.ui.le_target.text().strip()
        P = self.ui.le_kp.text().strip()
        I = self.ui.le_ki.text().strip()
        D = self.ui.le_kd.text().strip()
        # 拼接
        data_str:str = f"(t:{target},p:{P},i:{I},d:{D})\n"
        if self.serial_thread is not None and self.serial_thread.serial_port.is_open:
            self.serial_thread.send_data(data_str)
            print(f"已发送：{data_str.strip()}")
        print(f"未发送：{data_str.strip()}, 因为串口未打开")

    # 重写窗口关闭事件，保证安全退出
    def closeEvent(self, event):
        self.stop_serial()
        if self.plot_window:
            self.plot_window.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())