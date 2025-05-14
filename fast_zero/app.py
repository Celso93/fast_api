
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse)
def read_another_root():
    return """
    <html>
      <head>
        <title>Hello world!</title>
      </head>
      <body>
        <h1>Hello world</h1>
      </body>
    </html>"""
