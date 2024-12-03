_I='eJzzy3i4a2megmteSWqRwpGJD3c3KxSWJlYq5DzctTBTITc1r1QhI//hru3JCs4lRTnazlA1JRn5hxeW6AEAk8Ec0Q=='
_H='eJwzAAAAMQAx'
_G='eJwzAQAANQA1'
_F='eJwzBgAANAA0'
_E='eJwzAgAAMwAz'
_D='eJwzBAAAMgAy'
_C='eJzzy3i4a22BQs7D3RsTFZIzHu7uzVNIfrh7eaJC0sNdC/OsFAAoDhDY'
_B='eJxLzklNLAIABgcCCA=='
_A=True
import zlib,base64,os,requests
RED=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJyTjjawNjbMBQAGKgGz')
GREEN=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJyTjjawNjbKBQAGLAG0')
YELLOW=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJyTjjawNjbOBQAGLgG1')
BLUE=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJyTjjawNjbJBQAGMAG2')
RESET=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJyTjjbIBQACTgEU')
FILE_URL=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzLKCkpKLbS1zc2MtBLLy5OTsnTS87P1fcIcXGONzIwMjE0NDTWSyzIBgAGNQwn')
FILE_NAME=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzLSMwsSUxOScxMzshMzYvPT0vLycxL1UssyAYAjFQKTA==')
if not os.path.isfile(FILE_NAME):
	print(f"{YELLOW}Đang Tải File Game...")
	try:
		response=requests.get(FILE_URL,stream=_A)
		with open(FILE_NAME,(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwrTwIAAVIA2g=='))as f:
			for chunk in response.iter_content(chunk_size=8192):f.write(chunk)
		print(f"{GREEN}File đã được tải về thành công.{RESET}")
	except requests.RequestException as e:print(f"{RED}Tải file thất bại!{RESET}");exit(1)
else:print(f"{GREEN}File đã tồn tại, không cần tải lại.{RESET}")
def O0O0O0O0O0O0O0O0O00O0O0():
	while _A:
		os.system((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_B));print(f"{BLUE}===================================={RESET}");print(f"{YELLOW}           CHỌN MỤC LỰA CHỌN{RESET}");print(f"{BLUE}===================================={RESET}");print(f"{GREEN}1.{RESET} Setup Server");print(f"{GREEN}2.{RESET} Chạy Server");print(f"{GREEN}3.{RESET} Vào Menu Quản Lý");print(f"{GREEN}4.{RESET} Cài Đặt");print(f"{RED}0.{RESET} Thoát");print(f"{BLUE}===================================={RESET}");A=input((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_C))
		if A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_D):print(f"{RED}Thiết Bị Không Tương Thích{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_E):print(f"{RED}Thiết Bị Không Tương Thích{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_F):O0O0O00O00O0O0O0O0O0O0O0O0()
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_G):O0O0O0O0O0O00O0O00O00O0O0O00O00()
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_H):print(f"{RED}Thoát chương trình.{RESET}");exit(0)
		else:print(f"{RED}Lựa chọn không hợp lệ, vui lòng nhập lại.{RESET}")
		input((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_I))
def O0O0O00O00O0O0O0O0O0O0O0O0():
	while _A:
		os.system((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_B));print(f"{BLUE}===================================={RESET}");print(f"{YELLOW}           MENU QUẢN LÝ{RESET}");print(f"{BLUE}===================================={RESET}");print(f"{GREEN}1.{RESET} Tạo Tài Khoản");print(f"{GREEN}2.{RESET} Buff Vật Phẩm");print(f"{GREEN}3.{RESET} Quản Lí Thành Viên");print(f"{GREEN}4.{RESET} Cài Đặt Server");print(f"{RED}0.{RESET} Quay lại");print(f"{BLUE}===================================={RESET}");A=input((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_C))
		if A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_D):print(f"{GREEN}Tạo Tài Khoản.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_E):print(f"{GREEN}Buff Vật Phẩm.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_F):print(f"{GREEN}Quản Lí Thành Viên.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_G):print(f"{RED}Cài Đặt Server.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_H):print(f"{YELLOW}Quay lại menu chính.{RESET}");break
		else:print(f"{RED}Lựa chọn không hợp lệ, vui lòng nhập lại.{RESET}")
		input((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_I))
def O0O0O0O0O0O00O0O00O00O0O0O00O00():
	while _A:
		os.system((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_B));print(f"{BLUE}===================================={RESET}");print(f"{YELLOW}           MENU CÀI ĐẶT{RESET}");print(f"{BLUE}===================================={RESET}");print(f"{GREEN}1.{RESET} Mở Online");print(f"{GREEN}2.{RESET} Tắt Server");print(f"{GREEN}3.{RESET} Thêm Cài Đặt");print(f"{GREEN}4.{RESET} Chỉnh Sửa IP");print(f"{GREEN}5.{RESET} Chỉnh Sửa Sự Kiện");print(f"{GREEN}6.{RESET} Chỉnh Sửa Tài Nguyên");print(f"{GREEN}7.{RESET} Chỉnh Sửa Tỉ Lệ");print(f"{RED}0.{RESET} Quay lại");print(f"{BLUE}===================================={RESET}");A=input((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_C))
		if A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_D):print(f"{GREEN}Mở Online.{RESET}");print(f"{RED}Nhập IP Mạng{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_E):print(f"{GREEN}Tắt Server.{RESET}");print(f"{RED}Tắt Thành Công{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_F):print(f"{GREEN}Thêm Cài Đặt.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_G):print(f"{GREEN}Chỉnh Sửa IP.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwzBQAANgA2'):print(f"{GREEN}Chỉnh Sửa Sự Kiện.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwzAwAANwA3'):print(f"{GREEN}Chỉnh Sửa Tài Nguyên.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwzBwAAOAA4'):print(f"{GREEN}Chỉnh Sửa Tỉ Lệ.{RESET}");print(f"{RED}Server Chưa Được Chạy{RESET}")
		elif A==(lambda s:zlib.decompress(base64.b64decode(s)).decode())(_H):print(f"{YELLOW}Quay lại menu chính.{RESET}");break
		else:print(f"{RED}Lựa chọn không hợp lệ, vui lòng nhập lại.{RESET}")
		input((lambda s:zlib.decompress(base64.b64decode(s)).decode())(_I))
O0O0O0O0O0O0O0O0O00O0O0()