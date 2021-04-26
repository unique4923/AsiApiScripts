from Logger import Log
from Globals import Globals, Cairs
import SSH
import re
from Avaya.KeyCommands import NEXTPAGE, CANCEL

def DoDisplayStation(listStatNumbers):
    Log("->DisplayStation.DoDisplayStation")
    dumpLocation = Globals.MyCairsGlobals.GetVariable(Cairs.GENERAL, Cairs.SWITCHDUMPLOCATION)
    if dumpLocation == None or dumpLocation.strip() == "":
        raise Exception("There is no location to dump the report to.  Please specify the report dump location in the Cairs Switch > Global Variables > General.SwitchDumpLocation")
    try:
        fullPath = "{0}\\{1}".format(dumpLocation,"AvayaDispStats.txt")
        if SSH.RerouteOutputToFile(fullPath):
            Log("File output rerouted to location:{0}".format(fullPath))
            for num in listStatNumbers:
                GetStationInfo(num)
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
    SSH.SendCommand('Display Station {0}'.format(number))
    response = SSH.WaitForData("[2;38HSTATION")
    if response != None:
        currentPage = 1
        pageMax = GetPageMax(response)

        while currentPage <= pageMax:
            SSH.SendCommand(NEXTPAGE)
            SSH.ProgramBreak("{0} page {1} of {2}".format(number, currentPage, pageMax))
            #[2;38HSTATION
            nextPage = SSH.WaitForData("Page")
            if response != None:
                # SSH.SendCommand(CANCEL)
                currentPage += 1
    
    SSH.SendCommand(CANCEL)

_StationPagePattern = "\e\[0;7mPage\s+(?<CurrentPage>\d+)\s?of\s+(?<MaxPage>\d+)\e\[0m"
def GetPageMax(page):
    pageInfo = re.search(_StationPagePattern, page)
    if pageInfo != None:
        return int(pageInfo.group(2))