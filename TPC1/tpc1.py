import csv


def readFile():
    ficheiro = open('myheart.csv', 'r')
    reader = csv.reader(ficheiro)
    myList=[]
    i=0
    for linha in reader:
        corr =0
        #print(linha[0])
        if(i!=0):
            my_dictionary = {'idade':linha[0],'sexo':linha[1],'tensão':linha[2],'colesterol':linha[3],'batimento':linha[4],'temDoenca':linha[5]}
            myList.append(my_dictionary)
        i=i+1
    #print(myList)
    return myList


def distSex(lista ):
    ListfemSem=[]
    ListfemCom=[]
    ListMascSem= []
    ListMascCom=[]
    for linha in lista:
        print(linha)
        if (linha['temDoenca']=='0'):
            if(linha['sexo']=='M'):
                ListMascSem.append(linha)
            if(linha['sexo']=='F'):
                ListfemSem.append(linha)
        if (linha['temDoenca']=='1'):
            if(linha['sexo']=='M'):
                ListMascCom.append(linha)
            if(linha['sexo']=='F'):
                ListfemCom.append(linha)


#[30-34], [35-39], [40-44] , 45+
def escaloesetarios(lista):
    MyList30C=[]
    MyList35C=[]
    MyList40C=[]
    MyList45C=[]
    MyList30S=[]
    MyList35S=[]
    MyList40S=[]
    MyList45S=[]
    for linha in lista :
        if (linha['temDoenca']=='0'):
            if(linha['idade']>='30' and linha['idade']<='34'):
                MyList30S.append(linha)
            if(linha['idade']>='35' and linha['idade']<='39'):
                MyList35S.append(linha)
            if(linha['idade']>='40' and linha['idade']<='44'):
                MyList40S.append(linha)
            if(linha['idade']>'45'):
                MyList45S.append(linha)

        if (linha['temDoenca']=='1'):
            if(linha['idade']>='30' and linha['idade']<='34'):
                MyList30C.append(linha)
            if(linha['idade']>='35' and linha['idade']<='39'):
                MyList35C.append(linha)
            if(linha['idade']>='40' and linha['idade']<='44'):
                MyList40C.append(linha)
            if(linha['idade']>'45'):
                MyList45C.append(linha)
    
    print(MyList40C)


    



def main():
    myList =readFile()
    escaloesetarios(myList)


if __name__ == "__main__":
   main()

