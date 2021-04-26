from Logger import Log
# from Avaya.Reports import SetSync, PortSync
# from Avaya.Reports import PortSync, SetSync
import MyRequest
import Avaya.Reports.Runner


def Run(action):
    Log("Running Avaya Script!")
    
    if action == "SETSYNC":
        # Log("GV report location: {0}",MyCairsGlobals.GetVariable(MyCairsGlobals.GENERAL, MyCairsGlobals.SWITCHDUMPLOCATION))
        return Avaya.Reports.Runner.DoSetDump()
        # return SetSync.DoSetDump()
    elif action == "PORTSYNC":
        return Avaya.Reports.Runner.DoPortDump()
    else:
        raise Exception('No script for Avaya action: "{0}"'.format(MyRequest.Action))
    
    return False
