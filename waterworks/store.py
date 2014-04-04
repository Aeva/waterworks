import json

class StoreException(Exception):
	pass

class Store(dict):
	"""
		Persistant dictionary-like storage

		Will write out all changes to disk as their made
		NB: Will overwrite any changes made to disk not on class.
	"""

	filename = None

	def update(self, *args, **kwargs):
		return_value = super(Store, self).update(*args, **kwargs)
		self.save()
		return return_value

	def __setitem__(self, *args, **kwargs):
		return_value = super(Store, self).__setitem__(*args, **kwargs)
		self.save()
		return return_value

	def save(self):
		""" Saves dictionary to disk in JSON format. """
		if self.filename is None:
			raise StoreException("A filename must be set to write storage to disk")

		data = json.dumps(self)
		fout = open(self.filename, "w")
		fout.write(data)
		fout.close()

	@classmethod
	def load(cls, filename):
		""" Load JSON from disk into store object """
		data = open(filename).read()
		data = json.loads(data)
		store = cls(data)
		store.filename = filename
		return store