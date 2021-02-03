from flask import Flask
from pyfcm import FCMNotification


app = Flask(__name__)

@app.route("/")
def main():

    push_service = FCMNotification(api_key="Server Key di Firebase")
    registration_id = "registrasi id user yang dibuat dari android"
    message_title = "Judul"
    message_body = "Pesan"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    return "Berhasil mengirim notifikasi"



if __name__=="__main__":
    app.run(debug=True, port=8100)