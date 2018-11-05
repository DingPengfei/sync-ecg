# -*- coding: utf-8 -*-

import os
from tohdfs import HdfsOperation
from tohbase import HbaseOperation
from parseheader import HLWHeader
from parseheader import HLYHeader
from configparser import ConfigParser


class FileProcess:

    def __init__(self, file_path):
        cfg = ConfigParser()
        cfg.read('..\\config.ini')
        self.__hdfs_path = cfg.get('directory', 'hdfs_directory')
        self.__file_path = file_path

    def get_file_size(self):
        # filePath = unicode(filePath, 'utf8')
        fsize = os.path.getsize(self.__file_path)
        fsize = fsize/float(1024*1024)
        return round(fsize, 2)

    def read_file(self):
        binFile = open(self.__file_path, 'rb').read()
        return binFile

    def process_file(self, file_type):
        file_size = self.get_file_size()
        if file_type == 'hly':
            header = HLYHeader(self.__file_path).get_header()
            hbase_operation = HbaseOperation()
            if file_size > 10:
                header['content'] = self.__hdfs_path + self.__file_path.split('\\')[-1]
                hbase_operation.put_hly(header)
                HdfsOperation.add2hdfs(self.__file_path, self.__hdfs_path)
                print("file " + self.__file_path + " has uploaded to Hbase and HDFS")
            else:
                header['content'] = self.read_file()
                hbase_operation.put_hly(header)
                print("file " + self.__file_path + " has uploaded to Hbase")
        else:
            header = HLWHeader(self.__file_path).get_header()
            hbase_operation = HbaseOperation()
            if file_size > 10:
                header['content'] = self.__hdfs_path + self.__file_path.split('\\')[-1]
                hbase_operation.put_hlw(header)
                HdfsOperation.add2hdfs(self.__file_path, self.__hdfs_path)
                print("file " + self.__file_path + " has uploaded to Hbase and HDFS")
            else:
                header['content'] = self.read_file()
                hbase_operation.put_hlw(header)
                print("file " + self.__file_path + " has uploaded to Hbase")
