print("Number Guessing Game")
print("Enter value between 1 to 9: ")
number=int(input(""))

g=8

if(number<g):
    print("LOW")
elif(number>g):
    print("HIGH")
else:
    print("CORRECT")

