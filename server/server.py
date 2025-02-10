from flask import Flask, request, send_file, jsonify
from pytubefix import YouTube
from pytubefix.cli import on_progress
from platform import system

app = Flask(__name__)

@app.route("/download", methods=["GET"])
def baixar():
    try:
        url = request.args.get("url")
        print(url)

        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path="server/static")

        if system() == "Windows":
            titulo = ys.title.replace("/", "").replace("\\", "").replace(":", "").replace("*", "").replace("?", "").replace('"', "").replace("<", "").replace(">", "").replace("|", "")

            # Resolvendo problemas com caracteres do windows
            return send_file(f"static/{titulo}.mp4", as_attachment=True)

        else:
            titulo = ys.title.replace("/", "")

            # Resolvendo problemas com caracteres do linux
            return send_file(f"static/{titulo}.mp4", as_attachment=True)
    
    except:
        return jsonify("Ocorreu um erro tenter usar outra url")

app.run(port=3000, host="localhost")