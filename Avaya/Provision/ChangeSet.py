from Logger import Log
import SSH
import MyRequest
from Avaya.Function import Page
from Avaya.ManageConnection import LoginSsh, CloseSsh
from Avaya.KeyCommands import NEXTPAGE, CANCEL, ENTER, CLEARFIELD
from Avaya.RegexPattern import STATIONPAGEPATTERN
import json

def DoPreChangeVerification():
    Log("Verifying required data")
    if(MyRequest.ParamDictionary == None):
        raise Exception("No parameters found")
    changeDict = json.loads(MyRequest.ParamDictionary) 
    if(changeDict == None):
        raise Exception("Parameters dictionary cannot be deserialized.  Perhaps it's not in the correct Dictionary<string, string> format")
    if("Extension" not in changeDict):
        raise Exception("The Extension was not found in the parameters list")
    return changeDict

def DoChangeSet():
    Log("-> DoChangeSet")
    changeDictionary = DoPreChangeVerification()
    ext = changeDictionary["Extension"]
    Log("Changing Station: {0}".format(ext))
    connected = SSH.IsConnected
    Log("SSH connected: {0}".format(connected))
    if not connected:
        LoginSsh()
    
    SSH.SendCommand("Change Station {0}".format(ext))
    pageData = SSH.WaitForPattern(STATIONPAGEPATTERN, 1)
    if(pageData != None):
        pageDetails = Page.GetPageDetails(pageData)
        Log("page {0} of {1}".format(pageDetails.group(1), pageDetails.group(2)))
        SSH.SendCommand(CANCEL)
    else:
        raise Exception("Station {0} is locked, invalid or does not exist.".format(ext))
 
    SSH.ProgramBreak()

    return True