from src.tools.youtube.download_video import Downloader
from pytube import exceptions
from flask import Flask, render_template, request
import wsgiserver
import webbrowser

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/downloading', methods=["GET"])
def downloading():
    link = request.args.get('link')

    if link:
        try:
            Downloader.regular_download(link)
        except exceptions.VideoUnavailable:
            pass
        except exceptions.RegexMatchError:
            pass

    return render_template('index.html')


if __name__ == '__main__':
    server = wsgiserver.WSGIServer(app, host='127.0.0.1', port=5000)
    webbrowser.open('http://127.0.0.1:5000/')
    server.start()
