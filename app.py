from flask import Flask

app = Flask(__name__)

@app.route('/')
def boas_vindas():
    return "Bem-vindo ao meu site"

if __name__ == '__main__':
    app.run()
