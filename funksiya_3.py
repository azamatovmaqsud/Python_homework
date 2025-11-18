         ###_1
def son(*raqam):
    a=sum(raqam)
    return a
print(son(1,2,3,5,7))
         ###_2
def talaba(ism,familya,*yoshi,**mazili):
    info=f"{familya.title()} {ism.title()} {yoshi} yoshda {mazili}da yashaydi"
    return info
print(talaba('ali','komilov','21',manzili='urganch'))
