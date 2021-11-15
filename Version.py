
def GetScriptInfo():
    #Return Script Version Number (double) -> used to denote base master branch version these came from
    #Return Branch (string) -> "master branch" or specific customer
    #Return lastUpdateDate (string) -> Last day these scripts were updated
    version = 1.5
    branch = "Master"
    lastUpdateDate = "11/15/2021"
    history = GetHistory()
    return version, branch, lastUpdateDate, history 

def GetHistory():
    return (
        "1.5 - 11/15/21 - 'Set_Sync' to as Avaya action handle to run set sync\n"
        "1.4 - 9/15/21 - Code restructure for constants.  Added Consts folder.\n"
            "\tAdded ReturnDictionary (instantiated in MyRequest as C# Dictionary<string,string>) to be used throughout.  It's added to the ScriptReturnData in the end.\n"
        "1.3 - 5/15/21 - fixed bug in getting version from Capitain.py\n"
        "1.2 - 5/7/21 - More version modifications\n" +
        "1.1 - 5/6/21 - Architecture working.  Website working.  Avaya Set Sync commands working.  Stub for port sync.... lots to do still."
    )

scriptInfo = GetScriptInfo()
Version = scriptInfo[0]
Branch = scriptInfo[1] 
LastUpdateDate = scriptInfo[2]
History = scriptInfo[3]
