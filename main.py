import qrcode
import os
from PIL import Image

# Define the base URL and the range of table numbers
base_url = "http://192.168.1.51:3000/client/"
table_range = range(1, 51)

# Create an output directory if it doesn't exist
output_dir = "output_qr_codes"
os.makedirs(output_dir, exist_ok=True)

# Function to generate QR code with reduced padding
def generate_qr_code(url, img_path, border=1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=border,  # This sets the border size to reduce padding
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(img_path)

# Generate QR codes for each table
for i in table_range:
    url = f"{base_url}{i}"
    img_path = os.path.join(output_dir, f"{i}.jpg")
    generate_qr_code(url, img_path)

print(f"Generated {len(table_range)} QR codes and saved them to the '{output_dir}' directory.")
