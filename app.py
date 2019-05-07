import os
import africastalking
from flask import Flask, request, render_template

app = Flask(__name__)

# authenticate with the service
username = "sandbox"
api_key = "1e4cf2a010bf58ac0fffc089466e31c938395bc136a27c865e3a30dee334ab74"
africastalking.initialize(username, api_key)

sms = africastalking.SMS


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']

        print(sms_messsage)
        print(phone_number)

        response = sms.send(sms_message, [phone_number])
        print(response)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))

