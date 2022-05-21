import antigravity, sys

def geohashing():
    args = sys.argv
    if len(args) != 4:
        return (print("Wrong number of arguments!"))
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = sys.argv[3].encode('utf-8')
    except:
        return print("Input exapmle: 37.421542 -122.085589 2005-05-26-10458.68")
    antigravity.geohash(latitude, longitude, datedow)

if __name__ == '__main__':
    geohashing()