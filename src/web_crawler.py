from bs4 import BeautifulSoup
import urllib.request  # 引入urllib库
import chardet
import re
import datetime
import time
import os


def wlog(text):
    path = '../data/log'
    file = open(path, 'a')
    file.write(text + '\n')
    file.close()


def get_url_date(url):
    date = []
    start = url.find('html/') + len('html/')
    syear = url[start:start + 4]
    smonth = url[start + 5:start + 7]
    sday = url[start + 8:start + 10]
    date.append(syear)
    date.append(smonth)
    date.append(sday)
    return date


def get_url_text(url):
    try:
        time.sleep(0.2)
        response = urllib.request.urlopen(url)  # 发出请求并且接收返回文本对象
        html = response.read()  # 调用read()进行读取
        chardit = chardet.detect(html)  # 获取文本编码
        html_text = html.decode(chardit['encoding'])
        return html_text
    except:
        print('========= cant open url =========')
        print(url)
        wlog(url)
        print('=========')
        return -1


# 根据首页获取当天总版面目录url
# 返回版面目录url的list
def get_mulu_over(url) -> list:
    mulu_over_list = []
    html_text = get_url_text(url)
    if html_text != -1:
        soup = BeautifulSoup(html_text, 'lxml')
        date = get_url_date(url)
        for t in soup.find_all('a', id='pageLink'):
            mulu = re.sub('./', '', t.get('href'))
            mulu = 'http://paper.people.com.cn/rmrb/html/' + date[0] + '-' + date[1] + '/' + date[2] + '/' + mulu
            mulu_over_list.append(mulu)
        return mulu_over_list
    else:
        return -1


# 根据版面目录进入的页面来获取该版面的所有文章的url
def get_mulu_sub(url) -> list:
    article_list = []
    html_text = get_url_text(url)
    if html_text != -1:
        soup = BeautifulSoup(html_text, 'lxml')
        date = get_url_date(url)
        for t in soup.find_all(re.compile('area', re.I)):
            article = 'http://paper.people.com.cn/rmrb/html/' + date[0] + '-' + date[1] + '/' + date[
                2] + '/' + t.get(
                'href')
            article_list.append(article)
        return article_list
    else:
        return -1


# 根据文章url获取文章内容并写入文件
def set_content_url(url, file_name):
    date = get_url_date(url)
    path = '/mnt/project/NLPandNLG/DeepTalos/data/人民日报/' + date[0] + '/' + date[0] + date[1] + '/'
    if not os.path.exists(path):
        os.makedirs(path)
    filepath = path + file_name
    if os.path.exists(filepath):
        file = open(filepath, 'r+')
        c = file.read()
        if '\n+++\n' not in c:
            msg = '\n+++\n' + url + '\n+++'
            file.write(msg)
            file.close()
            print(str(file_name) + ' completed !')
    else:
        html_text = get_url_text(url)
        if html_text != -1:
            date = get_url_date(url)
            tstart = '<founder-title>'
            tend = '</founder-title>'
            title = html_text[html_text.find(tstart) + len(tstart):html_text.find(tend)]
            title = re.sub('\n+', '', title)
            title = re.sub('\r+', '', title)
            title = '---' + title + '---\n'

            # 文章开始标记
            str_start = '<!--enpcontent--><P mce_keep="true">'
            # 文章结束标记
            str_end = '</P><!--/enpcontent-->'
            # 换行符标记
            str_huanhang1 = '</P><P>'
            str_huanhang2 = '</P>\r+\n+<P>'
            str_huanhang3 = '</P>\r+\n+<P mce_keep="true">'

            str_copy = '<!-- 以下是供复制全文用 -->'
            fstart = html_text.find(str_copy)
            istart = html_text.find(str_start, fstart)
            iend = html_text.find(str_end, fstart)
            if istart == -1:
                # 文章开始标记
                str_start = '<founder-content><P>'
                # 文章结束标记
                str_end = '</P></founder-content>'
                istart = html_text.find(str_start, fstart)
                iend = html_text.find(str_end, fstart)
            if istart == -1:
                wlog('content error ::: ' + url)
                return
            article = html_text[istart: iend]
            article = re.sub(str_start, '', article)
            article = re.sub(str_end, '', article)
            article = re.sub(str_huanhang1, '\n', article)
            article = re.sub(str_huanhang2, '\n', article)
            article = re.sub(str_huanhang3, '\n', article)
            article = re.sub('　　', '\n', article)
            article = re.sub('&nbsp;', ' ', article)
            if article == '':
                return
            # msg = title + '\n=========\n' + article
            msg = title + article
            msg += '\n+++\n' + url + '\n+++'
            msg = re.sub('---', '\n---\n', msg)
            msg = re.sub('\n---', '---', msg, 1)
            msg = re.sub('\n+', '\n', msg)
            msg = re.sub('\n+', '\n', msg)

            if not os.path.exists(path):
                os.makedirs(path)
            file = open(filepath, 'w')
            file.write(msg)
            file.close()
            print(str(file_name) + ' completed !')

        else:
            return


def do_from_url(url):
    mulu_list = get_mulu_over(url)
    banhao = 0
    date = get_url_date(url)
    if mulu_list != -1:
        for mlist in mulu_list:
            banhao += 1
            wenzhanghao = 0
            mulu_sub = get_mulu_sub(mlist)
            if mulu_sub != -1:
                for msub in mulu_sub:
                    wenzhanghao += 1
                    fname = date[0] + date[1] + date[2] + '_' + str(banhao).zfill(2) + '_' + str(wenzhanghao).zfill(2)
                    set_content_url(msub, fname)


# url_0 = 'http://paper.people.com.cn/rmrbhwb/html/2008-06/12/node_865.htm'

# dstart = datetime.date(2019, 11, 10)
# dend = datetime.date(2018, 12, 31)
#
# dt = dstart - dend
#
# for i in range(dt.days):
#     day = dstart - datetime.timedelta(days=i)
#     dyear = day.year
#     dmonth = day.month
#     dday = day.day
#     url = 'http://paper.people.com.cn/rmrb/html/' + \
#           str(dyear) + '-' + str(dmonth).zfill(2) + '/' + str(dday).zfill(2) + \
#           '/nbs.D110000renmrb_01.htm'
#     do_from_url(url)

f = open('/mnt/project/NLPandNLG/DeepTalos/data/log', 'r')
lines = f.readlines()
for line in lines:
    date = get_url_date(line)
    i = line.index(date[0] + date[1] + date[2]) + len(date[0] + date[1] + date[2]) + 3
    j = line.index('.htm')
    banhao = line[i:j]
    k = line.index(date[0] + date[1] + date[2] + '_') + len(date[0] + date[1] + date[2] + '_')
    xuhao = line[k:k + 1].zfill(2)
    fname = date[0] + date[1] + date[2] + '_' + banhao + '_' + xuhao
    set_content_url(line, fname)