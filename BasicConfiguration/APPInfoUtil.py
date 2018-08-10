import subprocess
import re
from cmdutil import *



# cmd="mysqlclient -e \"SELECT PROPERTIES, PARTNER_ID FROM sigdb.APPLICATION_CAPABILITY_SUB WHERE APPLICATION_ID = 'CSRTOOLBOX'; SELECT PROPERTIES, PARTNER_ID FROM sigdb.APPLICATION WHERE APPLICATION_ID = 'CSRTOOLBOX';\""
# result_from_mql=run_cmd_r(cmd)
# print type(result_from_mql