from flask import Flask, render_template, request, url_for
import qrcode
import base64
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    if request.method == "POST":
        data = request.form.get("data")
        if data:
            # Generate QR code
            img = qrcode.make(data)
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)

            # Convert image to Base64 for inline display
            qr_code = base64.b64encode(buf.getvalue()).decode("utf-8")

    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)