# Adım 1: beatles adında boş bir liste oluşturun
beatles = []
print("Step 1:", beatles)

# Adım 2: append() metodunu kullanarak üyeleri ekleyin (John Lennon, Paul McCartney, George Harrison)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Adım 3: for döngüsü ve append() kullanarak kullanıcıdan Stu Sutcliffe ve Pete Best'i eklemesini isteyin
for i in range(2):
    yeni_uye = input("Grup üyesi girin (Stu Sutcliffe, Pete Best): ")
    beatles.append(yeni_uye)
print("Step 3:", beatles)

# Adım 4: Stu Sutcliffe ve Pete Best'i listeden çıkarmak için del komutunu kullanın
del beatles[-1]  # Son eklenen (Pete Best) silinir
del beatles[-1]  # Bir önceki (Stu Sutcliffe) silinir
print("Step 4:", beatles)

# Adım 5: Ringo Starr'ı listenin başına eklemek için insert() metodunu kullanın
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Liste uzunluğunu test etme
print("The Fab", len(beatles))
