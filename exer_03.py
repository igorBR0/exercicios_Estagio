faturamento = [236, 487, 195, 762, 312, 920, 567, 389, 781, 654, 123, 890, 341, 479, 760, 935, 274, 588, 607, 114, 999, 445, 314, 732, 220, 813, 1, 562, 777, 601, 489]

flag = 0
max_fat = 0

for i in range(31):
    if faturamento[i] > max_fat:
        max_fat = faturamento[i]
min_fat = max_fat

for j in range(31):
    if min_fat > faturamento[j]:
        min_fat = faturamento[j]

print (max_fat)
print(min_fat)

   
     
    