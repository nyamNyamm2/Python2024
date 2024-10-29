'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: ipaddress 실습
'''

import ipaddress as ipa

NetAddress = ['10.9.0.0/24', 'fdfd:87b5:b475:5e3e::/64']

for addr in NetAddress:
    net = ipa.ip_network(addr)
    print(f'Network Address: {net!r}')
    print(f'Is private: {net.is_private}')
    print(f'Broadcast Address: {net.broadcast_address}')
    print(f'Compressed Address: {net.compressed}')
    print(f'Addr with netmask: {net.with_netmask}')
    print(f'Addr with hostmask: {net.with_hostmask}')
    print(f'Num address: {net.num_addresses}')
    print()