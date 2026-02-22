from flask import (
    Blueprint,
    jsonify,
    request
)

from src.utils.youtube_util import (
    get_channel_id,
    get_uploads_playlist_id,
    get_video_details,
    get_video_ids_from_playlist
)

youtube_bp = Blueprint("youtube_api", __name__, url_prefix="/api")


@youtube_bp.route("/youtube", methods=["POST"])
def handle_youtube_request():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Requisito de Json no Body"}), 400

        channel_name = data.get("channel_name")
        tags = data.get("tags")

        if not channel_name or not isinstance(tags, list):
            return jsonify({"error": "Entrada invalida"}), 400

        channel_id = get_channel_id(channel_name)
        if not channel_id:
            return jsonify({"error": "Canal não encontrado"}), 404

        playlist_id = get_uploads_playlist_id(channel_id)
        video_ids = get_video_ids_from_playlist(playlist_id, max_results=20)

        videos = get_video_details(video_ids)

        # Filtragem por tags (case insensitive)
        filtered_videos = []

        for video in videos:
            video_tags = [t.lower() for t in video.get("tags", [])]
            input_tags = [t.lower() for t in tags]

            if any(tag in video_tags for tag in input_tags):
                filtered_videos.append(video)

        return jsonify({
            "channel_name": channel_name,
            "videos": filtered_videos
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500