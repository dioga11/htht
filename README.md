<h1 align="center">Welcome to Huyền Thoại Hải Tặc Offline </h1>
<img alt="7" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/7.png" />
<img alt="Homepage" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/5.png" />
  Chìa khóa Huyền Thoại hải tặc server termux

 - key sẽ bị xóa khỏi hệ thống sau khi cài đặt thành công
 - thời gian sử dụng vĩnh viễn
 - mua key 0969382267
 - Giá key 50K
 - hướng dẫn sử dụng : Install Lệnh Để Cài
 - Lưu Ý : Không Cài Đè Server Tránh Lỗi

## Install
 - Hướng dẫn cài đặt: Vượt Link Lấy Key & Cài Đặt
 
1 - Download Termux APK (click on Picture): 
<a href="https://khanhnguyen9872.github.io/Ninja_Server_Termux/CONF_FILE/termux_0.118.apk" target="_blank">
    <img alt="Termux" src="https://github.com/KhanhNguyen9872/Ninja_Server_Termux/raw/main/image/termux.png" />
</a>

2 - Install Termux APK

3 - Open Termux, copy this line and paste it on Termux

```bash
function install () {
  clear
  
  # Cài đặt công cụ phát triển
  echo "Cài đặt công cụ phát triển..."
  pkg update -y
  pkg upgrade -y
  pkg install -y clang make git openssl

  # Cài đặt shc trên Termux
  echo "Cài đặt shc trên Termux..."
  
  git clone https://github.com/neurobin/shc.git
  
  # Biên dịch shc
  make
  
  # Kiểm tra việc biên dịch có thành công không
  if [ -f ./shc ]; then
    make install
    echo "Cài đặt shc thành công!"
  else
    echo "Lỗi khi biên dịch shc. Tiến hành biên dịch thủ công..."
    
    # Biên dịch thủ công nếu không có file shc
    clang -o shc shc.c -lssl -lcrypto
    if [ -f ./shc ]; then
      echo "Biên dịch thủ công thành công!"
    else
      echo "Lỗi khi biên dịch thủ công shc!"
      cd ..
      rm -rf shc
      return 1
    fi
  fi
  
  cd ..
  rm -rf shc
  
  # Cài đặt script install.sh từ phucbaby.dev
  echo "Cài đặt script install.sh từ phucbaby.dev..."
  curl -L --max-redirs 15 --progress-bar "https://phucbaby.dev/api/install.sh" --output install.sh
  
  # Kiểm tra loại file install.sh có phải là script shell không
  if file install.sh | grep -q 'shell script'; then
    bash install.sh
  else
    echo "install.sh không phải là một script shell hợp lệ."
  fi

  # Dọn dẹp
  unset install
}

install
```

4 - Wait for install!
 
5 - Choose Source you want to use! 
 
6 - Enjoy!
<img alt="Homepage" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/6.png" />
<img alt="Homepage" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/4.png" />
<img alt="Homepage" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/1.png" />
<img alt="Homepage" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/2.png" />
<img alt="Homepage" src="https://github.com/haitac4754/huyenthoaihaitac/blob/main/image/3.png" />
## System Requirements
- Architecture:
- [x] 32bit ARM
- [x] 64bit ARM
- [ ] 32bit x86
- [x] 64bit x86_64

- Android:
- [x] 7
- [x] 8
- [x] 9
- [x] 10
- [x] 11
- [x] 12 
- [ ] 13
- [ ] 14

## Download Emulator (x86_64)

<a href="https://github.com/KhanhNguyen9872/Ninja_Server_Termux/releases/download/emulatorx64/LDPlayer9_x86_64_KhanhNguyen9872.exe" target="_blank">
    <img alt="LDPlayer9" src="https://github.com/KhanhNguyen9872/Ninja_Server_Termux/blob/main/image/ldplayer9.ico?raw=true" width="150" height="150" />
</a>

- [LDPlayer9](https://github.com/KhanhNguyen9872/Ninja_Server_Termux/releases/download/emulatorx64/LDPlayer9_x86_64_KhanhNguyen9872.exe)

## Author

👤 **PHUCBABY**

* Website: (https://phucbaby.dev/ )
* Github: [@NGUYENTRIEUPHUC]

