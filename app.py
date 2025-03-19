from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/get/<id>', methods=['GET'])
def get_articles(id):
    return render_template(f'{id}.html')
 
if __name__ == '__main__':
    app.run(debug=True)