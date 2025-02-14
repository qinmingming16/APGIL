import sys, pyautogui, time, subprocess, re, signal, pygame, webbrowser, ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QTextEdit,QFileDialog,QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QKeyEvent, QFont, QPixmap, QPainter

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 5

global score_type
score_type = 1

pygame.init()

pygame.mixer.set_num_channels(84)

sound1 = pygame.mixer.Sound(r'resource\Windsong_Lyre\Q.wav')
sound2 = pygame.mixer.Sound(r'resource\Windsong_Lyre\W.wav')
sound3 = pygame.mixer.Sound(r'resource\Windsong_Lyre\E.wav')
sound4 = pygame.mixer.Sound(r'resource\Windsong_Lyre\R.wav')
sound5 = pygame.mixer.Sound(r'resource\Windsong_Lyre\T.wav')
sound6 = pygame.mixer.Sound(r'resource\Windsong_Lyre\Y.wav')
sound7 = pygame.mixer.Sound(r'resource\Windsong_Lyre\U.wav')
sound8 = pygame.mixer.Sound(r'resource\Windsong_Lyre\A.wav')
sound9 = pygame.mixer.Sound(r'resource\Windsong_Lyre\S.wav')
sound10 = pygame.mixer.Sound(r'resource\Windsong_Lyre\D.wav')
sound11 = pygame.mixer.Sound(r'resource\Windsong_Lyre\F.wav')
sound12 = pygame.mixer.Sound(r'resource\Windsong_Lyre\G.wav')
sound13 = pygame.mixer.Sound(r'resource\Windsong_Lyre\H.wav')
sound14 = pygame.mixer.Sound(r'resource\Windsong_Lyre\J.wav')
sound15 = pygame.mixer.Sound(r'resource\Windsong_Lyre\Z.wav')
sound16 = pygame.mixer.Sound(r'resource\Windsong_Lyre\X.wav')
sound17 = pygame.mixer.Sound(r'resource\Windsong_Lyre\C.wav')
sound18 = pygame.mixer.Sound(r'resource\Windsong_Lyre\V.wav')
sound19 = pygame.mixer.Sound(r'resource\Windsong_Lyre\B.wav')
sound20 = pygame.mixer.Sound(r'resource\Windsong_Lyre\N.wav')
sound21 = pygame.mixer.Sound(r'resource\Windsong_Lyre\M.wav')

