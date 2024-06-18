from PIL import Image
import os

# Function to place QR code on flyer
def place_qr_on_flyer(flyer_path, qr_code_path, position, size, output_path):
    flyer = Image.open(flyer_path)
    qr_img = Image.open(qr_code_path).resize((size, size), Image.ANTIALIAS)
    flyer.paste(qr_img, position)
    flyer.save(output_path)

# Paths and positions
flyer_path = 'flyer.png'  # Path to your flyer image in the root directory
qr_codes_folder = 'output_qr_codes/'  # Folder containing the QR code images
output_folder = 'output/'  # Folder to save the output images
qr_position = (370, 660)  # Adjusted position (x, y) for the large QR code
qr_size = 670  # Size for the large QR code

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get list of QR code files and sort them numerically
qr_code_files = sorted(os.listdir(qr_codes_folder), key=lambda x: int(os.path.splitext(x)[0]))

# Place each QR code on the flyer
for index, qr_code_file in enumerate(qr_code_files):
    qr_code_path = os.path.join(qr_codes_folder, qr_code_file)
    output_path = os.path.join(output_folder, f'flyer_{index + 1}.png')
    place_qr_on_flyer(flyer_path, qr_code_path, qr_position, qr_size, output_path)
    print(f"Saved: {output_path}")

print("All QR codes have been processed and saved.")
