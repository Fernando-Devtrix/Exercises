print("How many Km did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 3)
print("You run {} km, that means {} mi".format(kms, miles))
