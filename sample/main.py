# -*- coding: utf-8 -*-

from configparser import ConfigParser
from watchdir import monitor
from fileprocess import FileProcess
import os

cfg = ConfigParser()
cfg.read('..\\config.ini')
path = cfg.get('directory', 'local_ecg_directory')
sync_type = cfg.get('upload', 'type')
uploaded = cfg.get('file', 'uploaded')
postfix_list = cfg.get('file', 'postfix').split(',')


def read_uploaded():
    file_context = open(uploaded).read().splitlines()  # file_context是一个list，每行文本内容是list中的一个元素
    return set(file_context)


def write_uploaded(file_name):
    # 打开一个文件
    fo = open(uploaded, "a")
    fo.write(file_name + '\n')
    # 关闭打开的文件
    fo.close()


def find_file(directory):
    directory = directory + '\\'
    files = os.listdir(directory)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        if os.path.isfile(directory + file):  # 判断是否是文件
            file_postfix = file.split('.')[-1]
            if file_postfix in postfix_list:
                file_processor = FileProcess(directory + file)
                file_processor.process_file(file_postfix)
        else:
            find_file(directory + file)


def first_upload():
    # 第一次导入全部文件
    find_file(path)


def offline_upload(directory):
    directory = directory + '\\'
    files = os.listdir(directory)  # 得到文件夹下的所有文件名称
    uploaded_set = read_uploaded()
    for file in files:  # 遍历文件夹
        if os.path.isfile(directory + file):  # 判断是否是文件
            file_postfix = file.split('.')[-1]
            if file_postfix in postfix_list:
                if file not in uploaded_set:
                    file_processor = FileProcess(directory + file)
                    file_processor.process_file(file_postfix)
                    write_uploaded(file)
        else:
            find_file(directory + file)


def main():
    if sync_type == 'online':
        first_upload()
        monitor(path)
    elif sync_type == 'offline':
        offline_upload(path)

if __name__ == '__main__':
    main()
