import time
import AutoDiscuss
import Data
import Login
import AutoNote
from selenium import webdriver


if __name__ == '__main__':
    # 迭代表格中的账号
    for user in Data.UserInfo :
        # 使用Edge浏览器打开智慧职教登陆界面
        edge = webdriver.Edge()
        edge.get('https://sso.icve.com.cn/sso/auth?mode=simple&source=2&redirect=https%3A%2F%2Fmooc.icve.com.cn%2Fcms%2F')
        # 将窗口最大化
        edge.maximize_window()
        # 登录
        Login.Login(user = user)
        # 进入课程
        Login.MoocLearn()
        # 调试代码
        # time.sleep(20000)
        # 填写笔记
        AutoNote.Note(Data.Notes)
        # 填写讨论
        AutoDiscuss.AutoSubmitDiscussion(dirPath='../Icons/Discussions', discussions=Data.Discuss.get(user[0]))
        # 退出浏览器
        edge.quit()
        # 输出完成的账号
        print(user)
