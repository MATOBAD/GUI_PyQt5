# coding: utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,\
    QLabel, QGridLayout, QMainWindow, QLineEdit
import sip


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')

        # Edit
        self.text = QLineEdit()

        # Button
        self.button = QPushButton('OK', self)
        self.button_quit = QPushButton('quit', self)
        self.label = QLabel('init_label')
        self.button.clicked.connect(self.button_click)
        self.button_quit.clicked.connect(self.quit_click)

        # レイアウト配置
        self.layout = QGridLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_quit)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.show()

    def button_click(self):
        # buttonのclickでラベルをクリア
        sent = self.text.text()
        self.textbox1 = QLineEdit()
        self.textbox1.setText(sent)
        self.layout.addWidget(self.textbox1)

    def quit_click(self):
        # アプリの終了
        app.quit()


if __name__ == '__main__':
    # アプリの定義
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
