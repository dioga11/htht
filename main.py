import zlib as A, base64 as B, os as G, requests as D

C = print
I = open
H = exit

# Thông báo
C("- HUYEN THOAI HAI TAC - https://huyenthoaihaitac.bio.link")
C("    - GAME ĐƯỢC PHÁT TRIỂN Bởi PHUCBABY - MUA SOURCE LIÊN HỆ ZALO Ở LINK BÊN DƯỚi")
C("    - KEY Sử DỤNG HUYỀN THOẠI HẢI TẬC")
C("    - Link Mua Key & Thông Tin Về Game :")
C("      https://huyenthoaihaitac.bio.link")
C("    - XIN QUÝ KHÁCH VUI LÒNG CHẠY MAIN.PY ĐịNH KÌ ĐỂ CẬP NHẬT THƯỞNG XUYÊN TRÁNH LỖI")
C("    - HÃY THAM GIA BOX ZALO ĐỂ NHẬN ĐƯỢC THÔNG TIN BẢN CẬP NHẬT GẦN NHẤT NHÉ")

T = "https://api-bot.online/api/v3/keys.txt"
U = "https://api-bot.online/api/v3/version.txt"
J = "version_info.txt"
P = "https://api-bot.online/api/v3/run.py"
F = "run.py"

if G.path.exists(J):
    with I(J, "r") as K:
        L = K.read().strip()
else:
    L = "1.0.0"
     
try:
    X = D.get(U)
    M = X.text.strip()
    C(f"\nPhiên bản hiện tại: {L}")
    C(f"Phiên bản mới nhất: {M}")
    if L != M:
        C("Phát hiện cập nhật mới. Đang tải...")
        if G.path.isfile(F):
            G.remove(F)
            C("Đã xoá phiên bản cũ.")
        try:
            N = D.get(P)
            with I(F, "wb") as O:
                O.write(N.content)
            C("Đã tải bản cập nhật mới.")
            with I(J, "w") as K:
                K.write(M)
            C("Đang khởi chạy bản mới...")
            G.system(f"python {F}")
            H(0)
        except D.RequestException as E:
            C(f"Tải file thất bại! Lỗi: {E}")
            H(1)
except D.RequestException as E:
    C(f"Không thể kiểm tra phiên bản mới. Lỗi: {E}")

if not G.path.isfile(F):
    C("Không tìm thấy file thực thi. Đang tải...")
    try:
        N = D.get(P)
        with I(F, "wb") as O:
            O.write(N.content)
        C("Đã tải file thành công.")
    except D.RequestException as E:
        C(f"Tải file thất bại! Lỗi: {E}")
        H(1)
else:
    C("File thực thi đã tồn tại.")

C("Đang khởi chạy...")
G.system(f"python {F}")
