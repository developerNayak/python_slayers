# number_one = 1000000000000000000
# number_two = 1556546535434354454356465
# number_three = 2035432453454524354354564545
# total = number_one + number_two + number_three

# print('the total is ')
# print(total)


# menu = ["1 : Addition" , "2 : Subtraction", "3: Multiplication", "4 : Division "]

# for each_menu_item in menu : 
# 	print(each_menu_item)

# user_input = int(input("enter your choice of operation? Please choose 1 or 2 or 3 or 4 : "))

# number_one = int(input("Please enter your first number : "))

# number_two = int(input("Please enter your second number : "))


# if user_input == 1 :
# 	result = number_one + number_two
# 	print(result)
# elif user_input == 2:
# 	result = number_one - number_two
# 	print(result)
# elif user_input == 3 :
# 	result = number_one * number_two
# 	print(result)
# elif user_input == 4 :
# 	if number_two == 0 :
# 		print("Infinity")
# 	else :
# 		result = number_one / number_two
# 		print(result)
	
# else :
# 	print("enter Please chooose a valid input and run the program again")







# car = input('whats your fav car?')

# print("your fav car is " + car)
# print('***********************************************')
# print("***********************************************")
# print("   Welcome to the Rectangle Area Calculator    ")
# print('***********************************************')
# print('***********************************************')
# length = int(input("please enter the length of the rectangle"))
# width = int(input("please enter the width of the rectangle"))

# area = length * width

# print("The area of the given rectangle is " + str(area))





# triangle area calculator 

# base = int(input("Enter the base of a triangle"))

# height = int(input("Enter the height of the triangle"))


# area = 0.5 * base * height


# print("the Area of the triangle is " + str(area))







# volume of a cone = 3.14 * radius * radius * height



# radius = input("enter the radius")


############################### bmr calculator############################################################ 


# weight = int(input("enter your weight in kgs "))

# height = int(input("enter your height in cms "))

# age = int(input("enter your age "))

# gender = input("Please specify if you are a male or a female? please enter (M/F) ")



# work_activity = [[1,'Light Activity : ' , 'Office worker getting little or no exercise ' , 1.53], [2, 'Moderately Active : ', 'A person running an equivalent of 1 hr daily' ], [3,'Vigorously Active : ', 'A person equivalent to swimming 2 hrs a day']]

# for each_activity in work_activity:
# 	print(str(each_activity[0]) + " " + each_activity[1] + " " + each_activity[2])



# user_activity = int(input("Please enter your level of activity. Please chooose from above (1/2/3) "))




# if gender == 'M' or gender == 'm':
# 	bmr = 10*weight + 6.25*height -5*age +5
# 	if user_activity == 1 :
# 		tee = bmr*1.53
# 	elif user_activity == 2:
# 		tee = bmr*1.76
# 	elif user_activity == 3:
# 		tee = bmr*2.25
# 	else :
# 		print("You entered a wrong activity choice")
# 	print("Your BMR is : " + str(bmr))
# 	print("Your total Energy Expenditure is : " + str(tee))



# elif gender == 'F' or gender == 'f':
# 	bmr = 10*weight + 6.25*height -5*age -161
# 	if user_activity == 1 :
# 		tee = bmr*1.53
# 	elif user_activity == 2:
# 		tee = bmr*1.76
# 	elif user_activity == 3:
# 		tee = bmr*2.25
# 	else :
# 		print("You entered a wrong activity choice")
# 	print("Your BMR is : " + str(bmr))
# 	print("Your total Energy Expenditure is : " + str(tee))


# else:
# 	print("You entered a wrong gender ")



# carbohydrates = [['Sweet Potato ' , 0.2], ['White Rice Basmati ', 0.77], ['Pasta ', 0.72], ['Quinoa', 0.64],['Lentils' , 0.60]]

# protiens = [['Canned Tuna - 3 Ounces', 20 ],  ['Chicken 3 Ounces ', 27 ], ['Kidney Beans (1/3 cup)', 4], ['Peanut Butter 2tbsp' , 7], ['Yogurt 1 cup', 9]]

