import os
import sys
import re


def extractInfomation(command, regex, path=None, failedToExtractCallBack=None, successCallBack=None, envs=None):
    env = ""
    try:
        env = [os.environ["ORACLE_HOME"] + "/bin/", path][path is not None]
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
            sys.exit("Failed to extract information.")
