from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import sys


username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
username = [username,""][username in [u"loginwindow", None, u""]]
print(username)
sys.stdout.write(username + "\n");'
