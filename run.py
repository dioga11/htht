j='4'
i='server_ip'
c='3'
b=exit
X='r'

V='w'
U='0'
T='2'
S='1'
O=True
L=open
H=input
D=print
import zlib as B,base64 as C,os as J,platform as k,requests as Y,json as M
from tqdm import tqdm
import time as I
from colorama import init,Fore as K
init(autoreset=O)
G=K.RED
E=K.GREEN
F=K.YELLOW
Q=K.BLUE
d=K.MAGENTA
Z=K.CYAN
A=K.RESET
l=(lambda B.decompress(C.b64decode).decode())('https://vinaflash.cloud/HUYENTHOAIHAITAC_OFFLINE_V1.apk')
m=(lambda B.decompress(C.b64decode).decode())('https://320.gsscdn.com/HTDC_20241113.ipa')
n=(lambda B.decompress(C.b64decode).decode())('HUYENTHOAIHAITAC_OFFLINE.apk')
o=(lambda B.decompress(C.b64decode).decode())('HAITACDAICHIEN_OFFLINE.ipa')
e=J.path.join(J.path.expanduser((lambda B.decompress(C.b64decode(s)).decode())('~')),(lambda B.decompress(C.b64decode).decode())('Downloads'))
p=J.path.join(e,n)
q=J.path.join(e,o)
P=(lambda s:B.decompress(C.b64decode).decode())('config.json')
r=(lambda s:B.decompress(C.b64decode).decode())('accounts.txt')
a=(lambda s:B.decompress(C.b64decode).decode())('items.json')
R=(lambda s:B.decompress(C.b64decode).decode())('events.json')
def N():
	if k.system()==(lambda s:B.decompress(C.b64decode(s)).decode())('Windows'):J.system((lambda s:B.decompress(C.b64decode(s)).decode())('cls'))
	else:J.system((lambda s:B.decompress(C.b64decode(s)).decode())('eJxLzklNLAIABgcCCA=='))
def f(O0O0O0O0O0O0O00O00O00O0O00O00O0O00O0O00O0O00O0O00O00O0O0O0O00O00O0O0O00O0O0O00O00O0O00O00O0O00O0O00O00O00O00O00O00O00O00O0O00O0O00O00O0O00O0O00O0O00O0O0O00O00O00O00O00O0O00O0O00O0O00O0O00O0O00O0O00O0O0O0O00O00O0O0O00O0O00O0O0O00O00O00O00O00O0O0O0O0O00O0O0O0O00O00O00O00):
	D(f"{Z}{O0O0O0O0O0O0O00O00O00O0O00O00O0O00O0O00O0O00O0O00O00O0O0O0O00O00O0O0O00O0O0O00O00O0O00O00O0O00O0O00O00O00O00O00O00O00O00O0O00O0O00O00O0O00O0O00O0O00O0O0O00O00O00O00O00O0O00O0O00O0O00O0O00O0O00O0O00O0O0O0O00O00O0O0O00O0O00O0O0O00O00O00O00O00O0O0O0O0O00O0O0O0O00O00O00O00}{A}",end=(lambda s:B.decompress(C.b64decode(s)).decode())(W))
	for E in range(3):D((lambda s:B.decompress(C.b64decode(s)).decode())('.'),end=(lambda s:B.decompress(C.b64decode(s)).decode())(W),flush=O);I.sleep(.5)
	D((lambda s:B.decompress(C.b64decode(s)).decode())(W))
def g():
	F=[(lambda s:B.decompress(C.b64decode(s)).decode())('Đang tải File Cấu Hình Server'),(lambda s:B.decompress(C.b64decode(s)).decode())('Load Sự Kiện Thành Công'),(lambda s:B.decompress(C.b64decode(s)).decode())('Load Vật Phẩm Thành Công'),(lambda s:B.decompress(C.b64decode(s)).decode())('Load Map Thành Công'),(lambda s:B.decompress(C.b64decode(s)).decode())('Load Tài Nguyên Thành Công'),(lambda s:B.decompress(C.b64decode(s)).decode())('Khởi Tạo Cơ Cở Dữ Liệu'),(lambda s:B.decompress(C.b64decode(s)).decode())('Kiểm Tra Cơ Sở Dữ Liệu Thành Công'),(lambda s:B.decompress(C.b64decode(s)).decode())('Kiểm Tra Kết Nối Mạng'),(lambda s:B.decompress(C.b64decode(s)).decode())('Kết Nối API VPS'),(lambda s:B.decompress(C.b64decode(s)).decode())('Khởi Động Unity'),(lambda s:B.decompress(C.b64decode(s)).decode())('Chạy Thử Nghiệm Server...')]
	for G in F:f(G);I.sleep(1.5)
	D(f"{E}Server đã sẵn sàng hoạt động!{A}");I.sleep(1)
