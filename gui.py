# coding: utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,\
    QLabel, QGridLayout
import sip


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle('QCheckBox')

        # Button
        self.button = QPushButton('Clear')
        self.label = QLabel('click')

        # buttonのclickでラベルをクリア
        self.button.clicked.connect(self.label.clear)

        # レイアウト配置
        self.grid = QGridLayout()
        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.grid.addWidget(self.label, 1, 0, 1, 2)
        self.setLayout(self.grid)


if __name__ == '__main__':
    # アプリの定義
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
