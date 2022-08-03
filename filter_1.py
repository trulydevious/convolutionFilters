# Implementacja filtru i przetwarzanie obrazu

import numpy as np                                  # Zaimportowanie odpowiednich funkcji
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve

file = "obraz.jpg"                                  # Wybór i wczytanie obrazu
image = plt.imread(file)
image = image[:, :, 0]

filtr_1 = np.array([[0, -1, 0],                     # Ustawienie filtra wyostrzającego
                    [-1, 5, -1],
                    [0, -1, 0]])
f1_image = convolve(image, filtr_1)

plt.subplot(1, 2, 1)                                # Ustawienie na wykresie oryginalengo obrazu
plt.imshow(image, cmap = "gray")
plt.axis("off")
plt.subplot(1, 2, 2)                                # Ustawienie na wykresie obrazu z filtrem
plt.imshow(f1_image, cmap = "gray")
plt.axis("off")                                     # Wyłączenie wyświetlania osi X i Y
plt.show()                                          # Wyświetlenie wykresu