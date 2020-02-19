
#Εργασια 12

date= input("Δωσε μια ημερομηνια της μορφης ΗΗ/ΜΜ/ΕΕΕΕ: ")
month=date.split('/')
if str(month[1])=='04' or str(month[1])=='06' or str(month[1])=='09' or str(month[1])=='11':
    print('Ο μηνας αυτης της ημερομηνιας εχει 30 ημερες')
elif str(month[1])=='02':
    year=int(month[2])%4
    if year==0:
        print('Ο μηνας αυτης της ημερομηνιας εχει 29 ημερες')
    else:
        print('Ο μηνας αυτης της ημερομηνιας εχει 28 ημερες')
else:
    print('Ο μηνας αυτης της ημερομηνιας εχει 31 ημερες')
import datetime
tday= datetime.datetime.today()
day=datetime.datetime(int(month[2]),int(month[1]),int(month[0]),0,0,0)



print('Η ημερομηνια απεχει',day-tday,'ωρες απο την σημερινη μερα')

    
    
    
    
         
         
         
         
