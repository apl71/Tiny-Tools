# Tiny-Tools

## password

生成强密码
使用方法：
        python passwd_gen.py [选项] {值}
支持的选项:
        -s {description}        自动将生成的密码保存在文件中，格式为{description}: {password}，若没有指定文件路径，则保存在本目录的passwd.txt中
        -p {path}               指定保存密码的文件路径，开启此选项默认需要保存密码
        -l {length}             指定生成密码的长度，length必须是一个正数，若不指定该参数，默认值为10
        -h                      显示本帮助
