from click_web import create_click_web_app

import command
from apps import cli

app = create_click_web_app(command, cli)