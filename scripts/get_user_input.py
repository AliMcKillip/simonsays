from getpass import getpass
#this script shows how to get user input

print "What is your name?"
name = raw_input()

color = getpass('What is your favorite color?')

print "Hi", name
print "Your favorite color is: ", color
