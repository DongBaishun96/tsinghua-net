import os
import subprocess
import chardet

from tsinghua_net.tools.parameter import connection_ping_url, tsinghua_wlans


def is_network_connection():
    res = subprocess.Popen("ping " + connection_ping_url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutput, erroutput) = res.communicate()
    encoding = chardet.detect(stdoutput)['encoding']
    output = stdoutput.decode(encoding)
    res = ("TTL=" in output)
    return res


def connect_wlan():
    for wlan_name in tsinghua_wlans:
        null = open(os.devnull, 'w')
        res = subprocess.call('netsh wlan connect name="' + wlan_name,
                              shell=True, stdout=null, stderr=null)
        if not res:
            return True
    return False
