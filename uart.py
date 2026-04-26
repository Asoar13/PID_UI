import serial
from PySide6.QtCore import QThread, Signal

class SerialThread(QThread):
    data_received_signal = Signal(bytes)
    error_signal = Signal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.running = False
        self.serial_port = None

    # 重写run
    def run(self):
        self.running = True
        try:
            # 初始化串口
            self.serial_port = serial.Serial(self.port, self.baudrate, timeout=1)
            
            # 接收数据循环
            while self.running:
                if self.serial_port.in_waiting > 0:
                    # 一行数据 (\n标志)
                    data = self.serial_port.read(self.serial_port.in_waiting)
                    if data:
                        self.data_received_signal.emit(data)

        except Exception as e:
            self.error_signal.emit(f"串口错误: {str(e)}")
            print(f"串口错误: {str(e)}")
        finally:
            # 退出循环后，确保关闭串口
            if self.serial_port and self.serial_port.is_open:
                self.serial_port.close()

    def stop(self):
        self.running = False
        self.wait() # 等待线程完全退出
        
    def send_data(self, data:str):
        if self.serial_port and self.serial_port.is_open:
            try:
                # 二进制发送
                self.serial_port.write(data.encode('utf-8'));
            except Exception as e:
                self.error_signal.emit(f"发送失败：{e}")
                print(f"发送失败：{e}")
            
        
        