
def GetScriptInfo():
    #Return Script Version Number (double) -> used to denote base master branch version these came from
    #Return Branch (string) -> "master branch" or specific customer
    #Return lastUpdateDate (string) -> Last day these scripts were updated
    version = 1.3
    branch = "Master"
    lastUpdateDate = "5/15/2021"
    history = GetHistory()
    return version, branch, lastUpdateDate, history 

def GetHistory():
    return (
        "1.3 - 5/15/21 - fixed bug in getting version from Capitain.py\n"
        "1.2 - 5/7/21 - More version modifications\n" +
        "1.1 - 5/6/21 - Architecture working.  Website working.  Avaya Set Sync commands working.  Stub for port sync.... lots to do still."
    )

scriptInfo = GetScriptInfo()
Version = scriptInfo[0]
Branch = scriptInfo[1] 
LastUpdateDate = scriptInfo[2]
History = scriptInfo[3]
