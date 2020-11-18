from niaaml.utilities import Factory
from niaaml import classifiers

__all__ = [
	'ClassifierFactory'
]

class ClassifierFactory(Factory):
	r"""Class with string mappings to classifiers.

	Attributes:
		_entities (Dict[str, Classifier]): Mapping from strings to classifiers.
	"""

	def _set_parameters(self, **kwargs):
		r"""Set the parameters/arguments of the factory.

		See Also:
			* :func:`niaaml.utilities.Factory._set_parameters`
		"""
		self._entities = {
			'AdaBoost': classifiers.AdaBoost,
			'Bagging': classifiers.Bagging,
			'ExtremelyRandomizedTrees': classifiers.ExtremelyRandomizedTrees,
			'LinearSVCClassifier': classifiers.LinearSVCClassifier,
			'MultiLayerPerceptron': classifiers.MultiLayerPerceptron,
			'RandomForestClassifier': classifiers.RandomForestClassifier
		}
	
	def get_result(self, name):
		r"""Get the resulting classifier.

		Arguments:
			name (str): String that represents the classifier.

		Returns:
			Classifier: Classifier according to the given name.
		"""
		return Factory.get_result(self, name).getRandomInstance()
