from flask import  render_template
from flask import Flask
from route.add_text import add,session
from route.update_text import update
from DataBase.dataTable import Text

app = Flask(__name__)
@app.route("/")
def text_home():
    return render_template('home.html')

@app.route('/text/api/test1.0/content',methods = ['GET'])
def text_add():
    return render_template("addText.html")

@app.route("/text/api/test1.0/content",methods = ['POST'])
def text_submittal():
    add()
    listText = session.query(Text).all()
    return render_template('textList.html', listText = listText)

@app.route("/text/api/test1.0/update",methods = ['GET'])
def text_update():
    update()
    render_template('updateText.html')

if __name__ == '__main__':
    app.run(debug=True)