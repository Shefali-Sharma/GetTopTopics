from core.Singleton import Singleton
import datetime

class Logger(Singleton):
    def __init__(self):
        super().__init__()
        self.level = 3
        self.currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("INFO: " + self.currentTime + " Level:" + str(self.level) + " " + fileName + " "+ message + "\n")
        logfile.close()

    def debug(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("DEBUGGING: " + self.currentTime + " Level:" + str(self.level) + " " + fileName + " "+ message + "\n")
        logfile.close()

    def warning(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("WARNING: " + self.currentTime + " Level:" + str(self.level) + " " + fileName + " "+ message + "\n")
        logfile.close()

    def error(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("ERROR: " + self.currentTime + " Level:" + str(self.level) + " " + fileName + " "+ message + "\n")
        logfile.close()
