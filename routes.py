
from flask import Blueprint, request, jsonify  # request and jsonify used to handle requests and responses
from models import comments  # stores the comments
from datetime import datetime  # used to get the current date and time

# Define the blueprint
api_routes = Blueprint('api_routes', __name__)  # created a blueprint

# GET all comments
@api_routes.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments), 200  # when a GET request is made to /comments, it returns the comments list as a JSON response

# POST a new comment
@api_routes.route('/comments', methods=['POST'])
def add_comment():
    data = request.json
    new_comment = {
        "id": len(comments) + 1,
        "text": data.get("text", ""),
        "author": data.get("author", ""),
        "timestamp": datetime.utcnow().isoformat()
    }
    comments.append(new_comment)  # adds the new comment to the comments list
    return jsonify(new_comment), 201

# PUT (update) a comment by ID
@api_routes.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    for comment in comments:
        if comment["id"] == comment_id:
            comment["text"] = data.get("text", comment["text"])
            comment["author"] = data.get("author", comment["author"])
            return jsonify(comment), 200
    return jsonify({"error": "Comment not found"}), 404

# DELETE a comment by ID
@api_routes.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    for comment in comments:
        if comment["id"] == comment_id:
            comments.remove(comment)
            return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Comment not found"}), 404

# right now we are using an in memory list to store the comments. thus, the comments will be lost when the server is stopped
@api_routes.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "Server is running"}), 200
    @api_routes.route('/stats', methods=['GET'])
    def stats():
        total = len(comments)
        unique_authors = len(set(c["author"] for c in comments))
        return jsonify({
            "total_comments": total,
            "unique_authors": unique_authors
        }), 200