import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


with open("a.txt", "w") as f:
    f.write("aa\n")
time.sleep(0.05)

event_handler = FileSystemEventHandler()
event_handler.on_any_event = print

print('--------')

observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
time.sleep(0.05)

print('[overwriting a file]')
f = open("a.txt", "w")
f.write("bb\n")
f.close()

time.sleep(0.05)
observer.stop()
observer.join()

f = open("a.txt", "w")

time.sleep(0.05)

print('--------')

observer = Observer()
observer.schedule(event_handler, ".")
observer.start()
time.sleep(0.05)

print('[appending to a file]')
f.write("cc\n")
f.flush()

time.sleep(0.05)

print('[appending to a file]')
f.write("dd\n")
f.flush()

time.sleep(0.05)
observer.stop()
observer.join()
time.sleep(0.05)

f.close()
