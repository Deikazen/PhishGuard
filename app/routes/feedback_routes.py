from flask import Blueprint
from app.controllers.feedback_controller import feedback


feedback_bp = Blueprint('feedback', __name__)


@feedback_bp.route('/api/feedback', methods=['POST'])
def feedback_route():
    return feedback()

