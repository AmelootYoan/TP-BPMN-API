from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

#@app.route('/skis/<int:nbSkis>', methods=['GET'])
#def ski(nbSkis):
#    value = 0
#    if nbskis == 123456:
#        value = 2000
#    return jsonify({"nb_materials": int(value)})

@app.route('/account/<int:noCompte>', methods=['GET'])
def compte(noCompte):
    if noCompte == 5564120575419258:
        value = 20000
        return jsonify({"somme": int(value)})
    else:
        return jsonify({"somme": "c'est pas ton compte..."})

if __name__ == '__main__':
    app.run(debug=True)
