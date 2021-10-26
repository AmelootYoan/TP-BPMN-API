from flask import Flask
from flask.json import jsonify

app = Flask(__name__)
int somme = 150

@app.route('/account', methods=['GET'])
def compte():
    return jsonify({"somme": somme})

if __name__ == '__main__':
    app.run(debug=True)
