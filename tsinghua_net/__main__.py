# Copyright [dongbaishun] [dongbaishun]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import requests
import argparse
import hashlib
import schedule
import time

from tsinghua_net.data_format import format_time, format_usage, username_valid, wireless_valid
from tsinghua_net.tsinghua_wifi import is_network_connection, connect_wlan
from tsinghua_net.parameter import login_url, status_url, headers
from urllib3.exceptions import ProtocolError

connection_type = 0  # 0代表有线连接，1代表无线连接


# 登录
def login(username, password):
    if connection_type == 1:
        is_network_connection()
        if connect_wlan():
            time.sleep(5)
        else:
            print('connect WLAN failed.\n')
            return
    try:
        password = '{MD5_HEX}' + hashlib.md5(password.encode('utf-8')).hexdigest()
        data = {
            'action': 'login',
            'username': username,
            'password': password,
            'ac_id': 1
        }

        resp = requests.post(login_url, data=data, headers=headers)
        print(resp.text)
        status()
    except (ConnectionResetError, ProtocolError, requests.exceptions.ConnectionError):
        login(username, password)


# 注销
def logout():
    try:
        data = {
            'action': 'logout'
        }

        resp = requests.post(login_url, data=data, headers=headers)
        print(resp.text)
    except (ConnectionResetError, ProtocolError, requests.exceptions.ConnectionError):
        logout()


# 查询状态
def status():
    try:
        resp = requests.post(status_url, headers=headers)
        if resp.status_code == 500:
            print('connect network failed, check system proxy.\n')
            return
        if len(resp.text) == 0:
            print('user not login.\n')
            return
        resp_fields = resp.text.split(',')
        online_time = int(resp_fields[2]) - int(resp_fields[1])
        data_usage = int(resp_fields[6])
        print("network status:\n  username: %s\n  IP: %s\n  online-time %s\n  data-usage: %s"
              % (resp_fields[0], resp_fields[8], format_time(online_time), format_usage(data_usage)))
    except (ConnectionResetError, ProtocolError, requests.exceptions.ConnectionError):
        status()


# 定时任务（5分钟登录一次，防止断网）
def schedule_job(username, password):
    print("Keep network online...\n")
    schedule.every(5).minutes.do(login, username, password)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    global connection_type
    parser = argparse.ArgumentParser(description='Tsinghua network tools')
    parser.add_argument('action', help='login / logout / status / schedule')
    parser.add_argument('--username', '-u')
    parser.add_argument('--password', '-p')
    parser.add_argument('--wireless', '-w',)
    args = parser.parse_args()
    if args.action == 'login':
        if not username_valid(args.username):
            return
        if not username_valid(args.password):
            return
        if wireless_valid(args.wireless):
            connection_type = 1
        login(args.username, args.password)
    elif args.action == 'logout':
        logout()
    elif args.action == 'status':
        status()
    elif args.action == 'schedule':
        if not username_valid(args.username):
            return
        if not username_valid(args.password):
            return
        if wireless_valid(args.wireless):
            connection_type = 1
        schedule_job(args.username, args.password)


if __name__ == '__main__':
    main()
