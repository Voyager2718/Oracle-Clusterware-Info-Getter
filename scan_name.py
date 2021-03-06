import extract
import settings


def run():
    scan_name = extract.extractInfomation(
        "srvctl config scan", "(?<=SCAN name: )(.*?),", path=settings.getOracleHome())
    print("SCAN Name: " + scan_name)
    return "SCAN: " + scan_name
