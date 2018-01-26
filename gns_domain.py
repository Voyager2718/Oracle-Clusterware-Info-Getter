import extract
import settings


def run():
    gns_result = extract.extractInfomation(
        "srvctl config gns", "(?<=Domain served by GNS: )(.*?)\n", failedToExtractCallBack=lambda: "Failed", path=settings.getOracleHome())
    if gns_result == "Failed":
        raise NotImplementedError("GNS not configured. Ignored.")
    print("GNS Domain: " + gns_result)
    return "GNS Domain: " + gns_result
