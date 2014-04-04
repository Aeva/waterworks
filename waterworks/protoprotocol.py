
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



class ProtoProtocol(object):
    """
    ProtoProtocol is the base clase which protocol plugins should
    inherit from.
    """

    def __init__(self):
        raise NotImplementedError()

    def get_features(self):
        """
        This returns the features supported by the protocol.  For example,
        an RSS plugin would not support anything except fort
        "get_updates".
        """
        pass

    def is_available(self):
        """
        If the protocol is dependent on other programs or libraries on the
        computer, return true or false to indicate if the protocol is
        available for use.
        """
        return False

    def connect(self, account):
        """
        Connect to the given protocol.  Account is probably a config entry 
        that includes relevant data to the protocol.
        """
        pass

    def disconnect(self):
        """
        """
        pass

    def send_msg(self, targets=[], msg):
        """
        Send a message to the given targets.  The targets are probably
        defined as strings or contacts.  In protocols that support it,
        an empty list for targets means the message is to be
        broadcasted.

        An example of this is for twitter or pump.io, targets=[] means
        a normal public message.  In twitter, specifying a single
        target means a DM.
        """
        pass

    def get_updates(self):
        """
        This is called to poll for new messages from the server.  If the
        protocol supports server push, the class should support such
        functionality either in a thread or subprocess; in any rate,
        the new messages should be accessible here for a coherent
        event interface.
        """
        pass

    def get_contacts(self):
        """
        Pulls your contacts list from the server.  This should not be
        called automatically on some protocols, but have a ui option
        for pushing and pulling contacts.  A config option may make
        this automatic.  It may be on by default for some protocols
        (eg facebook by way of xmpp it would make sense), but off for
        others (you might not want this by default with vanilla xmpp).
        """
        pass

    def push_contacts(self):
        """
        See .get_contacts help text.
        """
        pass

    def set_status(self, msg):
        """
        Used to set a status message.  In XMPP, this would be your away
        message.  In something like email this would not be used.
        """
        pass

    def set_state(self):
        """
        Used to set your state.  For example in XMPP this would be
        something like "invisible", "away", etc.
        """
        pass
