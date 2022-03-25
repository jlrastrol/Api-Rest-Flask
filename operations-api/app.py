from decimal import DivisionByZero
import flask
import module_operations.operations as operations

app = flask.Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    data = flask.request.json
    try:
        response = str(operations.suma(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    return response

@app.route('/resta', methods=['POST'])
def resta():
    data = flask.request.json
    try:
        response = str(operations.resta(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    return response

@app.route('/mult', methods=['POST'])
def mult():
    data = flask.request.json
    try:
        response = str(operations.mult(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    return response

@app.route('/divis', methods=['POST'])
def divis():
    data = flask.request.json
    try:
        response = str(operations.divis(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    except ZeroDivisionError:
        response = flask.Response("Division by 0 is not possible.",status=500)
    return response