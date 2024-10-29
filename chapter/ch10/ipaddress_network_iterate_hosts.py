'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: ipaddress 실습
'''

# 네트워크에 속하는 호스트 주소 확인 프로그램

import ipaddress

NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    for i, ip in zip(range(5), net.hosts()):
        print(ip)
    print()