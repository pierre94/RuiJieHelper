# encoding: gbk
"""
@version: 1.0
@author: pierre94
@license: Apache Licence 
@contact: admin@bear2.cn
@site: www.bear2.cn
@software: PyCharm Community Edition
@file: ruijie_spider
@time: 2015/11/26 15:13
"""
import cStringIO
import ruijie_db
import ruijie_vcode
import requests
import ruijie_re

def select(school_no,password):
    url = 'http://self.nwpu.edu.cn:8080/selfservice/module/scgroup/web/login_judge.jsf'
    code_url = 'http://self.nwpu.edu.cn:8080/selfservice/common/web/verifycode.jsp'
    cookie = requests.get('http://self.nwpu.edu.cn:8080/selfservice/entry.jsp').headers['set-cookie']
    headers = {'cookie':cookie}
    mistake = 1
    while(mistake == 1):
        code_img = cStringIO.StringIO(requests.get(code_url, headers = headers).content)
        code = ruijie_vcode.handle_vcode(code_img)

        payload = {"verify" : code, "password" : password, "name" : school_no, 'act' : 'add'}
        r = requests.post(url, data = payload, headers = headers)
        if r.content.find("verfiyError") == -1:
            mistake = 0
    res = requests.get('http://self.nwpu.edu.cn:8080/selfservice/module/webcontent/web/content_self.jsf', headers = headers)
    try:
        flow=ruijie_re.find_flow(res.content)
        money=ruijie_re.find_money(res.content)
        Used_G = float(flow.group(1))
        Used_M = (flow.group(2))
        All_G = float(flow.group(3))
        All_M = float(flow.group(4))

        if(Used_G==All_G):
            print "您的套餐内"+str(All_G)+"GB流量已经用完"
            print '账户余额还有' +money+"元"
        else:
            if((Used_M) == ''):
                #此处处理特殊用户的数据
                Used_M = Used_G
                Used_G= 0

            else:
                Used_M = float(Used_M)

            if All_M <= Used_M:
                mb = 1024 - Used_M
                gb = All_G - Used_G - 1
            else:
                mb = All_M - Used_M
                gb = All_G - Used_G
            print '您的套餐'+str(All_G)+'GB流量，'+'还有' + str(gb) + ' GB ' + str(mb) + ' MB '

    except:
        print "password is error!!!!\n"

def main():
    data=ruijie_db.select_user()
    if data:
        no=1
        for rec in data:
            print "#"*20
            print "第"+str(no)+"个账号的信息"
            print "账号"+rec[1]
            select(rec[1],rec[2])
            no+=1

if __name__ == '__main__':
    main()
