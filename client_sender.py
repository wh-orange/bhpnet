#-*-coding:utf-8-*-
import socket
import globalvar as gbv


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接目标主机

        client.connect((gbv.get_target(), int(gbv.get_port())))

        if len(buffer):
            client.send(buffer)

        while True:
            # 等待数据回传
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print response

            # 等待更多输入
            buffer = raw_input("")
            buffer += "\n"
            client.send(buffer)

    except:
        print "[*] Exception! Exiting."

    client.close()
