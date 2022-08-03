# Implementacja filtru i przetwarzanie obrazu

import numpy as np                                   # Zaimportowanie odpowiednich funkcji
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve

file = "obraz.jpg"                                   # Wybór i wczytanie obrazu
image = plt.imread(file)
image = image[:, :, 0]

filtr_2 = np.array([[0.04, 0.04, 0.04],              # Ustawienie filtra wygładzającego
                    [0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04]])
f2_image = convolve(image, filtr_2)

plt.subplot(1, 2, 1)                                 # Ustawienie na wykresie oryginalengo obrazu                                 
plt.imshow(image, cmap = "gray")
plt.axis("off")
plt.subplot(1, 2, 2)                                 # Ustawienie na wykresie obrazu z filtrem
plt.imshow(f2_image, cmap = "gray")
plt.axis("off")                                      # Wyłączenie wyświetlania osi X i Y
plt.show()                                           # Wyświetlenie wykresu