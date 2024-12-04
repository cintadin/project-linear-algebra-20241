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

    # Define skewing matrix
    skew_factor_x = 0.5  # Horizontal skew factor
    skew_factor_y = 0.2  # Vertical skew factor
    rows, cols = resized_image.shape[:2]

    skew_matrix = np.float32([
        [1, skew_factor_x, 0],
        [skew_factor_y, 1, 0]
    ])

    # Apply skewing to the image
    skewed_image = cv2.warpAffine(resized_image, skew_matrix, (cols + int(rows * skew_factor_x), rows + int(cols * skew_factor_y)))

    # Display resized and skewed images
    cv2.imshow('Resized Image', resized_image)
    cv2.imshow('Skewed Image', skewed_image)

    print("Tekan tombol 'q' untuk menutup semua jendela.")

    # Close all windows on 'q' key press
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
