inputSeconds = int(input("Enter a number of seconds to be converted: "))
hours = int(inputSeconds/3600)
minutes = int((inputSeconds%3600)/60)
seconds = inputSeconds % 60
print("That input is equal to",str(hours),"hours",str(minutes),"minutes and",str(seconds),"seconds.")
