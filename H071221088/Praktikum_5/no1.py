Index0= int(input("input nilai matrix pertama index 1,1 : "))
Index1= int(input("input nilai matrix pertama index 1,2 : "))
Index2= int(input("input nilai matrix pertama index 2,1 : "))
Index3= int(input("input nilai matrix pertama index 2,2 : "))
Index4= int(input("input nilai matrix kedua index 1,1 : "))
Index5= int(input("input nilai matrix kedua index 1,2 : "))
Index6= int(input("input nilai matrix kedua index 2,1 : "))
Index7= int(input("input nilai matrix kedua index 2,2 : "))

a= (Index0 * Index4) + (Index1*Index6)
b= (Index0 * Index5) + (Index1*Index7)
c= (Index2 * Index4) + (Index3*Index6)
d= (Index2 * Index5) + (Index3*Index7)

print("|",(Index0),(Index1),"| x |",(Index4),(Index5),"| = |",(a),(b),"|")
print("|",(Index2),(Index3),"|   |",(Index6),(Index7),"|   |",(c),(d),"|")