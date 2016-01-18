import unittest
from Capter9 import FileMane


class Capter9Test(unittest.TestCase):
    def setUp(self):
        self.data_read_type = ["read", "readline", "readlines"]
        self.data_seek = [21, 2, 2]
        self.data_write_type = ["write", "writelines"]
        self.data_write = "\nwrite\n"
        self.data_writelines = ["\nwritelines\n", "\nwrite lines\n"]


    def test_fileman_read(self):
        file = FileMane()
        print file.read(self.data_read_type[0]).decode("GBK").encode("utf-8")
        print file.read(self.data_read_type[1]).decode("GBK").encode("utf-8")
        for r in file.read(self.data_read_type[2]):
            print r.decode("GBK").encode("utf-8")
        file.read(0)

    def test_fileman_reads(self):
        file = FileMane()
        print file.reads(self.data_read_type[0], self.data_seek[0]).decode("GBK").encode("utf-8")
        print file.reads(self.data_read_type[1], self.data_seek[1]).decode("GBK").encode("utf-8")
        for r in file.reads(self.data_read_type[2], self.data_seek[2]):
            print r.decode("GBK").encode("utf-8")

    def test_fileman_write(self):
        file = FileMane()
        file.write(self.data_write_type[0], self.data_write)
        file.write(self.data_write_type[1], self.data_writelines)

    def test_fileman_seek(self):
        file = FileMane()
        file.seek()

    def test_filter_comments(self):
        file = FileMane()
        file.filter_comments()
        for line in file.filter_comment:
            print line