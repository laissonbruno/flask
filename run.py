from flask import Flask

app = Flask(__name__)
@app.route('/')

def ola():
    return 'Ola mundo'

if __name__ == "__main__":
    app.run()