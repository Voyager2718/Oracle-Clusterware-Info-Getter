INSTALLED_APPS = [
    'scan_name',
    'disk_string'
]

ENVIROMENTS = ["ORACLE_HOME=/u01/app/grid"]


def getEnvironments():
    result = ""
    for e in ENVIROMENTS:
        result += "export " + e + ";"
    
    return result[:-1]
