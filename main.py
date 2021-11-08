# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pytest
import pytest_html
import allure
import os
from common.public_path import get_filePath

if __name__ == '__main__':
    # pytest.main(["-v","-s", "./tests/"])
    pytest.main(["-v", "-s", "./tests/", "--alluredir",
                 "{0}/result".format(get_filePath(dirName="report", fileName=""))])
    import subprocess

    os.environ["PATH"] += os.pathsep + '/Users/administrator/.allure-2.7.0/bin'
    subprocess.call(
        'allure generate {0}/result/ -o {1}/html --clean'.format(get_filePath(dirName="report", fileName=""),
                                                                 get_filePath(dirName="report", fileName="")),
        shell=True)
    # subprocess.call('allure open -h 127.0.0.1 -p 8088 {0}/html'.format(Public_path().get_path(dirname="report",filename="")),shell=True)