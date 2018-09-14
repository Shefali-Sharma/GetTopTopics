from core.Singleton import Singleton
import datetime

currentTime = ""
level = 3
class Logger(Singleton):
    def __init__(self):
        super().__init__()
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("INFO: " + currentTime + " Level:" + str(level) + " " + fileName + " "+ message + "\n")
        logfile.close()

    def debug(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("DEBUGGING: " + currentTime + " Level:" + str(level) + " " + fileName + " "+ message + "\n")
        logfile.close()

    def warning(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("WARNING: " + currentTime + " Level:" + str(level) + " " + fileName + " "+ message + "\n")
        logfile.close()

    def error(self, fileName = '', message = ''):
        logfile = open('core/app.log', 'a+')
        logfile.write("ERROR: " + currentTime + " Level:" + str(level) + " " + fileName + " "+ message + "\n")
        logfile.close()
