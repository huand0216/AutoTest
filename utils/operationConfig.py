#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

from configparser import ConfigParser
from common.public_path import get_filePath

def get_configparser(label):
    config = ConfigParser()
    config.read(filenames=get_filePath(dirName="config",fileName="configparser.ini"))
    return dict(config.items(label))

if __name__ == '__main__':
    print(get_configparser("test"))




