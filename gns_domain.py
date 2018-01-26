import extract
import settings


def run():
    gns_result = extract.extractInfomation(
        "srvctl config gns", "(?<=Domain served by GNS: )(.*?)\n", failedToExtractCallBack=lambda: "GNS not configured.", path=settings.getOracleHome())
    if gns_result == "GNS not configured.":
        print(gns_result)
        return ""
    print("GNS Domain: " + gns_result)
    return "GNS Domain: " + gns_result
