from flask import  render_template
from flask import Flask
from route.add_text import add,session
from route.update_text import update
from DataBase.dataTable import Text

app = Flask(__name__)
@app.route("/")
def text_home():
    return render_template('home.html')

@app.route("/notices/<ID>",methods = ['GET'])
def text_add(ID):
    return render_template("addText.html",ID = Text.ID)

@app.route("/notices/", methods = ['POST'])
def text_submittal():
    add()
    listText = session.query(Text).all()
    return render_template('textList.html', listText= listText)

@app.route("/notices/update/<ID>",methods = ["GET"])
def text_update(ID):
        test = session.query(Text).filter_by(ID =ID).first()
        return  render_template('updateText.html',test =test)

@app.route("/notices/new",methods = ['GET'])
def text_list():
    listText = session.query(Text).all()
    return render_template('textList.html', listText = listText)

if __name__ == '__main__':
    app.run(debug=True)