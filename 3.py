#Ασκηση 3

def poso(pos,foros):
    return pos+((foros/100)*pos)

total=0
f=True
while f==True:
    p,fo=input("Δωσε τιμη και φορο ενω αν δεν υπαρχει αλλο προιον δωσε την τιμη 0 και στις 2 τιμες: ").split()
    if int(p)==0:
        f=False
    else:
        total=total+poso(float(p),float(fo))
print('Η τελικη τιμη των προιοντων ειναι: ',total)

#Ηξερα οτι επρεπε να χρησιμοποιησω λεξικο αλλα δεν καταλαβα την εκφωνηση :(

        
