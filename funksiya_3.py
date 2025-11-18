# def baho(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"talaba {ism.title()} ning bahosini kiriting:")
#         baholar[ism]=baho
#     return baholar
# talabalar=['ali','vali','hasan','olim']
# baholar=baho(talabalar)
# print(baholar)
#
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#
# ismlar=['ali','vali','hasan','husan']
# katta_harf(ismlar)
# print(ismlar)

# def summa(x,y,*sonlar):
#     """kiritilgan sonlar yigindisini hisoblaydigan"""
#     return x+y+sum(sonlar)
# print(summa(1,2,6,8))

# def avto_info(kompaniya,model,**malumotlar):
#     """avto haqida ma'lumotlarni lugat korinishida qaytar fun"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1=avto_info('gm','malibu',rang='qora',yil=2018)
# avto2=avto_info('kia','k5',rang='qizil',narh='3500')
# print(f"{avto1} \n{avto2}")


def oraliq(min,max,qadam=''):
    sonlar=[]
    if qadam == '':
        qadam=1
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
a=oraliq(2,20)
print(a)