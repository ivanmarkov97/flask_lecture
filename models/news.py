from datetime import date


class News:
	"""
	Класс представляющий собой абстракцию для работы новостями.
	"""

	def __init__(self, news_id: int, news_date: date, news_text: str) -> None:
		"""
		Инициализирует новую сущность новости через входные параметры.

		Args:
			news_id - Идентфиикатор новости.
			news_date - Дата создания.
			news_text - Текст новости.
		"""
		self._news_id = news_id
		self._news_date = news_date
		self._news_text = news_text

	@property
	def news_id(self):
		return self._news_id

	@property
	def news_date(self):
		return self._news_date

	@property
	def news_text(self):
		return self._news_text
