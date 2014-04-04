
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


import pypump
from waterworks.protoprotocol import ProtoProtocol



class PumpProtocol(ProtoProtocol):
    """ Protocol for interacting with the pump.io service """

    def __init__(self, config, storage):
        if "client" in storage:
            self.client = pypump.Client(
                webfinger=config["webfigner"],
                type="native",
                name="Waterworks",
                key=storage["client"].get("key"),
                secret=storage["client"].get("secret")
            )
        else:
            self.client = pypump.Client(
                webfinger=config["webfinger"],
                type="native",
                name="Waterworks"
            )
        self.pump = None

    def connect(self):
        self.pump = pypump.PyPump(
            client=self.client,
            verifier_callback=self.__verifier_callback
        )

    def __verifier_callback(self, url):
        
        print url
        verifier = raw_input("Verifier: ").strip(" ")
        return verifier

