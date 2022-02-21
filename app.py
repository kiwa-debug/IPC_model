
from flask import Flask , render_template , request
from ipc import  ipc_prediction, data_retrival, listToString

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def hello():
    mks=""
    x=""
    y=""
    if request.method =="POST":
        
        case = request.form['usercase']
        predicted_ipc = ipc_prediction(case)
        mks = predicted_ipc
        k=listToString(mks)
        x,y=data_retrival(k)
        print(mks, k , x ,y)
         

    return render_template("index.html", pred = mks, pred_detail=x,pred_punish=y)


'''@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == "POST":
        name = request.form["usercase"]

        return render_template("sub.html", n = name)'''

if __name__ == "__main__":
    app.run(debug=True)
