import cv2
import numpy as np

punkty_zaznaczenia = []
nazwa_okna = "image"
obraz_kopia = None # Kopia obrazu do wyświetlania na bieżąco
obraz_oryginalny = None # Oryginalny obraz

def mouse_callback(event, x, y, flags, param):
    global punkty_zaznaczenia, obraz_kopia, obraz_oryginalny

    if event == cv2.EVENT_LBUTTONDOWN:
        punkty_zaznaczenia.append((x, y))
   
        cv2.circle(obraz_kopia, (x, y), 5, (0, 0, 255), -1) 
        cv2.imshow(nazwa_okna, obraz_kopia)
        
       
        if len(punkty_zaznaczenia) == 2:
            obraz_kopia = obraz_oryginalny.copy()
            
            cv2.imshow(nazwa_okna, obraz_kopia)

def wykonaj_negatyw():
    global obraz_oryginalny, punkty_zaznaczenia

    if len(punkty_zaznaczenia) == 2:

        obraz_wynikowy = obraz_oryginalny.copy()

        p_poczatek = punkty_zaznaczenia[0]
        p_koniec = punkty_zaznaczenia[1]
    
        x_min = p_poczatek[0]
        y_min = p_koniec[1]
        x_max = p_koniec[0]
        y_max = p_poczatek[1]

        # 2. Wycinanie bloku (ROI)
        # [wiersze od Y_min do Y_max, kolumny od X_min do X_max]
        wyciety_blok = obraz_wynikowy[y_min:y_max, x_min:x_max]
    
        if wyciety_blok.size > 0:
            # 3. Wykonanie negatywu
            negatyw_bloku = 255 - wyciety_blok
        
            # 4. Wstawienie negatywu z powrotem do obrazu wynikowego
            obraz_wynikowy[y_min:y_max, x_min:x_max] = negatyw_bloku

    return obraz_wynikowy


path="lab1\AdditiveColor.png"

img = cv2.imread(path)

obraz_oryginalny = img
obraz_kopia = img.copy()
punkty_zaznaczenia = []

cv2.namedWindow(nazwa_okna)
cv2.setMouseCallback(nazwa_okna, mouse_callback)

while True:
    cv2.imshow(nazwa_okna, obraz_kopia)
    key = cv2.waitKey(1) & 0xFF

    if len(punkty_zaznaczenia)==2:
        wynik = wykonaj_negatyw()
        cv2.imshow(nazwa_okna, wynik)
        # Czekamy, aż użytkownik zamknie okno z wynikiem
        cv2.waitKey(0) 
        break
            
    elif key == ord('q') or key == 27: # 27 to klawisz ESC
        break

cv2.destroyAllWindows()



