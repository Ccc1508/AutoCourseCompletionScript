import time
import pyautogui as p
import pyperclip as pc
from typing import List


def Login(user : List[str]) -> None:
    """
    登录智慧职教网页
    此函数用于自动登录智慧职教网站，使用用户的账号和密码进行登录。
    参数:
        user: 一个列表，其中第一个元素是编号此函数中不被使用，第二个元素是用户名，第三个元素是密码。
    """

    # 隐藏PyCharm窗口，避免干扰自动化操作
    p.click(1, 1)
    time.sleep(0.5)

    # 将用户名复制到剪贴板
    pc.copy(user[1])

    # 定位账户输入框并点击
    account : p.Point = p.locateCenterOnScreen('../Icons/Account.png', confidence=0.9)
    p.click(account.x, account.y)

    # 使用快捷键粘贴用户名
    p.hotkey('ctrl', 'v')

    # 将密码复制到剪贴板
    pc.copy(user[2])

    # 定位密码输入框并点击
    password : p.Point = p.locateCenterOnScreen('../Icons/Password.png', confidence=0.9)
    p.click(password.x, password.y)

    # 使用快捷键粘贴密码
    p.hotkey('ctrl', 'v')

    # 定位并点击用户协议同意按钮
    userAgreement : p.Point = p.locateCenterOnScreen('../Icons/UserAgreement.png', confidence=0.9)
    p.click(userAgreement.x, userAgreement.y)

    # 定位并点击登录按钮
    login : p.Point = p.locateCenterOnScreen('../Icons/Login.png', confidence=0.9)
    p.click(login.x, login.y)

    # 等待页面加载
    time.sleep(1.5)

    # 定位并点击“不再提醒”按钮，避免弹窗干扰
    notRemind : p.Point = p.locateCenterOnScreen('../Icons/NotRemind.png', confidence=0.9)
    p.click(notRemind.x, notRemind.y)

    # 再次等待页面加载
    time.sleep(3)


def MoocLearn() -> None:
    """
    进入MOOC学习页面
    此函数用于导航至MOOC的学习页面，以便开始学习课程。
    """

    time.sleep(2)
    # 定位并点击我的MOOC图标
    myMooc : p.Point = p.locateCenterOnScreen('../Icons/MyMooc.png', confidence=0.9)
    p.click(myMooc.x, myMooc.y)

    # 等待页面加载
    time.sleep(2)

    # 定位并点击课程学习图标
    courseStudy : p.Point = p.locateCenterOnScreen('../Icons/CourseStudy.png', confidence=0.9)
    p.click(courseStudy.x, courseStudy.y)

    # 再次等待页面加载
    time.sleep(2)
