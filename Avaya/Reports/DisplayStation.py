from Logger import Log
from Globals import Globals, Cairs

def DoDisplayStation(listStatNumbers):
    Log("->DisplayStation.DoDisplayStation")
    dumpLocation = Globals.MyCairsGlobals.GetVariable(Cairs.GENERAL, Cairs.SWITCHDUMPLOCATION)
    if dumpLocation == None:
        raise Exception("There is no location to dump the report to.  Please specify the report dump location in the Cairs Switch > Global Variables > General.SwitchDumpLocation")

    Log("Report Location:{0}".format(dumpLocation))
