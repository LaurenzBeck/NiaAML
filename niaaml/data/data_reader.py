__all__ = [
	'DataReader'
]

class DataReader:
	r"""Class for implementing data readers with different sources of data.
	
	Date:
		2020

	Author
		Luka Pečnik

	License:
		MIT

	Attributes:
		_x (Iterable[any]): Array of rows from dataset without expected classification results.
		_y (Iterable[int]): Array of encoded expected classification results.
		_label_encoder (sklearn.preprocessing.LabelEncoder): LabelEncoder instance for encoding classification labels.
	"""

	_x = None
	_y = None
	_label_encoder = None

	def __init__(self, **kwargs):
		r"""Initialize data reader.
		"""
		self._set_parameters(**kwargs)
	
	def _set_parameters(self, **kwargs):
		r"""Set the parameters/arguments of the algorithm.
		"""
		return
	
	def get_x(self, **kwargs):
		r"""Get value of _x.

		Returns:
			Iterable[any]: Array of rows from dataset without expected classification results.
		"""
		return self._x
	
	def get_y(self, **kwargs):
		r"""Get value of _y.

		Returns:
			numpy.array[int]: Array of encoded expected classification results.
		"""
		return self._y

	def _read_data(self, **kwargs):
		r"""Read data from expected source.
		"""
		return