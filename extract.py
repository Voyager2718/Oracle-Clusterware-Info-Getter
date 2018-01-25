import os
import sys
import re


def extractInfomation(command, regex, path=None, failedToExtractCallBack=None, successCallBack=None):
    stdout = os.popen(os.environ["ORACLE_HOME"] + "srvctl config scan").read()
    env = ""
    try:
        env = os.environ[["ORACLE_HOME", path][path == "None"]]
    except KeyError:
        pass
    env += '/'
    stdout = os.popen(env + command).read()

    try:
        result = re.search(regex, stdout).group(1)
        if successCallBack is not None:
            successCallBack()
        return result
    except:
        if failedToExtract is not None:
            failedToExtract()
        else:
            sys.exit("Failed to extract SCAN Name.")
