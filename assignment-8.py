import qrcode
import cv2

def qr_code_encoder():
    print("""
    =======================================================
    QR Code Encoder
    Created by Neha Khan
    =======================================================
    """)
    # Get the data to encode
    data = input("Enter the information you want to encode in the QR code: ")

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill="black", back_color="white")
    img_name = input("Enter the name to save the QR code image (e.g., 'my_qrcode.png'): ")
    img.save(img_name)

    print(f"QR code saved as {img_name}!")

def qr_code_decoder():
    print("""
    =======================================================
    QR Code Decoder
    Created by Neha Khan
    =======================================================
    """)
    # Get the QR code image file name
    img_name = input("Enter the name of the QR code image file to decode (e.g., 'my_qrcode.png'): ")

    # Read and decode the QR code
    try:
        img = cv2.imread(img_name)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if bbox is not None:
            print(f"Decoded data from QR code: {data}")
        else:
            print("No QR code found in the image.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("""
    =======================================================
    QR Code Encoder/Decoder
    Created by Neha Khan
    =======================================================
    """)
    print("Choose an option:")
    print("1. Encode (Create a QR Code)")
    print("2. Decode (Read a QR Code)")

    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        qr_code_encoder()
    elif choice == "2":
        qr_code_decoder()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
