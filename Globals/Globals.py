from Logger import Log
import MyRequest
from Cairs import CairsGlobals

def Inititalize():
    # Log("Init globals")
    global MyCairsGlobals
    if MyRequest.CairsGlobals is not None:    
        MyCairsGlobals = CairsGlobals()
    
    #add more global variables here...