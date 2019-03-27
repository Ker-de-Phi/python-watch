#Question 1 :
def Bissextile(A):
    """Cette fonction renvoie un booléen indiquant si l'année A est bissextile ou non """
    if A%400==0 :
        return(True)
    
    else :
        if A%4==0 :
            if A%100!=0 :
                return(True)
    return(False)



#Question 2 :
def NombreJours(A):
    """Cette fonction renvoie le nombre de jours de l'année A"""
    if A%400==0 :
        return(366)
    
    else :
        if A==0 :
            if A%100!=0 :
                return(366)
    return(365)



#Question 3 :
def Calendrier(A):
    """Cette fonction renvoie le calendrier de l'année sous la forme suivante:
'nom_du_mois',nombre_de_jours_du_mois"""
    
#On définie les tuples équivalents aux couples ('mois',nombre_de_jours) communs aux années bissextiles et non bissextilles
    l1=('janvier',31)
    l3=('mars',31)
    l4=('avril',30)
    l5=('mai',31)
    l6=('juin',30)
    l7=('juillet',31)
    l8=('aout',31) #Ne pas oublier de rajouter le chapeau 
    l9=('septembre',30)
    l10=('octobre',31)
    l11=('novembre',30)
    l12=('décembre',31)
    
#On définie t2 le tuple équivalent au couple ('mois',nombre_de_jours) propre aux années bissextiles
    if A%400==0 :
        l2=('février',29)
    else :
        if A==0 :
            if A%100!=0 :
                l2=('février',29)
                
#On définie t2 le tuple équivalent au couple ('mois',nombre_de_jours) propre aux années non bissextiles
        else :
                l2=('février',28)
    L=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l9,l10,l11,l12]
    return(L)

#Question 4
def ConversionSecondes(S):
    """Cette fonction convertit le nombre de secondes S en j-jour(s), h-heure(s), m-minute(s) et s-seconde(s)"""
    m=S//60
    s=S%60

    h=m//60
    m=m%60

    j=h//24
    h=h%24

    return(j,h,m,s)

#Question 5
def HeureUTC():
    """Cette fonction renvoie l'heure UTC courante"""
    from time import time
    time=int(time())
    def ConversionSecondes(S):
        global j,h,m,s
        m=S//60
        s=S%60
    
        h=m//60
        m=m%60
    
        j=h//24
        h=h%24
    ConversionSecondes(time)
    J=j*24*60*60
    var=time-J
    ConversionSecondes(var)
    return 'UTC : '+str(h)+' heures '+str(m)+' minutes et '+str(s)+' secondes.'

#Question 6    
def Date2016(J):
    """Cette fonction renvoie la date obtenue en ajoutant J-jour(s) au 1er janvier 2016"""
    l1=('janvier',31)
    l2=('février',29)
    l3=('mars',31)
    l4=('avril',30)
    l5=('mai',31)
    l6=('juin',30)
    l7=('juillet',31)
    l8=('aout',31) #Ne pas oublier de rajouter le chapeau 
    l9=('septembre',30)
    l10=('octobre',31)
    l11=('novembre',30)
    l12=('décembre',31)
    L=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
    k=0
    J=J+1
    p=1
    for i in range(0,12,1):
        
        if J-((L[i])[1])>0 and p==1:
            J=J-(L[i])[1]
            k=k+1
        else :
            p=0
    M=(L[k])[0]
    return 'Date : '+str(J)+' '+str(M)+' 2016'

