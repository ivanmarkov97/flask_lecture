from datetime import date
from typing import Dict, Union, List

from models.news import News
from models.provider import DataProvider
from utils.db_cursor import MysqlDBCursor


class MysqlDataProvider(DataProvider):

	def __init__(self, config: Dict[str, Union[str, int]]) -> None:
		"""
		См. родителя.
		"""
		super().__init__(config)

	def get_all_news(self) -> List[News]:
		list_news = []
		with MysqlDBCursor(self._config) as connection:
			cursor = connection.cursor()
			_sql = "SELECT * FROM news_table"
			cursor.execute(_sql)
			for news_tuple in cursor.fetchall():
				list_news.append(
					News(news_id=int(news_tuple[0]),
					     news_date=news_tuple[1],
					     news_text=news_tuple[2])
				)
		return list_news

	def get_news_by_date(self, news_date: date) -> News:
		pass

	def create_news(self, news: News) -> None:
		pass
