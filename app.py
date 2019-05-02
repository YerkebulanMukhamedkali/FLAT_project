from flask import Flask, request
from flask import render_template
import parser
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            text = request.form.get('source')
            f = open('test.java', 'w')
            f.write(text)
            f.close()

            ans = parser.do_it('test.java')
            f = open('test.py', 'w').close()
            f1 = open('test.py', 'w')
            f1.write(ans)
            f1.close()

            return render_template('index.html', result = open('test.py').read())
        except:
            return "Error"

if __name__ == '__main__':
   app.run(debug=True)