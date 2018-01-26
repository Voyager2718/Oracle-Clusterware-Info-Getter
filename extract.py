import os
import sys
import re

from bcolors import bcolors


def extractInfomation(command, regex, path=None, failedToExtractCallBack=None, successCallBack=None, envs=None):
    env = ""
    try:
        env = [os.environ["ORACLE_HOME"] + "/bin/",
               path + "/bin/"][path is not None]
    except KeyError:
        env = ""

    if envs is not None:
        stdout = os.popen(envs + ';' + env + command).read()
    else:
        stdout = os.popen(env + command).read()

    try:
        result = re.search(regex, stdout).group(1)
        if successCallBack is not None:
            successCallBack()
        return result
    except:
        if failedToExtractCallBack is not None:
            failedToExtractCallBack()
        else:
            sys.exit(bcolors.FAIL +
                     "Failed to extract information. You may need to set ORACLE_HOME in ENVIRONMENTS in settings.py first." + bcolors.ENDC)
