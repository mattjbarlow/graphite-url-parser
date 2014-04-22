import graphite_url_parser
from flask import Flask
from flask import request
from flask import render_template
import re

app = Flask(__name__)

@app.route('/unencoded', methods=['GET', 'POST'])
def unencoded():
    if request.method == 'POST':
      unencoded_url = graphite_url_parser.decode(request.form['encoded_url'])
      return render_template('unencoded.html', unencoded_url=unencoded_url)

    elif request.method == 'GET':
      return render_template('unencoded.html', unencoded_url='')

@app.route('/', methods=['GET', 'POST'])
def encoded():
    if request.method == 'POST':
      encoded_url = graphite_url_parser.encode(request.form['unencoded_url'])
      return render_template('encoded.html', encoded_url=encoded_url)

    elif request.method == 'GET':
      return render_template('encoded.html', encoded_url='')

if __name__ == '__main__':
  app.run(0.0.0.0:80)
