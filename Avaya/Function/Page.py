import re
from Avaya.RegexPattern import STATIONPAGEPATTERN

def GetPageDetails(pagePatternMatch):
    pageInfo = re.search(STATIONPAGEPATTERN, pagePatternMatch)
    return pageInfo #currentpage = pageInfo.group(1), maxpage = pageInfo.group(2)

def GetPageMax(pagePatternMatch):
    pageInfo = re.search(STATIONPAGEPATTERN, pagePatternMatch)
    if pageInfo != None:
        return int(pageInfo.group(2))