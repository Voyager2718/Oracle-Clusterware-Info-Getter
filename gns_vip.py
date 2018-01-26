import extract
import settings


def run():
    gns_vip = extract.extractInfomation(
        "srvctl config gns -v", "(?<=GNS VIP addresses: )(.*?)\n", failedToExtractCallBack=lambda: "Failed", path=settings.getOracleHome())
    if gns_vip == "Failed":
        raise NotImplementedError("GNS VIP: GNS not configured. Ignored.")

    print("GNS VIP: " + gns_vip)
    return "GNS VIP: " + gns_vip
