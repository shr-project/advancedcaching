from distutils.core import setup
from glob import glob
import os, sys, shutil

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="agtl",
      version='___VERSION___',
      maintainer="daniel",
      maintainer_email="advancedcaching@fragcom.de",
      description="AGTL makes geocaching paperless!",
      long_description=read('agtl.longdesc'),
      package_dir={'agtl': 'advancedcaching'},
      packages = {"advancedcaching", "advancedcaching.actors"},
      package_data = {"advancedcaching": ["data/*", "qml/*"]},
      scripts = {"agtl"},
      data_files=[('applications',['agtl.desktop']),
                  ('icons/hicolor/64x64/apps', ['agtl.png'])],
)
