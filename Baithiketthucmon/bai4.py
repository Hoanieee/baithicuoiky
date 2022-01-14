NameId = input("Tên và ID của em là:")
print ("", NameId);

import re
Id = []
Name=[]

Id = re.sub(r'\D','', NameId)
print("Id của em là: ", Id);
Number =re.findall(r'\d',Id)
Idsplit=tuple(Number)
print ("",Idsplit)

Name=NameId.strip(Id)
Namesplit=tuple(Name)
print("Tên của em là:",Name)
print("",Namesplit)

