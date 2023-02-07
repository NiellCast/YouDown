import subprocess
from src.run.app import run
from flask import Flask, render_template, request
import wsgiserver
import webbrowser

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template('YouDown.html')


@app.route('/downloading', methods=["GET"])
def downloading():
    links = request.args.get('link')
    if links:
        run(links)

    return render_template('YouDown.html')


if __name__ == '__main__':
    server = wsgiserver.WSGIServer(app, host='127.0.0.1', port=5000)
    webbrowser.open('http://127.0.0.1:5000/')
    server.start()
