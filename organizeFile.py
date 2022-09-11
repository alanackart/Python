"""
organize file by date
"""
import unittest
import os
from datetime import datetime
from pathlib import Path
import shutil


def make_full_path(prefix, filename):
    return prefix + "\\" + filename


class MyTestCase(unittest.TestCase):

    def test_something(self):
        source_dir = r'G:\DCIM\102ND750'
        target_dir = r'F:\Nikon'
        for filename in os.listdir(source_dir):
            print(filename)
            source_file_path = make_full_path(source_dir, filename)
            if not Path(source_file_path).is_dir():
                ts = int(os.path.getmtime(source_file_path))
                folder = make_full_path(target_dir, datetime.utcfromtimestamp(ts).strftime('%Y%m%d'))
                if not Path(folder).exists():
                    os.makedirs(folder)
                print(folder)
                target_name = make_full_path(folder, filename)
                print(target_name)
                try:
                    if Path(target_name).exists():
                        print(target_name + " exist!")
                    else:
                        shutil.move(source_file_path, target_name)
                except Exception as err:
                    print("FileExistsError: {0}".format(err))


if __name__ == '__main__':
    unittest.main()
