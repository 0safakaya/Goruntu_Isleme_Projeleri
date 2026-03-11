import cv2

# Resmi yükle
img = cv2.imread('manzara1.jpg')

# Gri tonlama
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)

print("Gri tonlama tamamlandı! gray.jpg kaydedildi.")