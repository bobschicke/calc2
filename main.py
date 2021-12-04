"""This is the Main Method"""
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from csv_util.file_utils import Filehandler

def get_filename(filestr : str):
    """This method gets the filename from path/filename"""
    last = filestr.rfind("/") # reverse find gets the last occurrence of the "/" char
    file_name = filestr[last + 1: len(filestr)]
    return file_name

if __name__ == "__main__":
    PATTERNS = ["*"]
    IGNORE_PATTERNS = None
    IGNORE_DIRECTORIES = False
    CASE_SENSITIVE = True
    my_event_handler = PatternMatchingEventHandler(PATTERNS, IGNORE_PATTERNS,
                                                   IGNORE_DIRECTORIES, CASE_SENSITIVE)

    absolute_file_path = os.path.abspath(__file__)
    absolute_dir_path = os.path.dirname(absolute_file_path)
    print("Full path: " + absolute_file_path)
    print("Directory Path: " + absolute_dir_path)

    def on_created(event):
        """This is the file created interrupt"""
        print("hey," + event.src_path + "has been created!")
        if "csv" in event.src_path:
            print(event.src_path + " is CSV")
            nump_arr = Filehandler.read_csv(event.src_path) # Run test on file
            # Get the filename
            csv_filename = get_filename(event.src_path)
            # Process the array
            Filehandler.process_csv(nump_arr, csv_filename)
            # Move file to "done" folder
            # os.rename('old_dir/file', 'new_dir/file')
            os.rename(event.src_path, absolute_dir_path + "/done/" + csv_filename)
            # Create/Append to the log file

    my_event_handler.on_created = on_created

    WATCH_PATH = absolute_dir_path #+ "/input/"
    print("path = " + WATCH_PATH)
    GO_RECURSIVELY = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, WATCH_PATH, recursive=GO_RECURSIVELY)

    my_observer.start()
    INDEX = 0
    try:
        while True:
            time.sleep(15)
            print("Waiting " + str(INDEX))
            INDEX += 1
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
