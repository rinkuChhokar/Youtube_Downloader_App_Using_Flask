from flask import Flask, request
from flask import render_template
from pytube import YouTube

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def youtube_video_download():
    if request.method == "POST":
        link = request.form["urlLink"]
        resolution = request.form["resolution"]
        video = YouTube(link)
        stream = video.streams.filter(res=resolution).first()
        if stream:

            stream.download()
            return render_template('success.html')
        else:
            return "<p>Invalid resolution selected!!</p>"
        
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)