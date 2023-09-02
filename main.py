import multiprocessing
from multiprocessing import freeze_support

from output import output
from get_qq import get_qq
from qq_bot import qq_bot

"""
1.python执行exe文件时以当前路径执行
2.python进程不支持全局变量
3.python进程报错时会显示找不到文件
4.python进程的manage共享变量不要用切片操作，一切就死
5.python进程的arg属性必须以，结尾
6.当python进程内函数调用全局变量或是arg没以，结尾时不会报错，而是会自我崩溃，仅可执行第一个线程
7.with as内变量的定义域是有限的
8.正则表达式是个好东西
9.python最好别tm用全局变量
10.python里以多文件中的函数创建的多个线程调用同一个公有变量或是同时输出时有概率会出现错误
"""


if __name__ == '__main__':

    freeze_support()
    with multiprocessing.Manager() as manager:

        v_dic = manager.dict()
        v_dic['now_qq_group_id'] = ""
        v_dic['auto_water'] = False

        qq_message_ls = manager.list()

        output_ls = manager.list()

        # 创建进程
        t1 = multiprocessing.Process(target=output, args=(v_dic, qq_message_ls, output_ls,))
        t2 = multiprocessing.Process(target=get_qq, args=(v_dic, qq_message_ls, output_ls,))
        t3 = multiprocessing.Process(target=qq_bot, args=(v_dic, qq_message_ls, output_ls,))

        # 启动进程
        t1.start()
        t2.start()
        t3.start()

        # 等待进程结束
        t1.join()
        t2.join()
        t3.join()





