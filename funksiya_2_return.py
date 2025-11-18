                  ###_1
def mijoz_info(ism,familya,tugilgan_yil,joyi,gmil='',raqam=''):
    info={'ism':ism,
          'familya':familya,
          'tugilgan_yil':tugilgan_yil,
          'joyi':joyi,
          'gmil':gmil,
          'raqam':raqam}
    return info
print("mijoz malumotini kiriting: ")
mijozlar=[]
while True:
    ism=input("Ism: ")
    familya=input("Familya: ")
    tugilgan_yil=input("Tugilgan yil: ")
    joyi=input("Joyi: ")
    gmil=input("Gmail: ")
    raqam=input("Raqam: ")
    mijozlar.append(mijoz_info(ism,familya,tugilgan_yil,joyi,gmil,raqam))
    javob=input('davom etaszmi? (ha/yoq)')
    if javob=='yoq':
        break
print("mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familya'].title()}"
          f"{mijoz['tugilgan_yil']} yoshda , telefoni: {mijoz['raqam']}")

                   ##_3
def eng_katta(a,b,c):
    return max(a,b,c)
print(eng_katta(7,8,8))
              #_4
def aylana(radius,pi=3.14):
    info={'radius':radius,
          'diametr':2*radius,
          'perimetr':2*pi*radius,
          'yuzi':2*pi*radius**2}
    return info
a=aylana(5)
print(a)
                     ##_5
def tub_sonlar(min,max):
    tublar=[]
    for i in range(min,max+1):
        if i>1:
            tub =True
            for son in range(2,i):
                if i%son==0:
                    tub = False
                    break
            if tub:
                tublar.append(i)
    return tublar
print(tub_sonlar(2,50))

                     ##_6
def fibanachi(n):
    fib=[]
    a,b=0,1
    for i in range(n):
        fib.append(b)
        a,b=b,a+b
    return fib
print(fibanachi(20))
