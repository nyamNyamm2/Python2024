'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: ipaddress 실습
'''

# IP 주소가 네트워크에 속하는지 조사하는 프로그램

import ipaddress

NETWORKS = [
    ipaddress.ip_network('10.9.0.0/24'),
    ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64'),
]

ADDRESSES = [
    ipaddress.ip_address('10.9.0.6'),
    ipaddress.ip_address('10.7.0.31'),
    ipaddress.ip_address(
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'
    ),
    ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
]

for ip in ADDRESSES:
    for net in NETWORKS:
        if ip in net: #네트워크에 속하는가?
            print('{}\nis on {}'.format(ip, net))
            break
    else:
        print('{}\nis not on a known network'.format(ip))
    print()