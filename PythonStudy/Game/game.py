"""
类的综合实例
"""


class Game(object):
    # 历史最高分
    top_score = 10

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("help message")

    @classmethod
    def show_top_score(cls):
        print("top score is %d" % cls.top_score)

    def start(self):
        print("%s is playing game" % self.player_name)


# 查看游戏帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
gamer = Game("Tom")
gamer.start()
