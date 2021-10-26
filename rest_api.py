from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/skis/<int:nbSkis>', methods=['GET'])
def ski(nbSkis):
    value = 0
    if nbskis == 123456:
        value = 2000
    else:
        value = 0
    return jsonify({"nb_materials": int(value)})

if __name__ == '__main__':
    app.run(debug=True)
