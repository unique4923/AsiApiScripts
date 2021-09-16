from Logger import Log
import SSH
from Avaya.ManageConnection import Login, CloseSsh
from Consts import ScriptReturn

import MyRequest
def DoSetDump():
    import ListStation
    import DisplayStation
    Login()

    listStatNumbers = ListStation.GetNumbersInSwitch()
    MyRequest.ReturnDictionary[ScriptReturn.LIST_STAT_COUNT] = str(len(listStatNumbers))
    SSH.WaitForData("Command:")
    DisplayStation.DoDisplayStation(listStatNumbers)
    # Log(listStatNumbers)
    
    CloseSsh()
    return True

def DoPortDump():
    Log("-> DoPortDump")
    return False