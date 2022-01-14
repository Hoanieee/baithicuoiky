fullname = input("Họ và tên em là:")
print ("",fullname);

a = int(input("Nhập số nguyên dương a = "))
str1 = str(a)
str2 = str1[::-1]
if (str1 == str2):
    print(a," Là số thuận nghịch")
else:
    print(a," Không là số thuận nghịch")
 
