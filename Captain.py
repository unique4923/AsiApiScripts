import base64
import os
import sys
from Logger import Logger
from datetime import datetime
from Avaya.AvayaRun import AvayaScript

def DoSwitchRequest(req):
    if req.SwitchType == 5:
        script = AvayaScript(SSH, req)
        return script.Run()
        # print("The value of __name__ is:", repr(__name__))
    elif st == "Cisco":
        print "doing cisco"
        #NOT CURRENTLY IMPLEMENTED!!!!
        return False
    else:
        print("Switch type not supported")
        return False

print('C# console message -> Not python')

#todo: wrap this in try/catch since errors here won't be logged yet
log = Logger(MyRequest)

eventLogPath = log.GetBaseEventLogLocation()
# commLogPath = log.GetBaseCommLogLocation()

#debugConsole = sys.stdout # Save a reference to the original standard output
ScriptSuccess = False
ScriptErrorOrMessageText = ""
with open(eventLogPath, 'a') as f:
    sys.stdout = f # Change the standard output to the file we created.

    print
    print('################################################ {0} ################################################'.format(datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")))
    print("***EventLog location: " + eventLogPath)
    # print("***CommLog location: " + commLogPath)
    print("***SwitchType: " + str(MyRequest.SwitchType))
    print("***Action: " + MyRequest.Action)
    # sys.stdout = original_stdout # Reset the standard output to its original value

    try:
        ScriptSuccess = DoSwitchRequest(MyRequest)
        print("ScriptSuccess: " + str(ScriptSuccess))
    except Exception as e:
        ScriptSuccess = False
        print("ScriptSuccess: false - args: {0}").format(e.args)
        ScriptErrorOrMessageText = 'Error from script: "{0}".\nFor details see log:\n{1}'.format(e, eventLogPath)
        raise Exception(ScriptErrorOrMessageText)