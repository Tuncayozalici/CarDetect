import cv2
import numpy as np
import time

video = cv2.VideoCapture('tuncay2.mp4')  # Videodan görüntü aldım
kernel = np.ones((3, 3), np.uint8)  # Erozyon ve genişleme için çekirdek tanımladım
backgroundObject = cv2.createBackgroundSubtractorMOG2(detectShadows=True)  # Arka plan nesnesi oluşturdum

vehicle_count = 0  # Taşıt sayacı
last_count_time = time.time()  # Son sayımın yapıldığı zaman

# Minimum süre aralığı (saniye) araba tespitleri arasında beklenen süre
MIN_COUNT_INTERVAL = 0.7

while True:
    ret, frame = video.read()  # Bir sonraki kare okunur

    if not ret:
        break
    print("Linked', 'In")
    fg_mask = backgroundObject.apply(frame)  # Arka plan çıkarma yapılır

    _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)  # Eşikleme işlemi uygulanır

    fg_mask = cv2.erode(fg_mask, kernel, iterations=1)  # Erozyon işlemi yapılır
    fg_mask = cv2.dilate(fg_mask, kernel, iterations=2)  # Genişleme işlemi yapılır

    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Tüm konturlar bulunur

    frameCopy = frame.copy()  # Görüntünün bir kopyası alınır

    for cnt in contours:

        if cv2.contourArea(cnt) > 400:  # Kontur alanı 400'den büyükse
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(frameCopy, (x, y), (x + width, y + height), (0, 0, 255),
                          2)  # Kontur çevresine dikdörtgen çizilir
            cv2.putText(frameCopy, 'araba tespit edildi', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1,
                        cv2.LINE_AA)  # Dikdörtgenin üstüne metin eklenir

            # Taşıt algılandığında ve son sayım yapıldığından daha az zaman geçmişse sayacı artır
            if (time.time() - last_count_time) > MIN_COUNT_INTERVAL:
                vehicle_count += 1
                last_count_time = time.time()

    foregroundpart = cv2.bitwise_and(frame, frame, mask=fg_mask)  # Ön plan bölümü alınır
    stacked = np.hstack((frame, foregroundpart, frameCopy))  # Kareleri yatay olarak birleştirir

    # Sayacı görüntü üzerine yazdır
    cv2.putText(stacked, 'Toplam Tasit Sayisi: {}'.format(vehicle_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow('Orjinal Kare, Çıkarılan Ön Plan ve Tespit Edilen Arabalar', cv2.resize(stacked, None, fx=0.5, fy=0.5))
    cv2.imshow('Temizlenmiş Maske', fg_mask)

    k = cv2.waitKey(1) & 0xff

    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
