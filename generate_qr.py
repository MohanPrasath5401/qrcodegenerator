# Import the open-source libraries we installed
import qrcode
from PIL import Image  # This is part of Pillow

# The link (URL) you want the QR code to redirect to
# url = "https://web.whatsapp.com/" 
url = input("Enter your link: ")    # Hey, this is the place where we provide the link 

# Create a QR code object with some settings
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 is small, higher numbers make it bigger if needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction (good for simple links)
    box_size=10,         # Size of each black/white box in the QR code
    border=4,            # White space around the QR code
)

# Add your URL to the QR code
qr.add_data(url)
qr.make(fit=True)  # Automatically fit the data

# Create an image from the QR code (black on white background)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save("my_qr_code2.png")

# Print a message to let you know it's done
print("QR code generated! Check the file 'my_qr_code.png' in your folder.")