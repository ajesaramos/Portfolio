#fork con ageMajority boolean
# Further = calculate age based on date of birth, determine if user is of age. Allow, reject.

edad = int(input("How old are you?\r\n"))

ofAge= 18

if edad >= ofAge:
    print("You are allowed to register. Welcome!")
else:
    print("You are still underage, you are not allowed to enter this site")
    wait = str((ofAge - edad))
    print("Wait "+wait+" years :)!")
