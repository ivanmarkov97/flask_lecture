from typing import Dict, Union

from mysql import connector


class MysqlDBCursor:

	def __init__(self, config: Dict[str, Union[str, int]]) -> None:
		self._config = config

	def __enter__(self) -> connector:
		host = self._config['HOST']
		port = self._config['PORT']
		db = self._config['DB']
		user = self._config['USER']
		password = self._config['PASSWORD']

		self._connector = connector.connect(host=host,
		                                    port=port,
		                                    db=db,
		                                    user=user,
		                                    password=password,
		                                    auth_plugin='mysql_native_password')
		return self._connector

	def __exit__(self, exc_type, exc_val, exc_tb) -> None:
		self._connector.close()
