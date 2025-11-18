
         #___1
def ism_yosh(ismi,yoshi,hozirgi=2025):
    """foydalanuvchi ismi yilini aniqlovchi fumksiya"""
    print(f"foydalanuvchi ismi: {ismi.title()}")
    print(f"{ismi.title()} {hozirgi-yoshi}-yil")
ism_yosh('Alibek',20)

        #___2
def son(ixtiyoriy):
    """son sorrab kvadrati kubini topuvchi"""
    print(f"{ixtiyoriy}-sonini kvadrati {ixtiyoriy**2} ga teng")
    print(f"{ixtiyoriy}-sonini kubi {ixtiyoriy**3} ga teng ")
son(13)

       #___3
def son(ixtiyoriy):
    """son juftmi yoki toqmi konsolga chiqaradi"""
    if ixtiyoriy%2==0:
        print(f"{ixtiyoriy}-juft son")
    else:
        print(f"{ixtiyoriy}-toq son")
son(114)

       #___4
def son(son1,son2):
    """sonni kattasini konsolga chiqaradi agar teng bolsa 'ular teng'-deb chqaradi"""
    if son1>son2:
        print(f"{son1}-kattasi")
    elif son1<son2:
        print(f"{son2}-kattasi")
    else:
        print('bu sonlar teng')
son(12,12)

       #___5
def son(x,y):
    """ x ni y-darajaga kotaruvchi f-ya """
    print(f"{x} ning {y}-darajasi {x**y} ga teng")
son(3,4)

       #___6
def son(x,y=2):
    """ x ni 2-darajaga kotaruvchi f-ya """
    print(f"{x} ning 2-darajasi {x ** y} ga teng")
son(4)

      #___7
def son(k):
    """ k son 2-10 gacha qaysiga qoldiqsiz bolinishini topuvchi f-ya """
    for i in range(2,11):
     if k%i==0:
        print(f"{k} son {i} ga qoldiqsiz bolinadi")
son(144)