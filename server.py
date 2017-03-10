#-*-coding:utf-8-*-
import socket
import threading
import subprocess
import traceback

import globalvar as gbv


def server_loop():

    # 如果没有定义目标则监听所有接口
    if not len(gbv.get_target()):
        target = "0.0.0.0"
        gbv.set_target(target)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((gbv.get_target(), int(gbv.get_port())))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # 分拆一个线程处理新的客户端
        client_thread = threading.Thread(target=client_handler, args=(
            client_socket,))
        client_thread.start()


def client_handler(client_socket):

    if len(gbv.get_upd()):
        file_buffer = ""
        while True:
            data = client_socket.recv(4096)
            # bug
            if not data:
                break
            else:
                file_buffer += data
                client_socket.send("data received")
                break  # youbug qiangxingtiaoguo

        try:
            file_descriptor = open(gbv.get_upd(), "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send(
                "Successfully saved fied to %s\r\n" % gbv.get_upd())
        except:
            client_socket.send(
                "Failed to sava file to %s\r\n" % gbv.get_upd())

    if len(gbv.get_execute()):
        output = run_command(gbv.get_execute())
        client_socket.send(output)

    if gbv.get_command():
        try:
            while True:
                # 跳出一个窗口
                client_socket.send("<BHP:#> ")
                # 接受文件直到发现换行符（enter key）
                cmd_buffer = ""
                while "\n" not in cmd_buffer:
                    cmd_buffer += client_socket.recv(1024)
                    # 返回命令输出
                    response = run_command(cmd_buffer)
                    # 返回响应数据
                    client_socket.send(response)
        except:
            print "client quit"


def run_command(command):
    command = command.rstrip()
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n"

    return output
