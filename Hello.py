# PRINT HELLO WORLD
print ("hello world")
print ('hello world')

'''# PRINT POEM(MULTILINE)'''
#print('''twinkle, twinkle little STar,
#		how i wonder what u re!
#		up above the world so high''')

#variable
'''name = "Mitali"
num = 345

age = 45.33
is_adult = True  #boolean value   "T" is capital



name = "nidhi" #change value 

print(name)'''


#Exercise 1

'''fname = "Tony"
lname = "Stark"
age = 52
is_genius = True

print(fname + " " + lname)   #fname,lname  is also true 
print(age)
print(is_genius)'''

'''#===============TAKE INPUT FROM USER=====================

name = input("whatss ur name:")   #inpur stored in name
print("Hellooo :" + name)

#Exercise 2

string = input(" who is ur Superr Heroo:")
print("that's great : " + string)'''


#===============TYPE CONVERSION=====================
		#int to str, str to int , float..
'''
old_age = input ("enter your age: ")
new_age = int (old_age) + 2           
print(new_age)


number = 18
print (float(18))'''

# sum of 2 numers
'''first = input ("enter first num: ")
second = input("enter second num :")
sum = int(first) + int(second)  #first second take as string so int convert it into int
print("the sum is: " + str(sum))  #here also add str to convert int into  str'''



#===============String=====================

'''name = "Hellooo world"

print(name.upper())   #it convert str to upper case
print(name.lower())

print(name.find('R'))  #it print -1 bcoz capital R is not available in string
print(name.find('d'))

print(name.replace("Hellooo world", "How are youuu"))

#word is exist or not
print('o' in name)  #if 'o' is available in string than print true else false  ('in' is a keyword)
print('z' in name)'''

#===============OPERATORS=====================

'''print(10 + 20)
print(10 * 2)
print(30-10)
print(40/20)  # it print decimal num op=2.0
print(40//20) #it print int num op=2
print(5%2) 
print(2**4)  #2 to the power of 4 (2*2*2*2)'''


#add any num in existed number
 
'''i = 10
#i = i + 2
i += 2   #add 2 in i
print(i)

i -= 5
print(i)

i*= 2
print(i)'''

#===============OPERATORS PRECIDENCE=====================
	#first /, *, + ,-


'''result  = 2+3*5
print(result)'''



#COMPARISON OPERATOR
'''print(5<3)  #op= False
print(4==4) #op = True
print(6>3)	#op = True
print(4 != 3) #op = true'''

#LOGICAL OPERATOR
	#OR
	#1 is true than true or both are false than false
'''print(2 > 3 or 2 > 1)
#AND
#both are true otherwise false
print(3>2 and 2>1)

#NOT
#it give opposite reply;  true take as false and f as t

print( not 3 > 2)'''


#===============IF - ELSE=====================

age = 9

if age >= 18:
	print("you are an adult")
	print("you can vote")      #proper space indentation is needed
print("THANK YOU!!!")#if age <18 than print thanku


if age >= 18:
	print("you are an adult")
elif age<18 and age > 2:
	print("You are in school")
else:
	print("you are a child")


 