#Question 7
def HorlogeUTC2016():
    """Cette fonction utilisable uniquement en 2016 et ne prenant pas en compte les changements liés à l'heure d'été, renvoie la date UTC et l'heure UTC courante"""
    
    from time import time
    
    S=16801*24*60*60
    R=int(time())-S
    
    def ConversionSecondes(X):
        global j,h,M,m,s,H

        M=X//60
        s=X%60
        H=M//60
        j=H//24
        m=M%60
        h=H%24
       
    ConversionSecondes(R)
    
    def Date2016(J):
        l1=('janvier',31)
        l2=('février',29)
        l3=('mars',31)
        l4=('avril',30)
        l5=('mai',31)
        l6=('juin',30)
        l7=('juillet',31)
        l8=('aout',31) #Ne pas oublier de rajouter le chapeau 
        l9=('septembre',30)
        l10=('octobre',31)
        l11=('novembre',30)
        l12=('décembre',31)
        L=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        k=0
        J=J+1
        p=1
        for i in range(0,12,1):
        
            if J-((L[i])[1])>0 and p==1:
                J=J-(L[i])[1]
                k=k+1
            else :
                p=0
        M=(L[k])[0]
        k=i
                
        print('Date : '+str(J)+' '+str(M)+' 2016')
        
        
    Date2016(j)

    def HeureUTC():
        print('UTC : '+str(h)+' heures '+str(m)+' minutes et '+str(s)+' secondes.')
    
    HeureUTC()

#Question 8
def DateComp2016(J):
    """Cette fonction utilisable uniquement en 2016 et ne prenant pas en compte les changements liés à l'heure d'été, renvoie le nom du jour, la date UTC et l'heure UTC courante"""
    J=J+1
    global M,k,JO
    l1=('janvier',31)
    l2=('février',29)
    l3=('mars',31)
    l4=('avril',30)
    l5=('mai',31)
    l6=('juin',30)
    l7=('juillet',31)
    l8=('aout',31)
    l9=('septembre',30)
    l10=('octobre',31)
    l11=('novembre',30)
    l12=('décembre',31)
    L=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]            
    k=0
    p=1
    for i in range(0,12,1):
        if J-((L[i])[1])>0 and p==1:
            J=J-(L[i])[1]
            k=k+1
        else :
            p=0
    M=(L[k])[0]
    k=i
    JOU=J%7 
    if JOU==0:
        JO='jeudi'
    if JOU==1:
        JO='vendredi'
    if JOU==2:
        JO='samedi'
    if JOU==3:
        JO='dimanche'
    if JOU==4:
        JO='lundi'
    if JOU==5:
        JO='mardi'
    if JOU==6:
        JO='mercredi'

    print('Date : '+str(JO)+' '+str(J)+' '+str(M)+' 2016')


"""#Question 9
def Horloge2016():
 
    
    from time import time
    
    S=16801*24*60*60
    R=int(time())-S
    
    def ConversionSecondes(X):
        global J,j,h,M,m,s,H

        M=X//60
        s=X%60
        H=M//60
        j=H//24
        m=M%60
        h=H%24
        j=j+1
        J=j
       
    ConversionSecondes(R)
    j=J
    
    
    def DateComp2016(J):
        global M,k,JO
        l1=('janvier',31)
        l2=('février',29)
        l3=('mars',31)
        l4=('avril',30)
        l5=('mai',31)
        l6=('juin',30)
        l7=('juillet',31)
        l8=('aout',31)
        l9=('septembre',30)
        l10=('octobre',31)
        l11=('novembre',30)
        l12=('décembre',31)
        L=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
 
            
        k=0
        p=1
        for i in range(0,12,1):
            if J-((L[i])[1])>0 and p==1:
                J=J-(L[i])[1]
                k=k+1
            else :
                p=0
        M=(L[k])[0]
        k=i
                
                   
    DateComp2016(J)

    he=h

    
    if 2<k<9 :
        he=he+1
    else :
        if k==2 :
            if j>27 :
                he=he+1
            if j==27 :
                if he>=2:
                    he=he+1
        if k==9:
            if j<30:
                he=he+1
            if j==30 :
                if h<=3:
                    he=he+1
    if he>=24:
        j=j+1
        he=0
    JOU=j%7 
    if JOU==0:
        JO='jeudi'
    if JOU==1:
        JO='vendredi'
    if JOU==2:
        JO='samedi'
    if JOU==3:
        JO='dimanche'
    if JOU==4:
        JO='lundi'
    if JOU==5:
        JO='mardi'
    if JOU==6:
        JO='mercredi'
    
    #On ajuste ici l'heure d'été et d'hiver

    print('Date : '+str(JO)+' '+str(j)+' '+str(M)+' 2016')
    
    def HeureUTC():
        print('UTC : '+str(he)+' heures '+str(m)+' minutes et '+str(s)+' secondes.')
    
    HeureUTC()"""

