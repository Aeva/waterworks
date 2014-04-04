from setuptools import setup

setup(name="waterworks",
      version="0.0.0",
      description="Message agregation daemon.",
      url="https://github.com/Aeva/waterworks",
      author="Aeva Palecek",
      author_email="aeva.ntsc@gmail.com",
      license="GPLv3",
      packages=["waterworks"],
      zip_safe=False,

      entry_points = {
        "console_scripts" : [
            "waterworks=waterworks.waterworks:start_daemon",
            ],
        },

      install_requires = [
        ])
      
