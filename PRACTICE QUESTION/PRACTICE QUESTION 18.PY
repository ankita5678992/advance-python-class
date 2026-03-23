class Logger:
    def __init__(self, file):
        self.file = open(file, "a")

    def log(self, msg):
        self.file.write("INFO: " + msg + "\n")

    def log_warning(self, msg):
        self.file.write("WARNING: " + msg + "\n")

    def log_error(self, msg):
        self.file.write("ERROR: " + msg + "\n")

    def __del__(self):
        self.file.close()
        print("File closed")


l = Logger("log.txt")
l.log("Program started")
l.log_warning("Low memory")
l.log_error("Crash")