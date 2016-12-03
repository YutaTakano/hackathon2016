from flask import Flask,render_template,url_for
from py import get,varsha

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def get_root():
    #return render_template('index.html')
    return 'Hello world'
