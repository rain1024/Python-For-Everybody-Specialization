class FileLogger:
    # 1. CONSTRUCTOR (__init__) - Very common
    # Called when creating an object, used to open file and prepare.
    def __init__(self, filename):
        print(f"CONSTRUCTOR: Opening file '{filename}' for logging.")
        self.filename = filename
        # Opening file is an action to set up initial state.
        self.file_handle = open(filename, 'w', encoding='utf-8')

    # 2. ATTRIBUTE - Very common
    # 'filename' and 'file_handle' are object attributes.

    # 3. METHOD - Very common
    # A behavior of the object to write data to file.
    def log(self, message):
        self.file_handle.write(message + '\n')
        print(f"METHOD: Wrote '{message}' to file.")

    # 4. DESTRUCTOR (__del__) - Rarely used!
    # Called when object is about to be destroyed.
    # Its task is cleanup, here it's closing the file.
    def __del__(self):
        print(f"DESTRUCTOR: Closing file '{self.filename}'.")
        # Check if file exists and is open before closing.
        if self.file_handle:
            self.file_handle.close()

# --- Using the class ---
print("--- Creating Logger object ---")
logger = FileLogger("my_log.txt")
logger.log("First log entry")
logger.log("Second log entry")
print("--- Program about to end, 'logger' object will be destroyed ---")
# When variable 'logger' is no longer referenced, Destructor will be called.