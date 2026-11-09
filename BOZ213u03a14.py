my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Ek bilgi önerisine uygun olarak geçici/benzersiz elemanlar için yeni liste oluşturulur
unique_list = []

for sayi in my_list:
    if sayi not in unique_list:
        unique_list.append(sayi)

# my_list güncellenir
my_list = unique_list

print("The list with unique elements only:")
print(my_list)
