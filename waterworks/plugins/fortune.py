
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

from subprocess import check_output
from waterworks.protoprotocol import ProtoProtocol, ProtocolFeatures



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

    def is_available(self):
        """
        Checks availability by attempting to call the fortune command.
        """
        try:
            foo = self.__get_fortune()
            return True
        except OSError:
            return False

    def __get_fortune(self):
        """
        Tells your fortune!
        """
        return check_output("fortune")
    
