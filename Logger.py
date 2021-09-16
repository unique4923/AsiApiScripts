import os
from datetime import date, datetime

class Logger:
	def __init__(self, req):
		self.req = req
		self.eventLogPath = self.req.RequestLogPath
		# self.eventLogPath = self.req.RootLogPath + "\\{0}\\EventLogs".format(self.req.SwitchName)
		# self.commLogPath = self.req.RootLogPath + "\\{0}\\CommLogs".format(self.req.SwitchName)
		print(self.eventLogPath) #this is prior to changing printing output
		if not os.path.exists(self.eventLogPath):
			os.makedirs(self.eventLogPath)

		# if not os.path.exists(self.commLogPath):
		# 	os.makedirs(self.commLogPath)
		
	def GetBaseEventLogLocation(self):
		# return "{0}\\{1}_{2}_E.txt".format(self.eventLogPath, self.req.SwitchName, date.today().strftime("%b_%d_%Y"))
		return "{0}\\{1}_E.txt".format(self.eventLogPath, self.req.LogFileName)

	# def GetBaseCommLogLocation(self):
	# 	return "{0}\\{1}_{2}_C.txt".format(self.commLogPath, self.req.SwitchName, date.today().strftime("%b_%d_%Y"))

def Log(message, includeTimeStamp = True):
	if includeTimeStamp:
		totalMessage = "{0}: {1}".format(datetime.now().strftime("%H:%M:%S"), message)
	else:
		totalMessage = message
	# ServerLog(totalMessage)
	print(totalMessage)
		
