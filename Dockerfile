FROM python:3.10-slim-bullseye
#Instalamos pequeño SO para ejecutar Python
LABEL project = "nuclio-flask-api"
LABEL version="1.0"
LABEL owner = 'Toni'
# etiquetas
COPY . /app
#directorio donde copiará la imagen. Creara la carpeta app
WORKDIR /app
#Directorio contra el qeu vamos a trabajar
RUN pip install -r requirements.txt
#instala los requirements
CMD python3 app.py