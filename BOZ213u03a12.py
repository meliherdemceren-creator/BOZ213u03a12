hat_list = [1, 2, 3, 4, 5]  # Şapkanın içindeki sayı listesi

# Adım 1: Kullanıcıdan bir tamsayı alıp listenin ortasındaki elemanla (indeks 2) değiştirme
hat_list[2] = int(input("Ortadaki sayının yerine geçecek bir tamsayı girin: "))

# Adım 2: Listenin son elemanını silme
del hat_list[-1]

# Adım 3: Listenin güncel uzunluğunu ekrana yazdırma
print("Listenin uzunluğu:", len(hat_list))

print(hat_list)
