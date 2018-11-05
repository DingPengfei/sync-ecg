# -*- coding: utf8 -*-


class HLYHeader:
    def __init__(self, file_path):
        self.file_path = file_path
        # try:
        with open(self.file_path, 'rb') as f:
            self.company_name = f.read(20)
            self.version = f.read(4)
            self.ecg_wave = f.read(2)
            self.ecg_feq = f.read(2)
            self.other_wave = f.read(1)
            self.other_feq = f.read(16)
            if self.version == b'\x03\x00\x00\x01' or self.version == b'\x03\x01\x00\x01':
                self.file_length = f.read(4)
            elif self.version == b'\x04\x00\x00\x00':
                self.file_length = f.read(8)
            self.data_length = f.read(4)
            self.begin_time = f.read(6)
            self.end_time = f.read(6)
            self.crc_head = f.read(4)
            self.crc_data = f.read(4)
            self.id = f.read(50)
            print(self.file_path + " ID is =====> " + self.id.decode())
            self.name = f.read(50)
            self.birthday = f.read(20)
            self.sex = f.read(10)
            if self.version == b'\x03\x00\x00\x01' or self.version == b'\x03\x01\x00\x01':
                self.age = f.read(10)
            elif self.version == b'\x04\x00\x00\x00':
                self.age = f.read(50)
            self.height = f.read(20)
            self.weight = f.read(20)
            self.phone = f.read(50)
            self.unit = f.read(100)
            self.address = f.read(200)
            self.e_name = f.read(50)
            self.e_phone = f.read(50)
            self.bed = f.read(50)
            self.doctor = f.read(50)
            self.remark = f.read(500)
            if self.version == b'\x03\x00\x00\x01' or self.version == b'\x03\x01\x00\x01':
                self.field = b''
                self.reserved = f.read(697)
            elif self.version == b'\x04\x00\x00\x00':
                self.field = f.read(4)
                self.reserved = f.read(649)
        self.header = {
            'company_name': self.company_name,
            'version': self.version,
            'ecg_wave': self.ecg_wave,
            'ecg_feq': self.ecg_feq,
            'other_wave': self.other_wave,
            'other_feq': self.other_feq,
            'file_length': self.file_length,
            'data_length': self.data_length,
            'begin_time': self.begin_time,
            'end_time': self.end_time,
            'crc_head': self.crc_head,
            'crc_data': self.crc_data,
            'id': self.id,
            'name': self.name,
            'birthday': self.birthday,
            'sex': self.sex,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'phone': self.phone,
            'unit': self.unit,
            'address': self.address,
            'e_name': self.e_name,
            'e_phone': self.e_phone,
            'bed': self.bed,
            'doctor': self.doctor,
            'remark': self.remark,
            'field': self.field,
            'reserved': self.reserved,
            'content': ''
            }
        # except Exception:
        #     print("解析文件出错")

    def get_header(self):
            return self.header


class HLWHeader:
    def __init__(self, file_path):
        self.file_path = file_path
        # try:
        with open(self.file_path, 'rb') as f:
            self.company_name = f.read(20)
            self.version = f.read(4)
            self.ecg_wave = f.read(16)
            self.ecg_feq = f.read(2)
            self.file_length = f.read(4)
            self.data_length = f.read(4)
            self.begin_time = f.read(6)
            self.end_time = f.read(6)
            self.crc_head = f.read(4)
            self.crc_data = f.read(4)
            self.id = f.read(50)
            print(self.file_path + " ID is =====> " + self.id.decode())
            self.name = f.read(50)
            self.bed = f.read(50)
            self.birthday = f.read(20)
            self.sex = f.read(10)
            self.age = f.read(10)
            self.height = f.read(20)
            self.weight = f.read(20)
            self.phone = f.read(50)
            self.unit = f.read(100)
            self.address = f.read(200)
            self.e_name = f.read(50)
            self.e_phone = f.read(50)
            self.doctor = f.read(50)
            self.remark = f.read(500)
            self.reserved = f.read(697)

        self.header = {
            'company_name': self.company_name,
            'version': self.version,
            'ecg_wave': self.ecg_wave,
            'ecg_feq': self.ecg_feq,
            'file_length': self.file_length,
            'data_length': self.data_length,
            'begin_time': self.begin_time,
            'end_time': self.end_time,
            'crc_head': self.crc_head,
            'crc_data': self.crc_data,
            'id': self.id,
            'name': self.name,
            'birthday': self.birthday,
            'sex': self.sex,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'phone': self.phone,
            'unit': self.unit,
            'address': self.address,
            'e_name': self.e_name,
            'e_phone': self.e_phone,
            'bed': self.bed,
            'doctor': self.doctor,
            'remark': self.remark,
            'reserved': self.reserved,
            'content': ''
            }
        # except Exception:
        #     print("解析文件出错")

    def get_header(self):
            return self.header
