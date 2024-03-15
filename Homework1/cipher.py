
def encrypt(inputText, N, D):
    encrypted_text = ""
    for char in range(len(inputText) -1, -1, -1):
            fronttoback = chr((ord(inputText[char]) - 34 + (D * N)) % 93 + 34)
            encrypted_text += fronttoback
    return encrypted_text

def decrypt(inputText, N, D):
    decrypted_text = ""
    for char in range(len(inputText) -1, -1, -1):
            backtofront = chr((ord(inputText[char]) - 34 - (D * N)) % 93 + 34)
            decrypted_text += backtofront
    return decrypted_text


def Task3():
      message = open("database.txt", "r")
      messagebyline = message.readline().strip()
      while(messagebyline != ""):
            messagebyword = messagebyline.split()
            print(decrypt(messagebyword[0], 3, 1) + " " + decrypt(messagebyword[1], 3, 1))
            messagebyline = message.readline().strip()

"""
1).   Who is in the database above?
    Userid: assamant Password: Temp123
    Userid: skharel Password: Life15$
2). who has correct username but not same password?
    UserId: aissa
    UserId: bjha
3) Who doesn't meet requirements?
    Userid:Allay! because she included an exclamation point in her name


"""           


Task3()