class Glob:
    listen = False
    port = "0"
    execute = ""
    command = False
    upload_destination = ""
    target = ""
    upload = False


def set_listen(l):
    Glob.listen = l


def get_listen():
    return Glob.listen


def set_port(p):
    Glob.port = p


def get_port():
    return Glob.port


def set_execute(e):
    Glob.execute = e


def get_execute():
    return Glob.execute


def set_command(c):
    Glob.command = c


def get_command():
    return Glob.command


def set_upd(u):
    Glob.upload_destination = u


def get_upd():
    return Glob.upload_destination


def set_target(t):
    Glob.target = t


def get_target():
    return Glob.target


def set_upload(up):
    Glob.upload = up


def get_upload():
    return Glob.upload
