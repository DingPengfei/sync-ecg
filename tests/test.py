# -*- coding: utf-8 -*-
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    file = 'D:\\PycharmProjects\\sync-ecg\\files\\新建文件夹\\新建文件夹\\新建文本文档.txt'
    # # print file
    # print file.split('\\')[-1]
    tmp1 = b'\x04\x00\x00\x00'
    tm = tmp1[0]
    tmp = tmp1.decode()
    tmp2 = '4000'.encode()
    tmp3 = '丁鹏飞'.encode()
    tmp4 = '4'.encode()

    a1 = '3cca346364514503b73d4cfca00df3fa'[::-1]

    print(a1)

    pass

