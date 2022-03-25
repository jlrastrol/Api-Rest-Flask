import flask
import module_operations.operations as operations

app = flask.Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    data = flask.request.json
    suma =operations.suma(data["v1"], data["v2"])
    return str(suma)

@app.route('/resta', methods=['POST'])
def resta():
    data = flask.request.json
    resta =operations.resta(data["v1"], data["v2"])
    return str(resta)

@app.route('/mult', methods=['POST'])
def mult():
    data = flask.request.json
    suma =operations.mult(data["v1"], data["v2"])
    return str(mult)

@app.route('/divis', methods=['POST'])
def divis():
    data = flask.request.json
    divis =operations.divis(data["v1"], data["v2"])
    return str(divis)