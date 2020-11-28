from flask import current_app
from flask.views import MethodView

from models.mysql_provider import MysqlDataProvider
from views.news import AllNewsView


class NewsController(MethodView):

	def get(self) -> str:
		provider = MysqlDataProvider(current_app.config)
		news = provider.get_all_news()
		return AllNewsView.render_all_news(news)