# fats = [['Chia Seeds ', 8.71],['Avocado', 29], ['Eggs ', 5.3], ['Flax Seeds', 9],['Almond 1 ounces ', 14]]

# # the below is the algorithm to calculate the total cal from different nutrition

# cal_from_carbohydrates = 0.4 * tee / 4        

# cal_from_protiens = 0.3 * tee / 4

# cal_from_fats = 0.3 * tee / 4


# # the below to calculate the total mass required by each nutrition


# gm_of_each_carbohydrates = cal_from_carbohydrates/5

# gm_of_each_protien = cal_from_protiens /5

# gm_of_each_fat = cal_from_fats/5


# custom_meal_plan_decision = input("please enter if you want a meal plan. only (Yes/ No) ")



# if custom_meal_plan_decision == 'yes':

# 	print("*************************CARBOHYDRATES*********************************")
# 	for each_carbs in carbohydrates :
# 		total_mass = gm_of_each_carbohydrates/ each_carbs[1]
# 		print(str(round(total_mass)) + " gms of " + each_carbs[0])

# 	print("*************************Protiens*********************************")
# 	for each_protien in protiens :
# 		total_mass = gm_of_each_carbohydrates/ each_protien[1]
# 		print(str(round(total_mass)) + " gms of " + each_protien[0])

# 	print("*************************Fats*********************************")
# 	for each_fats in fats :
# 		total_mass = gm_of_each_carbohydrates/ each_fats[1]
# 		print(str(round(total_mass)) + " gms of " + each_fats[0])

# else :
# 	print("you can prepare your meal plan later")



# print("Thanks for using my application.. See you next time.........||||||||| have a good Day |||||||||||||||")
# print("Made by sanjeeb Nayak")










# gender = input("enter if you are a boy or a girl")


# if gender == 'boy' :
# 	print("You must be a fan of marvel")
# elif gender == 'girl' :
# 	print("You must love pink color") 
# else :
# 	print("OOPS, Your gender does not exist")



# student_name = input("Please enter your name")

# if student_name == 'ahaan':
# 	print("your are in grade 7 genesis")
# elif student_name == 'ronit':
# 	print("you are a goood friend of ahaan")
# elif student_name == 'vansh':
# 	print("you know how to dance")
# elif student_name == 'krishiv':
# 	print("you are my present youngest student")
# else:
# 	print("i dont know who you are")





#  this is nothing
# print("*************************************************")
# print('***********Welcome to Mini Calculator************')
# print("*************************************************")

#this is just to show the user the option
# print("1 : Addition")
# print("2 : Subtraction")
# print("3 : Multiplication")
# print("4 : Division")



# operation = input("Please enter what do you want to do? Please choose (1 or 2 or 3 or 4)  ")


# number_one = int(input("Enter your first number"))
# number_two = int(input("Enter your second number"))


# if operation == "1":
# 	result = number_one + number_two
# 	print(result)
# elif operation == '2':
# 	result = number_one - number_two
# 	print(result)
# elif operation == '3':
# 	result = number_one * number_two
# 	print(result)
# elif operation == '4':
# 	result = number_one/number_two
# 	print(result)
# else :
# 	print("you entered a wrong option please re run the program")






# user_input = input("enter which shape area do you want to find out  ? rectangle or triangle")

# if user_input == 'rectangle' :
# 	length = int(input("enter the length"))
# 	width = int(input("enter the width"))
# 	area = length * width
# 	print(area)

	
# elif user_input == 'triangle':
# 	base = int(input("enter the base"))
# 	height = int(input("enter the height"))
# 	area = 0.5 * base * height
# 	print(area)

# else :
# 	print("the feature is not available")

# print("THanks for using!!!!!!!!")





# how to calculate the volume of the shape cube cuboid cone sphere

# cube = length * length * length

# cuboid = length * width * height

# cone = 3.14 * radius * radius * height

