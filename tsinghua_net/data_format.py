# Response结果转换格式


def format_time(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return '%02d:%02d:%02d' % (h, m, s)


def format_usage(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.2f%s" % (value, units[i])
        value = value / size


def username_valid(username):
    if username is None or len(username) == 0:
        print('username cannot be empty\n')
        return False
    return True


def password_valid(password):
    if password is None or len(password) == 0:
        print('password cannot be empty\n')
        return False
    return True


def wireless_valid(wireless):
    if wireless is None or wireless != 'wireless':
        print('wireless is invalid\n')
        return False
    return True
