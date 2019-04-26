import sys
import random

# 从模块 PyQt5 导入所有 py 包
# PyQt5 图形程序框架
# PyQt5.QtCore:涵盖了包的核心的非GUI功能，此模块被用于处理程序中涉及的时间、文件、目录、数据类型、文本流、链接、QMimeData、线程或进程等对象
from PyQt5.QtCore import *
# PyQt5.QtWidgets:包含了一整套UI元素控件，用于建立符合系统风格的Classic界面，非常方便，可以在安装时选择是否使用此功能。
from PyQt5.QtWidgets import *
# PyQt5.QtGui:涵盖了多种基本图形功能的类，包括但不限于：窗口集、事件处理、2D图形、基本的图像和界面、字体和文本类
from PyQt5.QtGui import *


from game_setting import GameSetting


class GameCanvas(QLabel):

    p_set = GameSetting()
    p_set_can = p_set.CanvasSize
    p_set_num = p_set.GameNumPar
    p_num_style = p_set.NumberStyle
    p_num_font_style = p_set.NumFontStyle
    
    win = None
    cav = None

    def __init__(self, parent = None):

        super().__init__(parent)

        self.set_windows()
        
        self.set_canvas(self.win, self.p_set_can[0][0], self.p_set_can[1][0])

        self.cav.setFocusPolicy(Qt.StrongFocus)
        
        for i in range(len(self.p_set_num[1])):
            self.set_canvas(self.win, self.p_set_num[0][0], self.p_set_num[1][i])

        self.run()

    def run(self):
        self.ram_num_show()
        self.ram_num_show()
        #self.win.exec_()
        self.win.show()
        
    def set_windows(self):

        window = QDialog()
        window.setWindowTitle(self.p_set.GameName)
        window.resize(self.p_set.WindowSize["长"], self.p_set.WindowSize["宽"])
        
        self.win = window


    # item_set 值为 dict 包含大小和风格
    # item_pos 值为 dict 记录坐标

    def set_canvas(self, parent, item_set, item_pos):
        
        label = QLabel(parent)
        label.resize(item_set["主体"], item_set["主体"])
        label.move(item_pos["x"], item_pos["y"])
        label.setStyleSheet(item_set["Style"])
        self.cav = label

    # 随机数，在不为空的格子里，随机出现 2 或 4
    def ram_num_show(self):
        zero_ds = []
        for i in range(len(self.p_set_num[1])):
            if self.p_set_num[1][i]["value"] == 0:
                zero_ds.append(i)
        rnd = int(random.uniform(0, len(zero_ds)))
        # k 控制 2 、 4出现的概率，只有 random 出现 2 或 10时才出现 4
        k = int(random.uniform(0, 10))
        number = 2
        if k == 2 or k == 10:
            number = 4
        # 刷新设定表的记录
        self.p_set.GameNumPar[1][rnd]["value"] = number
        self.drow_num(self.win, self.p_set_num[0][0], self.p_set.GameNumPar[1][rnd])

    # 将数字展示到画面上
    def drow_num(self, parent, item_set, item_pos):

        label = QLabel(parent)
        label.resize(item_set["主体"], item_set["主体"])
        label.setFont(QFont(self.p_num_font_style["字体"], self.p_num_font_style["字号"], QFont.Bold))
        label.setAlignment(Qt.AlignCenter)

        label.setText(str(item_pos["value"]))
        label.move(item_pos["x"], item_pos["y"])
        label.setStyleSheet(self.p_num_style[str(item_pos["value"])])
        
    # 定义按键映射
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Up:
            print("向上")
        elif QKeyEvent.key() == Qt.Key_Down:
            print("向下")
        elif QKeyEvent.key() == Qt.Key_Left:
            print("向左")
        elif QKeyEvent.key() == Qt.Key_Right:
            print("向右")  


