from Logger import Log
import MyRequest

class ExternalGlobals:
    def __init__(self):
        if MyRequest.ExternalGlobals is not None:
            externalGlobalCount = len(MyRequest.ExternalGlobals)
            self.LoadGlobalsDictionary()
        else:
            externalGlobalCount = 0

        Log("***External Global Variables: {0} (Switch Dump Location - {1})".format(externalGlobalCount, self.GetVariable(GENERAL, SWITCHDUMPLOCATION)), False)
    
    def ReplaceCategoriesNames(self, category):
        if category.__contains__("Avaya"): return AVAYA
        elif category.__contains__("TB850"): return TELEBOSS
        elif category.__contains__("General"): return GENERAL
        elif category.__contains__("M1"): return M1
        elif category.__contains__("CS2100orSL100"): return CS2100orSL100
        elif category.__contains__("CS2100"): return CS2100

        else: return category 

    def LoadGlobalsDictionary(self):
        for gv in MyRequest.ExternalGlobals:
            category = self.ReplaceCategoriesNames(gv.Setting_Category)
            settingName = gv.Setting_Name
            settingValue = gv.Initial_Value

            if self._LookupDictionary.__contains__(category):
                subDict = self._LookupDictionary[category]
            else:
                subDict = {}
            
            subDict[settingName] = settingValue
            self._LookupDictionary[category] = subDict

        # Log(self._LookupDictionary.keys())    
        # Log(self._LookupDictionary)

    _LookupDictionary = {}
    
    def GetVariable(self, category, settingName):
        returnValue = ""
        
        if self._LookupDictionary is not None and category in self._LookupDictionary:
            subDict = self._LookupDictionary[category]
            if settingName in subDict:
                returnValue = subDict[settingName]
        
        return returnValue
            
#Group Names
AVAYA = "Avaya"
TELEBOSS = "Teleboss"
GENERAL = "General"
M1 = "M1"
CS2100orSL100 = "CS2100orSL100"
CS2100 = "CS2100"

#Setting Names
SWITCHDUMPLOCATION = "SwitchDumpLocation"
SWITCHDUMPFILENAME = "SwitchDumpFileName"
WAITTIME_REGULAR = "WaitTime_Regular"
WAITTIME_EXLONG = "WaitTime_ExLong"
WAITTIME_FAST = "WaitTime_Fast"
WAITTIME_FILLBUFFER = "WaitTime_FillBuffer"
WAITTIME_LONG = "WaitTime_Long"
WAITTIME_OPENCOM = "WaitTime_OpenCom"
WAITTIME_REGULAR = "WaitTime_Regular"
WAITTIME_SENDAFTERPROMPT = "WaitTime_SendAfterPrompt"
WAITTIME_SWITCHREPORT = "WaitTime_SwitchReport"
WAITTIME_WAITFORDATA = "WaitTime_WaitForData"

