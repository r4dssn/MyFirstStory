import random as r



slump = r.randint(1, 100)

print(slump)

def guess():
    run = True
    while(run):
        userinput = int(input("Gissa ett tal mellan 1 och 100: "))
        try:
            if(slump > userinput):
                print("Fel: större",)
                
            elif(slump < userinput):
                print("Fel: mindre",)
                
            else:
                print("Rätt:", slump)
                break
        except:
            print("Något blev fel")
            break


guess()
print("Hejdå")

"""

userinput = int(input("Välj ett tal mellan 1 och 100: "))

while(slump <= userinput):
    print("Slump innehåller nu", slump)
    slump = slump + 1
else:
    print("Skumt men funkar")
"""