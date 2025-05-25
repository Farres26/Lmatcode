print("Welcome to the laundromat.\n Please input your last name.")
#The users last name
user = input()
        
Choice1 = 0
#The function below prints a divider so the user doesn't get confused 
def split():
    '''This spits up the code this runs after every use of the program
    '''
    print('------------------------------------------------------')

#A thank you message that prints whenever the program gets done running or doing something
def thank():
    '''This is a thank you message to show the user how much their supports means to the program this runs after every use of the program
    '''
    print('The program ran successfully, thank you for using', user)

# The function below prints an error statement 
def error():
     print('Invalid input. Please unput a proper value.')
     
#I use a while statement with != 4 which means that is the user does not input 4 as their option that program would loop
while Choice1 !=4:
    split()
    
    print("please select from on of the opitions below.\n")

    print('1. calculate the total')
    print('2. change price per pound')
    print('3. customer information')
    print('4. Quit')

#This is the variables for tax rate and price per pound 
    price_per_pound = .50
    tax = .6 

    
    print("\nPlease input a number that goes with the option you want to choose(1 2 3 4):")

    Choice1 = int(input()) # What option the owner picks

#This is the dictionary for the user data and t is the variable for total
    userdict = {"N": 'Farres', "S": 23.00} #dictionary that holds the user's data (I use N for name of user and S for the amount user spent)
    
# This if statement starts with caculate the total and I do this by having the user input a variable as a float which makes it so they can use a decimal.
#Then the the weight varable is multiplied by the tax rate and price per pound and then I printed out the taxed and untaxed amount. 
    if Choice1 == 1:
        print('You choose option 1: calculate the total.')
        print('Please input the amount of pounds you have to wash today:')
        weight = float(input()) #user inputs the amount they plan to wash 
        total = weight * price_per_pound
        totalwithtax = total + tax
        print('The input was', weight, 'pound(s) of clothes.')
        print('Your total will be $', total ,'plus tax', tax ,'= $', totalwithtax)
        thank()
        split()
    #This option is for them t0 change price per pound by allowing them to pick from three options (I used \n to make spaces between the options because I wanted to save space in the if statement.
    elif Choice1 == 2: #If user pick two it allows them to change price per pound
        print('You choose option 2: Change price per pound.')
        print('Please input the number that goes with the option you want to change.\n1. Price pre pound\n2. Tax rate\n3.Both')
        changeuserwantmade = int(input()) #user option on what they want to update
        #This option is if they want to only change price per pound and I use a float variable again because they could use a decimal point.
        if changeuserwantmade == 1: 
            print('Price per pound.')
            print('The price per pound is currently', price_per_pound)
            print('What would you want the new price per pound to be?(Note that anything after a decimal is considered cents.)')
            price_per_pound = float(input())
            print('The new price per pound is', price_per_pound)
            thank()
            split()
        #This option is if they want to change Tax rate there. Percentage tax rate is the tax rate as a whole number inorder to make it look better for the user.
            #Then we have the user to input the new tax rate as ntax (new tax). I told the user to put it in as a whole number because it would be simple for them.
            #I divide it by 10 and then make it the new tax rate.
        elif changeuserwantmade == 2: 
            print('Tax rate.')
            percentagetax = tax *10#coverts the tax into a whole number
            print('The tax rate is currently',percentagetax,'%')
            print('What percentage would you want to change the tax rate to?(please input the number without a percentage. EX: 4)')
            ntax = int(input())
            tax = ntax / 10
            percentagetax = tax *10
            print('The tax is now',percentagetax,'%')
            thank()
            split()
            #This is if the user wants to change both tax rate and price per pound. It is the same as the other two codes just put together.
        elif changeuserwantmade == 3: 
            print('Both price per pound and tax rate.')
            print('We will first start with price per pound. Which is',price_per_pound)
            print('What would you like the new price per pound to be? (Note that anything after a decimal is considered cents.)')
            price_per_pound = float(input())
            print('Now the price per pound is',price_per_pound)
            print('Now on to the tax rate.')
            percentagetax = tax *10 #coverts the tax into a whole number
            print('The tax rate is currently',percentagetax,'%')
            print('What percentage would you want to change the tax rate to?(please input the number without a percentage. EX: 4)')
            ntax = int(input())
            tax = ntax / 10
            percentagetax = tax *10
            print('The tax is now',percentagetax,'%')
            print('The new price per pound is', price_per_pound,'and tax rate is',percentagetax,'%')
            thank()
            split()
        else: #error message -------------------------
            error()
            split()
    
    #Option three holds an if staement that holds one option for the user to print the top customers and the other for owner to input a new customer.
    elif Choice1 == 3: 
        print('You choose option 3: Customer information.')
        print('1. List of customers. ')
        print('2. Input new customer. ')
        print('input number that goes with option you want.(EX: 1)')
        option2 = int(input()) #Allows user to imput option they want
        if option2 == 1: #Option 1 prints top five customers 
            print('Option 1: List of customers.')
            for key in userdict:
                split()
                print(f' Customer: {userdict["N"]} spent ${userdict["S"]} in total.')
            #I have a print line with --- inorder to divide the list
            
        elif option2 == 2: #This is option two input new customer
            print('Please input the last name and last four numbers of customer')
            user = input() #Where user inputs the variable (EX: lastname1234)
            if user in userdict:#The user already exist
                userdict[name1] += round(total,2)
                print(f'Customer {userdict["N"]} has been updated, Total now is ${userdict["S"]}')
                thank()
                split()
            else: #adds the user
                userdict["N"] = userdict["S"] 
                print(f'New customer {userdict["N"]} has been added')
                thank()
                split()
                
        else:
             error()
             split()
             
      #This is the quit statements and how this works is because I used a while statement that was !=4 which means if it is not equal to 4 it will loop but if it is the program will end.      
    elif Choice1 == 4: #If user pick four the program ends
        print('You choose option 4: Quit.')
        thank()
        split()
     #Error statement   
    else:
        error()
        split()