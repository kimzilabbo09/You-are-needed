
from flask import Flask, render_template, send_file
import qrcode
import os
from io import BytesIO

app = Flask(__name__)

# Correct QR destination
PUBLIC_URL = "https://you-are-needed.onrender.com"
QR_URL = f"{PUBLIC_URL}/static/kimm.jpg"


@app.route("/")
def home():
    return render_template("index.html", website_url=PUBLIC_URL)


@app.route("/qr.png")
def qr_code():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4
    )

    qr.add_data(QR_URL)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="#222222",
        back_color="white"
    )

    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)

    return send_file(
        output,
        mimetype="image/png",
        download_name="website_qr_code.png"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
