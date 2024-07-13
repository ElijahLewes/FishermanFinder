import os
import sys

print(f"Python executable: {sys.executable}")
print(f"Virtual environment path: {os.environ.get('VIRTUAL_ENV', 'Not set')}")
