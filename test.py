import cv2
import time
import pytesseract

# Chargement de l'image en niveaux de gris
image = cv2.imread("img_test.png", cv2.IMREAD_GRAYSCALE)

# Configuration optimale pour un numéro de série :
# - Langue anglaise (eng)
# - PSM 7 (une seule ligne)
# - OEM 1 (LSTM pur)
# - Whitelist alphanumérique + tiret
# - Désactivation des dictionnaires linguistiques
custom_config = (
    r"--oem 1 --psm 1 "
    r"-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ- "
    r"-c load_system_dawg=0 -c load_freq_dawg=0"
)
t_debut = time.perf_counter()
texte_extrait = pytesseract.image_to_string(
    image, lang="eng", config=custom_config
)
t_fin = time.perf_counter()
duree_ms = (t_fin - t_debut) * 1000

print(f"--- Résultat ({duree_ms:.2f} ms) ---")
print("Numéro détecté :", texte_extrait.strip())