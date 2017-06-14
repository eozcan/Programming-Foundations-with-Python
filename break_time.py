import webbrowser
import time

print ("This program started on "+time.ctime())
for x in xrange(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=w_DKWlrA24k")



