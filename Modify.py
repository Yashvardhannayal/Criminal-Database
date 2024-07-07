import pickle
import os

def modify():
    f1 = open('criminals.dat','rb')
    f2 = open('temp.dat','wb')
    cn = int(input('Enter Convict Number to modify: '))
    sentence = input('Enter new sentence: ')
    flag = 0
    try:
        while True:
            record = pickle.load(f1)
            if cn in record:
                flag = 1
                record[cn][3] = sentence
                print('Record changed to: ', record)
                pickle.dump(record,f2)
            else:
                pickle.dump(record,f2)
    except EOFError:
        if flag == 0:
            print('Record not found')
    finally:
        f2.close()
        f1.close()
    os.remove('criminals.dat')
    os.rename('temp.dat','criminals.dat')