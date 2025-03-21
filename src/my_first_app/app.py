from flask import Flask

app = Flask(__name__)


@app.route('/')

def index():
    return 'Hello world'

@app.route('/<name>')
def hello(name):
    return f'Hello {name}'

@app.route('/check_file/<file_name>')
def check_file(file_name):
    try:
        with open(file_name) as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        return f'{file_name} not found'



app.run(host='0.0.0.0' , port=8000 , debug=True)