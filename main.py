import random

pounds = float(input("How many pounds of fish did you catch? "))

kilograms = pounds * 0.45359237

payment = kilograms * 2

print("Weight in kilograms:", round(kilograms, 2))
print("Your payment is:", round(payment, 2), "dollars")

if payment > 100:
    prizes = ["Hat", "Hook", "Bucket"]
    prize = random.choice(prizes)
    print("Congratulations! Your prize is:", prize)
