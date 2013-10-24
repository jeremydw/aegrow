import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pygrow'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'growedit'))

from grow import submodules
submodules.fix_imports()
