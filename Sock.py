import socket


def check_host_status(host ):
    port = [20, 21, 22, 25, 53, 80, 123, 179, 443, 500, 587, 3389]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(5)

    for prt in port:
        try:
            sock.connect((host,prt))
            return True

        except socket.error:
            pass

    sock.close()
    return False
def check_host():
    host = input("Enter an host")

    result = check_host_status(host)
    if result:
        print("the host is online \U0001F44D")
    else:
        print("the host is offline \U0001F614")

def check_host_by_range_port(host ,port_list ):
    for prt in port_list:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.settimeout(5)
            sock.connect((host,prt))
            service = socket.getservbyport(prt,'tcp')
            print('open port detected :' + host +'\t\t' + '-- port :' + str(prt) + '\t\t' + '-- service :' + service )

        except socket.error:
            pass

    sock.close()

def  check_host_by_range_port_runner():
    host = input('Enter host: ')
    port = []
    while True:
        pt = int(input('Enter port number: \t\tif input is completed enter -1'))
        if pt == -1:
            break
        port.append(pt)

    check_host_by_range_port(host,port)

f = int(input('Enter 1 for phase1 or 2 for phase2 :'))
if f == 2:
    check_host_by_range_port_runner()
elif f == 1 :
    check_host()