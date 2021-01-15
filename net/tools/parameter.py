# 接口请求参数

login_url = 'http://net.tsinghua.edu.cn/do_login.php'
status_url = 'http://net.tsinghua.edu.cn/rad_user_info.php'
connection_ping_url = 'net.tsinghua.edu.cn'

headers = {
    'Host': 'net.tsinghua.edu.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                       Chrome/87.0.4280.141 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'http://net.tsinghua.edu.cn',
    'Referer': 'http://net.tsinghua.edu.cn/wired/succeed.html?online',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

request_exception_keyword = "远程主机强迫关闭了一个现有的连接"

tsinghua_wlans = ['Tsinghua-Secure', 'Tsinghua-IPv4']
