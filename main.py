from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hallo():
    s=3
    m="/static/1.jpg"
    print (s)
    return render_template('index.html',s=s,m=m)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5006)

