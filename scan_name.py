import extract


def run():
    scan_name = extract.extractInfomation(
        "srvctl config scan", "(?<=SCAN name: )(.*?),")
    print("SCAN Name: " + scan_name)
    return "SCAN: " + scan_name
