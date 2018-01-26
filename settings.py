INSTALLED_APPS = [
    'scan_name',
    'gns_domain',
    'disk_string'
]

ENVIROMENTS = ["ORACLE_HOME=/u01/app/18101/grid"]


def getEnvironments():
    result = ""
    for e in ENVIROMENTS:
        result += "export " + e + ";"

    return result[:-1]


def getOracleHome():
    for e in ENVIROMENTS:
        if "ORACLE_HOME=" in e:
            return e[e.find('=') + 1:]
    return None
