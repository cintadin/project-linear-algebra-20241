import cv2
import matplotlib.pyplot as plt

try:
    # Load image
    image = cv2.imread(r'C:\Users\Lenovo\OneDrive\Gambar\pemandangan.jpg')

    if image is None:
        raise FileNotFoundError("File gambar tidak ditemukan. Periksa jalur file.")

    # Get dimensions
    height, width = image.shape[:2]

    # Input rotation angle
    angle = float(input("Masukkan sudut rotasi (dalam derajat): "))

    # Rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Rotate image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    # Save rotated image
    output_path = r'C:\Users\Lenovo\OneDrive\Gambar\pemandangan_rotated.jpg'
    cv2.imwrite(output_path, rotated_image)
    print(f"Gambar hasil rotasi disimpan di {output_path}")

    # Display image using matplotlib
    rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
    plt.imshow(rotated_image_rgb)
    plt.axis('off')
    plt.title(f"Hasil Rotasi {angle} Derajat")
    plt.show()

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
