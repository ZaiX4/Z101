
import re

class qq_message:

    # 解析群名函数
    def __init__(self, text):

        try:
            qq_group = re.search(r'收到群 (.*?) 内', text).group(1)

            self.qq_group_id = re.findall(r'\((.*?)\)', qq_group)[-1]

            self.qq_group_name = re.search(r'(.*?)\(', qq_group).group(1)

            qq_user = re.search(r'内 (.*?) 的消息', text).group(1)

            self.qq_user_id = re.findall(r'\((.*?)\)', qq_user)[-1]

            self.qq_user_name = re.search(r'(.*?)\(', qq_user).group(1)

            self.qq_text = re.search(r'的消息: (.*?) \(', text).group(1)

            self.ls = [self.qq_group_id, self.qq_group_name, self.qq_user_id, self.qq_user_name, self.qq_text]

            self.err = 0

        except:
            self.err = -1