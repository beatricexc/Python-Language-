#Regex -regular expressions- are descriptions for a pattern of text. Al Sweigart

#Creating regex objects
import re  #importing the re module
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # passing the desired pattern to the re.compile , "r" stands for raw string
mo = phoneNumRegex.search('My phone number is 415-555-4242.') #the search() method searches the string is passed for any mataches to the regex
print('Phone number found: ' + mo.group()) # Match  objects have a group()  method that will return the actual matched text from the searched string.

#Steps of Regex Matching
#1. Import the regex module with import re
#2. Create a Regex object with the re.compile() function (Don't forget about the raw string r)
#3. Pass the string you want to search into the Regex object's search() method.This returns a Match object (Mo in our case)
#4.Call the Match object's group() method to return a string of the actual matched text."""


