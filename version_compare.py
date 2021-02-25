#!/bin/python3.7.6
#
# Compare the version function
# Feb 24, 2021 by Robin 
"""Given two version strings, such as “10.3.2.3642” and “2.0a”, write a function that takes two version strings and compares them.
The function should return 1 if version string A > B, return 0 if A == B, and return -1 if A < B.
Please be mindful that not all version strings will be equal length, such as “1.0” and “1.0.0.1”.
Also keep in mind that software versions sometimes use letters to designate maintenance releases, for example “2.0a” might indicate a maintenance release issued as an update to “2.0”.
This can obviously be very different from vendor to vendor.

Optional:
If you’re up for more of a challenge, consider what kind of edge cases could arise from this loose definition of a version string, state what choices your implementation will make, and include support for those cases in your solution.
For example, how do “0.2.3” and “.2.3” compare? What about “1”, “1.0”, and “1.0.0”? What about “a8” and “a9” and “a10”?
If letters and numbers are allowed, what about “1.😀” compared with “1.0”?

We are interested in a complete approach to software development: which may include how clear & maintainable the code is, how thoroughly the code has been tested,and how the developer handles any ambiguity in the specification."""
#

def verionsCompare(ver1, ver2):
    verList1 = ver1.split(".")
    verList2 = ver2.split(".")
    maxLenth = len(verList1)
    if (len(verList1) < len(verList2)):
        maxLenth = len(verList2)
        for i in range(len(verList2) - len(verList1)):
            verList1.append("")
    else:
        for i in range(len(verList1) - len(verList2)):
            verList2.append("")
    for i in range(maxLenth):
        result = strCompare(verList1[i], verList2[i])
        if (result >= 0):
            return result
    return -1

def strCompare(s1, s2):
    if s1 == "":
        s1 = "0"
    if s2 == "":
        s2 = "0"
    int1 = getNumInStr(s1)
    int2 = getNumInStr(s2)
    if (int1 > int2):
        return 1
    elif (int1 < int2):
        return 0
    else:
        if (s1 > s2):
            return 1
        elif (s1 == s2):
            return -1
        else:
            return 0
    
def getNumInStr(str):
    numStr = ""
    for char in str:
        if char.isdigit():
            numStr += char
    if(numStr != ""):
        return int(numStr)
    else:
        return 0


def convertResult(result):
    if (result == 1):
        return " > " 
    elif (result == 0):
        return " < " 
    elif (result == -1):
        return " = "
    else:
        return " "
    

if __name__ == '__main__':
    testData =[["10.3.2.3642", "2.0a"],
               ["1.0", "1.0.0.1"],
               ["2","2.0a"],
               ["0.2.3", ".2.3"],
               ["1","1.0.0"],
               ["a8","a10"],
               ["1.😀","1.0"],
               ["1.😀","1.1"]
               ]
    expectedResult = [1, 0, 0, -1, -1, 0, 1, 0]
    for i in range(len(testData)):
        versionPair = testData[i]
        result = verionsCompare(versionPair[0], versionPair[1])
        if (result == expectedResult[i]):
            print("Test case " + str(i + 1) + " : Pass")
            print("Test result: " + versionPair[0] + convertResult(result) + versionPair[1] + "\n")
        else:
            print("Test case " + str(i + 1) + " : Fail")
            print("Expected result: " + versionPair[0] + convertResult(expectedResult[i]) + versionPair[1])
            print("Test result: " + versionPair[0] + convertResult(result) + versionPair[1]+ "\n")


