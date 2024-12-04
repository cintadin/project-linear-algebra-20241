import cv2
import numpy as np

try:
    # Load image
    image = cv2.imread(r'C:\Users\Lenovo\OneDrive\Gambar\pemandangan.jpg')

    if image is None:
        raise FileNotFoundError("File gambar tidak ditemukan. Periksa jalur file.")

    # Resizing image to specific dimensions
    target_size = (150, 150)  # Updated target size to 150x150
    image_resized_fixed = cv2.resize(image, target_size)

    # Resizing with Linear interpolation (scale factor 0.5)
    scale_factor = 0.5  # Updated scale factor to 0.5
    image_resized_linear = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    # Resizing with Cubic interpolation (scale factor 0.5)
    image_resized_cubic = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    # Displaying images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized to Fixed Size (150x150)', image_resized_fixed)
    cv2.imshow('Resized with Linear Interpolation', image_resized_linear)
    cv2.imshow('Resized with Cubic Interpolation', image_resized_cubic)

    print("Tekan tombol 'q' untuk menutup semua jendela.")

    # Close all windows on 'q' key press
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
