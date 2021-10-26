from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/skis/<int:nbSkis>', methods=['GET'])
def ski(nbSkis):
    if nbskis == 123456:
        return jsonify({"nb_materials": int(nbSkis*8)})
    else:
        return jsonify({"nb_materials": int(nbSkis*10)})

if __name__ == '__main__':
    app.run(debug=True)
