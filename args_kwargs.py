def yigindi(*sonlar):
    """sonlar yigindisini chiqaruvchi funksiya"""
    return sum(sonlar)
print(yigindi(1,4,3,2,321,4))

def avto_info(kompanya,model,**malumotlar):
    """avto haqida malumotlarni lugat korinishida chiqruvchi"""
    malumotlar['model']=model
    malumotlar['kompanya']=kompanya
    return malumotlar
print(avto_info('gm','malubu',rang='qora',narxi='2000$'))

def son(*sonlar):
    """sonlar kopaytmasini topuvchi funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
print(son(1, 2, 23))

def talaba(ismi,familyasi,**kvargs):
    kvargs['ismi']=ismi
    kvargs['familyasi']=familyasi
    return kvargs
talabalar=talaba('Suhrob','Komilov',yoshi=20,manzili='urganch tumani',oqish_joyi='TATU')
print(talabalar)
