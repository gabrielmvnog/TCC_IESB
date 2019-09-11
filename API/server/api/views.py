from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

api_blueprint = Blueprint('api', __name__)

class DepressionAnalysisAPI(MethodView):

    def post(self):

        post_data = request.get_json()

        response_object = {
            'status': 'success',
            'data': {
                #'predicted': predicted,
                #'time': end
            }
        }

        return make_response(response_object)

class SuicidalAnalysisAPI(MethodView):

    def post(self):

        post_data = request.get_json()

        response_object = {
            'status': 'success',
            'data': {
                #'predicted': predicted,
                #'time': end
            }
        }

        return make_response(response_object)

depression_view = DepressionAnalysisAPI.as_view('depression_api')
suicidal_view = SuicidalAnalysisAPI.as_view('suicidal_api')

api_blueprint.add_url_rule(
    '/api/depression',
    view_func=depression_view,
    methods=['POST']
)

api_blueprint.add_url_rule(
    '/api/suicidal',
    view_func=suicidal_view,
    methods=['POST']
)