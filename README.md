# Tsinghua-net
本项目针对清华校园网。
脚本挂起来，科研不断网！
让你的远程主机不再断网！

## 安装步骤

## 配置Python环境
## pip安装

```shell script
pip install git+https://github.com/DongBaishun96/tsinghua-net.git
```

## 使用说明
### 登录
```shell script
## 有线连接
tsinghua_net login -u xxx -p xxxxx
## 无线连接
tsinghua_net login -u xxx -p -w wireless
```

### 登出
```shell script
tsinghua_net logout
```

### 查看使用信息
```shell script
tsinghua_net status
```

### 循环检测，防止掉线
```shell script
## 有线连接
tsinghua_net schedule -u xxx -p xxxxx
## 无线连接
tsinghua_net schedule -u xxx -p -w wireless
```
### 加入开机启动
```shell
/bin/sh ./autostart.sh
```


## 卸载脚本
```shell script
pip uninstall tsinghua_net
```

## 感谢

- 各位开源的同学们
- @DongBaishun
- @YjGit
