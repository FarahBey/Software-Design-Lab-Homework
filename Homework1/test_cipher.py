import cipher

def testHW2():

    userIDs=['TEST}a"']
    passwords=["Temp123"]

    print(cipher.encrypt('TEST}a"', 95, 1))
    for i in range(1):
        text1=userIDs[i]
        text2=passwords[i]

        s=2
        d=1
        encrypteduserid=cipher.encrypt(text1, s, d)
        encryptedpasswd=cipher.encrypt(text2, s, d)

        originaluserid=cipher.decrypt(encrypteduserid, s, d)
        originalpasswd=cipher.decrypt(encryptedpasswd, s, d)
        if((text1==originaluserid)&(text2==originalpasswd)):
            print("Test Passed")
        else:
            print("Test Failed")
        
    
def main():
    print("Running HW2 tests......")
    testHW2()
    
main()