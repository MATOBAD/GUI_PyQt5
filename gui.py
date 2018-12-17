# coding: utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,\
    QLabel, QGridLayout, QMainWindow, QLineEdit, QHBoxLayout,\
    QVBoxLayout, QPlainTextEdit
import sip


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        # 画面を表示させる場所の指定(x, y, 横幅, 高さ)
        self.window = QWidget()
        self.setGeometry(300, 300, 250, 150)

        # Windowのタイトル
        self.setWindowTitle('QCheckBox')

        # Label
        self.label = QLabel('input_text: ')
        self.answer_label = QLabel('answer: ')

        # Edit
        self.input_text_box = QPlainTextEdit()
        self.textbox1 = QLineEdit()

        # Button
        self.button = QPushButton('OK', self)
        self.button_quit = QPushButton('quit', self)

        self.button.clicked.connect(self.button_click)
        self.button_quit.clicked.connect(self.quit_click)

        # レイアウト配置
        self.layout = QGridLayout()
        # レイアウトの位置を決める(widget, 開始する縦の位置, 開始する横の位置, 縦の大きさ, 横の大きさ)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.input_text_box, 0, 1, 20, 40)
        self.layout.addWidget(self.button, 20, 0)
        self.layout.addWidget(self.button_quit, 20, 1)
        self.layout.addWidget(self.answer_label, 21, 0)
        self.layout.addWidget(self.textbox1, 21, 1)
        self.setLayout(self.layout)

        self.show()

    def button_click(self):
        # buttonのclickでラベルをクリア
        sent = self.input_text_box.toPlainText()
        self.textbox1.setText(sent)

    def quit_click(self):
        # アプリの終了
        app.quit()


if __name__ == '__main__':
    # アプリの定義
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
