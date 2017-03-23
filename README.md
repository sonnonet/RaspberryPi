# RaspberryPi

RasberryPi Pin Map


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
  gcc -o test test.c -lwiringPi

