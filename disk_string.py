import extract
import settings


def run():
    storage = extract.extractInfomation(
        "asmcmd dsget", "(?<=parameter:)(.*?)\n", envs="export ORACLE_HOME=/u01/app/grid")
    print("Storage: " + storage)
    return "Storage: " + storage
