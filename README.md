# NoteSync

**NoteSync** is an automatic note-sorting utility that uses QR codes to determine where each note should be stored. Designed to streamline organization, it scans uploaded images for QR codes and moves them to one of three folders: **GREEN**, **RED**, or **BLUE**.

---

## How It Works

1. Place images containing QR codes in the `upload/` folder (located in the current working directory). It is assumed that QR codes would be printed on sheets of paper where work to be uploaded, would be done on.
2. QR codes contain keywords, `GREEN`, `RED`, or `BLUE` for this demo, corresponding to folder names.
3. The script reads the QR code from each image.
4. The image is moved to the corresponding folder inside the user's `~/noteSync/` directory.

---

## Folder Structure

Upon execution, NoteSync will create the following folders (if they don’t already exist):

~/noteSync/
├── green_folder/
├── red_folder/
└── blue_folder/

Example of the workflow:

- An image with a QR code embedded with the folder name `RED` will be moved to `~/noteSync/red_folder/`.
- If no QR code is found or the value is invalid, the file is skipped.

---

## Requirements

- Python 3.11+
- OpenCV (`cv2`)
- Pyzbar
