fullname = input("Tên đệm của em là: ")

b = int(input("Nhập số nguyên dương b = "))
S = 0;
temp = b;
while(b > 0):
    S = S + b % 10;
    b = b // 10;
print('Tổng các chữ số của', temp , 'là:' , S)