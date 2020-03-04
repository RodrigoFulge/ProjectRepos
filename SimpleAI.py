username = input('Introduce your name: ')
print( f'Greetings, {username}')
s_age = input('Age:')
age = int(s_age)
s_height  = input('Height:')
height = float(s_height)
print(f'So you are {age} years old and {height}m tall, interesting to say the least.')

print("I shall ask for some data, however, answering is not mandatory.")


You_gender=input('Your gender is... (m or f)?')
if You_gender == 'm':
        gender = ('Male')
        print("A male you are then")
        
if You_gender == 'f':
        gender = ('Female')
        print("A female you are then")
        
if (gender != "Male" and gender != "Female"):
        print("Interesting one I see")
    
answer=input("Can I have your E-mail Adress?(y/n)")
if answer=="y":
 
    You_email=input('¿What is your E-mail?')
    email=You_email
else: 
    email = ("")

answer=input( 'My I have your phone number? (y/n)')
if answer=='y':
	phone_number = input( 'Phone number:' )
else:
    phone_number = ("")
answer = input('Finally, I shall proceed to ask for your bank account details. May I have those? (y/n)')
if answer== 'y':
		bank_account=input( 'Account number:')
else:
    bank_account = ("")		
    
    
print('So well, the gathered information was:')
print(f"Name: {username}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Gender: {gender}")
print(f"E-Mail address: {email}")
print(f"Phone Number: {phone_number}")
print(f"Bank Account Number: {bank_account}")




