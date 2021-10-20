l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("\n- - - Monoalphabetic Cipher Code - - -\n")
s = input("Enter Your String : ")
n = list(input("\nEnter Key : ").upper())
print("\nCharacter Mapping : \n")
print(*l)
print("↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ")
print(*n)
print(f"\n String Before Encryption : {s}")
ans=""
for i in s:
    if i.isupper():
        ans+=n[ord(i)-65].upper()

    elif i.islower():
        ans+=n[ord(i)-97].lower()
    else :
        ans+=str(i)

print(f"\n String After Encryption : {ans}")

ans2=""
for i in ans:
    if i.isupper():
        ans2+=l[n.index(i)].upper()

    elif i.islower():
        ans2+=l[n.index(i.upper())].lower()
    else :
        ans2+=str(i)

print(f"\n String After Decryption : {ans2}")
