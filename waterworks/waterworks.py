
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

import glob
import imp
import os

from protoprotocol import ProtoProtocol

class WaterWorks(object):
    def __init__(self):
        pass

    def get_plugins(self):
        plugin_classes = []
        for plugin in glob.glob(os.path.join("plugins", "*.py")):
            plugin_name = os.path.split(plugin)[-1][:-3]
            plugin = imp.load_source(plugin_name, plugin)
            
            plugin_attrs = [getattr(plugin, attr) for attr in dir(plugin)]
            plugin_classes += [attr for attr in plugin_attrs if isinstance(attr, ProtoProtocol)]

        return plugin_classes

def start_daemon(*args):
    client = WaterWorks()
