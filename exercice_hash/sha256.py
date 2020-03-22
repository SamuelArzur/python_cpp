import sha256

print("Saisissez une ligne à hasher : ")
chaine = input()
print("Voici votre hash : \n"+sha256.hash(chaine))
