#A network admin decides to write an IP address in a particular formart, He does not want to keep the leading zeros in an IP address, e.g If the input IP address is 192.08.09.34 the output should be 192.8.9.34, Write a python program to help the network admin achieve this

import re
ip = "216.08.094.196"
string = re.sub('\.[0]*','.', ip)
print(string)