import time
import random
import pyautogui as p
import pyperclip as pc
from typing import List, Tuple


def Note(Notes : List[str]) -> None:
    """
    自动化填写课程笔记页面的笔记。

    参数:
        Notes (List[str]): 包含多条笔记内容的字符串列表。

    此函数执行以下步骤：
        1. 打开课程笔记页面。
        2. 重复18次：
            a. 打开一个新的笔记输入框。
            b. 随机选择并复制一条笔记内容。
            c. 粘贴内容到笔记输入框。
            d. 确认保存笔记。
    """

    # 定位并点击课程笔记图标，以打开课程笔记页面
    courseNote : p.Point = p.locateCenterOnScreen('../Icons/CourseNote.png', confidence=0.9)
    p.click(courseNote.x, courseNote.y)

    # 等待，确保笔记输入框已完全加载
    time.sleep(1)

    # 循环18次，以填写18条笔记
    for _ in range(18):
        # 定位并点击笔记图标，以打开新的笔记输入框
        note : p.Point = p.locateCenterOnScreen('../Icons/Note.png', confidence=0.9)
        p.click(note.x, note.y)

        # 等待，确保笔记输入框已完全加载
        time.sleep(0.1)

        # 定位并点击笔记输入框，使其成为活动窗口
        noteInput : p.Point = p.locateCenterOnScreen('../Icons/NoteInput.png', confidence=0.9)
        p.click(noteInput.x, noteInput.y)

        # 从Notes列表中随机选择一条笔记，复制到剪贴板
        pc.copy(Notes[random.randint(0, len(Notes) - 1)])

        # 使用快捷键粘贴笔记内容到笔记输入框
        p.hotkey('ctrl', 'v')

        # 等待，确保粘贴操作完成
        time.sleep(0.1)

        # 定位并点击确认按钮，以保存笔记
        noteConfirm : p.Point = p.locateCenterOnScreen('../Icons/NoteConfirm.png', confidence=0.9)
        p.click(noteConfirm.x, noteConfirm.y)

        # 等待，确保保存操作完成
        time.sleep(0.1)
