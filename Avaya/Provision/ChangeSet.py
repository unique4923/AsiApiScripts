from Logger import Log
import SSH
import MyRequest
import re
from Avaya.Function import Page
from Avaya.ManageConnection import Login, CloseSsh
from Avaya.KeyCommands import NEXTPAGE, CANCEL, ENTER, CLEARFIELD, NEXTFIELD, DOWNARROW, HELP
from Avaya.RegexPattern import STATIONPAGEPATTERN, FIELDVALUEPATTERN, PAGEENDINGPATTERN
from Avaya.AvayaConstant import PAGE_END_EDIT_MODE, EDITABLE_FIELD
import json

def DoPreChangeVerification():
    Log("Verifying required data")
    if(MyRequest.ParamDictionary == None):
        raise Exception("No parameters found")
    changeDict = json.loads(MyRequest.ParamDictionary) 
    if(changeDict == None):
        raise Exception("Parameters dictionary cannot be deserialized.  Perhaps it's not in the correct Dictionary<string, string> format")
    if("EXTENSION" not in changeDict):
        raise Exception("The Extension was not found in the parameters list")
    return changeDict

def DoChangeSet():
    Log("-> DoChangeSet")
    changeDictionary = DoPreChangeVerification()
    
    Login()
    
    ext = changeDictionary["EXTENSION"]
    Log("Changing Station: {0}".format(ext))
    SSH.SendCommand("Change Station {0}".format(ext))
    
    LastPage = False
    while not LastPage:
        pageHeader = SSH.WaitForPattern(STATIONPAGEPATTERN, 1)    
        if(pageHeader != None):
            pageNumbers = Page.GetPageDetails(pageHeader)
            currentPage = pageNumbers.group(1)
            maxPage = pageNumbers.group(2)
            LastPage = (currentPage == maxPage)
            Log("page {0} of {1}".format(currentPage, maxPage))
            SSH.SendCommand(HELP)
            DoPage(changeDictionary)
            
            if(not LastPage):
                SSH.SendCommand(NEXTPAGE)
        else:
            raise Exception("Station {0} is locked, invalid or does not exist.".format(ext))
 
    SSH.SendCommand(ENTER)
    SSH.WaitForData("Command successfully completed")
    return True

def DoPage(changeDict):
    SSH.ProgramBreak()
    positionSet = set()
    # currentLine = SSH.WaitForPattern(FIELDVALUEPATTERN, 2)
    # currentPage = SSH.WaitForPattern(PAGEENDINGPATTERN, 1)
    currentPage = SSH.WaitForData("[0;7m")
    if(currentPage != None):
        match = re.findall(FIELDVALUEPATTERN, currentPage)
        Log("matches:{0}".format(match))
    else:
        raise Exception("CurrentLine blank!")
    # LastField = False
    # while not LastField:
    #     currentLine = SSH.WaitForPattern(FIELDVALUEPATTERN, 1)
    #     if(currentLine != None):
    #         # Log("CurrentField:{0}".format(currentLine))
    #         match = re.search(FIELDVALUEPATTERN, currentLine)
    #         if(match == None): 
    #             raise("Error matching regex in script when server matched>Pattern:{0}, line:{1}".format(FIELDVALUEPATTERN, currentLine))
    #         fieldName = match.group("FIELD").strip().upper()
    #         position = match.group("POSITION")
    #         if(position in positionSet):
    #             #back to beginning of page
    #             return

    #         positionSet.add(position)
    #         Log("FieldName: {0}, Position {1}".format(fieldName, position))
    #         UpdateField(fieldName, changeDict)
    #         SSH.SendCommand(HELP)
    #         SSH.SendCommand(NEXTFIELD)
    #     else: 
    #         Log("End of editible fields")
    #         # Log("Set:{0}".format(positionSet))
    #         LastField = True
    
def UpdateField(fieldName, changeDict):
    if(fieldName in changeDict.keys()):
        newValue = changeDict[fieldName]
        Log("New Value: {0}".format(newValue))
        
        # SSH.SendCommand(newValue, False, False)
        # SSH.SendCommand(NEXTFIELD)
