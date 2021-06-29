from flask import Flask, render_template, request
import json
# from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def cv():
    return render_template('index.html')

# 淡入淡出轮播图
@app.route('/index1')
def index1():
	return render_template('html/index1.html')

# 左右切换轮播图
@app.route('/index2')
def index2():
	return render_template('html/index2.html')

if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
