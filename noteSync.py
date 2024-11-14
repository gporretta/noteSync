#!/usr/bin/env python3.11
import os
import cv2
import shutil
from pyzbar.pyzbar import decode

debug = True

home_directory = os.path.expanduser("~")
base_folder = os.path.join(home_directory, 'noteSync')
FOLDERS = {
    'GREEN': os.path.join(base_folder, 'green_folder'),
    'RED': os.path.join(base_folder, 'red_folder'),
    'BLUE': os.path.join(base_folder, 'blue_folder')
}

def createFolder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        if debug:
            print(f"{folder_name} created.")    
    elif debug:
        print(f"{folder_name} exists.")    

def uploadFile(directory, file_name, dest_folder_path):
    source = os.path.join(directory, file_name)
    
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)
        print(f"Created destination folder: {dest_folder_path}")
    
    destination = os.path.join(dest_folder_path, file_name)
    
    # Move the file
    try:
        shutil.move(source, destination)
        print(f"{file_name} moved to {dest_folder_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def read_qr_code(directory, file_name):
    # Load image
    image = cv2.imread(os.path.join(directory, file_name))
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    
    # Decode QR to get folder name
    qr_codes = decode(threshold_image)
    
    if not qr_codes:
        print("No QR code found in the image.")
        return None
    
    for qr_code in qr_codes:
        qr_data = qr_code.data.decode("utf-8")
        if debug:
            print(f"Decoded data: {qr_data}")
        
    return qr_data

def main():
    current_directory = os.getcwd()
    directory = os.path.join(current_directory, 'upload')

    # Ensure folders exist
    for folder in FOLDERS.values():
        createFolder(folder)

    # Process each image in the upload directory
    for image in os.listdir(directory):
        file_extension = image.split('.')[-1].lower()
        if file_extension in ['jpg', 'png']:
            folder_dest = read_qr_code(directory, image)
            if folder_dest is not None:
                for key, folder_path in FOLDERS.items():
                    if folder_dest == key:
                        uploadFile(directory, image, folder_path)
            else:
                print(f"Skipping non-image file: {image}")

if __name__ == "__main__":
    main()

