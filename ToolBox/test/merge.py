import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Append program base directory to system viriable.
sys.path.append(BASE_DIR)
from util.merge import get_file_extensions

print(BASE_DIR)
print(os.path.join(BASE_DIR, 'test/data/'))
print(get_file_extensions(os.path.join(BASE_DIR, 'test/data/')))
