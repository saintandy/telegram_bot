from .settings import *

try:
    from .local_settings import *
except:
    print("[-] Couldn't import from local_settings.py")
