
import flask

from module_operations.operations import operations

app = flask.Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    """
    Prueba comentarios
    """
    data = flask.request.json
    if("v1" not in data or "v2" not in data):
        response = flask.Response("The parameters are not valid.",status=500)
    else:
        oper = operations()
        try:
            response = str(oper.suma(data["v1"], data["v2"]))
        except TypeError:
            response = flask.Response("Variables should be of type list of numbers.",status=500)
        except OverflowError:
            response = flask.Response("The lists should have the same size.",status=500)
    return response

@app.route('/resta', methods=['POST'])
def resta():
    data = flask.request.json
    oper = operations()
    try:
        response = str(oper.resta(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    return response

@app.route('/mult', methods=['POST'])
def mult():
    data = flask.request.json
    oper = operations()
    try:
        response = str(oper.mult(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    return response

@app.route('/divis', methods=['POST'])
def divis():
    data = flask.request.json
    oper = operations()
    try:
        response = str(oper.divis(data["v1"], data["v2"]))
    except TypeError:
        response = flask.Response("Variables should be of type list.",status=500)
    except OverflowError:
        response = flask.Response("The lists should have the same size.",status=500)
    except ZeroDivisionError:
        response = flask.Response("Division by 0 is not possible.",status=500)
    return response