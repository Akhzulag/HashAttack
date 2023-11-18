import hashlib
from scipy.stats import uniform, t,norm

import numpy as np
from statistics import stdev, mean

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
    c = random_char()
    position = randon_number(0,len(st))
    st_list = list(st)

    st_list[position] = c

    return ''.join(st_list)

def second_type_prototype(data_to_hash):
    originalHASH = sha224_hash(data_to_hash)[52:]

    i = 0
    st = data_to_hash
    while True:
        st = change_str(st)
        hashed_data = sha224_hash(st)
        print(st)
        if hashed_data[52:] == originalHASH:
            print("PEREMOHA")
            print("ORIGINAL HASH", originalHASH)

            print(f"Original data: {data_to_hash}")
            print(st)
            print(f"SHA-224 Hash: {hashed_data}")
            break
        i += 1

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
            print(hashed_data[48:])
            dict[hashed_data[48:]] = data_to_hash + str(i)
        print(i)
        i += 1

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
            print(hashed_data[48:])
            dict[hashed_data[48:]] = st
        print(i)
        i += 1

# Приклад використання
data_to_hash = "Burzhymskiy Rostyslav"
hashed_data = sha224_hash(data_to_hash)
print(data_to_hash, hashed_data)

#second_type_prototype(data_to_hash)


#first_type_birth(data_to_hash)

#second_type_birth(data_to_hash)

# def random_string(size):
#     st = ""
#     randNum = uniform(loc=33, scale=127 - 33)
#     p = randNum.rvs(size)
#     for i in range(size):
#         st += chr(int(p[i]))
#     return st
#
#
# X = []
# for i in range(10000):
#     print(i)
#     st = random_string(10)
#     X.append(first_type_prototype(st))
#
# def sem(data):
#     return stdev(data) / np.sqrt(len(data))
#
# print(sem(X))
# print(t.interval(1-0.1, df=len(X)-1, loc=mean(X), scale=sem(X)))
