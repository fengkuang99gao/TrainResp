import sys

# 从模块 PyQt5 导入所有 py 包
# PyQt5 图形程序框架
# PyQt5.QtCore:涵盖了包的核心的非GUI功能，此模块被用于处理程序中涉及的时间、文件、目录、数据类型、文本流、链接、QMimeData、线程或进程等对象
from PyQt5.QtCore import *
# PyQt5.QtWidgets:包含了一整套UI元素控件，用于建立符合系统风格的Classic界面，非常方便，可以在安装时选择是否使用此功能。
from PyQt5.QtWidgets import *
# PyQt5.QtGui:涵盖了多种基本图形功能的类，包括但不限于：窗口集、事件处理、2D图形、基本的图像和界面、字体和文本类
from PyQt5.QtGui import *

from game_canvas import GameCanvas
from game_setting import GameSetting

app = QApplication(sys.argv)
dialog = GameCanvas()
