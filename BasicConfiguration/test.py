import glob
import time
import re
# listglob = glob.glob(r"/var/exposure/serverlog/DP*/Server.log.*")
# # listglob.sort()
# print listglob
# for file_name in listglob:
#


# a = "2013-10-10 23:40:00:500"
a = "20fgdfgdf13-10-10 23:40:00:500"
import time

timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S:%f")
timeStamp = int(time.mktime(timeArray))
print timeStamp
print int(time.time())

 str='''tac /var/exposure/serverlog/DP-RMAdapter-Traffic/Server.log|awk -F '[<>]' 'BEGIN{isinrange = 0;timerange=5*60}{a=$2;gsub(/[^0-9]/," ",a);b=mktime(a);c=systime();d=c-b;if(d<timerange){isinrange=1} }else {print FILENAME;print $0}}'' '''