#Question 10
def Date(A,J):
    """Cette fonction renvoie le jour obtenu en ajoutant J-jour(s) à l'année A"""
    J=J+1
    l1=('janvier',31)
    l2=('février',28)
    l21=('février',29)
    l3=('mars',31)
    l4=('avril',30)
    l5=('mai',31)
    l6=('juin',30)
    l7=('juillet',31)
    l8=('aout',31)
    l9=('septembre',30)
    l10=('octobre',31)
    l11=('novembre',30)
    l12=('décembre',31)
    L0=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
    #Liste pour année non bissextile
    L1=[l1,l21,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
    #Liste pour année bissextile
    
    def Bissextile(A):
        global B
        if A%400==0 :
            B=1
        else :
            if A%4==0 :
                if A%100!=0 :
                    B=1
                else:
                    B=0
            else :
                B=0
    Bissextile(A)
    while J>366:
        Bissextile(A)
        if B==1:
            J=J-366
        else:
            J=J-365
        A=A+1
        
    if J==366:
        if B==1:
            return('Date : 31 décembre '+str(A)+'.')
        else :
            return('Date : 1 janvier'+str(A+1)+'.')
    else:
        if B==1:
            L=L1
        else:
            L=L0
    k=0
    p=1
    for i in range(0,12,1):
        
        if J-((L[i])[1])>0 and p==1:
            J=J-(L[i])[1]
            k=k+1
        else:
            p=0
    M=(L[k])[0]
    return('Date : '+str(J)+' '+str(M)+' '+str(A)+'.')


#Question 9
def Horloge2016():
    """Cette fonction, utilisable uniquement en 2016, renvoie le nom du jour, la date UTC et l'heure UTC courante"""
    
    from time import time
    
    S=16436*24*60*60
    R=int(time())-S
    
    def ConversionSecondes(X):
        global J,j,he,M,m,s,H

        M=X//60
        s=X%60
        H=M//60
        j=H//24
        m=M%60
        he=H%24
        j=j+1
        J=j
       
    ConversionSecondes(R)
    j=J
    
    
    def Date(A,J):
        l1=('janvier',31)
        l2=('février',28)
        l21=('février',29)
        l3=('mars',31)
        l4=('avril',30)
        l5=('mai',31)
        l6=('juin',30)
        l7=('juillet',31)
        l8=('aout',31)
        l9=('septembre',30)
        l10=('octobre',31)
        l11=('novembre',30)
        l12=('décembre',31)
        L0=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année non bissextile
        L1=[l1,l21,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année bissextile
    
        def Bissextile(A):
            global B
            if A%400==0 :
                B=1
            else :
                if A%4==0 :
                    if A%100!=0 :
                        B=1
                    else:
                        B=0
                else :
                    B=0
        Bissextile(A)
        var=0
        while J>366:
            Bissextile(A)
            if B==1:
                J=J-366
            else:
                J=J-365
            A=A+1
            
        if J==366:
            if B==1:
                print('Date : 31 décembre '+str(A)+'.')
                var=1
            else :
                print('Date : 1 janvier'+str(A+1)+'.')
                var=1
        else:
            if B==1:
                L=L1
            else:
                L=L0
        k=0
        p=1
        for i in range(0,12,1):
        
            if J-((L[i])[1])>0 and p==1:
                J=J-(L[i])[1]
                k=k+1
            else:
                p=0
        M=(L[k])[0]
        if var==0 :
            print('Date : '+str(J)+' '+str(M)+' '+str(A)+'.')
                
                   
    Date(2015,j)

    
    def HeureUTC():
        print('UTC : '+str(he)+' heures '+str(m)+' minutes et '+str(s)+' secondes.')
    
    HeureUTC()


#Question 11.a)

def HorlogeUTC():
    
    from time import time
    
    S=16436*24*60*60
    R=int(time())-S
    
    def ConversionSecondes(X):
        global J,j,he,M,m,s,H

        M=X//60
        s=X%60
        H=M//60
        j=H//24
        m=M%60
        he=H%24
        j=j+1
        J=j
       
    ConversionSecondes(R)
    j=J
    
    
    def Date(A,J):
        l1=('janvier',31)
        l2=('février',28)
        l21=('février',29)
        l3=('mars',31)
        l4=('avril',30)
        l5=('mai',31)
        l6=('juin',30)
        l7=('juillet',31)
        l8=('aout',31)
        l9=('septembre',30)
        l10=('octobre',31)
        l11=('novembre',30)
        l12=('décembre',31)
        L0=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année non bissextile
        L1=[l1,l21,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année bissextile
    
        def Bissextile(A):
            global B
            if A%400==0 :
                B=1
            else :
                if A%4==0 :
                    if A%100!=0 :
                        B=1
                    else:
                        B=0
                else :
                    B=0
        Bissextile(A)
        var=0
        while J>366:
            Bissextile(A)
            if B==1:
                J=J-366
            else:
                J=J-365
            A=A+1
            
        if J==366:
            if B==1:
                print('Date : 31 décembre '+str(A)+'.')
                var=1
            else :
                print('Date : 1 janvier'+str(A+1)+'.')
                var=1
        else:
            if B==1:
                L=L1
            else:
                L=L0
        k=0
        p=1
        for i in range(0,12,1):
        
            if J-((L[i])[1])>0 and p==1:
                J=J-(L[i])[1]
                k=k+1
            else:
                p=0
        M=(L[k])[0]
        if var==0 :
            print('Date : '+str(J)+' '+str(M)+' '+str(A)+'.')
                
                   
    Date(2015,j)

    
    def HeureUTC():
        print('UTC : '+str(he)+' heures '+str(m)+' minutes et '+str(s)+' secondes.')
    
    HeureUTC()
        
#Question 11.b)
def HorlogeCompUTC():
    
    from time import time
    
    S=16436*24*60*60
    R=int(time())-S
    
    def ConversionSecondes(X):
        global J,j,he,M,m,s,H

        M=X//60
        s=X%60
        H=M//60
        j=H//24
        m=M%60
        he=H%24
        j=j+1
        J=j
       
    ConversionSecondes(R)
    j=J
    JOU=(j-1)%7
    if JOU==0:
        JO='jeudi'
    if JOU==1:
        JO='vendredi'
    if JOU==2:
        JO='samedi'
    if JOU==3:
        JO='dimanche'
    if JOU==4:
        JO='lundi'
    if JOU==5:
        JO='mardi'
    if JOU==6:
        JO='mercredi'
    
    
    def Date(A,J):
        l1=('janvier',31)
        l2=('février',28)
        l21=('février',29)
        l3=('mars',31)
        l4=('avril',30)
        l5=('mai',31)
        l6=('juin',30)
        l7=('juillet',31)
        l8=('aout',31)
        l9=('septembre',30)
        l10=('octobre',31)
        l11=('novembre',30)
        l12=('décembre',31)
        L0=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année non bissextile
        L1=[l1,l21,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année bissextile
    
        def Bissextile(A):
            global B
            if A%400==0 :
                B=1
            else :
                if A%4==0 :
                    if A%100!=0 :
                        B=1
                    else:
                        B=0
                else :
                    B=0
        Bissextile(A)
        var=0
        while J>366:
            Bissextile(A)
            if B==1:
                J=J-366
            else:
                J=J-365
            A=A+1
            
        if J==366:
            if B==1:
                print('Date : 31 décembre '+str(A)+'.')
                var=1
            else :
                print('Date : 1 janvier'+str(A+1)+'.')
                var=1
        else:
            if B==1:
                L=L1
            else:
                L=L0
        k=0
        p=1
        for i in range(0,12,1):
        
            if J-((L[i])[1])>0 and p==1:
                J=J-(L[i])[1]
                k=k+1
            else:
                p=0
        M=(L[k])[0]
        if var==0 :
            print('Date : '+str(JO)+' '+str(J)+' '+str(M)+' '+str(A)+'.')
                
                   
    Date(2015,j)

    
    def HeureUTC():
        print('UTC : '+str(he)+' heures '+str(m)+' minutes et '+str(s)+' secondes.')
    
    HeureUTC()

#Question 11. c)
def Horloge():
    c=0
    cc=0
    ccc=0
    
    from time import time
    
    S=16436*24*60*60
    R=int(time())-S
    
    def ConversionSecondes(X):
        global J,j,he,M,m,s,H

        M=X//60
        s=X%60
        H=M//60
        j=H//24
        m=M%60
        he=H%24
        j=j+1
        J=j
       
    ConversionSecondes(R)
    j=J
    JOU=(j-1)%7
    if JOU==0:
        JO='jeudi'
    if JOU==1:
        JO='vendredi'
    if JOU==2:
        JO='samedi'
    if JOU==3:
        JO='dimanche'
    if JOU==4:
        JO='lundi'
    if JOU==5:
        JO='mardi'
    if JOU==6:
        JO='mercredi'
    
    
    def Date(A,J):
        l1=('janvier',31)
        l2=('février',28)
        l21=('février',29)
        l3=('mars',31)
        l4=('avril',30)
        l5=('mai',31)
        l6=('juin',30)
        l7=('juillet',31)
        l8=('aout',31)
        l9=('septembre',30)
        l10=('octobre',31)
        l11=('novembre',30)
        l12=('décembre',31)
        L0=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année non bissextile
        L1=[l1,l21,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
        #Liste pour année bissextile
    
        def Bissextile(A):
            global B
            if A%400==0 :
                B=1
            else :
                if A%4==0 :
                    if A%100!=0 :
                        B=1
                    else:
                        B=0
                else :
                    B=0
        Bissextile(A)
        var=0
        while J>366:
            Bissextile(A)
            if B==1:
                J=J-366
            else:
                J=J-365
            A=A+1
            
        if J==366:
            if B==1:
                print('Date : 31 décembre '+str(A)+'.')
                var=1
            else :
                print('Date : 1 janvier'+str(A+1)+'.')
                var=1
        else:
            if B==1:
                L=L1
            else:
                L=L0
        k=0
        p=1
        for i in range(0,12,1):
        
            if J-((L[i])[1])>0 and p==1:
                J=J-(L[i])[1]
                k=k+1
            else:
                p=0
        M=(L[k])[0]
        print(c)
        if 2<k<9 and c==0 :
            R=R+60*60  #On rajoute l'heure pour l'heure d'été
            ConversionSecondes(R)
            c=1
        else :
            print(c)
            if k==2 and c==0 :
                if j>23 :
                    for o in range(j,32,1): #On regarde si on a passé le dernier dimanche du mois
                        if j%7==3 :
                            ccc=1
                        if ccc==0 :
                            R=R+60*60
                            ConversionSecondes(R)
                            c=1
            if k==9 and c==0:
                if j<32:
                    for o in range(j,32,1): #On regarde si on a passé le dernier dimanche du mois
                        if j%7==3 :
                            cc=1
                        if cc==1:
                            R=R+60*60
                            ConversionSecondes(R)
                            c=1
            if var==0 :
                print('Date : '+str(JO)+' '+str(J)+' '+str(M)+' '+str(A)+'.')
                
                   
    Date(2015,j)

    
    def HeureUTC():
        print('UTC : '+str(he)+' heures '+str(m)+' minutes et '+str(s)+' secondes.')
    
    HeureUTC()

    



    




