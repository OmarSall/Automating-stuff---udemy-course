
# import re

# message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

# #creating regular expression object

# phoneNumRegex = re.compile(r'/d/d/d-/d/d/d-/d/d/d/d')              #re.compile detects the pattern we are looking for

# #creating the match object

# # mo = phoneNumRegex.search(message)
# mo = phoneNumRegex.findall(message)
# print(mo.group())

##########################################################
""" VERSION WITHOUT REGEX """

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False  #not phone nr size
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False    #missing dash
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#             return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False    #missing last 4 digits
#     return True

# print(isPhoneNumber('415-123-2222'))

###############################################################

import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')              

# mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow')

# mo.group()

# print(mo)

#############################333

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())

########################################33

# batRegex = re.compile(r'Bat(wo)?man')       #the (wo)? can appear 1 or 0 times so I cannot be batwowowoman

# phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')    

# mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow')

########################################
# batRegex = re.compile(r'Bat(wo)*man')    #baywowowowoman will return true

# regex = re.compile(r'(\+\*\?)+')            #plus indicates the characters in the paranthesis can appear one or more times
# print(regex.search('i learned about +*? regex syntax'))

###########################################

# haRegex = re.compile(r'(Ha){3,5}')      #{x,y} minimum and max number of repetitions, {3,} - at least 3
# print(haRegex.search('he said "HaHaHa"'))

# beginsWithHelloRegex = re.compile(r'^Hello')
# print(beginsWithHelloRegex.search('Hello there!'))

# dotStar = re.compile(r'.*', re.DOTALL)
# ######################################
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
# print(namesRegex.sub('*','Agent Alice gave the secret documents to Agent Bob'))

# namesRegex = re.compile(r'Agent (\w)\w*')
# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
# print(namesRegex.sub(r'Agent \1***','Agent Alice gave the secret documents to Agent Bob'))
##############################################

re.compile(r"""
\d\d\d          #area code
-               #first digits
\d\d\d
-
\d\d\d\d""", re.VERBOSE)