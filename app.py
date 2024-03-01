# Creamos un servidor web con FLASK

from flask import Flask, request

app = Flask(__name__)

@app.route('/') #ruta/path principal > localhost:5000
def hello_world():
    return "Hello World"

@app.route('/melon') #ruta/path principal > localhost:5000/melon
def my_function():
    return "Hola melon"

# Si no se especifica el metodo siempre sera GET. Usamos el POST
# NOTA: La API POST no se puede probar desde navegador(nos saldrá 'Method Not Allowed'). Hay que usar POSTMAN ppara enviar los parametros.
@app.route('/predict', methods=['POST']) 
def print_square():
    recieved_value = int(request.get_json(force=True))
    return str(recieved_value**2)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)