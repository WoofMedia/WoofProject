from urllib.parse import urljoin

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Woof is Running"


@app.route("/anime/search/<string:keyword>")
def search_series(keyword):
    data = [
        {
            "category": "Fantasy %s" % index,
            "cover_url": "https://source.unsplash.com/random/300x200",
            "description": "Description heree",
            "module": "provider_name",
            "score": 80,
            "title": "Series %s" % index,
            "url": urljoin(request.host_url, "/anime/62696d6962696d697c32363931")
        } for index in range(10)
    ]
    return jsonify(data)


@app.route("/anime/<string:token>")
def series_detail(token):
    return jsonify(
        {
            "category": "Fantasy",
            "cover_url": "https://source.unsplash.com/random/300x400",
            "description": "Very Very Very Very Very Very Very long series detail",
            "module": "provider",
            "play_lists": [
                {
                    "name": "Playlist 1",
                    "num": 25,
                    "video_list": [
                        {
                            "info": urljoin(request.host_url, "/anime/62696d6962696d697c32363931/0/0"),
                            "name": "Episode 01",
                            "player": urljoin(request.host_url, "/anime/62696d6962696d697c32363931/0/0/player")
                        }
                    ]
                }
            ],
            "title": "Series Name"
        }
    )


@app.route("/anime/<string:token>/<string:playlist>/<string:episode>")
def episode_playback_info(token, playlist, episode):
    return jsonify(
        {
            "format": "mp4",
            "lifetime": 86399,
            "proxy_url": urljoin(request.host_url, "/proxy/anime/62696d6962696d697c32363931/0/0"),
            "raw_url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
            "size": 10000000
        }
    )


if __name__ == '__main__':
    app.run()
