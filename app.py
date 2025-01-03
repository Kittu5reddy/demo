from flask import Flask,render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('/main/home.html')





if __name__=="__main__":
    app.run(debug=True,port=4000)