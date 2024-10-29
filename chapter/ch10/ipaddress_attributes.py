'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: ipaddress 실습
'''

import binascii
import ipaddress as ipa

Addresses = [
    '192.168.0.5',
    '2001:0:9d38:6abd:480:f1f:3f57:fffb',
]

for ipaddr in Addresses:
    addr = ipa.ip_address(ipaddr)
    print(f'IP address: {addr!r}')                              #IP 주소
    print(f'IP Version: {addr.version}')                        #버전
    print(f'Packed addr: {binascii.hexlify(addr.packed)}')      #압축 바이너리 주소
    print(f'Integer addr: {int(addr)}')                         #정수형 주소
    print(f'Is private: {addr.is_private}')                     #사설망 조사
    print()