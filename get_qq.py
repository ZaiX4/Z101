import multiprocessing
import subprocess
import threading
import re
import time

import qq_bot
from qq_message import qq_message


# 第一个线程,用于接受qq信息
def get_qq(v_dict, qq_message_ls, output_ls):
    print("get_qq,启动!")

    # 获取exe输出
    def capture_output(process):
        _ = 1
        for line in process.stdout:
            time.sleep(0.1)
            ss = str(line.decode("utf-8"))

            if ss.find("收到群") == -1 or ss.find("内") == -1:
                #print(ss)
                output_ls.append("1")
            else:
                #print(ss)
                new_message = qq_message(str(ss))

                if new_message.err != -1:
                    qq_message_ls.append(new_message)



    def run_executable(path):
        process = subprocess.Popen(
            path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            text=False
        )
        process.terminate()

        process = subprocess.Popen(
            path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            text=False
        )

        capture_output(process)

        output_thread = threading.Thread(target=capture_output, args=(process,))
        output_thread.start()

        process.wait()
        output_thread.join()

    # 要执行的可执行文件路径
    path = "go-cqhttp.exe -faststart"

    # 运行可执行文件，同时捕获输出
    run_executable(path)
