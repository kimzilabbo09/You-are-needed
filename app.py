
from flask import Flask, render_template, send_file
import qrcode
import os
from io import BytesIO

app = Flask(__name__)

# Set this to your deployed website URL
PUBLIC_URL = os.environ.get(
    "PUBLIC_URL",
    "http://127.0.0.1:5000"
).rstrip("/")


@app.route("/")
def home():
    return render_template("index.html", website_url=PUBLIC_URL)


@app.route("/qr.png")
def qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4
    )

    qr.add_data(PUBLIC_URL)
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