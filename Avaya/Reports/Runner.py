from Logger import Log
import SSH
from Avaya.ManageConnection import Login, CloseSsh
import ListStation
import DisplayStation

def DoSetDump():
    Login()

    listStatNumbers = ListStation.GetNumbersInSwitch()
    SSH.WaitForData("Command:")
    DisplayStation.DoDisplayStation(listStatNumbers)
    # Log(listStatNumbers)
    
    CloseSsh()
    return True

def DoPortDump():
    Log("-> DoPortDump")
    return False