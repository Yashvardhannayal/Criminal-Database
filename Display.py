import pickle

def display():
    f = open('criminals.dat','rb')
    try:
        while True:
            record = pickle.load(f)
            print(record)
    except EOFError:
        print('File has come to an end')
    finally:
        f.close()
