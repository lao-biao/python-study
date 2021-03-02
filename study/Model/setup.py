from distutils.core import setup

setup(name="handle_message",  # 包名
      version="1.0",  # 版本
      description="描述信息",
      long_description="完整描述",
      author="author",  # 作者
      author_email="email",  # 作者邮箱
      url="www.xxx.com",  # 主页
      py_modules=[
          "handle_message.send_message",
          "handle_message.receive_message"])
