from flask import request
from DataBase.dataTable import Text,session

# 获取数据
def update():
    updateContent = session.query(Text).filter_by(Content = Text.Content).first()
    updateContent.Content = request.form['Content']

