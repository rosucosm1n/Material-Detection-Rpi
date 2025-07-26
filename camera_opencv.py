import cv2
import os
import time
from datetime import datetime

def capture_image(folder, clasa):    # cu libcamera pt ca cu openCV nu a mers
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # creez nume fisier temporar
    temp_file = f"/tmp/{clasa}_{timestamp}.jpg"

    # capturez imaginea cu libcamera
    command = f"libcamera-jpeg -n -o {temp_file} --width 640 --height 480 --quality 90"
    result = os.system(command)

    if result != 0 or not os.path.exists(temp_file):
        print("Eroare: Nu s-a putut captura imaginea.")
        return

    # citesc imaginea capturata
    img = cv2.imread(temp_file)
    if img is None:
        print("Eroare: Imaginea capturata nu poate fi incarcata.")
        return

    # creez folder-ul daca nu exista
    os.makedirs(folder, exist_ok=True)

    # salvez imaginea cu numele final
    final_path = os.path.join(folder, f"{clasa}_{timestamp}.jpg")
    cv2.imwrite(final_path, img)
    print(f"Imagine salvata: {final_path}")

    # confirm salvarea imaginii afisand-o
    cv2.imshow("Preview captura", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    clasa = input("Introdu eticheta clasei (ex: sticla, plastic, carton): ").strip().lower()
    folder = f"capturi/{clasa}"

    while True:
        comanda = input("Apasa ENTER pentru a captura.\n Scrie 'exit' in terminal pentru a iesi.").strip().lower()
        if comanda == "exit":
            break
        capture_image(folder, clasa)
