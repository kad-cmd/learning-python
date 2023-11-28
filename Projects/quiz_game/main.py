print("Welcome to my computer quiz!")

playing = input("Do you want to play? (y/n): ")

if playing.lower() != "y":
    quit()

print("Okay! let's play :) ")
score = 0


answer = input("what does CPU stand for?: ")
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")


answer = input("what does RAM stand for?: ")
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("what does GPU stand for?: ")
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("what does PSU stand for?: ")
if answer == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect")

print(score, "/ 4")
print(f"You scored : {(score/4) * 100}%")