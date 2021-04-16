from Logger import Log
import  SSH
import re
from Avaya.KeyCommands import NEXTPAGE

def GetNumbersInSwitch():
    Log("Doing ListStat")
    SSH.SendCommand("list stat")
    endMarker = "Command successfully completed"
    
    dnLine = "\e?\[\d{1,};1H(?<DN>[\d-]+)"
    gotEnd = False
    while not gotEnd:
        response = SSH.WaitForData("press NEXT PAGE to continue")
        Log(response)
        
        if response == None:
            response = SSH.GetCurrentMessage()
            
            if "Command:" in response:
                Log("Finished ListStat!")
                gotEnd = True
            else:
                Log("Not end / Not page: {0}".format(response))
                raise Exception("Not getting response")
        else:
            Log("Next Page")
            SSH.ProgramBreak()
            SSH.SendCommand(NEXTPAGE)
        
