print("Caesar Cipher")
s = input("Enter Your String : ")
n = int(input("Enter Key : "))
print(f"\n String Before Encyption : {s}")
ans=""
for i in s:
    
    if i.isupper():
        ans+=chr((ord(i)+n-65)%26+65)

    elif i.islower():
        ans+=chr((ord(i)+n-97)%26+97)
    else :
        ans+=str(i)

print(f"\n String After Encryption : {ans}")

ans2=""
for i in ans:
    
    if i.isupper():
        ans2+=chr((ord(i)-n-65)%26+65)

    elif i.islower():
        ans2+=chr((ord(i)-n-97)%26+97)
    else :
        ans2+=str(i)

print(f"\n String After Decryption : {ans2}")
