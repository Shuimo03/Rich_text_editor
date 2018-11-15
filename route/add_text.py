from flask import request
from uuid import uuid1
from DataBase.dataTable import Text,session
import time

def add():
    nowtime  = time.time()
    nowdate = time.localtime(nowtime)

    # uuid1()保证每次生成的值不会重复，由 MAC 地址（主机物理地址）、当前时间戳、随机数生成。
    # uuid().clock_seq_hi_variant 是指uuid1()前8位。
    #https://docs.python.org/3.1/library/uuid.html
    ID = uuid1().clock_seq_hi_variant
    Content = request.form['Content']
    EndShowDate = request.form['EndShowDate']
    DataCreateTime  = time.strftime("%Y-%m-%d-%H-%M", nowdate)
    text = Text(ID = ID, Content = Content,DataCreateTime = DataCreateTime,EndShowDate = EndShowDate)
    session.add(text)
    session.commit()