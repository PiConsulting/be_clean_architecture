from flask import Blueprint, jsonify

bp = Blueprint('external_services', __name__)

@bp.route('/external', methods=['GET'])
def external_service():
    return jsonify({"message": "External services endpoint"})
