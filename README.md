# 自动化学习助手

这个项目旨在自动化一系列在线教育平台（如智慧职教）的任务，包括登录、填写课程笔记、参与讨论等。通过使用Selenium和PyAutoGUI库，脚本可以模拟人类行为，自动执行常见的学习任务。

## 目录结构

  + `AutoDiscuss.py`: 包含自动提交讨论的逻辑。
  + `AutoNote.py`: 实现自动填写课程笔记的功能。
  + `Login.py`: 负责自动登录流程。
  + `Data.py`: 从Excel文件读取数据，如用户信息、讨论信息和笔记内容。
  + `CC.py`: 脚本的入口点，执行整个自动化流程。

## 功能

   + **自动登录**: 使用Excel中存储的用户信息登录网站。
   + **填写课程笔记**: 自动打开课程笔记页面，随机选择笔记内容并填写。
   + **参与讨论**: 自动进入讨论区，根据提供的讨论主题和内容提交讨论回复。

## 如何运行

1. **安装依赖**:
   ```Bash
   pip install selenium pyautogui pyperclip openpyxl opencv-python
   ```
2. **配置环境**:
   + 确保你的Excel文件(UserInfo.xlsx)位于项目的根目录或正确引用的路径中。
   + Excel文件应包含UserInfo, Discuss, 和Notes工作表。
   + 配置Selenium WebDriver（如EdgeDriver）的路径。
3. **运行脚本**:
   ```Bash
   python CC.py
   ```
   
## 注意事项

   + 请确保你的浏览器窗口在运行脚本前是关闭状态，以便脚本可以正确初始化WebDriver。
   + 脚本中使用了屏幕截图定位元素，这意味着它依赖于特定的UI布局和屏幕分辨率。
   + 在运行脚本前，请确保你已经同意网站的用户协议，并且不会违反任何使用条款。

## 贡献

   如果你发现任何问题或有改进的想法，欢迎提交Issue或Pull Request。

## 致谢

   感谢Selenium、PyAutoGUI、PyPerClip、OpenPyxl、OpenCV-Python库的开发者们，他们的工作使得这个项目成为可能。