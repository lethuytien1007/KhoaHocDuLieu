n = int(input("Nhap mot so tu nhien: ")) #tao mot bien da nhap

while(n < 0): #vong lap xu ly khi bien n < 0
    n = int(input("So khong hop le, vui long nhap lai: "))

a = 1 #tao mot bien giai thua = 1
for i in range(1,n+1): #vong lap xu ly giai thua
    a = a * i

print("Giai thua cua so",n,"la",a) #in ra ket qua