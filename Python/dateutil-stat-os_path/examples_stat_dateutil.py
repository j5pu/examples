import os.path
import sys
from stat import *

from dateutil.easter import *
from dateutil.parser import *
from dateutil.relativedelta import *
from dateutil.rrule import *

from vars import *

test_file_path = "/Volumes/HDD/Photos Library.photoslibrary/Masters/2017/03/21/20170321-154924/IMG-20130713-WA0001.jpg"
'''
dateutil
'''


def ejemplo_dateutil():
    now = parse("Sat Oct 11 17:13:46 UTC 2003")
    today = now.date()
    year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
    rdelta = relativedelta(easter(year), today)
    print(f"Today is: {today}")
    print(f"Year with next Aug 13th on a Friday is: {year}")
    print(f"How far is the Easter of that year: {rdelta}")
    print(f"And the Easter of that year is: {today + rdelta}")


'''
stat
'''


def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print(f'Skipping {pathname}')

def visitfile(file):
    print('visiting', file)

if __name__ == '__main__':
    sys.argv.append(FIND_DIR)
    print(sys.argv[1])
    walktree(sys.argv[1], visitfile)