
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return ('<h1>hello, world!</h1>')


@app.route('/it', methods=['GET'])
def ciaoMondo():
    return ('<h1>ciao, mondo!</h1>')

@app.route('/benvenuto', methods=['GET'])
def benvenuto():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)