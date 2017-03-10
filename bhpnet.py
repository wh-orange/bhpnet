#-*-coding:utf-8-*-
import sys
import socket
import getopt
import threading
import subprocess

import usage as ug
import client_sender as c_s
import server
import globalvar as gbv


def main():

    if not len(sys.argv[1:]):
        ug.usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", [
            "help", "listen", "execute=", "target=", "port=", "command", "upload="])
    except getopt.GetoptError as err:
        print str(err)
        ug.usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            ug.usage()
        elif o in ("-l", "--listen"):
            gbv.set_listen(True)
        elif o in ("-e", "--execute"):
            gbv.set_execute(a)
        elif o in ("-t", "--target"):
            gbv.set_target(a)
        elif o in ("-p", "--port"):
            gbv.set_port(a)
        elif o in ("-c", "--command"):
            gbv.set_command(True)
        elif o in ("-u", "--upload"):
            gbv.set_upd(a)
        else:
            assert False, "Unhandled Option"

# 选择监听还是从标准输入发送数据
    if not gbv.get_listen() and len(gbv.get_target()) and gbv.get_port() > 0:
        buffer = sys.stdin.read()
        c_s.client_sender(buffer)

    if gbv.get_listen():
        server.server_loop()

main()
