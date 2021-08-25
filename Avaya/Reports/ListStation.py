from Logger import Log
import  SSH
import re
from Avaya.KeyCommands import NEXTPAGE, CANCEL
from Avaya.RegexPattern import DNLINEPATTERN

# _DnLinePattern = "\e?\[\d{1,};1H(?<DN>[\d-]+)"

def ParsePage(page, p, incrementPageNumber = True):
    pageDnList = re.findall(DNLINEPATTERN, page)
    Log("Numbers On Page{0}:{1}".format(p.iPage, pageDnList))
    p.DnList += pageDnList
    if incrementPageNumber:
        p.iPage += 1

def ManagePage(page, p):
    if page == None:
        #could be pages end???
        response = SSH.GetCurrentMessage()
        if "Command:" in response:
            ParsePage(response, p, False)
            Log("Finished ListStat!")
            return True
        else:
            Log("ERROR: Not end / Not page: {0}".format(response))
            raise Exception("Not getting response")
    else:
        ParsePage(page, p)
        #####DEBUGGING 
        # return True
        #####END
        SSH.SendCommand(NEXTPAGE)
        return False

def GetNumbersInSwitch():
    Log("->ListStation.GetNumbersInSwitch()")
    SSH.SendCommand("list stat") 
    endMarker = "Command successfully completed"
    p = ListStatPageData()
    gotEnd = False

    while not gotEnd:
        response = SSH.WaitForData("press NEXT PAGE to continue")
        gotEnd = ManagePage(response, p)
    
    SSH.FillBuffer()
    SSH.SendCommand(CANCEL)
    p.PrintStatistics()
    return p.DnList
        
class ListStatPageData:
    DnList = []
    iPage = 1

    def PrintStatistics(self):
        Log("Total Pages: {0}".format(self.iPage))
        Log("Total Numbers: {0}".format(len(self.DnList)))