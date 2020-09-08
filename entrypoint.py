

import os

from flask import send_from_directory

from app import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

