
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
import sys
import traceback
import plugins

from protoprotocol import ProtoProtocol

class WaterWorks(object):
    def __init__(self):
        _plugins = self.get_plugins()
        print "Plugins found:", _plugins
        pass

    def get_plugins(self):
        plugin_classes = []

        base_dir = os.path.dirname(plugins.__file__)
        plugin_paths = glob.glob(os.path.join(base_dir, "*.py"))
        for path in plugin_paths:
            plugin_name = os.path.split(path)[-1][:-3]
            try:
                plugin = imp.load_source(plugin_name, path)
            except:
                print "!!! Failed to load plugin:", path
                traceback.print_exc()
                print ""
                continue
            plugin_attrs = [getattr(plugin, attr) for attr in dir(plugin)]
            plugin_classes = []
            for attr in plugin_attrs:
                try:
                    if issubclass(attr, ProtoProtocol) and attr.is_available():
                        plugin_classes.append(attr)
                except TypeError:
                    continue
        return plugin_classes

def start_daemon(*args):
    client = WaterWorks()
