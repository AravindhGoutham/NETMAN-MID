#!/usr/bin/env python3

import csv

data = [
    ['Hostname', 'Interface Type', 'Interface Name', 'IP/Subnet', 'OSPF Enabled', 'OSPF Process ID', 'OSPF Area'],
    ['R1', 'Loopback', '1', '10.0.0.1/32', 'Yes', '1', '0'],
    ['R1', 'FastEthernet', "0/0", '198.51.100.4/24', 'Yes', '1', '0'],
    ['R1', 'FastEthernet', "1/1", '198.51.101.3/24', 'Yes', '1', '0'],
    ['R1', 'FastEthernet', "2/0", '198.51.102.3/24', 'Yes', '1', '0'],
    ['R2', 'Loopback', '1', '20.0.0.1/32', 'Yes', '2', '0'],
    ['R2', 'FastEthernet', "1/0", '198.51.100.3/24', 'Yes', '2', '0'],
    ['R2', 'FastEthernet', "0/0", '198.51.101.4/24', 'Yes', '2', '0'],
    ['R3', 'Loopback', '1', '30.0.0.1/32', 'Yes', '3', '0'],
    ['R3', 'FastEthernet', "1/0", '198.51.100.1/24', 'Yes', '3', '0'],
    ['R3', 'FastEthernet', "0/0", '198.51.102.5/24', 'Yes', '3', '0']
    ]

filename = 'Router-Details.csv'

with open(filename, 'w', newline='')as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print(f"The details are writtern to {filename}")



