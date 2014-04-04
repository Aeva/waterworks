
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

import subprocess

from waterworks.protoprotocol import ProtoProtocol, ProtocolFeatures



def get_fortune():
    """
    Tells your fortune!
    """
    
    fortune = subprocess.Popen(["fortune"], stdout=subprocess.PIPE)
    fortune.wait()
    return fortune.communicate()[0]



class FortuneProtocol(ProtoProtocol):
    """
    Primarily for testing purposes, this class implements a protocol
    for an endless stream of fortunes.
    """

    UPDATE_DELAY = 10

    def __init__(self, storage):
        pass


    def get_features(self):
        """
        Fortune Protocol is a read-only protocol that does not require
        authentication, and really ought not to store any logs.
        """
        features = ProtocolFeatures()
        features.offline = True
        features.get_updates = True
        features.no_logging = True
        return features

    @staticmethod
    def is_available():
        """
        Checks availability by attempting to call the fortune command.
        """
        try:
            foo = get_fortune()
            return True
        except OSError:
            return False
