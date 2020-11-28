from typing import Dict, Union
from datetime import date

from models.news import News


class DataProvider:
	"""
	Класс для взаимодействия с хранилищем.
	"""

	def __init__(self, config: Dict[str, Union[str, int]]) -> None:
		"""
		Инициализируется конфигом для соединения с хранилищем данных.

		Args:
			config - Конфигурация для подключения к хранилищу.
		"""
		self._config = config

	def get_all_news(self):
		"""
		Метод для получения всех новостей из хранилища.
		"""
		raise NotImplementedError

	def get_news_by_date(self, news_date: date):
		"""
		Метод для получения всех новости на указанную дату.

		Args:
			news_date - дата новости.
		"""
		raise NotImplementedError

	def create_news(self, news: News):
		"""
		Метод для создания новой записи новости.

		news - Экземпляр новости.
		"""
		raise NotImplementedError
