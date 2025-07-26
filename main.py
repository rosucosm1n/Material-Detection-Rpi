import os
import cv2
import time
from senzor_ir import citeste_valoare_ir, clasifica_material_ir
from predictie_cnn import prezice_material

print("Pornit sistem combinat. Apasa ESC pentru a iesi.")
while True:
    os.system("libcamera-still -t 1 --width 800 --height 600 -o frame.jpg --nopreview")
    label_cnn = prezice_material("frame.jpg")
    valoare_ir, voltaj = citeste_valoare_ir()
    label_ir = clasifica_material_ir(valoare_ir)

    frame = cv2.imread("frame.jpg")
    if frame is not None:
        cv2.putText(frame, f"[CNN] Material vizual: {label_cnn}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"[IR] Valoare: {valoare_ir} | Material: {label_ir}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        cv2.imshow("Detectie combinata", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()