from Logger import Log
from Globals import ExternalGlobals
import SSH
import re
from Avaya.Function import Page
from Avaya.KeyCommands import NEXTPAGE, CANCEL
from Avaya.RegexPattern import STATIONPAGEPATTERN
# from enum import Enum  #ironpython 2.7 doesn't support python3 yet... retry when alpha version 3.4 is stablized

def DoDisplayStation(listStatNumbers):
    Log("->DisplayStation.DoDisplayStation")
    dumpLocation = ExternalGlobals.MyExternalGlobals.GetVariable(ExternalGlobals.GENERAL, ExternalGlobals.SWITCHDUMPLOCATION)
    if dumpLocation == None or dumpLocation.strip() == "":
        raise Exception("There is no location to dump the report to.  Please specify the report dump location in the Cairs Switch > Global Variables > General.SwitchDumpLocation")
    try:
        fullPath = "{0}\\{1}".format(dumpLocation,"AvayaDispStats.txt")
        if SSH.RerouteOutputToFile(fullPath):
            Log("File output rerouted to location:{0}".format(fullPath))
            Log("...")
            for num in listStatNumbers:
                # Log("BEGINNUMBER:{0}".format(num))
                GetStationInfo(num)
                # Log("ENDNUMBER:{0}".format(num))
        else:
            #won't hit here... will error on the c# side.
            raise Exception("Couldn't reroute file")
    except Exception as e:
        raise e
    finally:
        SSH.FillBuffer()
        SSH.EndRouteOutputToFile()
    
    Log("Display Stations Complete!")

def GetStationInfo(number):
    # SSH.ProgramBreak()
    SSH.SendCommand('Display Station {0}'.format(number))
    pageData = SSH.WaitForPattern(STATIONPAGEPATTERN, 1)
    pageMax = Page.GetPageMax(pageData)
    currentPage = 1
    
    # Log("page:{0} of {1}".format(currentPage, pageMax))
    pageEndMarker = "[0m" #found multiple times on a page but not in body of page
    while currentPage < pageMax:
        response = SSH.WaitForData(pageEndMarker, 1)
        SSH.SendCommand(NEXTPAGE)
        pageData = SSH.WaitForPattern(STATIONPAGEPATTERN, 1)
        currentPage += 1
        # Log("page:{0} of {1}".format(currentPage, pageMax)) 
    SSH.SendCommand(CANCEL)
    SSH.WaitForData("Command:")

# _StationPagePattern = "\e\[0;7mPage\s+(?<CurrentPage>\d+)\s?of\s+(?<MaxPage>\d+)\e\[0m"
# def GetPageMax(page):
#     pageInfo = re.search(STATIONPAGEPATTERN, page)
#     if pageInfo != None:
        
#         return int(pageInfo.group(2))

# class PageOptions(Enum):
#     PAGEMAX = 1
#     PAGECURRENT = 2
#     ALL = 3