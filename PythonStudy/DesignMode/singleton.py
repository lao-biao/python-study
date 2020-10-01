"""
单例模式
    让类创建的对象,在系统中只有为一个实例
    每一次执行类名()返回的对象,内存地址是相同的

__new__方法
    在内存中为对象分配空间
    返回对象的引用

重写__new__方法一定要 return super().__new__(cls),
否则Python的计时器得不到分配了空间的对象引用,就不会调用对象的初始化方法
注意:__new__是一个静态方法,在调用时需要主动传递cls参数

初始化只执行一次
"""


class MusicPlayer(object):
    # 定义类属性记录单例对象引用
    instance = None
    # 定义类属性记录初始化是否调用
    init_flag = False

    def __new__(cls, *args, **kwargs):
        """"# 创建对象
        print("创建对象,分配内存空间")
        # 分配内存空间
        # 返回对象的引用
        return super().__new__(cls)
        """
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类的方法,为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        """
        # 初始化会被再次调用
        print("初始化音乐播放器")
        """
        # 初始化方法只调用一次
        if MusicPlayer.init_flag:
            return
        print("初始化音乐播放器")
        # 修改标记
        MusicPlayer.init_flag = True


player = MusicPlayer()
print(player)

newPlayer = MusicPlayer()
print(newPlayer)

# 两个对象的地址是一样的
