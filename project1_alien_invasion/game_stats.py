# coding: utf-8

class GameStats():
    """ 跟踪游戏的统计信息 """

    def __init__(self, ai_settings):
        """ 初始化统计信息 """
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不应该重置最高得分
        self.read_high_score()

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    def read_high_score(self):
        """ 读取最高分 """
        self.high_score = 0
        filename = r'D:\learnCode\pythonBook\project1_alien_invasion\high_score.txt'
        try:
            with open(filename) as file_object:
                contents = file_object.read()
                self.high_score = int(contents)
        except FileNotFoundError:
            pass
            