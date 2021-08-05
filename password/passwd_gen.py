#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

length = 12
auto_save = False
passwd_file = "passwd.txt"
passwd_desc = "my website: "
num_list = [chr(i) for i in range(48, 60)]
low_list = [chr(i) for i in range(65, 91)]
up_list = [chr(i) for i in range(97, 123)]
spc_list = ['!', '@', '#', '$']
char_list = num_list + low_list + up_list + spc_list

def gen_passwd():
    passwd = ""
    for i in range(length):
        passwd = passwd + char_list[random.randint(0, len(char_list) - 1)]
    return passwd

def check_passwd(passwd):
    ## 检查大写、小写字母、数字和特殊字符
    up = False
    low = False
    num = False
    spc = False

    for i in passwd:
        if i in num_list:
            num = True
        if i in low_list:
            low = True
        if i in up_list:
            up = True
        if i in spc_list:
            spc = True
    return up and low and num and spc

def save_passwd(passwd):
    file = open(passwd_file, 'a')
    file.write(passwd + '\n')
    file.close()

if __name__ == "__main__":
    ## 读取参数
    i = 1
    while (i < len(sys.argv)):
        if (sys.argv[i] == "-s" and i + 1 != len(sys.argv)):
            passwd_desc = sys.argv[i + 1]
            auto_save = True
            i = i + 2
            continue
        if (sys.argv[i] == "-l" and i + 1 != len(sys.argv)):
            length = int(sys.argv[i + 1], 10)
            i = i + 2
            continue
        if (sys.argv[i] == "-p" and i + 1 != len(sys.argv)):
            passwd_file = sys.argv[i + 1]
            i = i + 2
            continue
        if (sys.argv[i] == "-h"):
            print("生成强密码")
            print("使用方法：")
            print("\tpython passwd_gen.py [选项] {值}")
            print("支持的选项:")
            print("\t-s {description}\t自动将生成的密码保存在文件中，格式为{description}: {password}，若没有指定文件路径，则保存在本目录的passwd.txt中")
            print("\t-p {path}\t\t指定保存密码的文件路径，开启此选项默认需要保存密码")
            print("\t-l {length}\t\t指定生成密码的长度，length必须是一个正数，若不指定该参数，默认值为10")
            print("\t-h\t\t\t显示本帮助")
            exit(0)

    passwd = ""
    while not check_passwd(passwd):
        passwd = gen_passwd()
    print(passwd)
    if auto_save:
        save_passwd(passwd_desc + ": " + passwd)
