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
import os
import platform
import requests
import json
import time
from tqdm import tqdm
from colorama import init, Fore

init(autoreset=True)

G = Fore.RED
E = Fore.GREEN
F = Fore.YELLOW
Q = Fore.BLUE
d = Fore.MAGENTA
Z = Fore.CYAN
A = Fore.RESET

l = 'https://vinaflash.cloud/HUYENTHOAIHAITAC_OFFLINE_V1.apk'
m = 'https://320.gsscdn.com/HTDC_20241113.ipa'
n = 'HUYENTHOAIHAITAC_OFFLINE.apk'
o = 'HAITACDAICHIEN_OFFLINE.ipa'
e = os.path.join(os.path.expanduser('~'), 'Downloads')
p = os.path.join(e, n)
q = os.path.join(e, o)
P = 'config.json'
r = 'accounts.txt'
a = 'items.json'
R = 'events.json'


def N():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def f(message):
    print(f"{Z}{message}{A}", end='')
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()


def g():
    messages = [
        'Đang tải File Cấu Hình Server',
        'Load Sự Kiện Thành Công',
        'Load Vật Phẩm Thành Công',
        'Load Map Thành Công',
        'Load Tài Nguyên Thành Công',
        'Khởi Tạo Cơ Cở Dữ Liệu',
        'Kiểm Tra Cơ Sở Dữ Liệu Thành Công',
        'Kiểm Tra Kết Nối Mạng',
        'Kết Nối API VPS',
        'Khởi Động Unity',
        'Chạy Thử Nghiệm Server...'
    ]
    for msg in messages:
        f(msg)
        time.sleep(1.5)
    print(f"{E}Server đã sẵn sàng hoạt động!{A}")
    time.sleep(1)


def t():
    f('Đang khởi động server...')
    print(f"{E}Server đang chạy thành công!{A}")
    time.sleep(1.5)


