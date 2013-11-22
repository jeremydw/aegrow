import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pygrow'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'growedit'))

from grow import submodules
submodules.fix_imports()

from growedit.users import boto_auth  # Needed to register AuthHandler.

def webapp_add_wsgi_middleware(app):
  from google.appengine.ext.appstats import recording
  app = recording.appstats_wsgi_middleware(app)
  return app

appstats_MAX_STACK = 20
