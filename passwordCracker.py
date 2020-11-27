import hashlib
from hashlib import sha256
import string
import re
x = []
y = []
def encrypt_string(hash_string):
    hashed_value = hashlib.sha256(hash_string.encode()).hexdigest()
    return hashed_value


# x = encrypt_string("password")
# print(x)
test = "670fa3af18302f4e1f0f25320cb830232b38712e5a5d20f07eb72459ddb5cf44"
alphString = "abcdefghijklmnopqrstuvwxyz"
string1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
for char in string1:
    y.append(char)
alph = []
for char in alphString:
    alph.append(char)

# def permutationsOfLengthK(set, k):   
#     n = len(set)  
#     findPasswordSalt(set, "", n, k) 

"""This function is used to find password salt and its position"""
def findPasswordSalt(set, prefix, k): 
    n = len(set)
    if (k == 0) : 
        preSalt = prefix + "password"
        postSalt = prefix + "password"
        preSaltHash = encrypt_string(preSalt)
        postSaltHash = encrypt_string(postSalt)
        if preSaltHash == test :
            print(preSalt)
            return preSalt
        if postSalt == test:
            print(postSalt) 
            return postSalt
        return
    for i in range(n):
        newPrefix = prefix + set[i] 
        findPasswordSalt(set, newPrefix, k - 1) 


# salt = re.sub("password", "", findPasswordSalt(y, "", 4))
# print(salt)
foundSalt = "$@1t"

"""Reads in password hashes from given files"""
def findPasswordFromFile(fileName):
    passwordList = []
    lineCount = 0
    with open(fileName) as file:
        for line in file:
            for word in line.split():
                if len(word) == 64:
                    passwordList.append(word)
                    lineCount += 1
    return lineCount, passwordList

"""Creates all string permutations given a set of characters and a string lenth"""
def createPerumationStrings(set, prefix, k,):
    global x
    n = len(set)
    if (k == 0) : 
        x.append(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i] 
        createPerumationStrings(set, newPrefix, k - 1) 



# createPerumationStrings(alph, "",4) 
# createPerumationStrings(alph,"", 5)
# createPerumationStrings(alph,"", 6)
# createPerumationStrings(alph,"",  7)

# for i in range(len(x)):
#     print(x[i] + "")

"""Writes contents of a list to a file"""
def buildRainbowTableFile(table, filename):
    with open(filename, "w") as file:
        for entry in table:
            string2 = entry + "\n"
            file.write(string2)

# buildRainbowTableFile(x, "preComputedHashes.txt")
""" Reads a text file and creates a hash table from text file"""
def buildRainbowTable(textFile):
    table = {}
    tableCount = 0
    with open(textFile) as file:
        for line in file:
            for word in line.split():
                if (len(word) >= 4 and len(word) <= 7) and word.isalpha():
                    table[encrypt_string(foundSalt + word)] = word
                    tableCount += 1
    return table, tableCount

testPasswordCount, testPasswordList = findPasswordFromFile("test.txt")
challengePasswordCount, challengePasswordList = findPasswordFromFile("challenge.txt")

rainbowTable, tableCount = buildRainbowTable("pass.txt")
print(tableCount)
testPassCount = 0
for password in challengePasswordList:
    if password in rainbowTable:
        print(rainbowTable[password])
        testPassCount += 1
print("Password detection Accuracy of:", + (testPassCount / challengePasswordCount ) * 100, "%")