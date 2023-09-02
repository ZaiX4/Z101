import time
import my_gpt
import send_qq

from qq_message import qq_message
import re


def qq_bot(v_dict, qq_message_ls, output_ls):
    print("qq_bot,启动!")

    def command(q_ms):


        # 获取指令
        if q_ms.qq_text.find("请") != 0:
            output_ls.append("指令错误\n")
            return

        c = q_ms.qq_text[2:]

        output_ls.append(c)
        if c == "机器人移步本群":
            v_dict["now_qq_group_id"] = q_ms.qq_group_id
            send_qq.qq_choise_group(q_ms.qq_group_id)

        elif c == "开启自动水群功能":
            v_dict["auto_water"] = True
            send_qq.qq_send_message("已开启自动水群功能")

        elif c == "输出更新日志":
            send_qq.qq_send_message("版本号:A104\n"
                                    "1.重构了代码,提升了运行稳定性\n"
                                    "2.增加了自动水群功能开关\n"
                                    "3.增加了实时切换群聊功能\n"
                                    "4.增加了指令功能\n"
                                    "5.优化了机器人性能\n"
                                    "6.大幅提升了开发者的情绪稳定性\n"
                                    "7.大幅提高了开发者的抽象程度\n")


    def read_qq(q_ms):

        if v_dict["auto_water"]:
            if q_ms.qq_text.find("?") != -1 or q_ms.qq_text.find("？") != -1 or q_ms.qq_text.find(
                    "吗") != -1 or q_ms.qq_text.find("为什么") != -1:
                send_qq.qq_send_message(my_gpt.get_gpt_text(q_ms.qq_text))

        pass

    while True:
        time.sleep(0.1)

        if len(qq_message_ls) == 0:
            continue
        else:
            # 取出第一个元素
            ss = qq_message_ls[0]
            del qq_message_ls[0]
            print(ss.ls)

            if ss.qq_user_id == "2017574364":
                command(ss)
            if ss.qq_group_id == v_dict["now_qq_group_id"]:
                read_qq(ss)
