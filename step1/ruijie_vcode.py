# encoding: gbk
"""
@version: 1.0
@author: pierre94
@license: Apache Licence 
@contact: admin@bear2.cn
@site: www.bear2.cn
@software: PyCharm Community Edition
@file: ruijie_vcode.py
@time: 2015/11/26 15:14
"""
from PIL import Image
import pytesseract

def handle_vcode(file):
    #file = cStringIO.StringIO(requests.get(code_url, headers = headers).content)
    image = Image.open(file)
    a=pytesseract.image_to_string(image)
    return a