class Player(QThread):
    def __init__(self):
        super().__init__()
        self._stop_event = False

    def run(self):
        time.sleep(20)
        time.sleep(5)
        if file_name[-4:] == '.exe':
            try:
                result = subprocess.run(file_name, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print("琴谱执行成功", result.stdout)
            except Exception as e:
                print(f"发生错误: {e}")
        elif file_name[-3:] == '.py':
            try:
                result = subprocess.run(['python', file_name], capture_output=True, text=True)
                print("琴谱执行成功", result.stdout)
            except Exception as e:
                print(f"发生错误: {e}")
        elif file_name[-4:] == '.txt':
            with open(file_name,'r',encoding='utf-8') as file:
                global file_content
                file_content = file.read()
                file_content = file_content.replace("\n", "")
            try:
                if score_type == 1:
                    p = 0
                    length = len(file_content)

                    def remove_chars(s, chars_to_remove):
                        for char in chars_to_remove:
                            s = s.replace(char, '')
                        return s

                    while p < length and self._stop_event == False:
                        if p + 5 < length and file_content[p] == '&':

                            original_string = file_content[p+1:p+6]
                            chars_to_remove = "0/"
                            processed_string = remove_chars(original_string, chars_to_remove)
                            pyautogui.hotkey(*processed_string)
                            p += 6
                            time.sleep(b*c)
                        elif p + 4 < length:

                            original_string = file_content[p:p+5]
                            chars_to_remove = "0/"
                            processed_string = remove_chars(original_string, chars_to_remove)
                            pyautogui.hotkey(*processed_string)
                            p += 5
                            time.sleep(b)
                        else:
                            print('琴谱执行成功')
                            break

            except Exception as e:
                print(f"发生错误: {e}")

    def stop(self):
        self._stop_event = True

class Worker(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._stop_flag = False

    def run(self):
        try:
            time.sleep(20)
            time.sleep(5)

            while QApplication.hasPendingEvents():
                QApplication.processEvents()

            if score_type == 2:
                def store_string(line):
                    stored_string = line.split('/')
                    del stored_string[-1]
                    return stored_string

                def separate_string(stored_string, m):
                    count = 0
                    separated_string = []
                    bracket_content = []
                    in_brackets = False

                    i = 0
                    while i < len(stored_string):
                        char = stored_string[i]
                        if char == '(':
                            in_brackets = True
                            bracket_content = []
                        elif char == ')':
                            if in_brackets:
                                separated_string.append(('combo', ''.join(bracket_content)))
                                count += 1
                                in_brackets = False
                        else:
                            if in_brackets:
                                bracket_content.append(char)
                            else:
                                if char == ' ':
                                    separated_string.append(('single', 'space'))
                                    count += 1
                                elif char.strip():
                                    separated_string.append(('single', char))
                                    count += 1
                        i += 1

                    if count == 0:
                        return

                    n = round(m/count, 2) if count > 0 else m

                    for key_type, key_value in separated_string:
                        if self._stop_flag:
                            return

                        try:
                            if key_type == 'combo':
                                
                                keys = [k.lower() for k in key_value]
                                pyautogui.hotkey(*keys)
                            else:
                                if key_value == 'space':
                                    pyautogui.press('space')
                                else:
                                    pyautogui.press(key_value.lower())

                            QApplication.processEvents()
                            time.sleep(n)

                        except Exception as e:
                            print(f"发生错误: {e}")

                lines = file_content.splitlines()
                current_m = None

                for line in lines:
                    if self._stop_flag:
                        break

                    if not line.strip():
                        continue

                    if re.match(r'^-?\d*\.?\d+$', line.strip()):
                        current_m = float(line)
                        continue

                    if current_m is not None:
                        stored_strings = store_string(line)
                        for stored_string in stored_strings:
                            if self._stop_flag:
                                break
                            separate_string(stored_string, current_m)

                self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))

    def stop(self):
        self._stop_flag = True
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resource\\background\\秦明明16.png'))
        self.worker = None
        self.player = None
        self.score_type = 1
        with open('resource\\setting\\background.txt', 'r', encoding='utf-8') as file:
            background_read = file.read()
        self.background = background_read
        global listening
        listening = False
        self.initUI()

    def initUI(self):
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

        self.setWindowTitle('原琴辅助演奏3.0')
        self.setGeometry(20, 60, 1350, 785)

        self.Label1 = QLabel('《原琴辅助演奏3.0-winx64》，正青春', self)
        self.Label1.move(160, 80)
        font = QFont("微软雅黑", 30)
        font.setBold(True)
        font.setItalic(True)
        self.Label1.setFont(font)

        self.sy1 = QPushButton('使用说明', self)
        self.sy1.move(160, 300)
        self.sy1.setFixedSize(650, 60)
        self.sy1.clicked.connect(self.sy1p)
        self.sy1.setFont(QFont("微软雅黑", 14))

        self.sy2 = QPushButton('交流反馈', self)
        self.sy2.move(160, 380)
        self.sy2.setFixedSize(650, 60)
        self.sy2.clicked.connect(self.sy2p)
        self.sy2.setFont(QFont("微软雅黑", 14))

        self.sy3 = QPushButton('退出程序', self)
        self.sy3.move(160, 460)
        self.sy3.setFixedSize(650, 60)
        self.sy3.clicked.connect(self.sy3p)
        self.sy3.setFont(QFont("微软雅黑", 14))

        self.dh1 = QPushButton('首页', self)
        self.dh1.move(40, 200)
        self.dh1.setFixedSize(80, 80)
        self.dh1.clicked.connect(self.dh1p)
        self.dh1.setFont(QFont("微软雅黑", 10))

        self.dh2 = QPushButton('自动演奏', self)
        self.dh2.move(40, 290)
        self.dh2.setFixedSize(80, 80)
        self.dh2.clicked.connect(self.dh2p)
        self.dh2.setFont(QFont("微软雅黑", 10))

        self.dh3 = QPushButton('曲谱编辑', self)
        self.dh3.move(40, 380)
        self.dh3.setFixedSize(80, 80)
        self.dh3.clicked.connect(self.dh3p)
        self.dh3.setFont(QFont("微软雅黑", 10))

        self.dh4 = QPushButton('模拟原琴', self)
        self.dh4.move(40, 470)
        self.dh4.setFixedSize(80, 80)
        self.dh4.clicked.connect(self.dh4p)
        self.dh4.setFont(QFont("微软雅黑", 10))

        self.dh5 = QPushButton('设置', self)
        self.dh5.move(40, 650)
        self.dh5.setFixedSize(80, 80)
        self.dh5.clicked.connect(self.dh5p)
        self.dh5.setFont(QFont("微软雅黑", 10))

        self.dh6 = QPushButton('''键盘映射
（外置）''', self)
        self.dh6.move(40, 560)
        self.dh6.setFixedSize(80, 80)
        self.dh6.clicked.connect(self.dh6p)
        self.dh6.setFont(QFont("微软雅黑", 10))

        self.yz1 = QPushButton('屏幕测量', self)
        self.yz1.move(160, 300)
        self.yz1.setFixedSize(520, 60)
        self.yz1.clicked.connect(self.yz1p)
        self.yz1.setFont(QFont("微软雅黑", 14))

        self.yz3 = QPushButton('选择文件', self)
        self.yz3.move(500, 460)
        self.yz3.setFixedSize(180, 25)
        self.yz3.clicked.connect(self.yz3p)
        self.yz3.setFont(QFont("微软雅黑", 10))

        self.yz4 = QLabel('键入琴谱路径', self)
        self.yz4.move(160, 460)
        self.yz4.setFont(QFont("微软雅黑", 10))

        self.yz5 = QLabel('键入音距(建筑谱)', self)
        self.yz5.move(160, 500)
        self.yz5.setFont(QFont("微软雅黑", 10))

        self.yz6 = QLabel('(支持浮点数、整数，单位s)', self)
        self.yz6.move(500, 500)
        self.yz6.setFont(QFont("微软雅黑", 10))

        self.yz7 = QLineEdit(self)
        self.yz7.move(270, 460)
        self.yz7.setFixedSize(210, 25)
        
        self.yz8 = QLineEdit(self)
        self.yz8.move(300, 500)
        self.yz8.setFixedSize(180, 25)

        self.yz9 = QPushButton('编译规则:建筑谱及可执行', self)
        self.yz9.move(720, 460)
        self.yz9.setFixedSize(200, 25)
        self.yz9.clicked.connect(self.yz9p)
        self.yz9.setFont(QFont("微软雅黑", 10))

        self.yz11 = QPushButton('切换到呱呱谱（外置）', self)
        self.yz11.move(720, 500)
        self.yz11.setFixedSize(200, 25)
        self.yz11.clicked.connect(self.yz11p)
        self.yz11.setFont(QFont("微软雅黑", 10))

        self.bj1 = QPushButton('追加新行', self)
        self.bj1.move(160, 460)
        self.bj1.setFixedSize(180, 50)
        self.bj1.clicked.connect(self.bj1p)
        self.bj1.setFont(QFont("微软雅黑", 14))

        self.bj2 = QPushButton('向行覆写', self)
        self.bj2.move(360, 460)
        self.bj2.setFixedSize(180, 50)
        self.bj2.clicked.connect(self.bj2p)
        self.bj2.setFont(QFont("微软雅黑", 14))

        self.bj3 = QLineEdit(self)
        self.bj3.move(160, 300)
        self.bj3.setFixedSize(60, 50)

        self.bj4 = QLineEdit(self)
        self.bj4.move(230, 300)
        self.bj4.setFixedSize(60, 50)

        self.bj5 = QLineEdit(self)
        self.bj5.move(300, 300)
        self.bj5.setFixedSize(60, 50)

        self.bj6 = QLineEdit(self)
        self.bj6.move(370, 300)
        self.bj6.setFixedSize(60, 50)

        self.bj7 = QLineEdit(self)
        self.bj7.move(440, 300)
        self.bj7.setFixedSize(60, 50)

        self.bj8 = QLineEdit(self)
        self.bj8.move(510, 300)
        self.bj8.setFixedSize(60, 50)

        self.bj9 = QLineEdit(self)
        self.bj9.move(580, 300)
        self.bj9.setFixedSize(60, 50)

        self.bj10 = QLineEdit(self)
        self.bj10.move(650, 300)
        self.bj10.setFixedSize(60, 50)

        self.bj11 = QLineEdit(self)
        self.bj11.move(720, 300)
        self.bj11.setFixedSize(60, 50)

        self.bj12 = QLineEdit(self)
        self.bj12.move(790, 300)
        self.bj12.setFixedSize(60, 50)

        self.bj13 = QLineEdit(self)
        self.bj13.move(860, 300)
        self.bj13.setFixedSize(60, 50)

        self.bj14 = QLineEdit(self)
        self.bj14.move(930, 300)
        self.bj14.setFixedSize(60, 50)

        self.bj15 = QLineEdit(self)
        self.bj15.move(1000, 300)
        self.bj15.setFixedSize(60, 50)

        self.bj16 = QLineEdit(self)
        self.bj16.move(1070, 300)
        self.bj16.setFixedSize(60, 50)

        self.bj17 = QLineEdit(self)
        self.bj17.move(1140, 300)
        self.bj17.setFixedSize(60, 50)

        self.bj18 = QLineEdit(self)
        self.bj18.move(1210, 300)
        self.bj18.setFixedSize(60, 50)

        self.bj19 = QLineEdit(self)
        self.bj19.move(160, 360)
        self.bj19.setFixedSize(60, 50)

        self.bj20 = QLineEdit(self)
        self.bj20.move(230, 360)
        self.bj20.setFixedSize(60, 50)

        self.bj21 = QLineEdit(self)
        self.bj21.move(300, 360)
        self.bj21.setFixedSize(60, 50)

        self.bj22 = QLineEdit(self)
        self.bj22.move(370, 360)
        self.bj22.setFixedSize(60, 50)

        self.bj23 = QLineEdit(self)
        self.bj23.move(440, 360)
        self.bj23.setFixedSize(60, 50)

        self.bj24 = QLineEdit(self)
        self.bj24.move(510, 360)
        self.bj24.setFixedSize(60, 50)

        self.bj25= QLineEdit(self)
        self.bj25.move(580, 360)
        self.bj25.setFixedSize(60, 50)

        self.bj26 = QLineEdit(self)
        self.bj26.move(650, 360)
        self.bj26.setFixedSize(60, 50)

        self.bj27 = QLineEdit(self)
        self.bj27.move(720, 360)
        self.bj27.setFixedSize(60, 50)

        self.bj28 = QLineEdit(self)
        self.bj28.move(790, 360)
        self.bj28.setFixedSize(60, 50)

        self.bj29 = QLineEdit(self)
        self.bj29.move(860, 360)
        self.bj29.setFixedSize(60, 50)

        self.bj30 = QLineEdit(self)
        self.bj30.move(930, 360)
        self.bj30.setFixedSize(60, 50)

        self.bj31 = QLineEdit(self)
        self.bj31.move(1000, 360)
        self.bj31.setFixedSize(60, 50)

        self.bj32 = QLineEdit(self)
        self.bj32.move(1070, 360)
        self.bj32.setFixedSize(60, 50)

        self.bj33 = QLineEdit(self)
        self.bj33.move(1140, 360)
        self.bj33.setFixedSize(60, 50)

        self.bj34 = QLineEdit(self)
        self.bj34.move(1210, 360)
        self.bj34.setFixedSize(60, 50)

        self.bj35 = QLineEdit(self)
        self.bj35.move(900, 475)
        self.bj35.setFixedSize(60, 25)

        self.bj36 = QLabel('覆写/追加行数', self)
        self.bj36.move(780, 475)
        self.bj36.setFont(QFont("微软雅黑", 10))

        self.bj37 = QPushButton('向行追加', self)
        self.bj37.move(560, 460)
        self.bj37.setFixedSize(180, 50)
        self.bj37.clicked.connect(self.bj37p)
        self.bj37.setFont(QFont("微软雅黑", 14))

        self.bj38 = QPushButton('建筑谱临时编辑', self)
        self.bj38.move(160, 220)
        self.bj38.setFixedSize(180, 50)
        self.bj38.clicked.connect(self.bj38p)
        self.bj38.setFont(QFont("微软雅黑", 14))

        self.bj39 = QPushButton('琴谱替换', self)
        self.bj39.move(360, 220)
        self.bj39.setFixedSize(180, 50)
        self.bj39.clicked.connect(self.bj39p)
        self.bj39.setFont(QFont("微软雅黑", 14))

        self.bj40 = QTextEdit(self)
        self.bj40.move(160, 300)
        self.bj40.setFixedSize(400, 400)
        self.bj40.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.bj40.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.bj40.setPlaceholderText('输入需替换的琴谱')

        self.bj41 = QTextEdit(self)
        self.bj41.move(600, 300)
        self.bj41.setFixedSize(400, 400)
        self.bj41.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.bj41.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.bj41.setPlaceholderText('替换结果')

        self.bj42 = QPushButton('替换', self)
        self.bj42.move(820, 220)
        self.bj42.setFixedSize(180, 50)
        self.bj42.clicked.connect(self.bj42p)
        self.bj42.setFont(QFont("微软雅黑", 14))

        self.bj43 = QLabel('替换规则：', self)
        self.bj43.move(1075, 230)
        self.bj43.setFont(QFont("微软雅黑", 10))

        self.bj44 = QPushButton('清空', self)
        self.bj44.move(620, 220)
        self.bj44.setFixedSize(180, 50)
        self.bj44.clicked.connect(self.bj44p)
        self.bj44.setFont(QFont("微软雅黑", 14))

        self.bj45 = QPushButton('清空', self)
        self.bj45.move(1075, 220)
        self.bj45.setFixedSize(180, 50)
        self.bj45.clicked.connect(self.bj45p)
        self.bj45.setFont(QFont("微软雅黑", 14))

        self.bj46 = QPushButton('选择文件', self)
        self.bj46.move(1195, 475)
        self.bj46.setFixedSize(80, 25)
        self.bj46.clicked.connect(self.bj46p)
        self.bj46.setFont(QFont("微软雅黑", 10))

        self.bj47 = QLineEdit(self)
        self.bj47.move(1080, 475)
        self.bj47.setFixedSize(100, 25)
        
        self.bj48 = QLabel('键入琴谱路径', self)
        self.bj48.move(970, 475)
        self.bj48.setFont(QFont("微软雅黑", 10))

        self.bj49 = QTextEdit(self)
        self.bj49.move(1050, 300)
        self.bj49.setFixedSize(200, 60)
        self.bj49.setPlaceholderText('输入需替换的字符')

        self.bj50 = QTextEdit(self)
        self.bj50.move(1050, 400)
        self.bj50.setFixedSize(200, 60)
        self.bj50.setPlaceholderText('输入替换为的字符')

        self.mn1 = QPushButton('', self)
        self.mn1.move(302, 489)
        self.mn1.setFixedSize(86, 86)
        self.mn1.clicked.connect(self.mn1p)

        self.mn2 = QPushButton('', self)
        self.mn2.move(427, 489)
        self.mn2.setFixedSize(86, 86)
        self.mn2.clicked.connect(self.mn2p)

        self.mn3 = QPushButton('', self)
        self.mn3.move(552, 489)
        self.mn3.setFixedSize(86, 86)
        self.mn3.clicked.connect(self.mn3p)

        self.mn4 = QPushButton('', self)
        self.mn4.move(677, 489)
        self.mn4.setFixedSize(86, 86)
        self.mn4.clicked.connect(self.mn4p)

        self.mn5 = QPushButton('', self)
        self.mn5.move(802, 489)
        self.mn5.setFixedSize(86, 86)
        self.mn5.clicked.connect(self.mn5p)

        self.mn6 = QPushButton('', self)
        self.mn6.move(927, 489)
        self.mn6.setFixedSize(86, 86)
        self.mn6.clicked.connect(self.mn6p)

        self.mn7 = QPushButton('', self)
        self.mn7.move(1052, 489)
        self.mn7.setFixedSize(86, 86)
        self.mn7.clicked.connect(self.mn7p)

        self.mn8 = QPushButton('', self)
        self.mn8.move(302, 591)
        self.mn8.setFixedSize(86, 86)
        self.mn8.clicked.connect(self.mn8p)

        self.mn9 = QPushButton('', self)
        self.mn9.move(427, 591)
        self.mn9.setFixedSize(86, 86)
        self.mn9.clicked.connect(self.mn9p)

        self.mn10 = QPushButton('', self)
        self.mn10.move(552, 591)
        self.mn10.setFixedSize(86, 86)
        self.mn10.clicked.connect(self.mn10p)

        self.mn11 = QPushButton('', self)
        self.mn11.move(677, 591)
        self.mn11.setFixedSize(86, 86)
        self.mn11.clicked.connect(self.mn11p)

        self.mn12 = QPushButton('', self)
        self.mn12.move(802, 591)
        self.mn12.setFixedSize(86, 86)
        self.mn12.clicked.connect(self.mn12p)

        self.mn13 = QPushButton('', self)
        self.mn13.move(927, 591)
        self.mn13.setFixedSize(86, 86)
        self.mn13.clicked.connect(self.mn13p)

        self.mn14 = QPushButton('', self)
        self.mn14.move(1052, 591)
        self.mn14.setFixedSize(86, 86)
        self.mn14.clicked.connect(self.mn14p)

        self.mn15 = QPushButton('', self)
        self.mn15.move(302, 693)
        self.mn15.setFixedSize(86, 86)
        self.mn15.clicked.connect(self.mn15p)

        self.mn16 = QPushButton('', self)
        self.mn16.move(427, 693)
        self.mn16.setFixedSize(86, 86)
        self.mn16.clicked.connect(self.mn16p)

        self.mn17 = QPushButton('', self)
        self.mn17.move(552, 693)
        self.mn17.setFixedSize(86, 86)
        self.mn17.clicked.connect(self.mn17p)

        self.mn18 = QPushButton('', self)
        self.mn18.move(677, 693)
        self.mn18.setFixedSize(86, 86)
        self.mn18.clicked.connect(self.mn18p)

        self.mn19 = QPushButton('', self)
        self.mn19.move(802, 693)
        self.mn19.setFixedSize(86, 86)
        self.mn19.clicked.connect(self.mn19p)

        self.mn20 = QPushButton('', self)
        self.mn20.move(927, 693)
        self.mn20.setFixedSize(86, 86)
        self.mn20.clicked.connect(self.mn20p)

        self.mn21 = QPushButton('', self)
        self.mn21.move(1052, 693)
        self.mn21.setFixedSize(86, 86)
        self.mn21.clicked.connect(self.mn21p)

        self.mn22 = QPushButton('  乐器选择∨', self)
        self.mn22.move(302, 300)
        self.mn22.setFixedSize(180, 50)
        self.mn22.clicked.connect(self.mn22p)
        self.mn22.setFont(QFont("微软雅黑", 14))

        self.mn24 = QPushButton('风物之诗琴', self)
        self.mn24.move(302, 350)
        self.mn24.setFixedSize(180, 25)
        self.mn24.clicked.connect(self.mn24p)
        self.mn24.setFont(QFont("微软雅黑", 10))

        self.mn25 = QPushButton('镜花之琴', self)
        self.mn25.move(302, 375)
        self.mn25.setFixedSize(180, 25)
        self.mn25.clicked.connect(self.mn25p)
        self.mn25.setFont(QFont("微软雅黑", 10))

        self.mn26 = QPushButton('老旧的诗琴', self)
        self.mn26.move(302, 400)
        self.mn26.setFixedSize(180, 25)
        self.mn26.clicked.connect(self.mn26p)
        self.mn26.setFont(QFont("微软雅黑", 10))

        self.mn27 = QPushButton('  乐器选择∧', self)
        self.mn27.move(302, 300)
        self.mn27.setFixedSize(180, 50)
        self.mn27.clicked.connect(self.mn27p)
        self.mn27.setFont(QFont("微软雅黑", 14))

        self.sz1 = QLabel('UI风格', self)
        self.sz1.move(160, 300)
        self.sz1.setFont(QFont("微软雅黑", 10))

        self.sz2 = QPushButton('  UI选择∨', self)
        self.sz2.move(220, 300)
        self.sz2.setFixedSize(180, 25)
        self.sz2.clicked.connect(self.sz2p)
        self.sz2.setFont(QFont("微软雅黑", 10))

        self.sz3 = QPushButton('风青', self)
        self.sz3.move(220, 325)
        self.sz3.setFixedSize(180, 25)
        self.sz3.clicked.connect(self.sz3p)
        self.sz3.setFont(QFont("微软雅黑", 10))

        self.sz4 = QPushButton('岩黄', self)
        self.sz4.move(220, 350)
        self.sz4.setFixedSize(180, 25)
        self.sz4.clicked.connect(self.sz4p)
        self.sz4.setFont(QFont("微软雅黑", 10))

        self.sz5 = QPushButton('雷紫', self)
        self.sz5.move(220, 375)
        self.sz5.setFixedSize(180, 25)
        self.sz5.clicked.connect(self.sz5p)
        self.sz5.setFont(QFont("微软雅黑", 10))

        self.sz6 = QPushButton('草绿', self)
        self.sz6.move(220, 400)
        self.sz6.setFixedSize(180, 25)
        self.sz6.clicked.connect(self.sz6p)
        self.sz6.setFont(QFont("微软雅黑", 10))

        self.sz7 = QPushButton('水蓝', self)
        self.sz7.move(220, 425)
        self.sz7.setFixedSize(180, 25)
        self.sz7.clicked.connect(self.sz7p)
        self.sz7.setFont(QFont("微软雅黑", 10))

        self.sz8 = QPushButton('火红', self)
        self.sz8.move(220, 450)
        self.sz8.setFixedSize(180, 25)
        self.sz8.clicked.connect(self.sz8p)
        self.sz8.setFont(QFont("微软雅黑", 10))

        self.sz9 = QPushButton('默认', self)
        self.sz9.move(220, 475)
        self.sz9.setFixedSize(180, 25)
        self.sz9.clicked.connect(self.sz9p)
        self.sz9.setFont(QFont("微软雅黑", 10))

        self.sz10 = QPushButton('  UI选择∧', self)
        self.sz10.move(220, 300)
        self.sz10.setFixedSize(180, 25)
        self.sz10.clicked.connect(self.sz10p)
        self.sz10.setFont(QFont("微软雅黑", 10))

        self.sz11 = QLabel('自动演奏', self)
        self.sz11.move(160, 520)
        self.sz11.setFont(QFont("微软雅黑", 10))

        self.sz12 = QLabel('建筑谱连音音距倍率', self)
        self.sz12.move(220, 520)
        self.sz12.setFont(QFont("微软雅黑", 10))

        self.sz13 = QLineEdit(self)
        self.sz13.move(340, 520)
        self.sz13.setFixedSize(60, 25)

        self.sz14 = QPushButton('保存', self)
        self.sz14.move(410, 520)
        self.sz14.setFixedSize(50, 25)
        self.sz14.clicked.connect(self.sz14p)
        self.sz14.setFont(QFont("微软雅黑", 10))

        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.yz9.setHidden(True)
        self.yz10.setHidden(True)
        self.yz11.setHidden(True)
        self.bj1.setHidden(True)
        self.bj2.setHidden(True)
        self.bj3.setHidden(True)
        self.bj4.setHidden(True)
        self.bj5.setHidden(True)
        self.bj6.setHidden(True)
        self.bj7.setHidden(True)
        self.bj8.setHidden(True)
        self.bj9.setHidden(True)
        self.bj10.setHidden(True)
        self.bj11.setHidden(True)
        self.bj12.setHidden(True)
        self.bj13.setHidden(True)
        self.bj14.setHidden(True)
        self.bj15.setHidden(True)
        self.bj16.setHidden(True)
        self.bj17.setHidden(True)
        self.bj18.setHidden(True)
        self.bj19.setHidden(True)
        self.bj20.setHidden(True)
        self.bj21.setHidden(True)
        self.bj22.setHidden(True)
        self.bj23.setHidden(True)
        self.bj24.setHidden(True)
        self.bj25.setHidden(True)
        self.bj26.setHidden(True)
        self.bj27.setHidden(True)
        self.bj28.setHidden(True)
        self.bj29.setHidden(True)
        self.bj30.setHidden(True)
        self.bj31.setHidden(True)
        self.bj32.setHidden(True)
        self.bj33.setHidden(True)
        self.bj34.setHidden(True)
        self.bj35.setHidden(True)
        self.bj36.setHidden(True)
        self.bj37.setHidden(True)
        self.bj38.setHidden(True)
        self.bj39.setHidden(True)
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj42.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj45.setHidden(True)
        self.bj46.setHidden(True)
        self.bj47.setHidden(True)
        self.bj48.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.mn1.setHidden(True)
        self.mn2.setHidden(True)
        self.mn3.setHidden(True)
        self.mn4.setHidden(True)
        self.mn5.setHidden(True)
        self.mn6.setHidden(True)
        self.mn7.setHidden(True)
        self.mn8.setHidden(True)
        self.mn9.setHidden(True)
        self.mn10.setHidden(True)
        self.mn11.setHidden(True)
        self.mn12.setHidden(True)
        self.mn13.setHidden(True)
        self.mn14.setHidden(True)
        self.mn15.setHidden(True)
        self.mn16.setHidden(True)
        self.mn17.setHidden(True)
        self.mn18.setHidden(True)
        self.mn19.setHidden(True)
        self.mn20.setHidden(True)
        self.mn21.setHidden(True)
        self.mn22.setHidden(True)
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.sz1.setHidden(True)
        self.sz2.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz10.setHidden(True)
        self.sz11.setHidden(True)
        self.sz12.setHidden(True)
        self.sz13.setHidden(True)
        self.sz14.setHidden(True)
        self.mn1.setIcon(QIcon('resource\Windsong_Lyre\A.png'))
        self.mn1.setIconSize(QSize(80, 80))
        self.mn2.setIcon(QIcon('resource\Windsong_Lyre\S.png'))
        self.mn2.setIconSize(QSize(80, 80))
        self.mn3.setIcon(QIcon('resource\Windsong_Lyre\D.png'))
        self.mn3.setIconSize(QSize(80, 80))
        self.mn4.setIcon(QIcon('resource\Windsong_Lyre\F.png'))
        self.mn4.setIconSize(QSize(80, 80))
        self.mn5.setIcon(QIcon('resource\Windsong_Lyre\G.png'))
        self.mn5.setIconSize(QSize(80, 80))
        self.mn6.setIcon(QIcon('resource\Windsong_Lyre\H.png'))
        self.mn6.setIconSize(QSize(80, 80))
        self.mn7.setIcon(QIcon('resource\Windsong_Lyre\J.png'))
        self.mn7.setIconSize(QSize(80, 80))
        self.mn8.setIcon(QIcon('resource\Windsong_Lyre\A.png'))
        self.mn8.setIconSize(QSize(80, 80))
        self.mn9.setIcon(QIcon('resource\Windsong_Lyre\S.png'))
        self.mn9.setIconSize(QSize(80, 80))
        self.mn10.setIcon(QIcon('resource\Windsong_Lyre\D.png'))
        self.mn10.setIconSize(QSize(80, 80))
        self.mn11.setIcon(QIcon('resource\Windsong_Lyre\F.png'))
        self.mn11.setIconSize(QSize(80, 80))
        self.mn12.setIcon(QIcon('resource\Windsong_Lyre\G.png'))
        self.mn12.setIconSize(QSize(80, 80))
        self.mn13.setIcon(QIcon('resource\Windsong_Lyre\H.png'))
        self.mn13.setIconSize(QSize(80, 80))
        self.mn14.setIcon(QIcon('resource\Windsong_Lyre\J.png'))
        self.mn14.setIconSize(QSize(80, 80))
        self.mn15.setIcon(QIcon('resource\Windsong_Lyre\A.png'))
        self.mn15.setIconSize(QSize(80, 80))
        self.mn16.setIcon(QIcon('resource\Windsong_Lyre\S.png'))
        self.mn16.setIconSize(QSize(80, 80))
        self.mn17.setIcon(QIcon('resource\Windsong_Lyre\D.png'))
        self.mn17.setIconSize(QSize(80, 80))
        self.mn18.setIcon(QIcon('resource\Windsong_Lyre\F.png'))
        self.mn18.setIconSize(QSize(80, 80))
        self.mn19.setIcon(QIcon('resource\Windsong_Lyre\G.png'))
        self.mn19.setIconSize(QSize(80, 80))
        self.mn20.setIcon(QIcon('resource\Windsong_Lyre\H.png'))
        self.mn20.setIconSize(QSize(80, 80))
        self.mn21.setIcon(QIcon('resource\Windsong_Lyre\J.png'))
        self.mn21.setIconSize(QSize(80, 80))

        QMessageBox.warning(self, '警告', '''禁止将软件本体用于任何商业用途
抵制无意义的原琴洗稿滥用
在向他人使用原琴辅助演奏3.0演奏时，建议进行声明''')

        self.update_background()

        with open('resource\setting\c.txt', 'r', encoding='utf-8') as file:
            c_read = file.read()
        self.sz13.setText(c_read)

    def yz2p(self):
        global c
        if self.sz13.text() != '':
            if  float(self.sz13.text()) >= 0:
                c = float(self.sz13.text())
            else:
                c = 0.6
        else:
            c = 0.6
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
            b = float(self.yz8.text()) if self.yz8.text() else 0
            if score_type == 2:
                file_name = self.yz7.text()
                if not self.worker or not self.worker.isRunning():
                    with open(file_name,'r',encoding='utf-8') as file:
                        global file_content
                        file_content = file.read()
                    self.worker = Worker()
                    self.worker.start()
                    warning = QMessageBox()
                    warning.setIcon(QMessageBox.Information)
                    warning.setWindowTitle('提示')
                    warning.setText('5秒后演奏开始！')
                    warning.setStandardButtons(QMessageBox.Ok)
                    warning.exec_()
                
            elif score_type == 1:
                if not self.player or not self.player.isRunning():
                    self.player = Player()
                    self.player.start()
                    warning = QMessageBox()
                    warning.setIcon(QMessageBox.Information)
                    warning.setWindowTitle('提示')
                    warning.setText('5秒后演奏开始！')
                    warning.setStandardButtons(QMessageBox.Ok)
                    warning.exec_()

    def yz10p(self):
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()
        if self.player and self.player.isRunning():
            self.player.stop()
            self.player.wait()

    def sy1p(self):
        url2 = r'https://www.bilibili.com/video/BV1MWKweoENK'
        webbrowser.open(url2)

    def sy2p(self):
        url2 = 'https://space.bilibili.com/1302740287'
        webbrowser.open(url2)

    def sy3p(self):
        sys.exit()

    def dh1p(self):
        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.yz9.setHidden(True)
        self.yz10.setHidden(True)
        self.yz11.setHidden(True)
        self.bj1.setHidden(True)
        self.bj2.setHidden(True)
        self.bj3.setHidden(True)
        self.bj4.setHidden(True)
        self.bj5.setHidden(True)
        self.bj6.setHidden(True)
        self.bj7.setHidden(True)
        self.bj8.setHidden(True)
        self.bj9.setHidden(True)
        self.bj10.setHidden(True)
        self.bj11.setHidden(True)
        self.bj12.setHidden(True)
        self.bj13.setHidden(True)
        self.bj14.setHidden(True)
        self.bj15.setHidden(True)
        self.bj16.setHidden(True)
        self.bj17.setHidden(True)
        self.bj18.setHidden(True)
        self.bj19.setHidden(True)
        self.bj20.setHidden(True)
        self.bj21.setHidden(True)
        self.bj22.setHidden(True)
        self.bj23.setHidden(True)
        self.bj24.setHidden(True)
        self.bj25.setHidden(True)
        self.bj26.setHidden(True)
        self.bj27.setHidden(True)
        self.bj28.setHidden(True)
        self.bj29.setHidden(True)
        self.bj30.setHidden(True)
        self.bj31.setHidden(True)
        self.bj32.setHidden(True)
        self.bj33.setHidden(True)
        self.bj34.setHidden(True)
        self.bj35.setHidden(True)
        self.bj36.setHidden(True)
        self.bj37.setHidden(True)
        self.bj38.setHidden(True)
        self.bj39.setHidden(True)
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj42.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj45.setHidden(True)
        self.bj46.setHidden(True)
        self.bj47.setHidden(True)
        self.bj48.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.mn1.setHidden(True)
        self.mn2.setHidden(True)
        self.mn3.setHidden(True)
        self.mn4.setHidden(True)
        self.mn5.setHidden(True)
        self.mn6.setHidden(True)
        self.mn7.setHidden(True)
        self.mn8.setHidden(True)
        self.mn9.setHidden(True)
        self.mn10.setHidden(True)
        self.mn11.setHidden(True)
        self.mn12.setHidden(True)
        self.mn13.setHidden(True)
        self.mn14.setHidden(True)
        self.mn15.setHidden(True)
        self.mn16.setHidden(True)
        self.mn17.setHidden(True)
        self.mn18.setHidden(True)
        self.mn19.setHidden(True)
        self.mn20.setHidden(True)
        self.mn21.setHidden(True)
        self.mn22.setHidden(True)
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.sz1.setHidden(True)
        self.sz2.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz10.setHidden(True)
        self.sz11.setHidden(True)
        self.sz12.setHidden(True)
        self.sz13.setHidden(True)
        self.sz14.setHidden(True)
        self.sy1.setHidden(False)
        self.sy2.setHidden(False)
        self.sy3.setHidden(False)
        global listening
        listening = False
        
    def dh2p(self):
        self.sy1.setHidden(True)
        self.sy2.setHidden(True)
        self.sy3.setHidden(True)
        self.bj1.setHidden(True)
        self.bj2.setHidden(True)
        self.bj3.setHidden(True)
        self.bj4.setHidden(True)
        self.bj5.setHidden(True)
        self.bj6.setHidden(True)
        self.bj7.setHidden(True)
        self.bj8.setHidden(True)
        self.bj9.setHidden(True)
        self.bj10.setHidden(True)
        self.bj11.setHidden(True)
        self.bj12.setHidden(True)
        self.bj13.setHidden(True)
        self.bj14.setHidden(True)
        self.bj15.setHidden(True)
        self.bj16.setHidden(True)
        self.bj17.setHidden(True)
        self.bj18.setHidden(True)
        self.bj19.setHidden(True)
        self.bj20.setHidden(True)
        self.bj21.setHidden(True)
        self.bj22.setHidden(True)
        self.bj23.setHidden(True)
        self.bj24.setHidden(True)
        self.bj25.setHidden(True)
        self.bj26.setHidden(True)
        self.bj27.setHidden(True)
        self.bj28.setHidden(True)
        self.bj29.setHidden(True)
        self.bj30.setHidden(True)
        self.bj31.setHidden(True)
        self.bj32.setHidden(True)
        self.bj33.setHidden(True)
        self.bj34.setHidden(True)
        self.bj35.setHidden(True)
        self.bj36.setHidden(True)
        self.bj37.setHidden(True)
        self.bj38.setHidden(True)
        self.bj39.setHidden(True)
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj42.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj45.setHidden(True)
        self.bj46.setHidden(True)
        self.bj47.setHidden(True)
        self.bj48.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.mn1.setHidden(True)
        self.mn2.setHidden(True)
        self.mn3.setHidden(True)
        self.mn4.setHidden(True)
        self.mn5.setHidden(True)
        self.mn6.setHidden(True)
        self.mn7.setHidden(True)
        self.mn8.setHidden(True)
        self.mn9.setHidden(True)
        self.mn10.setHidden(True)
        self.mn11.setHidden(True)
        self.mn12.setHidden(True)
        self.mn13.setHidden(True)
        self.mn14.setHidden(True)
        self.mn15.setHidden(True)
        self.mn16.setHidden(True)
        self.mn17.setHidden(True)
        self.mn18.setHidden(True)
        self.mn19.setHidden(True)
        self.mn20.setHidden(True)
        self.mn21.setHidden(True)
        self.mn22.setHidden(True)
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.sz1.setHidden(True)
        self.sz2.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz10.setHidden(True)
        self.sz11.setHidden(True)
        self.sz12.setHidden(True)
        self.sz13.setHidden(True)
        self.sz14.setHidden(True)
        self.yz1.setHidden(False)
        self.yz2.setHidden(False)
        self.yz3.setHidden(False)
        self.yz4.setHidden(False)
        self.yz5.setHidden(False)
        self.yz6.setHidden(False)
        self.yz7.setHidden(False)
        self.yz8.setHidden(False)
        self.yz9.setHidden(False)
        self.yz10.setHidden(False)
        self.yz11.setHidden(False)
        global listening
        listening = False

    def dh3p(self):
        self.sy1.setHidden(True)
        self.sy2.setHidden(True)
        self.sy3.setHidden(True)
        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.sy1.setHidden(True)
        self.sy2.setHidden(True)
        self.sy3.setHidden(True)
        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.yz9.setHidden(True)
        self.yz10.setHidden(True)
        self.yz11.setHidden(True)
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj45.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.mn1.setHidden(True)
        self.mn2.setHidden(True)
        self.mn3.setHidden(True)
        self.mn4.setHidden(True)
        self.mn5.setHidden(True)
        self.mn6.setHidden(True)
        self.mn7.setHidden(True)
        self.mn8.setHidden(True)
        self.mn9.setHidden(True)
        self.mn10.setHidden(True)
        self.mn11.setHidden(True)
        self.mn12.setHidden(True)
        self.mn13.setHidden(True)
        self.mn14.setHidden(True)
        self.mn15.setHidden(True)
        self.mn16.setHidden(True)
        self.mn17.setHidden(True)
        self.mn18.setHidden(True)
        self.mn19.setHidden(True)
        self.mn20.setHidden(True)
        self.mn21.setHidden(True)
        self.mn22.setHidden(True)
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.sz1.setHidden(True)
        self.sz2.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz10.setHidden(True)
        self.sz11.setHidden(True)
        self.sz12.setHidden(True)
        self.sz13.setHidden(True)
        self.sz14.setHidden(True)
        self.bj1.setHidden(False)
        self.bj2.setHidden(False)
        self.bj3.setHidden(False)
        self.bj4.setHidden(False)
        self.bj5.setHidden(False)
        self.bj6.setHidden(False)
        self.bj7.setHidden(False)
        self.bj8.setHidden(False)
        self.bj9.setHidden(False)
        self.bj10.setHidden(False)
        self.bj11.setHidden(False)
        self.bj12.setHidden(False)
        self.bj13.setHidden(False)
        self.bj14.setHidden(False)
        self.bj15.setHidden(False)
        self.bj16.setHidden(False)
        self.bj17.setHidden(False)
        self.bj18.setHidden(False)
        self.bj19.setHidden(False)
        self.bj20.setHidden(False)
        self.bj21.setHidden(False)
        self.bj22.setHidden(False)
        self.bj23.setHidden(False)
        self.bj24.setHidden(False)
        self.bj25.setHidden(False)
        self.bj26.setHidden(False)
        self.bj27.setHidden(False)
        self.bj28.setHidden(False)
        self.bj29.setHidden(False)
        self.bj30.setHidden(False)
        self.bj31.setHidden(False)
        self.bj32.setHidden(False)
        self.bj33.setHidden(False)
        self.bj34.setHidden(False)
        self.bj35.setHidden(False)
        self.bj36.setHidden(False)
        self.bj37.setHidden(False)
        self.bj38.setHidden(False)
        self.bj39.setHidden(False)
        self.bj45.setHidden(False)
        self.bj46.setHidden(False)
        self.bj47.setHidden(False)
        self.bj48.setHidden(False)
        global listening
        listening = False

    def dh4p(self):
        self.sy1.setHidden(True)
        self.sy2.setHidden(True)
        self.sy3.setHidden(True)
        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.yz9.setHidden(True)
        self.yz10.setHidden(True)
        self.yz11.setHidden(True)
        self.bj1.setHidden(True)
        self.bj2.setHidden(True)
        self.bj3.setHidden(True)
        self.bj4.setHidden(True)
        self.bj5.setHidden(True)
        self.bj6.setHidden(True)
        self.bj7.setHidden(True)
        self.bj8.setHidden(True)
        self.bj9.setHidden(True)
        self.bj10.setHidden(True)
        self.bj11.setHidden(True)
        self.bj12.setHidden(True)
        self.bj13.setHidden(True)
        self.bj14.setHidden(True)
        self.bj15.setHidden(True)
        self.bj16.setHidden(True)
        self.bj17.setHidden(True)
        self.bj18.setHidden(True)
        self.bj19.setHidden(True)
        self.bj20.setHidden(True)
        self.bj21.setHidden(True)
        self.bj22.setHidden(True)
        self.bj23.setHidden(True)
        self.bj24.setHidden(True)
        self.bj25.setHidden(True)
        self.bj26.setHidden(True)
        self.bj27.setHidden(True)
        self.bj28.setHidden(True)
        self.bj29.setHidden(True)
        self.bj30.setHidden(True)
        self.bj31.setHidden(True)
        self.bj32.setHidden(True)
        self.bj33.setHidden(True)
        self.bj34.setHidden(True)
        self.bj35.setHidden(True)
        self.bj36.setHidden(True)
        self.bj37.setHidden(True)
        self.bj38.setHidden(True)
        self.bj39.setHidden(True)
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj42.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj45.setHidden(True)
        self.bj46.setHidden(True)
        self.bj47.setHidden(True)
        self.bj48.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.sz1.setHidden(True)
        self.sz2.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz10.setHidden(True)
        self.sz11.setHidden(True)
        self.sz12.setHidden(True)
        self.sz13.setHidden(True)
        self.sz14.setHidden(True)
        self.mn1.setHidden(False)
        self.mn2.setHidden(False)
        self.mn3.setHidden(False)
        self.mn4.setHidden(False)
        self.mn5.setHidden(False)
        self.mn6.setHidden(False)
        self.mn7.setHidden(False)
        self.mn8.setHidden(False)
        self.mn9.setHidden(False)
        self.mn10.setHidden(False)
        self.mn11.setHidden(False)
        self.mn12.setHidden(False)
        self.mn13.setHidden(False)
        self.mn14.setHidden(False)
        self.mn15.setHidden(False)
        self.mn16.setHidden(False)
        self.mn17.setHidden(False)
        self.mn18.setHidden(False)
        self.mn19.setHidden(False)
        self.mn20.setHidden(False)
        self.mn21.setHidden(False)
        self.mn22.setHidden(False)
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        global listening
        listening = True

    def dh5p(self):
        self.sy1.setHidden(True)
        self.sy2.setHidden(True)
        self.sy3.setHidden(True)
        self.yz1.setHidden(True)
        self.yz2.setHidden(True)
        self.yz3.setHidden(True)
        self.yz4.setHidden(True)
        self.yz5.setHidden(True)
        self.yz6.setHidden(True)
        self.yz7.setHidden(True)
        self.yz8.setHidden(True)
        self.yz9.setHidden(True)
        self.yz10.setHidden(True)
        self.yz11.setHidden(True)
        self.bj1.setHidden(True)
        self.bj2.setHidden(True)
        self.bj3.setHidden(True)
        self.bj4.setHidden(True)
        self.bj5.setHidden(True)
        self.bj6.setHidden(True)
        self.bj7.setHidden(True)
        self.bj8.setHidden(True)
        self.bj9.setHidden(True)
        self.bj10.setHidden(True)
        self.bj11.setHidden(True)
        self.bj12.setHidden(True)
        self.bj13.setHidden(True)
        self.bj14.setHidden(True)
        self.bj15.setHidden(True)
        self.bj16.setHidden(True)
        self.bj17.setHidden(True)
        self.bj18.setHidden(True)
        self.bj19.setHidden(True)
        self.bj20.setHidden(True)
        self.bj21.setHidden(True)
        self.bj22.setHidden(True)
        self.bj23.setHidden(True)
        self.bj24.setHidden(True)
        self.bj25.setHidden(True)
        self.bj26.setHidden(True)
        self.bj27.setHidden(True)
        self.bj28.setHidden(True)
        self.bj29.setHidden(True)
        self.bj30.setHidden(True)
        self.bj31.setHidden(True)
        self.bj32.setHidden(True)
        self.bj33.setHidden(True)
        self.bj34.setHidden(True)
        self.bj35.setHidden(True)
        self.bj36.setHidden(True)
        self.bj37.setHidden(True)
        self.bj38.setHidden(True)
        self.bj39.setHidden(True)
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj42.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj45.setHidden(True)
        self.bj46.setHidden(True)
        self.bj47.setHidden(True)
        self.bj48.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.mn1.setHidden(True)
        self.mn2.setHidden(True)
        self.mn3.setHidden(True)
        self.mn4.setHidden(True)
        self.mn5.setHidden(True)
        self.mn6.setHidden(True)
        self.mn7.setHidden(True)
        self.mn8.setHidden(True)
        self.mn9.setHidden(True)
        self.mn10.setHidden(True)
        self.mn11.setHidden(True)
        self.mn12.setHidden(True)
        self.mn13.setHidden(True)
        self.mn14.setHidden(True)
        self.mn15.setHidden(True)
        self.mn16.setHidden(True)
        self.mn17.setHidden(True)
        self.mn18.setHidden(True)
        self.mn19.setHidden(True)
        self.mn20.setHidden(True)
        self.mn21.setHidden(True)
        self.mn22.setHidden(True)
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.sz1.setHidden(False)
        self.sz2.setHidden(False)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz10.setHidden(True)
        self.sz11.setHidden(False)
        self.sz12.setHidden(False)
        self.sz13.setHidden(False)
        self.sz14.setHidden(False)

    def dh6p(self):
        self.process = subprocess.Popen(['原琴辅助演奏3.0-全局键盘映射工具.exe'])

    def yz1p(self):
        size=pyautogui.size()
        size0=str(size)
        if size0 == 'Size(width=1440, height=900)':
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Information)
            warning.setWindowTitle('提示')
            warning.setText('屏幕分辨率正常！')
            warning.setStandardButtons(QMessageBox.Ok)
            warning.exec_()
        else:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle('提示')
            warning.setText('请调节屏幕分辨率至1440,900（如需使用模拟鼠标谱）！')
            warning.setStandardButtons(QMessageBox.Ok)
            warning.exec_()

    def yz3p(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*);;文本文档 (*.txt)", options=options)
        self.yz7.setText(file_path)

    def toggle_score_type(self):
        self.score_type = 2 if self.score_type == 1 else 1
        global score_type
        score_type = self.score_type
 
    def update_yz9_button(self):
        if self.score_type == 1:
            self.yz9.setText('编译规则:建筑谱及可执行')
        else:
            self.yz9.setText('编译规则:指尖/刻师傅谱')
 
    def yz9p(self):
        self.toggle_score_type()
        self.update_yz9_button()

    def yz11p(self):
        self.process = subprocess.Popen(['原琴辅助演奏3.0-外置呱呱谱演奏.exe'])

    def bj1p(self, file_path):
        pj1 = self.bj3.text()
        pj2 = self.bj4.text()
        pj3 = self.bj5.text()
        pj4 = self.bj6.text()
        pj5 = self.bj7.text()
        pj6 = self.bj8.text()
        pj7 = self.bj9.text()
        pj8 = self.bj10.text()
        pj9 = self.bj11.text()
        pj10 = self.bj12.text()
        pj11 = self.bj13.text()
        pj12 = self.bj14.text()
        pj13 = self.bj15.text()
        pj14 = self.bj16.text()
        pj15 = self.bj17.text()
        pj16 = self.bj18.text()
        pj17 = self.bj19.text()
        pj18 = self.bj20.text()
        pj19 = self.bj21.text()
        pj20 = self.bj22.text()
        pj21 = self.bj23.text()
        pj22 = self.bj24.text()
        pj23 = self.bj25.text()
        pj24 = self.bj26.text()
        pj25 = self.bj27.text()
        pj26 = self.bj28.text()
        pj27 = self.bj29.text()
        pj28 = self.bj30.text()
        pj29 = self.bj31.text()
        pj30 = self.bj32.text()
        pj31 = self.bj33.text()
        pj32 = self.bj34.text()

        if len(pj1) < 2:
            pj1 = pj1.ljust(2, '0')
        else:
            pj1 = pj1[:2]
        if len(pj2) < 2:
            pj2 = pj2.ljust(2, '0')
        else:
            pj2 = pj2[:2]
        if len(pj3) < 2:
            pj3 = pj3.ljust(2, '0')
        else:
            pj3 = pj3[:2]
        if len(pj4) < 2:
            pj4 = pj4.ljust(2, '0')
        else:
            pj4 = pj4[:2]
        if len(pj5) < 2:
            pj5 = pj5.ljust(2, '0')
        else:
            pj5 = pj5[:2]
        if len(pj6) < 2:
            pj6 = pj6.ljust(2, '0')
        else:
            pj6 = pj6[:2]
        if len(pj7) < 2:
            pj7 = pj7.ljust(2, '0')
        else:
            pj7 = pj7[:2]
        if len(pj8) < 2:
            pj8 = pj8.ljust(2, '0')
        else:
            pj8 = pj8[:2]
        if len(pj9) < 2:
            pj9 = pj9.ljust(2, '0')
        else:
            pj9 = pj9[:2]
        if len(pj10) < 2:
            pj10 = pj10.ljust(2, '0')
        else:
            pj10 = pj10[:2]
        if len(pj11) < 2:
            pj11 = pj11.ljust(2, '0')
        else:
            pj11 = pj11[:2]
        if len(pj12) < 2:
            pj12 = pj12.ljust(2, '0')
        else:
            pj12 = pj12[:2]
        if len(pj13) < 2:
            pj13 = pj13.ljust(2, '0')
        else:
            pj13 = pj13[:2]
        if len(pj14) < 2:
            pj14 = pj14.ljust(2, '0')
        else:
            pj14 = pj14[:2]
        if len(pj15) < 2:
            pj15 = pj15.ljust(2, '0')
        else:
            pj15 = pj15[:2]
        if len(pj16) < 2:
            pj16 = pj16.ljust(2, '0')
        else:
            pj16 = pj16[:2]
        if len(pj17) < 2:
            pj17 = pj17.ljust(2, '0')
        else:
            pj17 = pj17[:2]
        if len(pj18) < 2:
            pj18 = pj18.ljust(2, '0')
        else:
            pj18 = pj18[:2]
        if len(pj19) < 2:
            pj19 = pj19.ljust(2, '0')
        else:
            pj19 = pj19[:2]
        if len(pj20) < 2:
            pj20 = pj20.ljust(2, '0')
        else:
            pj20 = pj20[:2]
        if len(pj21) < 2:
            pj21 = pj21.ljust(2, '0')
        else:
            pj21 = pj21[:2]
        if len(pj22) < 2:
            pj22 = pj22.ljust(2, '0')
        else:
            pj22 = pj22[:2]
        if len(pj23) < 2:
            pj23 = pj23.ljust(2, '0')
        else:
            pj23 = pj23[:2]
        if len(pj24) < 2:
            pj24 = pj24.ljust(2, '0')
        else:
            pj24 = pj24[:2]
        if len(pj25) < 2:
            pj25 = pj25.ljust(2, '0')
        else:
            pj25 = pj25[:2]
        if len(pj26) < 2:
            pj26 = pj26.ljust(2, '0')
        else:
            pj26 = pj26[:2]
        if len(pj27) < 2:
            pj27 = pj27.ljust(2, '0')
        else:
            pj27 = pj27[:2]
        if len(pj28) < 2:
            pj28 = pj28.ljust(2, '0')
        else:
            pj28 = pj28[:2]
        if len(pj29) < 2:
            pj29 = pj29.ljust(2, '0')
        else:
            pj29 = pj29[:2]
        if len(pj30) < 2:
            pj30 = pj30.ljust(2, '0')
        else:
            pj30 = pj30[:2]
        if len(pj31) < 2:
            pj31 = pj31.ljust(2, '0')
        else:
            pj31 = pj31[:2]
        if len(pj32) < 2:
            pj32 = pj32.ljust(2, '0')
        else:
            pj32 = pj32[:2]

        compounded_string = pj1+pj17+'/'+pj2+pj18+'/'+pj3+pj19+'/'+pj4+pj20+'/'+pj5+pj21+'/'+pj6+pj22+'/'+pj7+pj23+'/'+pj8+pj24+'/'+pj9+pj25+'/'+pj10+pj26+'/'+pj11+pj27+'/'+pj12+pj28+'/'+pj13+pj29+'/'+pj14+pj30+'/'+pj15+pj31+'/'+pj16+pj32+'/'
        file_name = self.bj47.text()
        if not file_name:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle('提示')
            warning.setText('未选择文件路径！')
            warning.setStandardButtons(QMessageBox.Ok)
            warning.exec_()
        else:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.writelines('\n' + compounded_string)

    def bj2p(self):
        pj1 = self.bj3.text()
        pj2 = self.bj4.text()
        pj3 = self.bj5.text()
        pj4 = self.bj6.text()
        pj5 = self.bj7.text()
        pj6 = self.bj8.text()
        pj7 = self.bj9.text()
        pj8 = self.bj10.text()
        pj9 = self.bj11.text()
        pj10 = self.bj12.text()
        pj11 = self.bj13.text()
        pj12 = self.bj14.text()
        pj13 = self.bj15.text()
        pj14 = self.bj16.text()
        pj15 = self.bj17.text()
        pj16 = self.bj18.text()
        pj17 = self.bj19.text()
        pj18 = self.bj20.text()
        pj19 = self.bj21.text()
        pj20 = self.bj22.text()
        pj21 = self.bj23.text()
        pj22 = self.bj24.text()
        pj23 = self.bj25.text()
        pj24 = self.bj26.text()
        pj25 = self.bj27.text()
        pj26 = self.bj28.text()
        pj27 = self.bj29.text()
        pj28 = self.bj30.text()
        pj29 = self.bj31.text()
        pj30 = self.bj32.text()
        pj31 = self.bj33.text()
        pj32 = self.bj34.text()

        if len(pj1) < 2:
            pj1 = pj1.ljust(2, '0')
        else:
            pj1 = pj1[:2]
        if len(pj2) < 2:
            pj2 = pj2.ljust(2, '0')
        else:
            pj2 = pj2[:2]
        if len(pj3) < 2:
            pj3 = pj3.ljust(2, '0')
        else:
            pj3 = pj3[:2]
        if len(pj4) < 2:
            pj4 = pj4.ljust(2, '0')
        else:
            pj4 = pj4[:2]
        if len(pj5) < 2:
            pj5 = pj5.ljust(2, '0')
        else:
            pj5 = pj5[:2]
        if len(pj6) < 2:
            pj6 = pj6.ljust(2, '0')
        else:
            pj6 = pj6[:2]
        if len(pj7) < 2:
            pj7 = pj7.ljust(2, '0')
        else:
            pj7 = pj7[:2]
        if len(pj8) < 2:
            pj8 = pj8.ljust(2, '0')
        else:
            pj8 = pj8[:2]
        if len(pj9) < 2:
            pj9 = pj9.ljust(2, '0')
        else:
            pj9 = pj9[:2]
        if len(pj10) < 2:
            pj10 = pj10.ljust(2, '0')
        else:
            pj10 = pj10[:2]
        if len(pj11) < 2:
            pj11 = pj11.ljust(2, '0')
        else:
            pj11 = pj11[:2]
        if len(pj12) < 2:
            pj12 = pj12.ljust(2, '0')
        else:
            pj12 = pj12[:2]
        if len(pj13) < 2:
            pj13 = pj13.ljust(2, '0')
        else:
            pj13 = pj13[:2]
        if len(pj14) < 2:
            pj14 = pj14.ljust(2, '0')
        else:
            pj14 = pj14[:2]
        if len(pj15) < 2:
            pj15 = pj15.ljust(2, '0')
        else:
            pj15 = pj15[:2]
        if len(pj16) < 2:
            pj16 = pj16.ljust(2, '0')
        else:
            pj16 = pj16[:2]
        if len(pj17) < 2:
            pj17 = pj17.ljust(2, '0')
        else:
            pj17 = pj17[:2]
        if len(pj18) < 2:
            pj18 = pj18.ljust(2, '0')
        else:
            pj18 = pj18[:2]
        if len(pj19) < 2:
            pj19 = pj19.ljust(2, '0')
        else:
            pj19 = pj19[:2]
        if len(pj20) < 2:
            pj20 = pj20.ljust(2, '0')
        else:
            pj20 = pj20[:2]
        if len(pj21) < 2:
            pj21 = pj21.ljust(2, '0')
        else:
            pj21 = pj21[:2]
        if len(pj22) < 2:
            pj22 = pj22.ljust(2, '0')
        else:
            pj22 = pj22[:2]
        if len(pj23) < 2:
            pj23 = pj23.ljust(2, '0')
        else:
            pj23 = pj23[:2]
        if len(pj24) < 2:
            pj24 = pj24.ljust(2, '0')
        else:
            pj24 = pj24[:2]
        if len(pj25) < 2:
            pj25 = pj25.ljust(2, '0')
        else:
            pj25 = pj25[:2]
        if len(pj26) < 2:
            pj26 = pj26.ljust(2, '0')
        else:
            pj26 = pj26[:2]
        if len(pj27) < 2:
            pj27 = pj27.ljust(2, '0')
        else:
            pj27 = pj27[:2]
        if len(pj28) < 2:
            pj28 = pj28.ljust(2, '0')
        else:
            pj28 = pj28[:2]
        if len(pj29) < 2:
            pj29 = pj29.ljust(2, '0')
        else:
            pj29 = pj29[:2]
        if len(pj30) < 2:
            pj30 = pj30.ljust(2, '0')
        else:
            pj30 = pj30[:2]
        if len(pj31) < 2:
            pj31 = pj31.ljust(2, '0')
        else:
            pj31 = pj31[:2]
        if len(pj32) < 2:
            pj32 = pj32.ljust(2, '0')
        else:
            pj32 = pj32[:2]

        compounded_string = pj1+pj17+'/'+pj2+pj18+'/'+pj3+pj19+'/'+pj4+pj20+'/'+pj5+pj21+'/'+pj6+pj22+'/'+pj7+pj23+'/'+pj8+pj24+'/'+pj9+pj25+'/'+pj10+pj26+'/'+pj11+pj27+'/'+pj12+pj28+'/'+pj13+pj29+'/'+pj14+pj30+'/'+pj15+pj31+'/'+pj16+pj32+'/'
        file_name = self.bj47.text()
        appointed_line_number = int(self.bj35.text()) if self.bj35.text() else 0
        if not file_name:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle('提示')
            warning.setText('未选择文件路径！')
            warning.setStandardButtons(QMessageBox.Ok)
            warning.exec_()
        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_lines = file.readlines()
            if 1 <= appointed_line_number <= len(file_lines):
                file_lines[appointed_line_number - 1] = compounded_string + '\n'

                with open(file_name, 'w', encoding='utf-8') as file:
                    file.writelines(file_lines)
            else:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setWindowTitle('提示')
                warning.setText(f"行号 {appointed_line_number} 无效，文件只有 {len(file_lines)} 行。")
                warning.setStandardButtons(QMessageBox.Ok)
                warning.exec_()
                
    def bj37p(self):
        pj1 = self.bj3.text()
        pj2 = self.bj4.text()
        pj3 = self.bj5.text()
        pj4 = self.bj6.text()
        pj5 = self.bj7.text()
        pj6 = self.bj8.text()
        pj7 = self.bj9.text()
        pj8 = self.bj10.text()
        pj9 = self.bj11.text()
        pj10 = self.bj12.text()
        pj11 = self.bj13.text()
        pj12 = self.bj14.text()
        pj13 = self.bj15.text()
        pj14 = self.bj16.text()
        pj15 = self.bj17.text()
        pj16 = self.bj18.text()
        pj17 = self.bj19.text()
        pj18 = self.bj20.text()
        pj19 = self.bj21.text()
        pj20 = self.bj22.text()
        pj21 = self.bj23.text()
        pj22 = self.bj24.text()
        pj23 = self.bj25.text()
        pj24 = self.bj26.text()
        pj25 = self.bj27.text()
        pj26 = self.bj28.text()
        pj27 = self.bj29.text()
        pj28 = self.bj30.text()
        pj29 = self.bj31.text()
        pj30 = self.bj32.text()
        pj31 = self.bj33.text()
        pj32 = self.bj34.text()

        if len(pj1) < 2:
            pj1 = pj1.ljust(2, '0')
        else:
            pj1 = pj1[:2]
        if len(pj2) < 2:
            pj2 = pj2.ljust(2, '0')
        else:
            pj2 = pj2[:2]
        if len(pj3) < 2:
            pj3 = pj3.ljust(2, '0')
        else:
            pj3 = pj3[:2]
        if len(pj4) < 2:
            pj4 = pj4.ljust(2, '0')
        else:
            pj4 = pj4[:2]
        if len(pj5) < 2:
            pj5 = pj5.ljust(2, '0')
        else:
            pj5 = pj5[:2]
        if len(pj6) < 2:
            pj6 = pj6.ljust(2, '0')
        else:
            pj6 = pj6[:2]
        if len(pj7) < 2:
            pj7 = pj7.ljust(2, '0')
        else:
            pj7 = pj7[:2]
        if len(pj8) < 2:
            pj8 = pj8.ljust(2, '0')
        else:
            pj8 = pj8[:2]
        if len(pj9) < 2:
            pj9 = pj9.ljust(2, '0')
        else:
            pj9 = pj9[:2]
        if len(pj10) < 2:
            pj10 = pj10.ljust(2, '0')
        else:
            pj10 = pj10[:2]
        if len(pj11) < 2:
            pj11 = pj11.ljust(2, '0')
        else:
            pj11 = pj11[:2]
        if len(pj12) < 2:
            pj12 = pj12.ljust(2, '0')
        else:
            pj12 = pj12[:2]
        if len(pj13) < 2:
            pj13 = pj13.ljust(2, '0')
        else:
            pj13 = pj13[:2]
        if len(pj14) < 2:
            pj14 = pj14.ljust(2, '0')
        else:
            pj14 = pj14[:2]
        if len(pj15) < 2:
            pj15 = pj15.ljust(2, '0')
        else:
            pj15 = pj15[:2]
        if len(pj16) < 2:
            pj16 = pj16.ljust(2, '0')
        else:
            pj16 = pj16[:2]
        if len(pj17) < 2:
            pj17 = pj17.ljust(2, '0')
        else:
            pj17 = pj17[:2]
        if len(pj18) < 2:
            pj18 = pj18.ljust(2, '0')
        else:
            pj18 = pj18[:2]
        if len(pj19) < 2:
            pj19 = pj19.ljust(2, '0')
        else:
            pj19 = pj19[:2]
        if len(pj20) < 2:
            pj20 = pj20.ljust(2, '0')
        else:
            pj20 = pj20[:2]
        if len(pj21) < 2:
            pj21 = pj21.ljust(2, '0')
        else:
            pj21 = pj21[:2]
        if len(pj22) < 2:
            pj22 = pj22.ljust(2, '0')
        else:
            pj22 = pj22[:2]
        if len(pj23) < 2:
            pj23 = pj23.ljust(2, '0')
        else:
            pj23 = pj23[:2]
        if len(pj24) < 2:
            pj24 = pj24.ljust(2, '0')
        else:
            pj24 = pj24[:2]
        if len(pj25) < 2:
            pj25 = pj25.ljust(2, '0')
        else:
            pj25 = pj25[:2]
        if len(pj26) < 2:
            pj26 = pj26.ljust(2, '0')
        else:
            pj26 = pj26[:2]
        if len(pj27) < 2:
            pj27 = pj27.ljust(2, '0')
        else:
            pj27 = pj27[:2]
        if len(pj28) < 2:
            pj28 = pj28.ljust(2, '0')
        else:
            pj28 = pj28[:2]
        if len(pj29) < 2:
            pj29 = pj29.ljust(2, '0')
        else:
            pj29 = pj29[:2]
        if len(pj30) < 2:
            pj30 = pj30.ljust(2, '0')
        else:
            pj30 = pj30[:2]
        if len(pj31) < 2:
            pj31 = pj31.ljust(2, '0')
        else:
            pj31 = pj31[:2]
        if len(pj32) < 2:
            pj32 = pj32.ljust(2, '0')
        else:
            pj32 = pj32[:2]

        compounded_string = pj1+pj17+'/'+pj2+pj18+'/'+pj3+pj19+'/'+pj4+pj20+'/'+pj5+pj21+'/'+pj6+pj22+'/'+pj7+pj23+'/'+pj8+pj24+'/'+pj9+pj25+'/'+pj10+pj26+'/'+pj11+pj27+'/'+pj12+pj28+'/'+pj13+pj29+'/'+pj14+pj30+'/'+pj15+pj31+'/'+pj16+pj32+'/'
        file_name = self.bj47.text()
        appointed_line_number = int(self.bj35.text()) if self.bj35.text() else 0

        if not file_name:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle('提示')
            warning.setText('未选择文件路径！')
            warning.setStandardButtons(QMessageBox.Ok)
            warning.exec_()
        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_lines = file.readlines()
            if 1 <= appointed_line_number <= len(file_lines):
                file_lines[appointed_line_number - 1] = file_lines[appointed_line_number - 1].rstrip('\n') + compounded_string + '\n'

                with open(file_name, 'w', encoding='utf-8') as file:
                    file.writelines(file_lines)
            else:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setWindowTitle('提示')
                warning.setText(f"行号 {appointed_line_number} 无效，文件只有 {len(file_lines)} 行。")
                warning.setStandardButtons(QMessageBox.Ok)
                warning.exec_()

    def bj42p(self):
        replace_rule1 = self.bj49.toPlainText()
        replace_rule2 = self.bj50.toPlainText()
        string_to_replace = self.bj40.toPlainText()
        
        new_string = string_to_replace.replace(replace_rule1, replace_rule2)
        self.bj41.setText(new_string)

    def bj44p(self):
        self.bj40.clear()
        self.bj41.clear()
        self.bj49.clear()
        self.bj50.clear()

    def bj45p(self):
        self.bj3.clear()
        self.bj4.clear()
        self.bj5.clear()
        self.bj6.clear()
        self.bj7.clear()
        self.bj8.clear()
        self.bj9.clear()
        self.bj10.clear()
        self.bj11.clear()
        self.bj12.clear()
        self.bj13.clear()
        self.bj14.clear()
        self.bj15.clear()
        self.bj16.clear()
        self.bj17.clear()
        self.bj18.clear()
        self.bj19.clear()
        self.bj20.clear()
        self.bj21.clear()
        self.bj22.clear()
        self.bj23.clear()
        self.bj24.clear()
        self.bj25.clear()
        self.bj26.clear()
        self.bj27.clear()
        self.bj28.clear()
        self.bj29.clear()
        self.bj30.clear()
        self.bj31.clear()
        self.bj32.clear()
        self.bj33.clear()
        self.bj34.clear()

    def bj38p(self):
        self.bj40.setHidden(True)
        self.bj41.setHidden(True)
        self.bj42.setHidden(True)
        self.bj43.setHidden(True)
        self.bj44.setHidden(True)
        self.bj49.setHidden(True)
        self.bj50.setHidden(True)
        self.bj1.setHidden(False)
        self.bj2.setHidden(False)
        self.bj3.setHidden(False)
        self.bj4.setHidden(False)
        self.bj5.setHidden(False)
        self.bj6.setHidden(False)
        self.bj7.setHidden(False)
        self.bj8.setHidden(False)
        self.bj9.setHidden(False)
        self.bj10.setHidden(False)
        self.bj11.setHidden(False)
        self.bj12.setHidden(False)
        self.bj13.setHidden(False)
        self.bj14.setHidden(False)
        self.bj15.setHidden(False)
        self.bj16.setHidden(False)
        self.bj17.setHidden(False)
        self.bj18.setHidden(False)
        self.bj19.setHidden(False)
        self.bj20.setHidden(False)
        self.bj21.setHidden(False)
        self.bj22.setHidden(False)
        self.bj23.setHidden(False)
        self.bj24.setHidden(False)
        self.bj25.setHidden(False)
        self.bj26.setHidden(False)
        self.bj27.setHidden(False)
        self.bj28.setHidden(False)
        self.bj29.setHidden(False)
        self.bj30.setHidden(False)
        self.bj31.setHidden(False)
        self.bj32.setHidden(False)
        self.bj33.setHidden(False)
        self.bj34.setHidden(False)
        self.bj35.setHidden(False)
        self.bj36.setHidden(False)
        self.bj37.setHidden(False)
        self.bj45.setHidden(False)
        self.bj46.setHidden(False)
        self.bj47.setHidden(False)
        self.bj48.setHidden(False)

    def bj39p(self):
        self.bj40.setHidden(False)
        self.bj41.setHidden(False)
        self.bj42.setHidden(False)
        self.bj43.setHidden(False)
        self.bj44.setHidden(False)
        self.bj49.setHidden(False)
        self.bj50.setHidden(False)
        self.bj1.setHidden(True)
        self.bj2.setHidden(True)
        self.bj3.setHidden(True)
        self.bj4.setHidden(True)
        self.bj5.setHidden(True)
        self.bj6.setHidden(True)
        self.bj7.setHidden(True)
        self.bj8.setHidden(True)
        self.bj9.setHidden(True)
        self.bj10.setHidden(True)
        self.bj11.setHidden(True)
        self.bj12.setHidden(True)
        self.bj13.setHidden(True)
        self.bj14.setHidden(True)
        self.bj15.setHidden(True)
        self.bj16.setHidden(True)
        self.bj17.setHidden(True)
        self.bj18.setHidden(True)
        self.bj19.setHidden(True)
        self.bj20.setHidden(True)
        self.bj21.setHidden(True)
        self.bj22.setHidden(True)
        self.bj23.setHidden(True)
        self.bj24.setHidden(True)
        self.bj25.setHidden(True)
        self.bj26.setHidden(True)
        self.bj27.setHidden(True)
        self.bj28.setHidden(True)
        self.bj29.setHidden(True)
        self.bj30.setHidden(True)
        self.bj31.setHidden(True)
        self.bj32.setHidden(True)
        self.bj33.setHidden(True)
        self.bj34.setHidden(True)
        self.bj35.setHidden(True)
        self.bj36.setHidden(True)
        self.bj37.setHidden(True)
        self.bj45.setHidden(True)
        self.bj46.setHidden(True)
        self.bj47.setHidden(True)
        self.bj48.setHidden(True)

    def bj46p(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*);;文本文档 (*.txt)", options=options)
        self.bj47.setText(file_path)
        return file_path

    def mn1p(self):
        sound1.play()
    def mn2p(self):
        sound2.play()
    def mn3p(self):
        sound3.play()
    def mn4p(self):
        sound4.play()
    def mn5p(self):
        sound5.play()
    def mn6p(self):
        sound6.play()
    def mn7p(self):
        sound7.play()
    def mn8p(self):
        sound8.play()
    def mn9p(self):
        sound9.play()
    def mn10p(self):
        sound10.play()
    def mn11p(self):
        sound11.play()
    def mn12p(self):
        sound12.play()
    def mn13p(self):
        sound13.play()
    def mn14p(self):
        sound14.play()
    def mn15p(self):
        sound15.play()
    def mn16p(self):
        sound16.play()
    def mn17p(self):
        sound17.play()
    def mn18p(self):
        sound18.play()
    def mn19p(self):
        sound19.play()
    def mn20p(self):
        sound20.play()
    def mn21p(self):
        sound21.play()

    def keyPressEvent(self, event):
        if event.key() == 65 and listening:
            sound8.play()
        elif event.key() == 83 and listening:
            sound9.play()
        elif event.key() == 68 and listening:
            sound10.play()
        elif event.key() == 70 and listening:
            sound11.play()
        elif event.key() == 71 and listening:
            sound12.play()
        elif event.key() == 72 and listening:
            sound13.play()
        elif event.key() == 74 and listening:
            sound14.play()
        elif event.key() == 81 and listening:
            sound1.play()
        elif event.key() == 87 and listening:
            sound2.play()
        elif event.key() == 69 and listening:
            sound3.play()
        elif event.key() == 82 and listening:
            sound4.play()
        elif event.key() == 84 and listening:
            sound5.play()
        elif event.key() == 89 and listening:
            sound6.play()
        elif event.key() == 85 and listening:
            sound7.play()
        elif event.key() == 90 and listening:
            sound15.play()
        elif event.key() == 88 and listening:
            sound16.play()
        elif event.key() == 67 and listening:
            sound17.play()
        elif event.key() == 86 and listening:
            sound18.play()
        elif event.key() == 66 and listening:
            sound19.play()
        elif event.key() == 78 and listening:
            sound20.play()
        elif event.key() == 77 and listening:
            sound21.play()

    def mn22p(self):
        self.mn24.setHidden(False)
        self.mn25.setHidden(False)
        self.mn26.setHidden(False)
        self.mn22.setHidden(True)
        self.mn27.setHidden(False)

    def mn24p(self):
        global sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, sound12, sound13, sound14, sound15, sound16, sound17, sound18, sound19, sound20, sound21
        sound1 = pygame.mixer.Sound(r'resource\Windsong_Lyre\Q.wav')
        sound2 = pygame.mixer.Sound(r'resource\Windsong_Lyre\W.wav')
        sound3 = pygame.mixer.Sound(r'resource\Windsong_Lyre\E.wav')
        sound4 = pygame.mixer.Sound(r'resource\Windsong_Lyre\R.wav')
        sound5 = pygame.mixer.Sound(r'resource\Windsong_Lyre\T.wav')
        sound6 = pygame.mixer.Sound(r'resource\Windsong_Lyre\Y.wav')
        sound7 = pygame.mixer.Sound(r'resource\Windsong_Lyre\U.wav')
        sound8 = pygame.mixer.Sound(r'resource\Windsong_Lyre\A.wav')
        sound9 = pygame.mixer.Sound(r'resource\Windsong_Lyre\S.wav')
        sound10 = pygame.mixer.Sound(r'resource\Windsong_Lyre\D.wav')
        sound11 = pygame.mixer.Sound(r'resource\Windsong_Lyre\F.wav')
        sound12 = pygame.mixer.Sound(r'resource\Windsong_Lyre\G.wav')
        sound13 = pygame.mixer.Sound(r'resource\Windsong_Lyre\H.wav')
        sound14 = pygame.mixer.Sound(r'resource\Windsong_Lyre\J.wav')
        sound15 = pygame.mixer.Sound(r'resource\Windsong_Lyre\Z.wav')
        sound16 = pygame.mixer.Sound(r'resource\Windsong_Lyre\X.wav')
        sound17 = pygame.mixer.Sound(r'resource\Windsong_Lyre\C.wav')
        sound18 = pygame.mixer.Sound(r'resource\Windsong_Lyre\V.wav')
        sound19 = pygame.mixer.Sound(r'resource\Windsong_Lyre\B.wav')
        sound20 = pygame.mixer.Sound(r'resource\Windsong_Lyre\N.wav')
        sound21 = pygame.mixer.Sound(r'resource\Windsong_Lyre\M.wav')
        self.mn1.setIcon(QIcon('resource\Windsong_Lyre\A.png'))
        self.mn1.setIconSize(QSize(80, 80))
        self.mn2.setIcon(QIcon('resource\Windsong_Lyre\S.png'))
        self.mn2.setIconSize(QSize(80, 80))
        self.mn3.setIcon(QIcon('resource\Windsong_Lyre\D.png'))
        self.mn3.setIconSize(QSize(80, 80))
        self.mn4.setIcon(QIcon('resource\Windsong_Lyre\F.png'))
        self.mn4.setIconSize(QSize(80, 80))
        self.mn5.setIcon(QIcon('resource\Windsong_Lyre\G.png'))
        self.mn5.setIconSize(QSize(80, 80))
        self.mn6.setIcon(QIcon('resource\Windsong_Lyre\H.png'))
        self.mn6.setIconSize(QSize(80, 80))
        self.mn7.setIcon(QIcon('resource\Windsong_Lyre\J.png'))
        self.mn7.setIconSize(QSize(80, 80))
        self.mn8.setIcon(QIcon('resource\Windsong_Lyre\A.png'))
        self.mn8.setIconSize(QSize(80, 80))
        self.mn9.setIcon(QIcon('resource\Windsong_Lyre\S.png'))
        self.mn9.setIconSize(QSize(80, 80))
        self.mn10.setIcon(QIcon('resource\Windsong_Lyre\D.png'))
        self.mn10.setIconSize(QSize(80, 80))
        self.mn11.setIcon(QIcon('resource\Windsong_Lyre\F.png'))
        self.mn11.setIconSize(QSize(80, 80))
        self.mn12.setIcon(QIcon('resource\Windsong_Lyre\G.png'))
        self.mn12.setIconSize(QSize(80, 80))
        self.mn13.setIcon(QIcon('resource\Windsong_Lyre\H.png'))
        self.mn13.setIconSize(QSize(80, 80))
        self.mn14.setIcon(QIcon('resource\Windsong_Lyre\J.png'))
        self.mn14.setIconSize(QSize(80, 80))
        self.mn15.setIcon(QIcon('resource\Windsong_Lyre\A.png'))
        self.mn15.setIconSize(QSize(80, 80))
        self.mn16.setIcon(QIcon('resource\Windsong_Lyre\S.png'))
        self.mn16.setIconSize(QSize(80, 80))
        self.mn17.setIcon(QIcon('resource\Windsong_Lyre\D.png'))
        self.mn17.setIconSize(QSize(80, 80))
        self.mn18.setIcon(QIcon('resource\Windsong_Lyre\F.png'))
        self.mn18.setIconSize(QSize(80, 80))
        self.mn19.setIcon(QIcon('resource\Windsong_Lyre\G.png'))
        self.mn19.setIconSize(QSize(80, 80))
        self.mn20.setIcon(QIcon('resource\Windsong_Lyre\H.png'))
        self.mn20.setIconSize(QSize(80, 80))
        self.mn21.setIcon(QIcon('resource\Windsong_Lyre\J.png'))
        self.mn21.setIconSize(QSize(80, 80))
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.mn22.setHidden(False)

    def mn25p(self):
        global sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, sound12, sound13, sound14, sound15, sound16, sound17, sound18, sound19, sound20, sound21
        sound1 = pygame.mixer.Sound(r'resource\Floral_Zither\Q.wav')
        sound2 = pygame.mixer.Sound(r'resource\Floral_Zither\W.wav')
        sound3 = pygame.mixer.Sound(r'resource\Floral_Zither\E.wav')
        sound4 = pygame.mixer.Sound(r'resource\Floral_Zither\R.wav')
        sound5 = pygame.mixer.Sound(r'resource\Floral_Zither\T.wav')
        sound6 = pygame.mixer.Sound(r'resource\Floral_Zither\Y.wav')
        sound7 = pygame.mixer.Sound(r'resource\Floral_Zither\U.wav')
        sound8 = pygame.mixer.Sound(r'resource\Floral_Zither\A.wav')
        sound9 = pygame.mixer.Sound(r'resource\Floral_Zither\S.wav')
        sound10 = pygame.mixer.Sound(r'resource\Floral_Zither\D.wav')
        sound11 = pygame.mixer.Sound(r'resource\Floral_Zither\F.wav')
        sound12 = pygame.mixer.Sound(r'resource\Floral_Zither\G.wav')
        sound13 = pygame.mixer.Sound(r'resource\Floral_Zither\H.wav')
        sound14 = pygame.mixer.Sound(r'resource\Floral_Zither\J.wav')
        sound15 = pygame.mixer.Sound(r'resource\Floral_Zither\Z.wav')
        sound16 = pygame.mixer.Sound(r'resource\Floral_Zither\X.wav')
        sound17 = pygame.mixer.Sound(r'resource\Floral_Zither\C.wav')
        sound18 = pygame.mixer.Sound(r'resource\Floral_Zither\V.wav')
        sound19 = pygame.mixer.Sound(r'resource\Floral_Zither\B.wav')
        sound20 = pygame.mixer.Sound(r'resource\Floral_Zither\N.wav')
        sound21 = pygame.mixer.Sound(r'resource\Floral_Zither\M.wav')
        self.mn1.setIcon(QIcon('resource\Floral_Zither\A.png'))
        self.mn1.setIconSize(QSize(80, 80))
        self.mn2.setIcon(QIcon('resource\Floral_Zither\S.png'))
        self.mn2.setIconSize(QSize(80, 80))
        self.mn3.setIcon(QIcon('resource\Floral_Zither\D.png'))
        self.mn3.setIconSize(QSize(80, 80))
        self.mn4.setIcon(QIcon('resource\Floral_Zither\F.png'))
        self.mn4.setIconSize(QSize(80, 80))
        self.mn5.setIcon(QIcon('resource\Floral_Zither\G.png'))
        self.mn5.setIconSize(QSize(80, 80))
        self.mn6.setIcon(QIcon('resource\Floral_Zither\H.png'))
        self.mn6.setIconSize(QSize(80, 80))
        self.mn7.setIcon(QIcon('resource\Floral_Zither\J.png'))
        self.mn7.setIconSize(QSize(80, 80))
        self.mn8.setIcon(QIcon('resource\Floral_Zither\A.png'))
        self.mn8.setIconSize(QSize(80, 80))
        self.mn9.setIcon(QIcon('resource\Floral_Zither\S.png'))
        self.mn9.setIconSize(QSize(80, 80))
        self.mn10.setIcon(QIcon('resource\Floral_Zither\D.png'))
        self.mn10.setIconSize(QSize(80, 80))
        self.mn11.setIcon(QIcon('resource\Floral_Zither\F.png'))
        self.mn11.setIconSize(QSize(80, 80))
        self.mn12.setIcon(QIcon('resource\Floral_Zither\G.png'))
        self.mn12.setIconSize(QSize(80, 80))
        self.mn13.setIcon(QIcon('resource\Floral_Zither\H.png'))
        self.mn13.setIconSize(QSize(80, 80))
        self.mn14.setIcon(QIcon('resource\Floral_Zither\J.png'))
        self.mn14.setIconSize(QSize(80, 80))
        self.mn15.setIcon(QIcon('resource\Floral_Zither\A.png'))
        self.mn15.setIconSize(QSize(80, 80))
        self.mn16.setIcon(QIcon('resource\Floral_Zither\S.png'))
        self.mn16.setIconSize(QSize(80, 80))
        self.mn17.setIcon(QIcon('resource\Floral_Zither\D.png'))
        self.mn17.setIconSize(QSize(80, 80))
        self.mn18.setIcon(QIcon('resource\Floral_Zither\F.png'))
        self.mn18.setIconSize(QSize(80, 80))
        self.mn19.setIcon(QIcon('resource\Floral_Zither\G.png'))
        self.mn19.setIconSize(QSize(80, 80))
        self.mn20.setIcon(QIcon('resource\Floral_Zither\H.png'))
        self.mn20.setIconSize(QSize(80, 80))
        self.mn21.setIcon(QIcon('resource\Floral_Zither\J.png'))
        self.mn21.setIconSize(QSize(80, 80))
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.mn22.setHidden(False)

    def mn26p(self):
        global sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, sound12, sound13, sound14, sound15, sound16, sound17, sound18, sound19, sound20, sound21
        sound1 = pygame.mixer.Sound(r'resource\Vintage_Lyre\Q.wav')
        sound2 = pygame.mixer.Sound(r'resource\Vintage_Lyre\W.wav')
        sound3 = pygame.mixer.Sound(r'resource\Vintage_Lyre\E.wav')
        sound4 = pygame.mixer.Sound(r'resource\Vintage_Lyre\R.wav')
        sound5 = pygame.mixer.Sound(r'resource\Vintage_Lyre\T.wav')
        sound6 = pygame.mixer.Sound(r'resource\Vintage_Lyre\Y.wav')
        sound7 = pygame.mixer.Sound(r'resource\Vintage_Lyre\U.wav')
        sound8 = pygame.mixer.Sound(r'resource\Vintage_Lyre\A.wav')
        sound9 = pygame.mixer.Sound(r'resource\Vintage_Lyre\S.wav')
        sound10 = pygame.mixer.Sound(r'resource\Vintage_Lyre\D.wav')
        sound11 = pygame.mixer.Sound(r'resource\Vintage_Lyre\F.wav')
        sound12 = pygame.mixer.Sound(r'resource\Vintage_Lyre\G.wav')
        sound13 = pygame.mixer.Sound(r'resource\Vintage_Lyre\H.wav')
        sound14 = pygame.mixer.Sound(r'resource\Vintage_Lyre\J.wav')
        sound15 = pygame.mixer.Sound(r'resource\Vintage_Lyre\Z.wav')
        sound16 = pygame.mixer.Sound(r'resource\Vintage_Lyre\X.wav')
        sound17 = pygame.mixer.Sound(r'resource\Vintage_Lyre\C.wav')
        sound18 = pygame.mixer.Sound(r'resource\Vintage_Lyre\V.wav')
        sound19 = pygame.mixer.Sound(r'resource\Vintage_Lyre\B.wav')
        sound20 = pygame.mixer.Sound(r'resource\Vintage_Lyre\N.wav')
        sound21 = pygame.mixer.Sound(r'resource\Vintage_Lyre\M.wav')
        self.mn1.setIcon(QIcon('resource\Vintage_Lyre\A.png'))
        self.mn1.setIconSize(QSize(80, 80))
        self.mn2.setIcon(QIcon('resource\Vintage_Lyre\W.png'))
        self.mn2.setIconSize(QSize(80, 80))
        self.mn3.setIcon(QIcon('resource\Vintage_Lyre\D.png'))
        self.mn3.setIconSize(QSize(80, 80))
        self.mn4.setIcon(QIcon('resource\Vintage_Lyre\F.png'))
        self.mn4.setIconSize(QSize(80, 80))
        self.mn5.setIcon(QIcon('resource\Vintage_Lyre\G.png'))
        self.mn5.setIconSize(QSize(80, 80))
        self.mn6.setIcon(QIcon('resource\Vintage_Lyre\Y.png'))
        self.mn6.setIconSize(QSize(80, 80))
        self.mn7.setIcon(QIcon('resource\Vintage_Lyre\J.png'))
        self.mn7.setIconSize(QSize(80, 80))
        self.mn8.setIcon(QIcon('resource\Vintage_Lyre\A.png'))
        self.mn8.setIconSize(QSize(80, 80))
        self.mn9.setIcon(QIcon('resource\Vintage_Lyre\S.png'))
        self.mn9.setIconSize(QSize(80, 80))
        self.mn10.setIcon(QIcon('resource\Vintage_Lyre\D.png'))
        self.mn10.setIconSize(QSize(80, 80))
        self.mn11.setIcon(QIcon('resource\Vintage_Lyre\F.png'))
        self.mn11.setIconSize(QSize(80, 80))
        self.mn12.setIcon(QIcon('resource\Vintage_Lyre\G.png'))
        self.mn12.setIconSize(QSize(80, 80))
        self.mn13.setIcon(QIcon('resource\Vintage_Lyre\H.png'))
        self.mn13.setIconSize(QSize(80, 80))
        self.mn14.setIcon(QIcon('resource\Vintage_Lyre\J.png'))
        self.mn14.setIconSize(QSize(80, 80))
        self.mn15.setIcon(QIcon('resource\Vintage_Lyre\A.png'))
        self.mn15.setIconSize(QSize(80, 80))
        self.mn16.setIcon(QIcon('resource\Vintage_Lyre\S.png'))
        self.mn16.setIconSize(QSize(80, 80))
        self.mn17.setIcon(QIcon('resource\Vintage_Lyre\D.png'))
        self.mn17.setIconSize(QSize(80, 80))
        self.mn18.setIcon(QIcon('resource\Vintage_Lyre\F.png'))
        self.mn18.setIconSize(QSize(80, 80))
        self.mn19.setIcon(QIcon('resource\Vintage_Lyre\G.png'))
        self.mn19.setIconSize(QSize(80, 80))
        self.mn20.setIcon(QIcon('resource\Vintage_Lyre\H.png'))
        self.mn20.setIconSize(QSize(80, 80))
        self.mn21.setIcon(QIcon('resource\Vintage_Lyre\J.png'))
        self.mn21.setIconSize(QSize(80, 80))
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.mn22.setHidden(False)

    def mn27p(self):
        self.mn24.setHidden(True)
        self.mn25.setHidden(True)
        self.mn26.setHidden(True)
        self.mn27.setHidden(True)
        self.mn22.setHidden(False)

    def update_background(self):
        if self.background != '':
            self.background_pixmap = QPixmap(self.background)
        else:
            self.background_pixmap = ''

        self.update()

    def sz2p(self):
        self.sz2.setHidden(True)
        self.sz3.setHidden(False)
        self.sz4.setHidden(False)
        self.sz5.setHidden(False)
        self.sz6.setHidden(False)
        self.sz7.setHidden(False)
        self.sz8.setHidden(False)
        self.sz9.setHidden(False)
        self.sz10.setHidden(False)

    def sz3p(self):
        self.background = 'resource\\background\\Mondstadt.jpg'
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('resource\\background\\Mondstadt.jpg')

    def sz4p(self):
        self.background = 'resource\\background\\Liyue.jpg'
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('resource\\background\\Liyue.jpg')

    def sz5p(self):
        self.background = 'resource\\background\\Inazuma.jpg'
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('resource\\background\\Inazuma.jpg')

    def sz6p(self):
        self.background = 'resource\\background\\Sumeru.jpg'
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('resource\\background\\Sumeru.jpg')

    def sz7p(self):
        self.background = 'resource\\background\\Fontaine.jpg'
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('resource\\background\\Fontaine.jpg')

    def sz8p(self):
        self.background = 'resource\\background\\Natlan.jpg'
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('resource\\background\\Natlan.jpg')

    def sz9p(self):
        self.background = ''
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

        self.update_background()

        with open('resource\\setting\\background.txt', 'w', encoding='utf-8') as file:
            file.write('')

    def sz10p(self):
        self.sz10.setHidden(True)
        self.sz3.setHidden(True)
        self.sz4.setHidden(True)
        self.sz5.setHidden(True)
        self.sz6.setHidden(True)
        self.sz7.setHidden(True)
        self.sz8.setHidden(True)
        self.sz9.setHidden(True)
        self.sz2.setHidden(False)

    def sz14p(self):
        with open('resource\setting\c.txt', 'w', encoding='utf-8') as file:
            file.write(self.sz13.text())

    def paintEvent(self, event):

        if self.background == '':
            self.Label1.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.dh1.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.dh2.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.dh3.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.dh4.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.dh5.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.dh6.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.yz4.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.yz5.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.yz6.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.bj36.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.bj48.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.bj43.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.sz1.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.sz11.setStyleSheet(f'color: rgb(0, 0, 0);')
            self.sz12.setStyleSheet(f'color: rgb(0, 0, 0);')
        else:

            if self.background == 'resource\\background\\Mondstadt.jpg':
                self.Label1.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.dh1.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.dh2.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.dh3.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.dh4.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.dh5.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.dh6.setStyleSheet(f'color: rgb(50, 150, 150);')
                self.yz4.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz5.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz6.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj43.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj36.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj48.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz1.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz11.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz12.setStyleSheet(f'color: rgb(255, 255, 255);')

            if self.background == 'resource\\background\\Liyue.jpg':
                self.Label1.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.dh1.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.dh2.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.dh3.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.dh4.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.dh5.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.dh6.setStyleSheet(f'color: rgb(205, 145, 70);')
                self.yz4.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz5.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz6.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj43.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj36.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj48.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz1.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz11.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz12.setStyleSheet(f'color: rgb(255, 255, 255);')

            if self.background == 'resource\\background\\Inazuma.jpg':
                self.Label1.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.dh1.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.dh2.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.dh3.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.dh4.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.dh5.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.dh6.setStyleSheet(f'color: rgb(105, 90, 185);')
                self.yz4.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz5.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz6.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj43.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj36.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj48.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz1.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz11.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz12.setStyleSheet(f'color: rgb(255, 255, 255);')

            if self.background == 'resource\\background\\Sumeru.jpg':
                self.Label1.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.dh1.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.dh2.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.dh3.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.dh4.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.dh5.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.dh6.setStyleSheet(f'color: rgb(105, 175, 25);')
                self.yz4.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz5.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz6.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj43.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj36.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj48.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz1.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz11.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz12.setStyleSheet(f'color: rgb(255, 255, 255);')

            if self.background == 'resource\\background\\Fontaine.jpg':
                self.Label1.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.dh1.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.dh2.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.dh3.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.dh4.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.dh5.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.dh6.setStyleSheet(f'color: rgb(75, 145, 200);')
                self.yz4.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz5.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz6.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj43.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj36.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj48.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz1.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz11.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz12.setStyleSheet(f'color: rgb(255, 255, 255);')

            if self.background == 'resource\\background\\Natlan.jpg':
                self.Label1.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.dh1.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.dh2.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.dh3.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.dh4.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.dh5.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.dh6.setStyleSheet(f'color: rgb(235, 75, 35);')
                self.yz4.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz5.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.yz6.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj43.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj36.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.bj48.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz1.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz11.setStyleSheet(f'color: rgb(255, 255, 255);')
                self.sz12.setStyleSheet(f'color: rgb(255, 255, 255);')
            
            painter = QPainter(self)

            window_size = self.size()

            scaled_pixmap = self.background_pixmap.scaled(window_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            x = (window_size.width() - scaled_pixmap.width()) // 2
            y = (window_size.height() - scaled_pixmap.height()) // 2

            painter.drawPixmap(x, y, scaled_pixmap)

            painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myappid = "MAGIL"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
