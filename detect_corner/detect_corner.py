# HAREKET TESPİT ETME ,NESNE ALGILAMA İÇİN KULLANILABİLİR
import numpy as np
import cv2

resim = cv2.imread("detect.png")

griton = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)  # griye çeviriyoruz

griton = np.float32(griton)  # tip donuşumu yapıyoruz koseşelri belirledik

koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01,
                                  10, )  # 0,06 dikdortgen yok , 100=300 dersek komple buradaki değerleri değiştirerek daha iyi köşe tespit edebiliriz

koseler = np.int0(koseler)  # tekrardan eski tipe donusturuyoruz

for kose in koseler:
    x, y = kose.ravel()
    cv2.circle(resim, (x, y), 3, 255, -1)

cv2.imshow("Resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
