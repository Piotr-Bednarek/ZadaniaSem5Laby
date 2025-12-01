import cv2
import numpy as np

path = "lab1\\AdditiveColor.png"
nazwa_okna = "img"
img = None
obraz_kopia = None
new_color = None
kolor_piksela = []


def empty_callback(val):
    pass


def mouse_callback(event, x, y, flags, param):
    global new_color, obraz_oryginalny, kolor_piksela

    if event == cv2.EVENT_LBUTTONDOWN and new_color is None:
        new_color = obraz_oryginalny[y, x].tolist()
        if 0 <= y < obraz_oryginalny.shape[0] and 0 <= x < obraz_oryginalny.shape[1]:
            kolor_piksela[0] = (x, y)


def przetworz_obraz():
    global obraz_oryginalny, new_color

    if new_color is None:
        return obraz_oryginalny.copy()

    newR = cv2.getTrackbarPos("R", nazwa_okna)
    newG = cv2.getTrackbarPos("G", nazwa_okna)
    newB = cv2.getTrackbarPos("B", nazwa_okna)

    nowy_kolor_BGR = np.array([newB, newG, newR], dtype=np.uint8)

    kolor_min = np.array(new_color, dtype=np.uint8)
    kolor_max = np.array(new_color, dtype=np.uint8)

    maska = cv2.inRange(obraz_oryginalny, kolor_min, kolor_max)

    obraz_wynikowy = obraz_oryginalny.copy()

    obraz_wynikowy[maska > 0] = nowy_kolor_BGR

    return obraz_wynikowy


# --- Główny kod programu ---
if __name__ == "__main__":
    # Wczytanie obrazu
    obraz_oryginalny = cv2.imread(path)
    if obraz_oryginalny is None:
        print(f"BŁĄD: Nie można wczytać pliku {path}. Zmień ścieżkę.")
    else:
        obraz_kopia = obraz_oryginalny.copy()

        # 1. Konfiguracja okna i suwaków
        cv2.namedWindow(nazwa_okna)
        cv2.setMouseCallback(nazwa_okna, mouse_callback)

        # Suwaki do wyboru nowego koloru (0-255)
        # UWAGA: W OpenCV kolejność to BGR!
        cv2.createTrackbar("R", nazwa_okna, 0, 255, empty_callback)
        cv2.createTrackbar("G", nazwa_okna, 0, 255, empty_callback)
        cv2.createTrackbar("B", nazwa_okna, 0, 255, empty_callback)

        # Ustawienie wartości początkowych na biały
        cv2.setTrackbarPos("R", nazwa_okna, 255)
        cv2.setTrackbarPos("G", nazwa_okna, 255)
        cv2.setTrackbarPos("B", nazwa_okna, 255)

        while True:
            if new_color is None:
                cv2.imshow(nazwa_okna, obraz_kopia)

            else:
                wynik = przetworz_obraz()
                cv2.imshow(nazwa_okna, wynik)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:
                break

        cv2.destroyAllWindows()
