# import sys
from scapy.all import *
# import os

# The sendpacket function should create a spoofed UDP packet with
# the payload and send it over to the destination IP and port specified.

# You should ensure that the payload does not exceed 150 bytes.
# If it does, your function gracefully exits.
def sendpacket(src_ip, dst_ip, dst_port, payload):
    if len(payload) > 150: # check condition
        exit(0)

    ip = IP(dst=dst_ip, src=src_ip)
    udp = UDP(dport=dst_port) # UDP(sport=dst_port,dport=dst_port)
    packet = ip/udp/payload

    send(packet)


# for testing purposes... delete later
# def main():
#     sendpacket('192.168.1.1','192.168.1.1',1234,'\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x01\x0f\x0f')
#     # return 0
#     # print(os.sys.path)

# if __name__ == "__main__":
#     sys.exit(main())