import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from csv_util.pandas_csv_test import Filehandler


def getFilename(filestr : str):
    last = filestr.rfind("/") # reverse find gets the last occurrence of the "/" char
    filename = filestr[last + 1: len(filestr)]
    return filename






if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    absolute_path = os.path.abspath(__file__)
    print("Full path: " + absolute_path)
    print("Directory Path: " + os.path.dirname(absolute_path))

    def on_created(event):
        print(f"hey," + event.src_path + "has been created!")
        if "csv" in event.src_path:
            print(event.src_path + " is CSV")
            fh = Filehandler() # Create a Filehandler object
            fh.test_pandas(event.src_path) # Run test on file
            # Move file to "done" folder
            filename = getFilename(event.src_path)
            os.rename(filename, "done/" + filename)  # os.rename('old_directory/test_file.txt', 'new_directory/test_file.txt')



    def on_deleted(event):
        print(f"what the f**k! Someone deleted " + event.src_path)

    def on_modified(event):
        print(f"hey buddy, {event.src_path} has been modified")

    def on_moved(event):
        print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

    my_event_handler.on_created = on_created

    my_event_handler.on_deleted = on_deleted

    my_event_handler.on_modified = on_modified

    my_event_handler.on_moved = on_moved

    path = "/home/myuser/"    #"."
    print("path = " + path)
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()

    try:
        while True:
            time.sleep(5)
            print("sleep")
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()