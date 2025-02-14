import sys, time, subprocess, re, signal, pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QFont, QPixmap, QPainter

pyautogui.PAUSE = 5

class Player(QThread):

    def __init__(self):
        super().__init__()
        self._stop_flag = False

    def run(self):

        def process_string(file_content):
            n = len(file_content)
            i = 0
            buffer = []
            plus_count = 0

            while i < n and not self._stop_flag:
                if file_content[i].isalpha():
                    buffer.append(file_content[i])
                    plus_count = 0
                    i += 1
                else:
                    if buffer:
                        pyautogui.hotkey(*(''.join(buffer)))
                        buffer = []

                    if file_content[i] == '=':
                        time.sleep(b)
                    elif file_content[i] == '-':
                        time.sleep(b*2)
                    elif file_content[i] == '+':
                        time.sleep(b*4)
                        plus_count += 1
                        if plus_count >= 44:
                            self._stop_flag = True
                    else:
                        plus_count = 0

                    i += 1

            if buffer and not self._stop_flag:
                pyautogui.hotkey(*(''.join(buffer)))
        
        time.sleep(5)
        time.sleep(20)
        with open(file_name,'r',encoding='utf-8') as file:
            global file_content
            file_content = file.read()
        lines = file_content.split('\n')

        def is_chinese(char):
            return '\u4e00' <= char <= '\u9fff'

        filtered_lines = [line for line in lines if not (line and is_chinese(line[0]))]
        file_content = '\n'.join(filtered_lines)

        file_content = file_content.replace("\n", "")
                
        process_string(file_content)

    def stop(self):
        self._stop_flag = True

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.player = None
        self.initUI()

    def initUI(self):

        self.setWindowTitle('原琴辅助演奏3.0-外置呱呱谱演奏')
        self.setGeometry(20, 60, 900, 550)
        
        self.yz2 = QPushButton('开始', self)
        self.yz2.move(160, 380)
        self.yz2.setFixedSize(250, 60)
        self.yz2.clicked.connect(self.yz2p)
        self.yz2.setFont(QFont("微软雅黑", 14))

        self.yz10 = QPushButton('停止', self)
        self.yz10.move(430, 380)
        self.yz10.setFixedSize(250, 60)
        self.yz10.clicked.connect(self.yz10p)
        self.yz10.setFont(QFont("微软雅黑", 14))

        self.yz3 = QPushButton('选择文件', self)
        self.yz3.move(500, 460)
        self.yz3.setFixedSize(180, 25)
        self.yz3.clicked.connect(self.yz3p)
        self.yz3.setFont(QFont("微软雅黑", 10))

        self.yz4 = QLabel('键入琴谱路径', self)
        self.yz4.move(160, 460)
        self.yz4.setFont(QFont("微软雅黑", 10))

        self.yz5 = QLabel('按键速度(呱呱谱)', self)
        self.yz5.move(160, 500)
        self.yz5.setFont(QFont("微软雅黑", 10))

        self.yz6 = QLabel('(支持浮点数、整数，单位ms)', self)
        self.yz6.move(500, 500)
        self.yz6.setFont(QFont("微软雅黑", 10))

        self.yz7 = QLineEdit(self)
        self.yz7.move(270, 460)
        self.yz7.setFixedSize(210, 25)

        self.yz8 = QLineEdit(self)
        self.yz8.move(300, 500)
        self.yz8.setFixedSize(180, 25)

        self.Label1 = QLabel('《原琴辅助演奏3.0-winx64》，正青春', self)
        self.Label1.move(80, 80)
        font = QFont("微软雅黑", 30)
        font.setBold(True)
        font.setItalic(True)
        self.Label1.setFont(font)

        self.Label2 = QLabel('外置呱呱谱演奏', self)
        self.Label2.move(160, 320)
        font = QFont("微软雅黑", 20)
        font.setBold(True)
        self.Label2.setFont(font)

    def yz2p(self):
        if not self.player or not self.player.isRunning():
            global file_name
            file_name = self.yz7.text()
            if not file_name:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setWindowTitle('提示')
                warning.setText('未选择文件路径！')
                warning.setStandardButtons(QMessageBox.Ok)
                warning.exec_()
            else:
                
                global b
                b = float(self.yz8.text())/1000 if self.yz8.text() else 0
                self.player = Player()
                self.player.start()
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Information)
                warning.setWindowTitle('提示')
                warning.setText('5秒后演奏开始！')
                warning.setStandardButtons(QMessageBox.Ok)
                warning.exec_()

    def yz10p(self):
        if self.player and self.player.isRunning():
        
            self.player.stop()

    def yz3p(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*);;文本文档 (*.txt)", options=options)
        self.yz7.setText(file_path)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
