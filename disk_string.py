import extract
import settings


def run():
    storage = extract.extractInfomation(
        "asmcmd dsget", "(?<=parameter:)(.*?)\n", envs=settings.getEnvironments())
    print("Storage: " + storage)
    return "Storage: " + storage
