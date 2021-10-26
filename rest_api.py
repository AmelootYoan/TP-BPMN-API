from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/account/<int:somme_compte>', methods=['GET'])
def compte(somme_compte):
    value = 0;
    if account_number = 123456:
           value = 20000
    return jsonify({"somme": value})

if __name__ == '__main__':
    app.run(debug=True)
