import os
import time
import Data
import pyautogui as p
import pyperclip as pc
from typing import List, Generator


def GetAllFilesInDir(dirPath: str) -> Generator[str, None, None]:
    """
    遍历目录及其子目录下的所有文件。

    参数:
        dirPath (str): 目录路径。

    返回:
        生成器，遍历目录下所有的文件路径。
    """

    for root, dirs, files in os.walk(dirPath):
        for filename in files:
            filepath = os.path.join(root, filename)
            yield filepath


def AutoSubmit(path : str, discuss : str) -> None:
    """
    自动提交讨论回复。

    参数:
        path (str): 讨论主题的屏幕截图路径。
        discuss (str): 要提交的讨论内容。
    """
    try:
        time.sleep(2)
        AutoDiscuss(path)
    except p.ImageNotFoundException:
        # 如果找不到目标图片，则滚动页面以查看更多的讨论
        backupTarget : p.Point = p.locateCenterOnScreen('../Icons/DiscussTop.png', confidence=0.5)
        p.moveTo(backupTarget.x, backupTarget.y)
        for _ in range(20):
            p.scroll(-20)
        # 重新提交评论
        AutoDiscuss(path)

    # 定位讨论输入框并点击
    discussionInput : p.Point = p.locateCenterOnScreen('../Icons/DiscussionInput.png', confidence=0.8)
    p.click(discussionInput.x, discussionInput.y)

    # 复制讨论内容
    pc.copy(discuss)

    # 粘贴讨论内容
    p.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # 定位提交按钮并点击
    discussionSubmit : p.Point = p.locateCenterOnScreen('../Icons/DiscussionSubmit.png', confidence=0.9)
    p.click(discussionSubmit.x, discussionSubmit.y)
    time.sleep(2)



def AutoSubmitDiscussion(dirPath : str, discussions : List[str]) -> None:
    """
    自动提交多个讨论回复。

    参数:
        dirPath (str): 包含讨论主题屏幕截图的目录路径。
        discussions (list): 讨论内容列表。
    """
    time.sleep(2)

    # 定位并点击主题讨论图标
    theme : p.Point = p.locateCenterOnScreen('../Icons/TopicDiscussion.png', confidence=0.9)
    p.click(theme.x, theme.y)

    # 获取目录下所有文件的路径
    filePaths : List[str] = [file_path for file_path in GetAllFilesInDir(dirPath)]

    # 遍历文件路径和讨论内容，逐一提交
    for filepath, discussion in zip(filePaths, discussions):
        AutoSubmit(filepath, discussion)


def AutoDiscuss(path : str) -> None:
    """
    进入讨论主题并滚动页面。

    参数:
        path (str): 讨论主题的屏幕截图路径。
    """

    # 定位并点击讨论主题
    theme : p.Point = p.locateCenterOnScreen(path, confidence=0.8, grayscale=True)
    p.click(theme.x, theme.y)
    time.sleep(1)
    # 移动鼠标到屏幕中心并点击
    p.moveTo(Data.screen_width // 2, Data.screen_height // 2)
    p.click()
    # 向下滚动页面
    p.scroll(-20000)
    time.sleep(3)