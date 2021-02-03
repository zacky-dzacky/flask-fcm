# FCM with flask
> Project ini berisi beberapa baris kode bagaimana cara menggunakan _Firebase Cloud Messaging_ dengan sangat sederhana menggunakan flask. Salah satu alasan kenapa python sangat sehat untuk waktu mu.

## Table of contents
* [Flask Project](#flask-project)
* [Instalasi module](#instalasi-module)
* [Firebase console](#firebase-console)

## Buat Flask Project
Pastikan anda menginstall pip terlebih dahulu
```
$ easy_install pip
```
Install module virutal environment menggunakan pip
```
$ pip install virtualenv
```
Jalankan module virtualenv
```
$ python -m virtualenv env
``` 
Install module-module pada file requirements.txt
```
$ pip install -r requirements.txt
``` 
	
## Instalasi module
Module yang diperlukkan:
* [Flask: 1.0.2](https://www.flynerd.pl/)
* [pyfcm: 2.33](https://pypi.org/project/pyfcm/)
	
## Firebase console
* Buka konsol firebase `https://console.firebase.com`
* Masuk ke "Project settings"
* Pilih tab "Cloud messaging" dan klik "Add server key" jika anda belum memiliki "Server key"
* Copy "Server key" dan masukkan ke "api_key" pada file main.py
* Copy token aplikasi android yang akan menerima notifikasi