#### list from Cairs in python --- Avaya30 is replaced by "Avaya" in lookup dict
# Avaya.DNLength = None
# Avaya.FindAvailableExtMarker = 13H
# Avaya30.AnalogBoardCodes = None
# Avaya30.AnalogBoardType = ANA
# Avaya30.AvailableDNBeginMarker = ;9H
# Avaya30.AvailableDNEndMarker = ;24H
# Avaya30.DefaultAnalogSet = 2500
# Avaya30.DefaultDigitalSet = 6408
# Avaya30.defaultSIPTrunk = 
# Avaya30.DigitalBoardCodes = None
# Avaya30.DigitalBoardType = DIG
# Avaya30.DNLength = None
# Avaya30.Do_Not_BusyStat = 0
# Avaya30.duplicateStationAnalog = None
# Avaya30.duplicateStationDigital = None
# Avaya30.duplicateStationIP = None
# Avaya30.EndDNRange = None
# Avaya30.EPNLength = 5
# Avaya30.ExtraErrorLogging = 
# Avaya30.FieldValuesWithFakePageEndings = 
# Avaya30.IPSets = None
# Avaya30.LeaveConnectionOpen = None
# Avaya30.PINonLogin = None
# Avaya30.PINTextToWaitFor = None
# Avaya30.SendSingleChr13InsteadOfSendLine = None
# Avaya30.SyncDataSets = None
# Avaya30.UseAutoSatOnLogin = None
# CS2100.Cards_Analog = None
# CS2100.Cards_Analog_Generic = None
# CS2100.Cards_Digital = None
# CS2100.Cards_Digital_Generic = None
# CS2100.Cards_IP = None
# CS2100.Cards_IP_Generic = None
# CS2100.CBMTextForLogout = None
# CS2100.DefaultAnalogLENPrefix = None
# CS2100.DefaultCustomerGroup = None
# CS2100.DefaultCustomerSubGroup = None
# CS2100.DefaultDigitalLENPrefix = None
# CS2100.DefaultIPLENPrefix = None
# CS2100.InputPrompt = >
# CS2100.Intercept_Name = None
# CS2100.LATANAME = None
# CS2100.LeaveGateOpen = 0
# CS2100.Line_Treatment_Group = None
# CS2100.MustConfirm = 0
# CS2100.NCOS_Delinquent = None
# CS2100.NetName_Private = Private
# CS2100.NetName_Public = Public
# CS2100.OutSetOnLenChange = None
# CS2100.SIP_DN_Length = None
# CS2100.UseDNINVwithQCUSTinSync = None
# CS2100.UseGateForSetSnyc = None
# CS2100.UseGateForSetSync = None
# CS2100.UseIPClientPromptForAdd = None
# CS2100.UseOneLineLogIn = -1
# CS2100.UseSERVORD = 
# CS2100.Login.UseCMTLogin = 0
# DigiPort.LoginName = None
# DigiPort.PasswordName = None
# DigiPort.Use_DigiPortServer = None
# DigiPort.UseSSHForLogin = None
# DL150.UsePassThrough = 0
# DotNet.CS2100.ProvisionLoginType = OSSGATE
# DotNet.CS2100orSL100.DefaultCustomerGroup = None
# DotNet.CS2100orSL100.DefaultCustomerSubGroup = None
# DotNet.CS2100orSL100.InputPrompt = >
# DotNet.CS2100orSL100.Intercept_Name = None
# DotNet.CS2100orSL100.MustConfirm = 0
# DotNet.CS2100orSL100.SwitchType = None
# DotNet.General.LeaveConnectionOpen = 0
# DotNet.General.SingleLineLogin = 0
# EWSD.ActiveShelves = None
# EWSD.NoResponseCount = None
# EWSD.SealCurTemplate = None
# EWSD.UseChrgOnDigital = None
# EWSD.UseSwitchDefaultValueForILNATT = None
# EWSD.VirtualShelves = None
# EWSD.WaitBetweenChars = None
# General.AreaCode = None
# General.AuthCodeLength = None
# General.AuthPart = None
# General.AvailDNTotalRange = 50
# General.Debug_Mode = 0
# General.Debug_Mode_Disable_Logging = 0
# General.Debug_Mode_TraceExec_Detail = 0
# General.Debug_Mode_TraceExecution = 0
# General.DefaultAreaCode = None
# General.DefaultPrefix = None
# General.DigitalLineUnit = None
# General.DN_Length = None
# General.DNSearchRange = None
# General.EWSDDnLength = None
# General.EWSDPrompt = None
# General.ExecutableFileName = None
# General.ExecutableFilePath = None
# General.FindAndReplaceTextCommandString = 
# General.FindAndReplaceTextLocation = 
# General.Ftr_Delimiter = None
# General.Line_Distribution_Method = None
# General.M1_AreaCode_NumberRange = None
# General.NumberPlanRanges = None
# General.SwitchDumpFileName = None
# General.SwitchDumpLocation = D:\SwitchReports
# General.SwitchIDNumber = None
# General.TempSkip = None
# General.TotalBufferCountPass = 3
# General.UseSendDataToSend = None
# General.WaitTime_Break = 1000
# General.WaitTime_ExLong = 10000
# General.WaitTime_Fast = 250
# General.WaitTime_FillBuffer = 1500
# General.WaitTime_Long = 750
# General.WaitTime_OpenCom = 1500
# General.WaitTime_Regular = 2000
# General.WaitTime_SendAfterPrompt = 2000
# General.WaitTime_SwitchReport = 120000
# General.WaitTime_WaitForData = 5000
# HiPath.DestinationReportFolder = None
# HiPath.DNLength = None
# HiPath.DnRoutingFormatOptions = None
# HiPath.InternalDialingExchange = None
# HiPath.InternalDNLength = None
# HiPath.InternalReRoute = None
# HiPath.IP_SDMI_Card_Type = IP2
# HiPath.LeaveConnectionOpen = None
# HiPath.UseOwnNode = None
# ISDN.CS2100orSL100.ABS = None
# ISDN.CS2100orSL100.CS = None
# ISDN.CS2100orSL100.DEFLTERM = None
# ISDN.CS2100orSL100.EKTS = None
# ISDN.CS2100orSL100.ISDNOPTIONS = None
# ISDN.CS2100orSL100.ISSUE = None
# ISDN.CS2100orSL100.LTCLASS = None
# ISDN.CS2100orSL100.MAXKEYS = None
# ISDN.CS2100orSL100.PS = None
# ISDN.CS2100orSL100.TEITYPE = None
# ISDN.CS2100orSL100.VERSION = None
# Lucent.DefaultFRL = None
# Lucent.DialingPlans = None
# Lucent.OutputDevice = None
# Lucent.Prompt = None
# M1.Add_TNList_During_Set_Sync = None
# M1.BranchOfficeSoftware = None
# M1.CPND_LANG =  
# M1.CPND_XPLN =  
# M1.CPNDDisplayFormat =  
# M1.DN_Length = None
# M1.IPEnabled = None
# M1.LeaveConnectionOpen = 0
# M1.PCA_Digits = None
# M1.Send_Escape_Asterisk = 0
# M1.SleepBetweenSendCharacters = 10
# M1.SoftwareVersion = None
# M1.TN_Balancing_Method = SUPERLOOP
# M1.TTYPortNumber = None
# M1.Use_CHRString_13_only = None
# M1.UseCPND = 0
# M1.UsingSymposium = 0
# M1.DL150.Use_DL150 = 0
# M1.ISDN.SPID1Prefix = None
# M1.ISDN.SPID2Prefix = None
# M1.TB850.JoinPassthroughSessions = 0
# M1.TB850.LoginRequired = -1
# M1.TB850.PasswordOnlyRequired = 0
# M1.TB850.Use_TB850 = -1
# M1.TB850.WOPRbypassPort = 1
# SL100.AvailableDNTreatment = None
# SL100.Cards_Analog = None
# SL100.Cards_Analog_Generic = None
# SL100.Cards_Digital = None
# SL100.Cards_Digital_Generic = None
# SL100.Cards_ISDN = None
# SL100.Cards_ISDN_Generic = None
# SL100.Character_Limitation_Block_Size = None
# SL100.Customer_Group = None
# SL100.DefaultCustomerGroup = None
# SL100.DefaultCustomerSubGroup = None
# SL100.DNLength = None
# SL100.EndofQDNWRKReport = None
# SL100.FailedLoginText = None
# SL100.Group = None
# SL100.InputPrompt = None
# SL100.Intercept_Name = None
# SL100.IPConnection = None
# SL100.LATANAME = None
# SL100.LeaveConnectionOpen = 0
# SL100.Len_Total_Length = 15
# SL100.LoginPrompt = $$
# SL100.NCOS_Default = None
# SL100.NCOS_Delinquent = None
# SL100.NCOS_Suspend = None
# SL100.NetName_Private = Private
# SL100.NetName_Public = Public
# SL100.Shelfs_Per_Switch = None
# SL100.SubGroup = None
# SL100.UserAlreadyLoggedInText = None
# TB850.BypassPort = None
# TB850.CmdToPromptSwitch = None
# TB850.JoinPassthroughSessions = 0
# TB850.KeySettingsFileName = TelebossKSF.txt
# TB850.KeySettingsFilePath = C:\Program Files\WOPR-ASI
# TB850.KSFname = KSF.txt
# TB850.KSFpath = C:\Program Files\WOPR-ASI\
# TB850.Prompt = None
# TB850.SendBreak_Character = ~
# TB850.SSHByPassNumber = None
# TB850.SwitchPromptCmdToSend = None
# TB850.TBLoginPrompt = None
# TB850.TelebossLoginRequired = 1
# TB850.Use_Teleboss850 = -1
# TB850.Use_UsernamePassword = None
# TB850.UsePasswordOnlyOnLogin = 0
# TB850.UseSSHForLogin = None
# TB850.SVZ.CoreIP = None
# TB850.SVZ.OSSGate_IP = None
# TB850.SVZ.OSSGate_Port = None
# TB850.SVZ.Prompt = None
# TB850.SVZ.UseSVZ_TB850 = None
# TB850_SVZ.Prompt = None
# Teleboss.KSFname = KSF.txt
# Teleboss.KSFpath = C:\Program Files\WOPR-ASI\