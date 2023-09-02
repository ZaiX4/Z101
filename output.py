import time




def output(v_dict, qq_message_ls, output_ls):
    print("output,启动!")
    while True:
        time.sleep(0.1)
        #print("output_ls", output_ls)

        if len(output_ls) == 0:
            continue
        else:
            # 取出第一个元素
            ss = output_ls[0]
            del output_ls[0]
            print(ss, end="")


