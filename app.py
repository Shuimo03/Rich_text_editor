from flask import  render_template
from flask import Flask
from route.add_text import add,session
from route.update_text import updateText
from DataBase.dataTable import Text

app = Flask(__name__)
@app.route("/")
def text_home():
    return render_template('home.html')

@app.route("/notices/",methods = ['GET'])
def text_add():
    return render_template("addText.html")

@app.route("/notices/", methods = ['POST'])
def text_submittal():
    add()
    listText = session.query(Text).all()
    return render_template('textList.html', listText= listText)

@app.route("/notices/<ID>",methods = ["GET"])
def text_update(ID):
        text = session.query(Text).filter_by(ID =ID).first()
        return  render_template('updateText.html',text =text)

#在原本内容上进行修改，但是不会覆盖原来内容
@app.route("/notices/<Content>",methods = ["POST"])
def sumbit_update(Content):
    updateText(Content = Content)
    listText = session.query(Text).all()
    return render_template('textList.html', listText=listText)

@app.route("/notices/new",methods = ['GET'])
def text_list():
    listText = session.query(Text).all()
    return render_template('textList.html', listText = listText)

if __name__ == '__main__':
    app.run(debug=True)