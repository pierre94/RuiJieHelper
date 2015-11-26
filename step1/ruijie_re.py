# encoding: gbk
"""
@version: 1.0
@author: pierre94
@license: Apache Licence 
@contact: admin@bear2.cn
@site: www.bear2.cn
@software: PyCharm Community Edition
@file: ruijie_re.py
@time: 2015/11/26 15:23
"""
import re
def find_flow(content):
    return re.search('国内下行流量:([0-9.]*)[ GB]*([0-9.]*) MB /([0-9.]*) GB ([0-9.]*) MB', content)

def find_money(content):
    return re.search('([0-9.]*)</span>元',content).group(1)

