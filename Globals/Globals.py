from Logger import Log
import MyRequest
from ExternalGlobals import ExternalGlobals

def Inititalize():
    Log("Initialize Globals")
    global MyExternalGlobals
    if MyRequest.ExternalGlobals is not None:   
        MyExternalGlobals = ExternalGlobals()
        Log("myexternalglobals:{0}".format(MyExternalGlobals))
    else:
        Log("No external variables found")
    #add more global variables here...