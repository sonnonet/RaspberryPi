# RaspberryPi basic 
- [x] wiringPi
- [x] How to use github
- [ ] wlan setting file dir (you'll add about how to setting)
- [x] Usb Mount

# How to use GPIO Pin (wiringPi)


* install
git clone git://git.drogon.net/wiringPi
```
cd wiringPi
./bulid
gpio -v
gpio readall
```
* use

c language

if do you have problem like this "undefined refrence to 'wiringPiSetup' 

you have to add option

```
gcc -o objfile sourcefile.c -lwiringPi
```
# How To use Git hub
1. Create Git Project
2. git init
3. git config --global user.name "sonnonet"
4. git config --global user.email "korea.sonnonet@gmail.com"
5. git remote add origin github (ex: https://github.com/sonnonet/tinyos.git)
6. git clone git project address (ex : https//github.com/sonnonet/maps.git)
after modification of file
7. cd tinyos (modification of dir)
8. git add *
9. git commit -m " commit message"
10. git push origin master

## wireless wlan setting file dir

- /etc/wpa_supplicant/wpa_supplicant.conf

## How to Use USB Mount

- 1.step : Check for your usb device
   <pre> $ sudo fdisk -l (ex: /dev/sda1) </pre>
- 2.step : Make dir /mnt/usb
   <pre> $ sudo mkdir /mnt/usb </pre>
- 3.step : Authorization for root
   <pre> $ chown pi:pi /mnt/usb </pre>
- 4.step : run to mount
   <pre> $ sudo mount -t ntfs -o uid=pi,gid=pi /dev/sda1 (check) /mnt/usb
- 5.step : Autorun for next time
   <pre> $ sudo echo "/dev/sda1 /mnt/usb ntfs -3g uid=pi,gid=pi 00" >> sudo /etc/fstab