# sphere = 1.33 * 3.14 * radius * radius * radius


# print("1 : Cube")
# print("2 : Cuboid")
# print("3 : Cone")
# print("4 : Sphere")



# shape = input("enter the 3D shape whose volume you want to calculate  ")

# if shape == '1':
# 	length = int(input("Please enter the length of the cube  "))
# 	volume = length * length * length
# 	print("The volume of the Cube is " + str(volume))

# elif shape == '2':
# 	length = int(input("Please enter the length of the cuboid  "))
# 	width = int(input("Please enter the width of the cuboid  "))
# 	height = int(input("Please enter the height of the cuboid  "))
# 	volume = length * width * height
# 	print("The volume of the Cuboid is " + str(volume))


# elif shape == '3':
# 	radius = int(input("Please enter the radius of the cone  "))
# 	height = int(input("Please enter the height of the cone  "))
# 	volume = 3.14 * radius * radius * height/3
# 	print("The volume of the Cone is " + str(volume))

# elif shape == '4':
# 	radius = int(input("Please enter the radius of the sphere  "))
# 	volume = 1.33 * 3.14 * radius * radius * radius
# 	print("The volume of the Sphere is " + str(volume))

# else : 
# 	print("the input which you enter is not available yet.... Please try again later ")

# print("Thanks for using this application . Hope to see you again soon ")






# month = input("enter the month whose holiday you want to know ")


# if month == 'january':
# 	print("26 Jan : Republic Day")
# elif month == 'february':
# 	print("21 feb : Maha Shivaratri")
# elif month == 'march':
# 	print("10 mar : Holi")
# elif month == 'april':
# 	print("02 apr : Ram Navami")
# 	print("06 apr : Mahavir Jayanti")
# 	print("10 apr : Good Friday")
# 	print("14 apr : Dr. Babasaheb Ambedkar Jayanti")
# elif month == 'may':
# 	print("1")

# else :
# 	print("the month does not exist")


# print("thansks for using this calender")



# in conditional statement or and 


# name = input("enter your name ")

# if name == 'krishiv' or name == 'Krishiv' or name == 'KRISHIV':
# 	print("Krishiv lives in Surat")
# elif name == 'ahaan' or name == 'Ahaan' or name == 'AHAAN':
# 	print("Ahaan lives in Noida")
# else:
# 	print("The name is unknown")



# # mini authentication

# username_registration = input("Enter your username ")
# password_registration = input("Enter your password ")


# user_login = input("Please enter your username to login ")
# pass_login = input("Please enter your password to login ")


# if user_login == username_registration and pass_login == password_registration:
# 	print("Your are logged in ")
# 	print("Welcome to the application. Soon we will have lots of features")
# else:
# 	if user_login != username_registration:
# 		print("your entered a wrong username")
# 	elif pass_login != password_registration:
# 		print("you entered a wrong password")




# player1_name = input("enter player 1 name ")
# player2_name = input("enter player 2 name ")


# player1_choice = input("enter rock, paper or scissors  player 1 ")
# player2_choice = input("enter rock, paper or scissors player 2 ")


# if player1_choice == player2_choice :
# 	print("both of your choose same. ")
# 	print("game tied")

# elif player1_choice == 'rock':      
# 	if player2_choice == 'paper':            
# 		print(player2_name + " Wins")
# 	elif player2_choice == 'scissors':
# 		print(player1_name + " Wins")


# elif player1_choice == 'paper':
# 	if player2_choice == 'rock':
# 		print(player1_name + " Wins")
# 	elif player2_choice == 'scissors':
# 		print(player2_name + " Wins")


# elif player1_choice == 'scissors':
# 	if player2_choice == 'rock':
# 		print(player1_name + " Wins")
# 	elif player2_choice == 'paper':
# 		print(player2_name + " Wins")



############################################################################
#      				List practice python slayers                           #
############################################################################



# make a list of months

# structure = ['Name' , 'Address' , 'Age', 'Grade' , 'Color' , ' Sports' , 'Personality']

