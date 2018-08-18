# convert so co hai chu so sang word

a = int(input("enter a interger number with two members"))
b = (a//10)
c = (a%10)

list1 = [b,c]
if list1[0] == 0:
    B = "khong"
elif list1[0] == 1:
    B = "mot"
elif list1[0] == 2:
    B = "hai"
elif list1[0] == 3:
    B = "ba"
elif list1[0] == 4:
    B = "bon"
elif list1[0] == 5:
    B = "nam"
elif list1[0] == 6:
    B = "sau"
elif list1[0] == 7:
    B = "bay"
elif list1[0] == 8:
    B = "tam"
else:
    B = "chin"
# ..............................
if list1[1] == 0:
    C = "khong"
elif list1[1] == 1:
    C = "mot"
elif list1[1] == 2:
    C = "hai"
elif list1[1] == 3:
    C = "ba"
elif list1[1] == 4:
    C = "bon"
elif list1[1] == 5:
    C = "nam"
elif list1[1] == 6:
    C = "sau"
elif list1[1] == 7:
    C = "bay"
elif list1[1] == 8:
    C = "tam"
else:
    C = "chin"


print('')
print("  %s muoi %s  " %(B,C))