from flask import request
from DataBase.dataTable import Text,session
import time



# 获取数据
def updateText(Content):
    nowtime = time.time()
    nowdate = time.localtime(nowtime)
    updateContent = request.form['updateContent']
    updateEndShowDate = request.form['updateEndShowDate']
    DataCreateTime = time.strftime("%Y-%m-%d-%H-%M", nowdate)
    text = Text(Content=updateContent, DataCreateTime=DataCreateTime, EndShowDate=updateEndShowDate)
    session.query(Text).filter_by(Content = Content).first()
    session.add(text)
    session.commit()