# krishiv = ['Krishiv Singh', 'Eldeco utopia', 12, 7, 'red', 'tennis', 'a warm hearted person loves his gaming headphones']


# vansh = ['Vansh Arora', 'Sector 50', 12 , 7, 'white', 'dance', 'youtuber and gamer']


# ronit = ['Ronit Gupta', 'Sector 46', 11, 7, 'blue', 'football', 'ronit is friendly']



# print("1: Name")
# print("2: Address")
# print("3: age")
# print("4: grade")
# print("5: color")
# print("6: sports")
# print("7: personality")


# name = input("enter the name of the person ronit, vansh or krishiv ")
# option = int(input("enter what you want to know about "))

# list_index = option -1

# if name == 'krishiv'  or name == 'Krishiv' or name == 'KRISHIV':
# 	print(structure[list_index] +"  : " + krishiv[list_index])

# elif name == 'vansh'  or name == 'Vansh' or name == 'VANSH':
# 	print(structure[list_index] +"  : " + vansh[list_index])

# elif name == 'ronit'  or name == 'Ronit' or name == 'RONIT':
# 	print(structure[list_index] +"  : " + ronit[list_index])

# else :
# 	print("Name doesn't exist")


# print("Krishiv  : " + str(krishiv[list_index]))
# print("Vansh  : " + str(vansh[list_index]))
# print("Ronit  : " + str(ronit[list_index]))





# dry : Don't repeat yourself

# wet : write every time





#make a list of festivals of the month

# input from the user about which month 

# display all the festival of the month using tracing the list


# for each_number in range(1,10):
# 	print(each_number)



#####################################################
#        printing the table of 15
#####################################################



# for each_number in range(1,11):
# 	print("17 " + " * " +  str(each_number) + " = " + str(17*each_number))



# number = int(input("enter the number whose table you would like to seee "))


# for each_number in range(1,11):
# 	print(str(number) + " * " + str(each_number) + " = " + str(number*each_number))

  

#############################################################
#                   Even and odd number                     #
#############################################################




# number = int(input("Till what number do you want to find the even number "))




# for each_number in range(1,number+1):
# 	if each_number%2 == 0 :
# 		print(each_number)





# number = int(input("enter the number whose multiples you want to be printed "))
# last_number = int(input("enter the number you want to see the multiples till "))


# for each_number in range(1, last_number+1):
# 	if each_number%number == 0:
# 		print(each_number)


# monday = ['Science', 'Maths', 'Library/Reading', 'French/German/Spanish/Hindi','Design']


# tuesday = ['Individual & Socities', 'French/German/Spanish/Hindi','Physical Health Education', 'Science','Math']


# wednesday = ['Literature and English Second Language', 'Service as action', 'Dance', 'First Language English/ English Second Language','Music']


# thrusday = ['Design', 'Club', 'Visual Arts', 'Literature & English', 'First Language English/English Second Language']


# friday = ['Individual & Socities', 'Physical Health Education', 'French/German/Spanish/Hindi', 'Math', 'Science']



# status = 'yes'

# while (status == 'yes'):
# 	day = input("enter which days time table you want to see ")
# 	if day == 'monday':
# 		for each_session in monday:
# 			print(each_session)

# 	elif day == 'tuesday':
# 		for each_session in tuesday:
# 			print(each_session)


# 	elif day == 'wednesday':
# 		for each_session in wednesday:
# 			print(each_session)


# 	elif day == 'thrusday':
# 		for each_session in thrusday:
# 			print(each_session)


# 	elif day == 'friday':
# 		for each_session in friday:
# 			print(each_session)

# 	elif  day == 'saturday' or day == 'sunday':
# 		print("Its a holiday today !!!!!!!!!!")

# 	else :
# 		print("the day doesnot exist")
# 	status = input('enter yes if you want to repeat and end if you want to end')


# print("Thanks for visiting the timetable !!! See you soon ")






############################################################
#                       Hcf and Lcm                        #
############################################################


