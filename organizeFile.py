import unittest
import os
from datetime import datetime
from pathlib import Path

"""
organize file by date
"""
def make_full_path(prefix, filename):
    return prefix + "\\" + filename


class MyTestCase(unittest.TestCase):

    def test_something(self):
        paths = r'G:'
        for filename in os.listdir(paths):
            print(filename)
            fullPath = make_full_path(paths, filename)
            if not Path(fullPath).is_dir():
                ts = int(os.path.getmtime(fullPath))
                folder = make_full_path(paths, datetime.utcfromtimestamp(ts).strftime('%Y%m%d'))
                if not Path(folder).exists():
                    os.makedirs(folder)
                print(folder)
                target = make_full_path(folder, filename)
                print(target)
                os.rename(fullPath, target)


if __name__ == '__main__':
    unittest.main()
