from Logger import Log
import SSH
from Avaya.ManageConnection import LoginSsh, CloseSsh
import ListStation
import DisplayStation

def DoSetDump():
    Log("-> DoSetDump")
    connected = SSH.IsConnected
    Log("SSH connected: {0}".format(connected))
    if not connected:
        LoginSsh()

    listStatNumbers = ListStation.GetNumbersInSwitch()
    SSH.WaitForData("Command:")
    DisplayStation.DoDisplayStation(listStatNumbers)
    # Log(listStatNumbers)
    
    CloseSsh()
    return True

def DoPortDump():
    Log("-> DoPortDump")
    return False