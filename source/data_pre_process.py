from bs4 import BeautifulSoup
import urllib.request  # 引入urllib库
import chardet
import re
import datetime
import time
import os
import linecache


def wlog(text):
    path = '../data/log'
    file = open(path, 'a')
    file.write(text + '\n')
    file.close()


path = '../data/202002'
path_all = '../data/all_data'
if os.path.isfile(path_all) == False:
    fd = open(path_all, mode="w", encoding="utf-8")
    fd.close()

fall = open(path_all, 'w+')
rall = fall.read()

for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
        f = open(os.path.join(root, file), 'r')
        r = f.read()
        r = re.sub('---\n', '', r)
        i = r.find('+++')
        r = r[0:i]
        r += '\n---------\n'
        fall.write(r)
        f.close()
fall.close()
