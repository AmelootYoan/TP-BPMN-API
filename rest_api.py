from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/account/<int:noCompte>', methods=['GET'])
def compte(noCompte):
    if noCompte == 5564120575419258:
        value = 20000
        return jsonify({"somme": int(value)})
    else:
        value = 0
        return jsonify({"somme": int(value)})

if __name__ == '__main__':
    app.run(debug=True)
