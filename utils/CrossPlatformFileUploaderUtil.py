import platform
import pyperclip
from pynput.keyboard import Controller, Key
import time


class CrossPlatformFileUploaderUtil:
    def __init__(self, file_path):
        """
        文件上传工具类，支持 Windows、macOS 和 Linux

        :param file_path: 文件路径
        """
        self.file_path = file_path
        self.os_name = platform.system().lower()
        self.keyboard = Controller()

    def upload_file(self):
        """
        执行文件上传逻辑
        """
        # 将文件路径复制到剪贴板
        self.copy_to_clipboard(self.file_path)

        # 调用对应平台的上传逻辑
        if "windows" in self.os_name:
            self.upload_for_windows()
        elif "darwin" in self.os_name:  # macOS
            self.upload_for_mac()
        elif "linux" in self.os_name:
            self.upload_for_linux()
        else:
            raise OSError(f"Unsupported operating system: {self.os_name}")

    @staticmethod
    def copy_to_clipboard(text):
        """
        将文本内容复制到系统剪贴板

        :param text: 文本内容
        """
        pyperclip.copy(text)

    def upload_for_windows(self):
        """
        Windows 系统文件上传逻辑
        """
        self.simulate_key_combination(Key.ctrl, 'v')
        self.press_enter()

    def upload_for_mac(self):
        """
        macOS 系统文件上传逻辑
        """
        self.simulate_key_combination(Key.cmd, 'v')
        self.press_enter()

    def upload_for_linux(self):
        """
        Linux 系统文件上传逻辑
        """
        self.simulate_key_combination(Key.ctrl, 'v')
        self.press_enter()

    def simulate_key_combination(self, modifier_key, char_key):
        """
        模拟组合键按下和释放

        :param modifier_key: 修饰键 (如 Ctrl, Cmd)
        :param char_key: 字符键 (如 'v')
        """
        time.sleep(0.5)
        self.keyboard.press(modifier_key)
        self.keyboard.press(char_key)
        self.keyboard.release(char_key)
        self.keyboard.release(modifier_key)

    def press_enter(self):
        """
        模拟按下 Enter 键
        """
        time.sleep(0.5)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

# # 示例用法
# if __name__ == "__main__":
#     try:
#         file_path = "C:\\path\\to\\your\\file.txt"  # 修改为实际文件路径
#         uploader = FileUploader(file_path)
#         uploader.upload_file()
#         print("文件上传操作完成！")
#     except Exception as e:
#         print(f"文件上传失败: {e}")
