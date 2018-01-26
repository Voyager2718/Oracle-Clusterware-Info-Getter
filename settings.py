import os

INSTALLED_APPS = [
    'owner',
    'scan_name',
    'gns_vip',
    'gns_domain',
    'disk_string'
]

ENVIROMENTS = ["ORACLE_HOME=/u01/app/18101/grid"]


def getEnvironments():
    result = ""
    oh = ""
    try:
        oh = os.environ["ORACLE_HOME"]
    except NameError:
        pass

    for e in ENVIROMENTS:
        if "ORACLE_HOME=" in e and oh is not "":
            result += "export ORACLE_HOME=" + oh + ';'
        else:
            result += "export " + e + ';'
    return result[:-1]


def getOracleHome():
    for e in ENVIROMENTS:
        if "ORACLE_HOME=" in e:
            return e[e.find('=') + 1:]
    return None