def t():f((lambda s:B.decompress(C.b64decode(s)).decode())('Đang khởi động server...'));D(f"{E}Server đang chạy thành công!{A}");I.sleep(1.5)
def h(O0O0O0O0O0O0O0O0O00O00O00O00O0O00O0O0O00O00O0O0O00O0O00O0O0O0O00O00O00O0O00O00O00O00O00O00O0O00O00O0O00O0O0O0O00O0O0O00O0O00O0O00O00O00O0O0O00O0O0O0O00O0O00O00O0O0O00O0O00O00O0O00O00O00O00O0O00O0O0O00O0O00O00O0O0O0O0O0O00O0O0O0O0O00O0O0O0O00O00O0O0O0O00O00O00O00O0,O0O0O0O0O0O0O0O0O0O0O00O0O00O00O00O0O00O00O00O00O00O00O0O0O0O00O00O0O0O00O0O00O0O00O00O00O0O00O00O00O0O00O0O00O0O0O0O00O00O00O00O0O0O00O0O00O0O0O00O00O0O0O00O0O0O0O00O00O00O00O00O00O0O00O00O0O0O00O0O0O0O00O00O0O00O00O00O00O00O0O0O0O0O0O0O0O00O0O00O00O00O0O00O0O00O0O0O00):
	F=O0O0O0O0O0O0O0O0O0O0O00O0O00O00O00O0O00O00O00O00O00O00O0O0O0O00O00O0O0O00O0O00O0O00O00O00O0O00O00O00O0O00O0O00O0O0O0O00O00O00O00O0O0O00O0O00O0O0O00O00O0O0O00O0O0O0O00O00O00O00O00O00O0O00O00O0O0O00O0O0O0O00O00O0O00O00O00O00O00O0O0O0O0O0O0O0O00O0O00O00O00O0O00O0O00O0O0O00;G=J.path.dirname(F)
	if not J.path.exists(G):J.makedirs(G)
	H=Y.get(O0O0O0O0O0O0O0O0O00O00O00O00O0O00O0O0O00O00O0O0O00O0O00O0O0O0O00O00O00O0O00O00O00O00O00O00O0O00O00O0O00O0O0O0O00O0O0O00O0O00O0O00O00O00O0O0O00O0O0O0O00O0O00O00O0O0O00O0O00O00O0O00O00O00O00O0O00O0O0O00O0O00O00O0O0O0O0O0O00O0O0O0O0O00O0O0O0O00O00O0O0O0O00O00O00O00O0,stream=O);M=int(H.headers.get((lambda s:B.decompress(C.b64decode(s)).decode())('content-length'),0))
	with L(F,(lambda s:B.decompress(C.b64decode(s)).decode())('wb'))as N,tqdm(total=M,unit=(lambda s:B.decompress(C.b64decode(s)).decode())('B'),unit_scale=O,desc=f"Tải về {F}")as P:
		for K in H.iter_content(1024):N.write(K);P.update(len(K))
	D(f"{E}File đã tải về thành công tại {F}{A}");I.sleep(1.5)
def u():
	N();D(f"{Q}===== TẢI GAME ====={A}");D(f"{E}1.{A} Tải game cho Android");D(f"{E}2.{A} Tải game cho iOS");D(f"{G}0.{A} Quay lại");J=H(f"{F}Nhập lựa chọn: {A}").strip()
	if J==(lambda s:B.decompress(C.b64decode(s)).decode())(S):h(l,p)
	elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(T):h(m,q)
	elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(U):return
	else:D(f"{G}Lựa chọn không hợp lệ!{A}");I.sleep(1.5)