# number_one = int(input('enter the first number'))

# number_two = int(input("enter the second number "))

# hcf = 1
# lcm = number_one*number_two

# # for each_number in range(1, number_one*number_two):
# # 	if number_one % each_number == 0 and number_two % each_number == 0 :
# # 		print(each_number)
# # 		hcf = each_number

# # print("the highest common factor is " + str(hcf))


# for each_number in range(1,number_one*number_two):
# 	if each_number % number_one == 0 and each_number % number_two == 0 :
# 		print("the lcm of the two numbers are  " + str(each_number))
# 		break






# name , class, school

# Your name is sanjeeb and you are in grade 6 and you study in genesis global school


# all the common multiples of two number between 3000 and 4000

# number_lower_input = int(input("asjg"))
# number_upper_input = int(input("asjg"))


# number_one = int(input("asjg"))
# number_two = int(input("asjg"))

# for each_number in range(number_lower_input,number_upper_input):
# 	if each_number%number_one ==0 and each_number % number_two== 0 :
# 		print(each_number)
	



##########################################################################
#              how to find out percentages of the students               #
##########################################################################



subjects = [ 'maths ', 'science ', 'Individual and Socities ', 'English ']

student_one = []

student_two = []

student_three = []


student_one_name = input("enter the name of the student ")

for each_subject in subjects:
	score = int(input("enter the score scored in " + each_subject))
	student_one.append(score)


student_two_name = input("enter the name of the student ")

for each_subject in subjects:
	score = int(input("enter the score scored in " + each_subject))
	student_two.append(score)


student_three_name = input("enter the name of the student ")

for each_subject in subjects:
	score = int(input("enter the score scored in " + each_subject))
	student_three.append(score)

# this is student 1
print("#########################")
print(student_one_name)
print("#########################")
total = 0
for each_score in student_one:
	total = total + each_score
	percentage = total/400 *100

for each_item in range(0,4):
	print(subjects[each_item] + " : " + str(student_one[each_item]))

print("Percentage Scored " + " : " + str(percentage) + " %")


# this is student 2
print("#########################")
print(student_two_name)
print("#########################")
total = 0
for each_score in student_two:
	total = total + each_score
	percentage = total/400 *100

for each_item in range(0,4):
	print(subjects[each_item] + " : " + str(student_two[each_item]))

print(student_two_name + " : " + str(percentage) + " %")


# this is student 3
print("#########################")
print(student_three_name)
print("#########################")
total =0
for each_score in student_three:
	total = total + each_score
	percentage = total/400 *100


for each_item in range(0,4):
	print(subjects[each_item] + " : " + str(student_three[each_item]))

print(student_three_name + " : " + str(percentage) + " %")






####################################################################################
#                       how to use list                                            #
####################################################################################


# list_architecture = ['name ', 'address ', ' age ', 'fav food ']

# krishiv = ['krishiv', 'surat', '10', 'pizza and milk ' ]

# ahaan = ['ahaan', ' noida', ' 11', ' sphagetti and pancakes ']




# print('###################################################')
# print("              " + krishiv[0])
# print("###################################################")

# print("you live in " + krishiv[1])
# print("your age is " + krishiv[2])
# print("your fav food is " + krishiv[3])


# print('###################################################')
# print("              " + ahaan[0])
# print("###################################################")

# print("you live in " + ahaan[1])
# print("your age is " + ahaan[2])
# print("your fav food is " + ahaan[3])


#############################################################################
# finding the smallest number in a list
#########################################################################

# print("Hi, i can help you in finding the smallest number  ")


# numbers = int(input("enter how many number you want to input "))

# input_numbers = []

# for each_number in range(numbers):
# 	number = int(input("enter the number "))
# 	input_numbers.append(number)

# # print(input_numbers)

# smallest = input_numbers[0]

# for each_number in input_numbers:
# 	if smallest > each_number:
# 		smallest = each_number

# print("the smallest number you have entered is " + str(smallest))






















































































































































