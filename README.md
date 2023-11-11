# CarDetect
Bu proje, OpenCV kütüphanesi kullanılarak geliştirilmiş bir araç sayma ve tespit sistemi içerir.
Projede, bir video dosyasından alınan görüntüler üzerinde arka plan çıkarma, eşikleme, erozyon, genişleme ve kontur tespiti gibi görüntü işleme teknikleri kullanılarak araç tespiti yapılmaktadır.

Proje Özellikleri:

Videodan alınan görüntüler üzerinde arka plan çıkarma işlemi yapılır.
Eşikleme işlemi ile ön plan maske oluşturulur.
Erozyon ve genişleme işlemleri ile maske temizlenir.
Kontur tespiti ile araçlar belirlenir ve dikdörtgen çizilir.
Her araç tespit edildiğinde bir sayıcı artırılır.
Belirlenen süre aralığında birden fazla tespit yapılmamasına dikkat edilir.
Sonuçlar, orijinal görüntü, çıkarılan ön plan ve tespit edilen araçların birleşiminden oluşan bir pencere üzerinde gösterilir.
Toplam araç sayısı ekrana yazdırılır.
