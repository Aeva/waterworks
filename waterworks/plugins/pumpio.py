
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

try:
    import pypump
except ImportError:
    pass

from waterworks.protoprotocol import ProtoProtocol

class PumpProtocol(ProtoProtocol):
    """ Protocol for interacting with the pump.io service """

    pump = None

    def __init__(self, config, storage):
        self.storage = storage
        self.config = config

    def connect(self):
        """ Setup PyPump client and instance """
        if "client" in storage:
            self.client = pypump.Client(
                webfinger=self.config["webfigner"],
                type="native",
                name="Waterworks",
                key=self.storage["client"].get("key"),
                secret=self.storage["client"].get("secret")
            )
        else:
            self.client = pypump.Client(
                webfinger=self.config["webfinger"],
                type="native",
                name="Waterworks"
            )

        self.pump = pypump.PyPump(
            client=self.client,
            verifier_callback=self.__verifier_callback
        )

    def __verifier_callback(self, url):
        """
        Handles OAuth out of band authentication

        We need the user to click on the URL, follow the instructions
        and then provide the verifier token via stdin. A possible future
        consideration could be to send a request to any connected clients
        to ask the user to open this URL.
        """
        print url
        verifier = raw_input("Verifier: ").strip(" ")
        return verifier

    def send_msg(self, msg, targets=None):
        if targets is None:
            # If it's got no specific targets send it to everyone (i.e. public)
            targets = [self.pump.Lists.Public]

        note = self.pump.Note(msg)
        note.to = targets
        note.send()

    def get_updates(self):
        if self.previous_message is None:
            # We don't have any preverious messages so just give back the last 20
            notes = self.pump.Inbox[:20]
            self.previous_message = notes[0].id
            return notes

        # really we should have a way of getting the messages since another message
        # but until we're able to easily do that we can force it to hand back whatever
        # the last messages where
        #
        # Related bug: https://github.com/xray7224/PyPump/issues/100
        self.previous_message = None
        return self.get_update()

    def is_available(self):
        try:
            import pypump
            return True
        except:
            return False
