from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/get/<id>', methods=['GET'])
def get_articles(id):
    return render_template(f'{id}.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)