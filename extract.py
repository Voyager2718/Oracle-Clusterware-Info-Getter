import os
import sys
import re

from bcolors import bcolors


def extractInfomation(command, regex, path=None, failedToExtractCallBack=None, successCallBack=None, envs=None):
    env = ""
    try:
        env = os.environ["ORACLE_HOME"] + "/bin/"
    except KeyError:
        try:
            env = path + "/bin/"
        except TypeError:
            env = ""

    if envs is not None:
        stdout = os.popen(envs + ';' + env + command).read()
    else:
        stdout = os.popen(env + command).read()

    try:
        result = re.search(regex, stdout).group(1)
        if successCallBack is not None:
            return successCallBack()
        return result
    except:
        if failedToExtractCallBack is not None and "PRKF-1110" in stdout:
            return failedToExtractCallBack()
        else:
            print(stdout)
            sys.exit(bcolors.FAIL +
                     "Failed to extract information. You may need to export ORACLE_HOME or change it in settings.py" + bcolors.ENDC)
