from Logger import Log
import MyRequest


def Run(action):
    Log("Running Avaya Script!")
    
    if action == "SETSYNC":
        import Avaya.Reports.Runner
        return Avaya.Reports.Runner.DoSetDump()
        # return SetSync.DoSetDump()
    elif action == "PORTSYNC":
        import Avaya.Reports.Runner
        return Avaya.Reports.Runner.DoPortDump()
    elif action == "CHANGESET":
        import Avaya.Provision.ChangeSet
        return Avaya.Provision.ChangeSet.DoChangeSet()
    else:
        raise Exception('No script for Avaya action: "{0}"'.format(MyRequest.Action))
    
    return False
