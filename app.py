from flask import Flask
from config import Config
from controller.news import NewsController

app = Flask(__name__)
app.config.from_object(Config())

app.add_url_rule('/', view_func=NewsController.as_view('all_news'))

if __name__ == '__main__':
	app.run(host='localhost', port=5001)
