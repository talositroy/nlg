from bs4 import BeautifulSoup
import urllib.request  # 引入urllib库
import chardet
import re
import datetime
import time
import os
import linecache


# 数据预处理

def wlog(text):
    path = '../data/log'
    file = open(path, 'a')
    file.write(text + '\n')
    file.close()


# path = '/home/talos/Videos/mako/'
# path_all = '../data/all_data'
# if os.path.isfile(path_all) == False:
#     fd = open(path_all, mode="w", encoding="utf-8")
#     fd.close()
#
# fall = open(path_all, 'w+')
# rall = fall.read()
#

#         f = open(os.path.join(root, file), 'r')
#         r = f.read()
#         r = re.sub('---\n', '', r)
#         i = r.find('+++')
#         r = r[0:i]
#         r += '\n---------\n'
#         fall.write(r)
#         f.close()
# fall.close()

# path = '/mnt/project/NLPandNLG/learning-nlp-master/chapter-5/stopword.txt'
# path_1 = '/mnt/project/NLPandNLG/nlg/data/stopwords.txt'
#
# f1 = open(path_1, 'w')
# msg = []
#
# f = open(path, 'r')
# lines = f.readlines()
# for line in lines:
#     if line not in msg:
#         msg.append(line)
#
# for m in msg:
#     f1.write(m)
#
# f1.close()
