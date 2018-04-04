# -*- coding: utf-8 -*-
import random

Intake=0


def Display(ADCI,RDCI,username):
    final=float((ADCI/RDCI)*100)
    
    if(final< 90):
        print username+", your daily calorie intake is lower than the recommended with "+str(90-final)+"%. This rhythm will make you lose weight, just make sure your meals contain all nutritional value needed. It’s recommended that you do not fall under the healthy weight and that you keep a balanced lifestyle."
    elif ((final>90) and (final<110)):
        print username+", your daily calorie intake is close to the recommended one! You have a balanced healthy lifestyle, well done!"
    elif (final>110):
        print username+", your daily calorie intake is higher than the recommended with "+str(final-110)+"%. This rhythm will make you gain weight which will lead to health concerns. It’s recommended that you either lower your calorie intake, either exercise more! Careful with those temptations!"


def  WeekDetails(username,RDCI):
    global Intake
    for days in range(7):
        print "A: Day "+str(days+1)+": were your meals very unhealthy (1), unhealthy (2), healthy (3), or very healthy (4)?\n Enter the corresponding number."
        corrNo=int(raw_input("U: "))
        if ((corrNo >= 1) or (corrNo <= 4)):
            ran=random.choice([1, 0, 1,0,0])
            if (corrNo==1):
                if (ran==1):
                    Intake=float(Intake)+float((RDCI*150)/100)+float(random.randrange(50, 150, 3))
                    print "A: It also looks like this day you’ve been tempted! Naughty..."
                else:
                    Intake=float(Intake)+float((RDCI*150)/100)
            elif (corrNo==2):
                if (ran==1):
                    Intake=float(Intake)+float((RDCI*120)/100)+float(random.randrange(50, 150, 3))
                    print "A: It also looks like this day you’ve been tempted! Naughty..."
                else:
                    Intake=float(Intake)+float((RDCI*120)/100)
            elif (corrNo==3):
                if (ran==1):
                    Intake=float(Intake)+float(RDCI)+float(random.randrange(50, 150, 3))
                    print "A: It also looks like this day you’ve been tempted! Naughty..."
                else:
                    Intake=float(Intake)+float(RDCI)
            elif (corrNo==4):
                if (ran==1):
                    Intake=float(Intake)+float((RDCI*80)/100)+float(random.randrange(50, 150, 3))
                    print "A: It also looks like this day you’ve been tempted! Naughty..."
                else:
                    Intake=float(Intake)+float((RDCI*80)/100)
            ADCI=float(Intake/7)
            
        else:
            print "Sorry enter only 1 to 4 number,let's start again"
            return WeekDetails(username,RDCI)
    print "A: Thank you "+username+"! I’m computing your results…"
    Display(ADCI,RDCI,username)
    
    
def CalRDCI(gender,username,age,weight,height):
    if gender=="M":
        RDCI=(float(weight)*10 + float(height)*6.25 - float(age)*5 - 5)
        WeekDetails(username,RDCI)
    else:
         RDCI=(float(weight)*10 + float(height)*6.25 - float(age)*5 - 161)
         WeekDetails(username,RDCI)
       

def Height(gender,username,age,weight):
    print "A: What is your height in cm?"
    height=raw_input("U: ")
    if not height:
        return  Height(gender,username,age,weight)
    elif ((float(height)<80) and (float(height)>230)):
        print "A: I’m sorry, I cannot understand. What is your height in cm?"
        height=raw_input("U: ")
        print "A: Thank you for the information "+username+"! Let’s see how healthy your meals were last week. "
        CalRDCI(gender,username,age,weight,height)
    else:
        try:
            int(height)
        except ValueError:
            print "A: I’m sorry, I cannot understand. What is your height in cm?"
            height=raw_input("U: ")
            print "A: Thank you for the information "+username+"! Let’s see how healthy your meals were last week. "
            CalRDCI(gender,username,age,weight,height)
        else:
             print "A: Thank you for the information "+username+"! Let’s see how healthy your meals were last week. "
             CalRDCI(gender,username,age,weight,height)

    
def Weight(gender,username,age):
    print "A: What is your current weight in kg?"
    weight=raw_input("U: ")
    if not weight:
        return Weight(gender,username,age)
    elif ((float(weight)<40) and (float(weight)>150)):
        print "A: I’m sorry, I cannot understand. What is your current weight in kg?"
        weight=raw_input("U: ")
        Height(gender,username,age,weight)
    else:
        try:
            int(weight)
        except ValueError:
            print "A: I’m sorry, I cannot understand. What is your current weight in kg?"
            weight=raw_input("U: ")
            Height(gender,username,age,weight)
        else:
            Height(gender,username,age,weight)


def Age(gender,username):
    print "A: What is your age in years?"
    age=raw_input("U: ")
    if not age:
        return Age(gender,username)
    elif ((float(age)<18) and (float(age)>99)):
        print "A: I’m sorry, I cannot understand. What is your age in years?"
        age=raw_input("U: ")
        Weight(gender,username,age)
    else:
        try:
            int(age)
        except ValueError:
            print "A: I’m sorry, I cannot understand. What is your age in years?"
            age=raw_input("U: ")
            Weight(gender,username,age)
        else:
            Weight(gender,username,age)


def Gender(gender,username):
    if  not gender:
              
        return Permission('Y',username)
    else:
        if (gender == "f" or gender == "F" or gender == "m" or gender == "M"):
            Age(gender,username)
        else:
            print "A: I’m sorry, I cannot understand. What is your gender? Enter M for male or F for female."
            gender=raw_input("U: ")
            return Gender(gender,username)
            
            
def Permission(info,username):
    if info == 'N':
        print "A: That’s alright, good bye "+ username
        
    elif info == 'Y':
            print "A: Great "+ username+", let’s start! What is your gender? Enter M for male or F for female."
            gender=raw_input("U: ")
            Gender(gender,username)
            
    else:
        print "\nA: I’m sorry, I cannot understand. To properly assist you, we will need some personal information such as age, gender, weight and height. Do you want to continue? Enter Y for yes or N for no."
        ConfirmConti=raw_input("U: ")
        return Permission(ConfirmConti,username)
         
                   
def Confirm(username):
    print "\nA: Hi "+ username +"! To properly assist you, we will need some personal information such as age, gender, weight and height. Do you want to continue? Enter Y for yes or N for no."
    info=raw_input("\nU: ")
    if not info:
        return Confirm(username)
    else:
        Permission(info,username)


def TakeName(username):
    if not username:
        print ('A: Don\'t be shy! What is your name?')
        username=raw_input('\nU: ')
        if not username:
            return TakeName("")
        else:
            Confirm(username)
    else:
        Confirm(username)
    
        
def main():
     print ("A: Welcome to the Calorie Intake Assistant, my name is Cal. What is your name?")
     username=raw_input('\nU: ')
     TakeName(username)
    
if __name__== "__main__":
    main()