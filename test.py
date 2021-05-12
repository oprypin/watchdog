import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


f = open("a.txt", "w")

event_handler = FileSystemEventHandler()
event_handler.on_any_event = print

observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
time.sleep(0.1)

print('[appending to a file]')
f.write("aa\n")
f.flush()

time.sleep(0.1)
observer.stop()
observer.join()

f.close()

print('--------')

observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
time.sleep(0.1)

print('[overwriting a file]')
f = open("a.txt", "w")
f.write("bb\n")
f.close()

time.sleep(0.1)
observer.stop()
observer.join()