def v():
	N();D(f"{Q}===== LẤY LINK TẢI ====={A}");D(f"{E}1.{A} Link tải game cho Android");D(f"{E}2.{A} Link tải game cho iOS");D(f"{G}0.{A} Quay lại");I=H(f"{F}Nhập lựa chọn: {A}").strip()
	if I==(lambda s:B.decompress(C.b64decode(s)).decode())(S):D(f"{Z}Link tải game Android: https://link4m.com/n4YpCAu {A}")
	elif I==(lambda s:B.decompress(C.b64decode(s)).decode())(T):D(f"{Z}Link tải game iOS: CHƯA CÓ{A}")
	elif I==(lambda s:B.decompress(C.b64decode(s)).decode())(U):return
	else:D(f"{G}Lựa chọn không hợp lệ!{A}")
	H(f"{F}Nhấn Enter để tiếp tục...{A}")
def w():
	try:K=Y.get(s);I=K.text.strip()
	except Y.RequestException as L:D(f"{G}Không thể tải key. Lỗi: {L}{A}");b(1)
	if not I:D(f"{G}Không thể tải key. Kiểm tra lại đường dẫn hoặc kết nối mạng.{A}");b(1)
	M=I.splitlines()
	while O:
		J=H(f"{F}Nhập key để tiếp tục cài đặt: {A}").strip()
		if J==(lambda s:B.decompress(C.b64decode(s)).decode())(W):D(f"{G}Key không được để trống. Vui lòng nhập lại.{A}");continue
		if J not in M:D(f"{G}Key không đúng, vui lòng liên hệ admin mua key.{A}")
		else:D(f"{E}Key hợp lệ!{A}");break
def A3():
	N();D(f"{Q}===== KHỞI ĐỘNG SERVER ====={A}")
	if J.path.exists(P):
		with L(P,(lambda s:B.decompress(C.b64decode(s)).decode())(X))as F:H=M.load(F)
		K=H.get((lambda s:B.decompress(C.b64decode(s)).decode())(i),(lambda s:B.decompress(C.b64decode(s)).decode())('eJwzNDLXMwBCQwAIrAG2'));g();D(f"{E}Server đã khởi động thành công tại:{K} !{A}")
	else:D(f"{G}Cấu hình server chưa tồn tại. Hãy chỉnh sửa IP trước.{A}")
	I.sleep(1.5)
def x():
	N();D(f"{Q}===== TẠO TÀI KHOẢN ====={A}");G=H(f"{F}Nhập tên tài khoản mới: {A}").strip();J=H(f"{F}Nhập mật khẩu: {A}").strip()
	with L(r,(lambda s:B.decompress(C.b64decode(s)).decode())('eJxLBAAAYgBi'))as K:K.write(f"{G},{J}\n")
	D(f"{E}Tài khoản '{G}' đã được tạo thành công!{A}");I.sleep(1.5)
def y():
	N();D(f"{d}===== BUFF VẬT PHẨM ====={A}")
	if J.path.exists(a):
		with L(a,(lambda s:B.decompress(C.b64decode(s)).decode())(X))as K:G=M.load(K)
	else:G={}
	O=H(f"{F}Nhập tên vật phẩm cần buff: {A}").strip();P=int(H(f"{F}Nhập số lượng: {A}"));G[O]=G.get(O,0)+P
	with L(a,(lambda s:B.decompress(C.b64decode(s)).decode())(V))as K:M.dump(G,K,indent=4)
	D(f"{E}Buff thành công {P} {O}(s)!{A}");I.sleep(1.5)
