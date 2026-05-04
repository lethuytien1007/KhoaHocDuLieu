n = int(input("Nhap mot so tu nhien lon hon 0: "))

while(n < 0): #Vòng lap xu ly neu bien la so am thi se nhap lai
    n = int(input("So khong hop le,nhap lai: "))

sum = int((1+n)*n/2)
print(sum)