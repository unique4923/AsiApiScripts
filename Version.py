
def GetScriptInfo():
    #Return Script Version Number (double) -> used to denote base master branch version these came from
    #Return Branch (string) -> "master branch" or specific customer
    #Return lastUpdateDate (string) -> Last day these scripts were updated
    version = 1.1
    branch = "Master"
    lastUpdateDate = "5/7/2021"
    return version, branch, lastUpdateDate  

scriptInfo = GetScriptInfo()
Version = scriptInfo[0]
Branch = scriptInfo[1] 
LastUpdateDate = scriptInfo[2]

#HISTORY
# 1.1 5/6/21 - Architecture working.  Website working.  Avaya Set Sync commands working.  Stub for port sync.... lots to do still.