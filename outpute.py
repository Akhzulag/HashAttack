import hashlib
from scipy.stats import uniform, t,norm, randint
import keyboard
import cProfile
import random
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

        print("\\\\"+f"Повідомлення: {data_to_hash + str(i)}"+"\\\\")
        print(f"Геш значення: {hashed_data[:52]}"+"\\textcolor{red}" +'{'+f"{hashed_data[52:]}"+'}'+"\\\\")
        if hashed_data[52:] == originalHASH:
            print("PEREMOHA")
            print("ORIGINAL HASH", originalHASH)
            print(f"Original data: {data_to_hash}")
            print(f"SHA-224 Hash: {hashed_data}")
            break
        i += 1

    return i

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
        print("\\\\" + f"Повідомлення {i}: {st}" + "\\\\")
        print(f"Геш значення: {hashed_data[:52]}" + "\\textcolor{red}" + '{' + f"{hashed_data[52:]}" + '}' + "\\\\")
        if i == 30:
            user_input = input("Введіть щось: ")
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
        print("\\\\" + f"Повідомлення: {data_to_hash + str(i)}" + "\\\\")
        print(f"Геш значення: {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\")
        if i == 30:
            user_input = input("Введіть щось: ")
        if hashed_data[48:] in dict:
            print("PEREMOHA. collision was found")
            print(f"X1 {data_to_hash + str(i)} => h(X1) = {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\")
            hashed_data = sha224_hash(dict[hashed_data[48:]])
            print(f"X2 {dict[hashed_data[48:]]} => h(X2) = {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\")
            break
        else:
            dict[hashed_data[48:]] = data_to_hash + str(i)

        i += 1

def second_type_birth(data_to_hash):
    dict = {}
    i = 0
    st = data_to_hash
    with open("out.txt", 'w') as output_file:
        while True:
            st = change_str(st)
            hashed_data = sha224_hash(st)
            print("\\\\" + f"Повідомлення {i}: {st}" + "\\\\")
            print(f"Геш значення: {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\")

            output_file.write("\\\\" + f"Повідомлення {i}: {st}" + "\\\\\n")
            output_file.write(f"Геш значення: {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\\n")

            if i == 30:
                user_input = input("Введіть щось: ")
            if hashed_data[48:] in dict:
                if dict[hashed_data[48:]] == st:
                    continue
                print("PEREMOHA. collision was found")
                print(f"X1 {st} => h(X1) = {hashed_data[48:]}")
                print(f"X2 {dict[hashed_data[48:]]} => h(X2) = {hashed_data[48:]}")
                print(f"X1 {st} => h(X1) = {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\")
                hashed_data = sha224_hash(dict[hashed_data[48:]])
                print(f"X2 {dict[hashed_data[48:]]} => h(X2) = {hashed_data[:48]}" + "\\textcolor{red}" + '{' + f"{hashed_data[48:]}" + '}' + "\\\\")

                break
            else:

                dict[hashed_data[48:]] = st
            i += 1

# Приклад використання
data_to_hash = "Burzhymskiy Rostyslav"
hashed_data = sha224_hash(data_to_hash)
print(data_to_hash, hashed_data)
print(change_str(data_to_hash))
print(change_str(data_to_hash))
print(change_str(data_to_hash))
print(change_str(data_to_hash))
print(change_str(data_to_hash))

#cProfile.run('second_type_birth(data_to_hash)', sort='cumulative')

#first_type_birth(data_to_hash)
second_type_birth(data_to_hash)
#first_type_prototype(data_to_hash)
#second_type_prototype(data_to_hash)

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
