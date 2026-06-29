#     Name
name =input("Enter Your Name :").strip().capitalize()
print(f"Welcome to Samreen Company, {name} . Please fill out the form to apply for a job.")
print ("#"*50)

#     The Form
First_question =input("Does the student have a command of Python? (y / n)").strip().lower()

while True :
    try:
        Another_question =float(input("How many years of experience do you have?"))
        break
    except ValueError:
        print("Please enter valid numbers.")

while True :
    try:
        Question_Three =float(input("How many projects do you have?"))
        break
    except ValueError:
        print("Please enter valid numbers.")

The_final_question =input("Does he have a university degree in computing or has he completed an intensive bootcamp? (y / n)").strip().lower()

if (First_question == "y") and (The_final_question == "y") :
    print("Congratulations! You have been accepted for the next stage of interviews.")

elif (First_question == "y") and (Another_question >= 2 or Question_Three >= 2):
    print("Congratulations! You have been accepted for the next stage of interviews.")
else:
    print("Sorry, your current qualifications do not match the job requirements.")



