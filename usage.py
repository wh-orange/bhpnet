def usage():
    print "BHP Net Tool\n"
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen                   - listen on [host]:[port] \
    for incoming connection"
    print "-e --execute=file_to_run      - execute the given file  \
    upon receiving a connection"
    print "-c --command                  - initialize a command shell"
    print "-u --upload=destination       -upon receiving connection\
     upload a file and write to [destination]"
    print "\n\n"
    print "Examples: "
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print r"bhpnet.py -t 192.168.1.1 -p 5555 -l -u=c:\\target.exe"
    print r'bhpnet.py -t 192.168.1.1 -p 5555 -l -e=\"cat /etc/passwd"'
    print "echo 'ABCDEFGHI' |  ./bhpnet.py -t 192.168.11.12 -p 135"
