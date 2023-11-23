import hashlib
from scipy.stats import uniform, t,norm,randint
import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev, mean
import random
def sha224_hash(data):

    sha224 = hashlib.sha224()

    sha224.update(data.encode('utf-8'))

    hashed_data = sha224.hexdigest()

    return hashed_data

def first_type_prototype(data_to_hash):

    hashed_data = sha224_hash(data_to_hash)

    originalHASH = hashed_data[52:]  # 52
    print(hashed_data)
    print("OOOOOOO", originalHASH)
    i = 0
    while True:
        hashed_data = sha224_hash(data_to_hash + str(i))

        # print(f"Original data: {data_to_hash + str(i)}")
        # print(f"SHA-224 Hash: {hashed_data}")
        if hashed_data[52:] == originalHASH:

            print("PEREMOHA")
            print(data_to_hash +"   "+ str(i))
            print("ORIGINAL HASH", originalHASH)
            print(f"Original data: {data_to_hash}")
            print(f"SHA-224 Hash: {hashed_data}")
            break
        i += 1

    return i

# def randomNumber(begin, end):
#     randNum = uniform(loc=begin, scale=end - begin)
#     r = [0]*1000
#     for i in range(100000):
#         p: int = randNum.rvs(1)[0]
#         print(int(p))
#         r[int(p)] += 1
#     print(r)

def randon_number(begin, end):
    randNum = uniform(loc=begin, scale=end - begin)
    p = randNum.rvs(1)[0]
    return(int(p))

def random_char():
    return chr(randon_number(33,127))

def change_str(st):
    ask = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    index_to_change = randint.rvs(0, len(st),size=1)[0]

    new_char = random.choice(ask)

    return st[:index_to_change] + new_char + st[index_to_change + 1:]

def second_type_prototype(data_to_hash):
    originalHASH = sha224_hash(data_to_hash)[52:]

    i = 0
    st = data_to_hash
    while True:
        st = change_str(st)
        hashed_data = sha224_hash(st)
        #print(st)
        if hashed_data[52:] == originalHASH:
            print("PEREMOHA")
            print("ORIGINAL HASH", originalHASH)

            print(f"Original data: {data_to_hash}")
            print(st)
            print(f"SHA-224 Hash: {hashed_data}")
            break
        i += 1
    return i
def first_type_birth(data_to_hash):
    dict = {}
    i = 0
    while True:
        hashed_data = sha224_hash(data_to_hash + str(i))
        if hashed_data[48:] in dict:
            print("PEREMOHA. collision was found")
            print(f"X1 {data_to_hash + str(i)} => h(X1) = {hashed_data[48:]}")
            print(f"X2 {dict[hashed_data[48:]]} => h(X2) = {hashed_data[48:]}")
            break
        else:
            dict[hashed_data[48:]] = data_to_hash + str(i)
        i += 1
    return i
def second_type_birth(data_to_hash):
    dict = {}
    i = 0
    st = data_to_hash
    while True:
        st = change_str(st)
        hashed_data = sha224_hash(st)
        if hashed_data[48:] in dict and dict[hashed_data[48:]] != st:
            print("PEREMOHA. collision was found")
            print(f"X1 {st} => h(X1) = {hashed_data[48:]}")
            print(f"X2 {dict[hashed_data[48:]]} => h(X2) = {hashed_data[48:]}")
            break
        else:
            dict[hashed_data[48:]] = st
        i += 1
    return i
# Приклад використання
data_to_hash = "Burzhymskiy Rostyslav"
hashed_data = sha224_hash(data_to_hash)
print(data_to_hash, hashed_data)

#second_type_prototype(data_to_hash)


#first_type_birth(data_to_hash)

#second_type_birth(data_to_hash)

def random_string(size):
    st = ""
    randNum = uniform(loc=33, scale=127 - 33)
    p = randNum.rvs(size)
    for i in range(size):
        st += chr(int(p[i]))
    return st




def sem(data):
    return stdev(data) / np.sqrt(len(data))


def build_interval_plot(f):
    X = []
    for i in range(100):
        print(i)
       # lenST = randint.rvs(13,100,size=1)[0]
        st = random_string(20)
        X.append(f(st))

    print(X)
    for i in range(100):
        print(i+1, '&', X[i])
    print(stdev(X))
    print(f"{norm.interval(1-0.5, loc=mean(X), scale=sem(X))}")
    plt.bar(range(len(X)), X, label='Зміна значень у списку X')
    plt.xlabel('Крок')
    plt.ylabel('Значення')
    plt.title('Зміна значень у списку X на 100 кроків')
    plt.legend()
    plt.show()

build_interval_plot(first_type_prototype)

#(87532.20134958814, 93896.25865041185)