import getopt
import sys

import settings


def usage():
    print("Usage")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    output = '/var/opt/info'    # Default output location.
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "Invalid option."

    results = []

    app_list = map(lambda x: __import__(x), settings.INSTALLED_APPS)

    for app in app_list:
        results += [app.run()]

    fd = open(output, "w+")

    for result in results:
        fd.write(result)

    fd.close()


if __name__ == "__main__":
    main()
