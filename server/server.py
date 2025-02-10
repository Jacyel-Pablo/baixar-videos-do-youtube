from flask import Flask, request, send_file
from pytubefix import YouTube
from pytubefix.cli import on_progress

app = Flask(__name__)

@app.route("/download")
def baixar():
    url = request.args.get("url")
    print(url)

    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path="server/static")

    return send_file(f"static/{ys.title}.mp4", as_attachment=True)

app.run(port=3000, host="localhost")