partyPeople = []

while 1 > 0:
    name = input("Enter invitee's name (or just enter to finish): ")
    if name == "":
        break
    partyPeople.append(name)
    

print()
for i in partyPeople:
    print(f"{i}, please attend our party this Saturday!")