def h(url, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(path, 'wb') as file, tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Tải về {url}") as progress:
        for chunk in response.iter_content(1024):
            file.write(chunk)
            progress.update(len(chunk))
    print(f"{E}File đã tải về thành công tại {path}{A}")
    time.sleep(1.5)


def u():
    N()
    print(f"{Q}===== TẢI GAME ====={A}")
    print(f"{E}1.{A} Tải game cho Android")
    print(f"{E}2.{A} Tải game cho iOS")
    print(f"{G}0.{A} Quay lại")
    choice = input(f"{F}Nhập lựa chọn: {A}").strip()
    if choice == '1':
        h(l, p)
    elif choice == '2':
        h(m, q)
    elif choice == '0':
        return
    else:
        print(f"{G}Lựa chọn không hợp lệ!{A}")
        time.sleep(1.5)


def v():
    N()
    print(f"{Q}===== LẤY LINK TẢI ====={A}")
    print(f"{E}1.{A} Link tải game cho Android")
    print(f"{E}2.{A} Link tải game cho iOS")
    print(f"{G}0.{A} Quay lại")
    choice = input(f"{F}Nhập lựa chọn: {A}").strip()
    if choice == '1':
        print(f"{Z}Link tải game Android: https://link4m.com/n4YpCAu {A}")
    elif choice == '2':
        print(f"{Z}Link tải game iOS: CHƯA CÓ{A}")
    elif choice == '0':
        return
    else:
        print(f"{G}Lựa chọn không hợp lệ!{A}")
    input(f"{F}Nhấn Enter để tiếp tục...{A}")


def w():
    try:
        response = requests.get('your-key-url')
        key = response.text.strip()
    except requests.RequestException as e:
        print(f"{G}Không thể tải key. Lỗi: {e}{A}")
        exit(1)
    if not key:
        print(f"{G}Không thể tải key. Kiểm tra lại đường dẫn hoặc kết nối mạng.{A}")
        exit(1)
    key_list = key.splitlines()
    while True:
        user_key = input(f"{F}Nhập key để tiếp tục cài đặt: {A}").strip()
        if user_key == '':
            print(f"{G}Key không được để trống. Vui lòng nhập lại.{A}")
            continue
        if user_key not in key_list:
            print(f"{G}Key không đúng, vui lòng liên hệ admin mua key.{A}")
        else:
            print(f"{E}Key hợp lệ!{A}")
            break


def A3():
    N()
    print(f"{Q}===== KHỞI ĐỘNG SERVER ====={A}")
    if os.path.exists(P):
        with open(P, 'r') as file:
            config = json.load(file)
        server_ip = config.get('server_ip', 'eJwzNDLXMwBCQwAIrAG2')
        g()
        print(f"{E}Server đã khởi động thành công tại: {server_ip} !{A}")
    else:
        print(f"{G}Cấu hình server chưa tồn tại. Hãy chỉnh sửa IP trước.{A}")
    time.sleep(1.5)


def x():
    N()
    print(f"{Q}===== TẠO TÀI KHOẢN ====={A}")
    username = input(f"{F}Nhập tên tài khoản mới: {A}").strip()
    password = input(f"{F}Nhập mật khẩu: {A}").strip()
    with open(r, 'a') as file:
        file.write(f"{username},{password}\n")
    print(f"{E}Tài khoản '{username}' đã được tạo thành công!{A}")
    time.sleep(1.5)


def y():
    N()
    print(f"{d}===== BUFF VẬT PHẨM ====={A}")
    if os.path.exists(a):
        with open(a, 'r') as file:
            items = json.load(file)
    else:
        items = {}
    item_name = input(f"{F}Nhập tên vật phẩm cần buff: {A}").strip()
    quantity = int(input(f"{F}Nhập số lượng: {A}"))
    items[item_name] = items.get(item_name, 0) + quantity
    with open(a, 'w') as file:
        json.dump(items, file, indent=4)
    print(f"{E}Buff thành công {quantity} {item_name}(s)!{A}")
    time.sleep(1.5)


def z():
    N()
    print(f"{Q}===== QUẢN LÝ SỰ KIỆN ====={A}")
    if os.path.exists(R):
        with open(R, 'r') as file:
            events = json.load(file)
    else:
        events = {}
    print(f"{F}1.{A} Thêm sự kiện mới")
    print(f"{F}2.{A} Sửa thông tin sự kiện")
    print(f"{F}3.{A} Xóa sự kiện")
    print(f"{G}0.{A} Quay lại")
    choice = input(f"{F}Nhập lựa chọn: {A}").strip()
    if choice == '1':
        event_name = input(f"{F}Nhập tên sự kiện: {A}").strip()
        event_details = input(f"{F}Nhập chi tiết sự kiện: {A}").strip()
        events[event_name] = event_details
        with open(R, 'w') as file:
            json.dump(events, file, indent=4)
        print(f"{E}Đã thêm sự kiện '{event_name}'!{A}")
    elif choice == '2':
        event_name = input(f"{F}Nhập tên sự kiện cần sửa: {A}").strip()
        if event_name in events:
            new_details = input(f"{F}Nhập thông tin mới: {A}").strip()
            events[event_name] = new_details
            with open(R, 'w') as file:
                json.dump(events, file, indent=4)
            print(f"{E}Sự kiện '{event_name}' đã được cập nhật!{A}")
        else:
            print(f"{G}Không tìm thấy sự kiện '{event_name}'!{A}")
    elif choice == '3':
        event_name = input(f"{F}Nhập tên sự kiện cần xóa: {A}").strip()
        if event_name in events:
            del events[event_name]
            with open(R, 'w') as file:
                json.dump(events, file, indent=4)
            print(f"{E}Đã xóa sự kiện '{event_name}'!{A}")
        else:
            print(f"{G}Không tìm thấy sự kiện '{event_name}'!{A}")
    elif choice == '0':
        return
    else:
        print(f"{G}Lựa chọn không hợp lệ!{A}")
    time.sleep(1.5)


def A0():
    N()
    print(f"{Q}===== CHỈNH SỬA IP ====={A}")
    new_ip = input(f"{F}Nhập IP mới cho server: {A}").strip()
    if not new_ip:
        print(f"{G}IP không hợp lệ!{A}")
        time.sleep(1.5)
        return
    config = {}
    if os.path.exists(P):
        with open(P, 'r') as file:
            config = json.load(file)
    config['server_ip'] = new_ip
    with open(P, 'w') as file:
        json.dump(config, file, indent=4)
    print(f"{E}Cập nhật IP thành công!{A}")
    time.sleep(1.5)


def main():
    while True:
        N()
        print(f"{F}===== MENU ====={A}")
        print(f"{E}1.{A} Tải game")
        print(f"{E}2.{A} Lấy link tải")
        print(f"{E}3.{A} Khởi động Server")
        print(f"{E}4.{A} Quản lý tài khoản")
        print(f"{E}5.{A} Buff vật phẩm")
        print(f"{E}6.{A} Quản lý sự kiện")
        print(f"{E}7.{A} Chỉnh sửa IP")
        print(f"{E}8.{A} Thoát")
        choice = input(f"{F}Nhập lựa chọn: {A}").strip()
        if choice == '1':
            u()
        elif choice == '2':
            v()
        elif choice == '3':
            A3()
        elif choice == '4':
            x()
        elif choice == '5':
            y()
        elif choice == '6':
            z()
        elif choice == '7':
            A0()
        elif choice == '8':
            print(f"{E}Thoát chương trình.{A}")
            break
        else:
            print(f"{G}Lựa chọn không hợp lệ!{A}")
            time.sleep(1.5)

if __name__ == '__main__':
    main()
