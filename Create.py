import pickle
import os

def create():
    if not os.path.isfile('sno.txt'):
        g = open('sno.txt','w')
        g.write('0')
        g.close()
    g = open('sno.txt','r')
    srlno = int(g.read())
    g.close()
    f = open('criminals.dat','ab')
    while True:
        srlno += 1
        record = dict()
        print('New record is for Convict Number:',srlno)
        name = input('Name of Convict: ')
        location = input('Location of Arrest: ')
        crime = input('Crime Comitted: ')
        sentence = input('Sentence Awarded: ')
        d = [name,location,crime,sentence]
        record[srlno] = d
        print('Record Entered:\n',record)
        pickle.dump(record,f)
        ch = input('Enter more records? (yes/no)')
        if ch.lower() != 'yes':
            break
    f.close()
    g = open('sno.txt','w')
    g.write(str(srlno))
    g.close()
