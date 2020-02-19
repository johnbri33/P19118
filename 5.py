
#Εργασια 5


arx= input("Δωσε ονομα αρχειου: "
f= open(arx,"r")
list1= [line.rstrip() for line in f] #λιστα με τις προτασεις του αρθρου
f.close()

for i in range(0,len(list1)):
    list2=list1[i].split(' ') #λστα με καθε λεξη του αρθρου
    for k in range(0,len(list2)):
        word=list2[k] #παιρνει καθε λεξη ξεχωριστα
        if len(word)>3:
            let=word[0]
            word2=word[1:]+let+'ay'
        if len(word)>3:
            print('Η λεξη',word,'μετατρεπεται σε:',word2)
        else:
            print('H λεξη παραμενει:',word)
        
            
            
    
    
