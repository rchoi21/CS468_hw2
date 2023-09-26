import hashlib
import sys

def sha224_only(password):
    try:
        f = open("dictionary.txt")
    except:
        print("dictionary.txt cannot be opened")
    else:
        for line in f:
            line = line.strip()
            line = line.encode()
            hashed_pw = hashlib.sha224(line).hexdigest()
            if hashed_pw == password:
                return line.decode()
        return ""
    
def sha3_224_only(password):
    try:
        f = open("dictionary.txt")
    except:
        print("dictionary.txt cannot be opened")
    else:
        for line in f:
            line = line.strip()
            line = line.encode()
            hashed_pw = hashlib.sha3_224(line).hexdigest()
            if hashed_pw == password:
                return line.decode()
        return ""
    
# def salt(password):
#     try:
#         f = open("dictionary.txt")
#     except:
#         print("dictionary.txt cannot be opened")
#     else:
#         alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#                     '[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
#                     'u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'] # len = 68
#         for line in f:
#             line = line.strip()
#             cipher = ""
#             for i in range(128):
#                 for c in line:
#                     c_idx = alphabet.index(c)



        #     line = line.encode()
        #     hashed_pw = hashlib.sha224(line).hexdigest()
        #     if hashed_pw == password:
        #         return line.decode()
        # return ""

def main():
    pw = "b9703614d138ef18234e74df390c58b39a63b10ac56134d56e61d097"
    found_pw = sha3_224_only(pw)



    if found_pw != "":
        print("heres the found pw:", found_pw)
    else:
        print("more decoding to be done :(")

if __name__ == "__main__":
    sys.exit(main())