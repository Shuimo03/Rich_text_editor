from flask import request
from DataBase.dataTable import Text,session

# 获取数据
def update():
    Text.Content = request.form['Content']
    Text.EndShowDate = request.form['EndShowDate']
    session.commit()