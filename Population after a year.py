currentPopulation = int(input("What is the current population? "))
birthRate = int(input("How often is a baby born in seconds? "))
deathRate = int(input("How often does someone die in seconds? "))
immigrationRate = int(input("How often does someone immigrate in seconds? "))
emmigrationRate = int(input("how often does someone emmigrate in seconds? "))
secondsInYear = 365 * 24 * 60 * 60
futurePopulation = int(currentPopulation + (secondsInYear/birthRate) - (secondsInYear/deathRate) + (secondsInYear/immigrationRate)-(secondsInYear/emmigrationRate))
print("The population one year from now will be "+str(futurePopulation))