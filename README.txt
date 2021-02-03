First 
1. Create virtual environment (Virtual environment used to create your virtual server for your project)
   * Pastikan anda menginstall pip terlebih dahulu
     ("easy_install pip)
   * Install module virutal environment menggunakan pip ("pip install virtualenv")
   * jalankan module virtualenv ("python -m virtualenv env")  "env" adalah alias dari nama virtual server kita
   * Jalankan source env/bin/activate
2. Buat file "requirements.txt" yang berisi semua model yang akan dipakai 
   * Install module-module pada file requirements.txt ("pip install -r requirements.txt") 

3. Bukan firebase console
   * https://console.firebase.com
   * Masuk ke "Project settings"
   * Pilih tab "Cloud messaging" dan klik "Add server key" jika anda belum memiliki "Server key"
   * Copy "Server key" dan masukkan ke "api_key" pada file main.py
   * Copy token aplikasi android yang akan menerima notifikasi

4. Jalankan aplikasi
