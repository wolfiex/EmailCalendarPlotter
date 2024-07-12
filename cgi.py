#!/var/www/mipcvs/envs/calendar/bin/python 

import cgi
import cgitb

# Enable CGI traceback in case of errors (optional but useful for debugging)
cgitb.enable()

# # Print Content-Type header
print("Content-Type: text/html\n")

import make_html