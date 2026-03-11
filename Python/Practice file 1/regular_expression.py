#practice question- CWH(CodeWithHarry)

import re

# pattern= "Odia"
pattern = r"[A-Z]+dia" #r - raw string = does not parse escape sequence characters 
#+ - one or more occurences
text = '''Pana Sankranti, (Odia: ପଣା ସଙ୍କ୍ରାନ୍ତି), also known as Maha Bishuba Sankranti (Odia: ମହା ବିଷୁବ ସଙ୍କ୍ରାନ୍ତି),is the traditional new year day festival of Odia people in Odisha, India.The festival occurs in the solar Odia calendar (the lunisolar Hindu calendar followed in Odisha) on the first day of the traditional solar month of Meṣa, hence equivalent lunar month Baisakha. This falls on the Purnimanta system of the Indian Hindu calendar. It therefore falls on 13/14 April every year on the Gregorian calendar.'''

#match = re.search(pattern, text) #First occurence 
#re.search stops at first match
# print(match)

matches = re.finditer(pattern, text) #all occurences
#for all occurences
for match in matches:
    # print(match) #- prints match (regex type)
    print(match.span()) #- gets it's span (tuple type)



#================================# META CHAR
# link - https://www.ibm.com/docs/en/guardium/10.6?topic=discover-regular-expressions || python docs || https://regexr.com/
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs