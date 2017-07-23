import os
import time
newpath = os.path.join('D:', 'Study', 'Codes', time.strftime("%B %y"))
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)
