
# This file is part of Waterworks
#
# Waterworks is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Waterworks is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Waterworks.  If not, see <http://www.gnu.org/licenses/>.

import json
import os

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
    def get_filename(cls):
        raise NotImplemented()

    @classmethod
    def load(cls, filename=None):
        """ Load JSON from disk into store object """
        if filename is None:
            filename = cls.get_filename()

        if os.path.isfile(filename):
            data = open(filename).read()
            data = json.loads(data)
            store = cls(data)
        else:
            store = cls()

        store.filename = filename
        return store
