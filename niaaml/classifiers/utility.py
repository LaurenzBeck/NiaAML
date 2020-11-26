from niaaml.utilities import Factory
from niaaml import classifiers

__all__ = [
	'ClassifierFactory'
]

class ClassifierFactory(Factory):
	r"""Class with string mappings to classifiers.

	Attributes:
		_entities (Dict[str, Classifier]): Mapping from strings to classifiers.

    See Also:
        * :class:`niaaml.utilities.Factory`
	"""

	def _set_parameters(self, **kwargs):
		r"""Set the parameters/arguments of the factory.
		"""
		self._entities = {
			'AdaBoost': classifiers.AdaBoost,
			'Bagging': classifiers.Bagging,
			'ExtremelyRandomizedTrees': classifiers.ExtremelyRandomizedTrees,
			'LinearSVCClassifier': classifiers.LinearSVCClassifier,
			'MultiLayerPerceptron': classifiers.MultiLayerPerceptron,
			'RandomForestClassifier': classifiers.RandomForestClassifier
		}
