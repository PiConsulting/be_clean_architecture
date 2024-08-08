from flask import Blueprint, jsonify

bp = Blueprint('client', __name__)

@bp.route('/client', methods=['GET'])
def get_client():
    return jsonify({"message": "Client endpoint"})
