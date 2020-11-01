from pythonping import ping
import nmap
import sys
ascii = """
  ____             _        _   _____ _        _____                           __  __          ______
 |  _ \           | |      | | |  __ (_)      / ____|              _          |  \/  |   /\   |  __  |
 | |_) |_ __ _   _| |_ __ _| | | |__) | _ __ | |  __  ___ _ __   _| |_   _ __ | \  / |  /  \  | |__) |
 |  _ <| '__| | | | __/ _` | | |  ___/ | '_ \| | |_ |/ _ \ '__| |_   _| | '_ \| |\/| | / /\ \ |  ___/
 | |_) | |  | |_| | || (_| | | | |   | | | | | |__| |  __/ |      |_|   | | | | |  | |/ ____ \| |
 |____/|_|   \__,_|\__\__,_|_| |_|   |_|_| |_|\_____|\___|_|            |_| |_|_|  |_/_/    \_\_|    By Nan

 Press CTRL+C To Exit While Running.
 """
print (ascii)
option = eval(input("1: Ping 2: Nmap: 3: About: 4: Quit: "))
if option == 1:
    ip = input ("IP: ")
    ping(ip, verbose=True, count=99999)
elif option == 2:
    ip = input ("IP: ")
    startport = eval(input("First Port To Scan: "))
    lastport = eval(input("Last Port To Scan: "))
    begin = startport
    end = lastport
    target = ip

    # instantiate nmap
    scanner = nmap.PortScanner()

    for i in range(begin,end+1):

        # scan the target port
        res = scanner.scan(target,str(i))

        res = res['scan'][target]['tcp'][i]['state']

        print(f'port {i} is {res}.')
elif option == 3:
    print("I'm A 14 year old new to coding and this is my first working script. It pings and can use nmap with specified ports. Please, feel free to fork and add upon it!")
elif option == 4:
    sys.exit()
else:
    print("Incorrect Option, Try Again!")
#Does this coding stuff get harder?????
