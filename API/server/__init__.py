import os

from flask import Flask

application = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'server.config.DevelopmentConfig'
)
application.config.from_object(app_settings)

from server.api.views import api_blueprint
application.register_blueprint(api_blueprint)