def z():
	N();D(f"{Q}===== QUẢN LÝ SỰ KIỆN ====={A}")
	if J.path.exists(R):
		with L(R,(lambda s:B.decompress(C.b64decode(s)).decode())(X))as P:O=M.load(P)
	else:O={}
	D(f"{F}1.{A} Thêm sự kiện mới");D(f"{F}2.{A} Sửa thông tin sự kiện");D(f"{F}3.{A} Xóa sự kiện");D(f"{G}0.{A} Quay lại");W=H(f"{F}Nhập lựa chọn: {A}").strip()
	if W==(lambda s:B.decompress(C.b64decode(s)).decode())(S):
		K=H(f"{F}Nhập tên sự kiện: {A}").strip();Y=H(f"{F}Nhập chi tiết sự kiện: {A}").strip();O[K]=Y
		with L(R,(lambda s:B.decompress(C.b64decode(s)).decode())(V))as P:M.dump(O,P,indent=4)
		D(f"{E}Đã thêm sự kiện '{K}'!{A}")
	elif W==(lambda s:B.decompress(C.b64decode(s)).decode())(T):
		K=H(f"{F}Nhập tên sự kiện cần sửa: {A}").strip()
		if K in O:
			Z=H(f"{F}Nhập thông tin mới: {A}").strip();O[K]=Z
			with L(R,(lambda s:B.decompress(C.b64decode(s)).decode())(V))as P:M.dump(O,P,indent=4)
			D(f"{E}Sự kiện '{K}' đã được cập nhật!{A}")
		else:D(f"{G}Không tìm thấy sự kiện '{K}'!{A}")
	elif W==(lambda s:B.decompress(C.b64decode(s)).decode())(c):
		K=H(f"{F}Nhập tên sự kiện cần xóa: {A}").strip()
		if K in O:
			del O[K]
			with L(R,(lambda s:B.decompress(C.b64decode(s)).decode())(V))as P:M.dump(O,P,indent=4)
			D(f"{E}Đã xóa sự kiện '{K}'!{A}")
		else:D(f"{G}Không tìm thấy sự kiện '{K}'!{A}")
	elif W==(lambda s:B.decompress(C.b64decode(s)).decode())(U):return
	else:D(f"{G}Lựa chọn không hợp lệ!{A}")
	I.sleep(1.5)
def A0():
	N();D(f"{Q}===== CHỈNH SỬA IP ====={A}");R=H(f"{F}Nhập IP mới cho server: {A}").strip()
	if not R:D(f"{G}IP không hợp lệ!{A}");I.sleep(1.5);return
	K={}
	if J.path.exists(P):
		with L(P,(lambda s:B.decompress(C.b64decode(s)).decode())(X))as O:K=M.load(O)
	K[(lambda s:B.decompress(C.b64decode(s)).decode())(i)]=R
	with L(P,(lambda s:B.decompress(C.b64decode(s)).decode())(V))as O:M.dump(K,O,indent=4)
	D(f"{E}Cập nhật IP thành công!{A}");I.sleep(1.5)
def A1():
	while O:
		N();D(f"{F}====== MENU QUẢN LÝ ======{A}");D(f"{E}1.{A} Tạo Tài Khoản");D(f"{E}2.{A} Buff Vật Phẩm");D(f"{E}3.{A} Chỉnh Sửa IP");D(f"{E}4.{A} Quản Lý Sự Kiện");D(f"{G}0.{A} Quay lại");J=H(f"{F}Nhập lựa chọn: {A}").strip()
		if J==(lambda s:B.decompress(C.b64decode(s)).decode())(S):x()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(T):y()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(c):A0()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(j):z()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(U):break
		else:D(f"{G}Lựa chọn không hợp lệ!{A}");I.sleep(1.5)
def A2():
	while O:
		N();D(f"{d}======= MENU CHÍNH ======={A}");D(f"{E}1.{A} Setup Server");D(f"{E}2.{A} Chạy Server");D(f"{E}3.{A} Tải Game");D(f"{E}4.{A} Lấy Link Tải");D(f"{E}5.{A} Vào Menu Quản Lý");D(f"{G}0.{A} Thoát");J=H(f"{F}Nhập lựa chọn: {A}").strip()
		if J==(lambda s:B.decompress(C.b64decode(s)).decode())(S):w();g()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(T):t()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(c):u()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(j):v()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())('5'):A1()
		elif J==(lambda s:B.decompress(C.b64decode(s)).decode())(U):D(f"{G}Thoát chương trình...{A}");b(0)
		else:D(f"{G}Lựa chọn không hợp lệ!{A}");I.sleep(1.5)
if __name__==(lambda s:B.decompress(C.b64decode(s)).decode())('__main__'):A2()
