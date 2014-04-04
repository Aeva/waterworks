import os

from store import Store

class Config(Store):

    read_only = True
    
    @classmethod
    def get_filename(self):
        base = os.environ.get("XDG_CONFIG_HOME", "~/.config")
        base = os.path.expanduser(base)
        base = os.path.join(base, "waterworks")
        if not os.path.isdir(base):
            os.mkdir(base)

        return os.path.join(base, "waterworks.json")

config = Config.load() 
