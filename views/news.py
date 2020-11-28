from typing import List

from flask import render_template
from models.news import News


class AllNewsView:

	@staticmethod
	def render_all_news(news: List[News]) -> str:
		return render_template('all_news.html', all_news=news)
