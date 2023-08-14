import os
import time
import base64

from constants.HTML_constants import *

# write to file
def write_to_file(text, filename):
    with open(os.path.join("downloads", filename), "w") as f:
        f.write(text)
    return filename

# generate filename
def generate_name():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "Document"+timestr+".txt"
    return filename

# download file
def make_downloadable(filename):
    readfile = open(os.path.join("downloads", filename)).read()
    b64 = base64.b64encode(readfile.encode()).decode()
    return HREF.format(b64)