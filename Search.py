import pickle

def search():
    f = open('criminals.dat','rb')
    cn = int(input('Enter Convict Number to search: '))
    flag = 0
    try:
        while True:
            record = pickle.load(f)
            if cn in record:
                flag = 1
                print(record)
    except EOFError:
        if flag == 0:
            print('Record not found')
    finally:
        f.close()