import qrcode

# Data to be encoded
data = "https://visionxweb.netlify.app"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or fewer errors can be corrected
    box_size=10,  # Controls how many pixels each “box” of the QR code is
    border=4,  # Controls the thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
