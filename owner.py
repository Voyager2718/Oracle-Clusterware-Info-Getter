def run():
    try:
        input = raw_input
    except NameError:
        pass
    ret = "Owner: " + input("Please input the owner of this cluser: ")
    print(ret)
    return ret
