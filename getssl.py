# coding=utf-8
# @Author   : zpchcbd HG team
# @Time     : 2021-08-29 14:19

import socket
import ssl


s = socket.socket()
s.settimeout(1)
c = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='./cacert.pem')
c.settimeout(10)
c.connect(('www.geely.com', 443))
cert = c.getpeercert()
print(cert)