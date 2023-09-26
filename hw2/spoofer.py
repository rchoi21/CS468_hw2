import sys
from scapy.all import *

# The sendpacket function should create a spoofed UDP packet with
# the payload and send it over to the destination IP and port specified.

# You should ensure that the payload does not exceed 150 bytes.
# If it does, your function gracefully exits.
def sendpacket(src_ip, dst_ip, dst_port, payload):
    if payload > 150:
        sys.exit()

    ip = IP(dst = dst_ip, src = src_ip)
    udp = UDP(dport=dst_port)
    packet = ip/udp/payload
    send(packet)

# for testing purposes... delete later
def main():
    return 0

if __name__ == "__main__":
    sys.exit(main())