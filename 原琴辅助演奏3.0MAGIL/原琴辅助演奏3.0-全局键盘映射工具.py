import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QFont

class KeyMapper(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('原琴辅助演奏3.0-全局键盘映射工具')
        self.setGeometry(20, 60, 900, 550)

        self.Label1 = QLabel('《原琴辅助演奏3.0-winx64》，正青春', self)
        self.Label1.move(80, 80)
        font = QFont("微软雅黑", 30)
        font.setBold(True)
        font.setItalic(True)
        self.Label1.setFont(font)

        self.Label2 = QLabel('外置全局键盘映射工具', self)
        self.Label2.move(160, 240)
        font = QFont("微软雅黑", 20)
        font.setBold(True)
        self.Label2.setFont(font)

        self.label = QLabel('输入要映射的键（例如：a -> b）', self)
        self.label.move(160, 280)
        self.label.setFont(QFont("微软雅黑", 10))

        self.input_key = QLineEdit(self)
        self.input_key.setPlaceholderText('输入原键')
        self.input_key.move(160, 300)
        self.input_key.setFixedSize(400, 30)

        self.output_key = QLineEdit(self)
        self.output_key.setPlaceholderText('输入目标键')
        self.output_key.move(160, 340)
        self.output_key.setFixedSize(400, 30)

        self.map_button = QPushButton('映射', self)
        self.map_button.clicked.connect(self.map_keys)
        self.map_button.move(160, 380)
        self.map_button.setFixedSize(190, 30)
        self.map_button.setFont(QFont("微软雅黑", 14))

        self.unmap_button = QPushButton('取消映射', self)
        self.unmap_button.clicked.connect(self.unmap_keys)
        self.unmap_button.move(370, 380)
        self.unmap_button.setFixedSize(190, 30)
        self.unmap_button.setFont(QFont("微软雅黑", 14))

    def map_keys(self):
        input_key = self.input_key.text().strip()
        output_key = self.output_key.text().strip()

        if not input_key or not output_key:
            QMessageBox.warning(self, '错误', '请输入原键和目标键')
            return

        try:
            keyboard.remap_key(input_key, output_key)
            QMessageBox.information(self, '成功', f'已映射 {input_key} -> {output_key}')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'映射失败: {str(e)}')

    def unmap_keys(self):
        input_key = self.input_key.text().strip()

        if not input_key:
            QMessageBox.warning(self, '错误', '请输入原键')
            return

        try:
            keyboard.unremap_key(input_key)
            QMessageBox.information(self, '成功', f'已取消映射 {input_key}')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'取消映射失败: {str(e)}')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mapper = KeyMapper()
    mapper.show()
    sys.exit(app.exec_())
