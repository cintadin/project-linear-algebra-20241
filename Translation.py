import cv2
import numpy as np

try:
    # Load image
    image = cv2.imread(r'C:\Users\Lenovo\OneDrive\Gambar\pemandangan.jpg')

    if image is None:
        raise FileNotFoundError("File gambar tidak ditemukan. Periksa jalur file.")

    # Resize image to smaller dimensions for better handling
    scale_factor = 0.5  # Reduce the scale of the image by half
    resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # Define translation offsets
    offset_x, offset_y = 50, 50  # Adjust translation offsets here

    # Create translation matrix
    translation_matrix = np.float32([[1, 0, offset_x], [0, 1, offset_y]])

    # Apply translation matrix to the resized image
    translated_image = cv2.warpAffine(resized_image, translation_matrix, (resized_image.shape[1] + offset_x, resized_image.shape[0] + offset_y))

    # Display resized and translated images
    cv2.imshow('Resized Image', resized_image)
    cv2.imshow('Translated Image', translated_image)

    print("Tekan tombol 'q' untuk menutup semua jendela.")

    # Close all windows on 'q' key press
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
