##RuiJieHelper step 1
###
###1.0 基本说明
锐捷查询脚本，内有文件：

* ruijie_main.py
    主文件，目前内容还耦合在ruijie_spider.py里，故目前为空
* ruijie_spider.py
    目前的主文件，包含爬取页面部分
* ruijie_re.py
    自定义的正则文件，包含目前需要用到的正则函数
* ruijie_db.py
    自定义的数据库操作文件，包含所有的数据库操作函数
* ruijie_vcode.py
    自定义的验证码识别文件
* ruijie.sql
    mysql的sql语句

###
###2.0 安装说明
2.1 相关库的安装，若验证码的库安装错误，可以查阅[python的验证码识别](http://blog.bear2.cn/post/13) 

2.2 mysql数据库，建立新库ruijie，导入ruijie.sql

2.3 现在是运行ruijie_spider.py

###
###3.0 最后
目前问题比较多，希望有人加入来解决更多问题 admin@bear2.cn

