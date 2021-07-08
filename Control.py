from flask import Flask,render_template, request, redirect
from App import cal
app = Flask(__name__,template_folder='Template')


@app.route('/', methods=[ 'GET' , 'POST' ])
def hello_world():
    if request.method=='POST':
      result = cal(request.form['clump'], request.form['size'],
                         request.form['shape'], request.form['margd'], request.form['epithsize'], request.form['bland'],request.form['nn'],request.form['mit'])
      print(result)
      if(result==2):
           result="Benign: mild state"
      else:
           result="Malignant: evil state"
    else:
        result = " "

    return render_template('view.html',result1 = result)
if __name__ == '__main__':
    app.run()
