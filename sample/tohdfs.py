# -*- coding: utf8 -*-

from hdfs import InsecureClient
from configparser import ConfigParser


class HdfsOperation:

    def __init__(self):
        cfg = ConfigParser()
        cfg.read('..\\config.ini')
        self.client_hdfs = InsecureClient(cfg.get('hdfs', 'url'))

    def add2hdfs(self, file_path, hdfs_path):
        # client_hdfs = InsecureClient('http://192.168.9.224:50070')
        try:
            # 默认文件名称不会重复
            self.client_hdfs.upload(hdfs_path + file_path.split('\\')[-1], file_path)
        except Exception:
            print("文件上传出现错误！")
