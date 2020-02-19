
#Εργασια 2

arx= input("Δωσε ονομα αρχειου: ")
f= open(arx,"r")
list1= [line.rstrip() for line in f] #λιστα με τις προτασεις του αρθρου
f.close()

for i in range(0,len(list1)):
    list2=list1[i].split(' ') #λιστα με καθε λεξη του αρθρου
    for k in range(0,len(list2)):
        list3=list2[k] #παιρνει καθε λεξη του αρθρου 
        bw=0 #πληθος κακων γραμματων
        gw=0 #πληθος καλων γραμματων
        ow=0 #πληθος ουδετερων γραμματων που δν χρειαζεται πουθενα ουσιαστικα
        for n in range(0,len(list3)):
            l=list3[n]
            if l=='f' or l=='c' or l=='k' or l=='r':
                bw+=1
            elif l=='a' or l=='e' or l=='i' or l=='o' or l=='y' or l=='u':
                ow+=1
            else:
                gw+=1
        if gw>bw:
            print('Η λεξη',list3,'ειναι καλη.')
        else:
            print('Η λεξη',list3,'ειναι κακη.')
        
            
            


        
        
            
            
        
    
    
