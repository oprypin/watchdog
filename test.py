import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


f = open("a.txt", "w")

logging.basicConfig(level=logging.DEBUG)
event_handler = LoggingEventHandler()

observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
time.sleep(0.1)

f.write("aa\n")
f.flush()

time.sleep(0.1)
observer.stop()
observer.join()

f.close()

logging.info('--------')

observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
time.sleep(0.1)

f = open("a.txt", "w")
f.write("bb\n")
f.close()

time.sleep(0.1)
observer.stop()
observer.join()
