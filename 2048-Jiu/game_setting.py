# 进行游戏设定
class GameSetting:

    GameName = "2048小游戏"
    WindowSize = {"长": 540, "宽": 540}
    CanvasSize = [[{"主体": 500, "边距": 20, "Style": "QLabel{background-color:#bbada0;color:#bbada0;border-radius:6}"}],
                  [{"x": 20, "y": 20}]
                  ]

    GameNumPar = [[{"主体": 105, "边距": 16, "Style": "QLabel{background-color:#cdc1b4;color:#cdc1b4;border-radius:6}"}],[]
                ]

    NumberStyle = {"2": "QLabel{background-color:#eee4da;color:#776e65;border-radius:6}",
                   "4": "QLabel{background-color:#ede0c8;color:#776e65;border-radius:6}",
                   "8": "QLabel{background-color:#f2b179;color:#ffffff;border-radius:6}",
                   "16": "QLabel{background-color:#f59563;color:#ffffff;border-radius:6}",
                   "32": "QLabel{background-color:#f67c5f;color:#ffffff;border-radius:6}",
                   "64": "QLabel{background-color:#f65e3b;color:#ffffff;border-radius:6}",
                   "128": "QLabel{background-color:#edcf72;color:#ffffff;border-radius:6}",
                   "256": "QLabel{background-color:#edcc61;color:#776e65;border-radius:6}",
                   "512": "QLabel{background-color:#EFCB52;color:#776e65;border-radius:6}",
                   "1024": "QLabel{background-color:#EFC739;color:#776e65;border-radius:6}",
                   "2048": "QLabel{background-color:#EFC329;color:#776e65;border-radius:6}",
                   "4096": "QLabel{background-color:#FF3C39;color:#ffffff;border-radius:6}"
                   }

    NumFontStyle = {"字体": "\"Clear Sans\", \"Helvetica Neue\", Arial, sans-serif","字号": 55}

    def __init__(self):
        
        self.match_game_num_par()

    # 计算游戏方块参数
    def match_game_num_par(self):
        
        pos = []
        for i in range(1,5):
            for j in range(1,5):
                # 计算窗口位移坐标
                x = self.CanvasSize[0][0]["边距"] + self.GameNumPar[0][0]["边距"] * j + self.GameNumPar[0][0]["主体"] * (j - 1)
                y = self.CanvasSize[0][0]["边距"] + self.GameNumPar[0][0]["边距"] * i + self.GameNumPar[0][0]["主体"] * (i - 1)
                pos.append({"坐标行": j, "坐标列": i, "x": x, "y": y, "value": 0})
                
        self.GameNumPar[1] = pos


    


    
