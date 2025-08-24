
#*************************< التفكير المنطقي لبناء كود اللعبة >********************************

#1) لقد استدعيت دالة الاختيار العشوائي 
#2) لقد عملت قائمة ووضعت فيها ثلاثة اختيارات للعبة الشهيرة
# 2)    لقد عملت ثلاثة متغيرات وخزنت في كل واحد منهم شكل يمثل الاسم اللي بقائمة اللعبة
#3) لقد كتبت رسالة ترحيبية للعبة الشهيرة
#4) سوال يطلب من المستخدم اختيار مساعدة لاضهار قواعد اللعبة او يضغط انتر لكي يستمر
#5) قواعد اللعبة
#6) يضهر هاذا السوال للمستخدم اذا طلب مساعده او اذا ضغط انتر للاستمرار في اللعب
# 7) لقد عملت متقير وخزنت فيه ما الاختيار العشوائي للكمبيوتر
# 8) لقد عملت تحقق شرطي لاضهار الشكل الرسومي بدلن من الكلمة التي اختارها المستخدم من القائمة
# 9) وهاذا التحقق الشرطي لقد عملته للكمبيوتر بدلاّّ من ان يتم طباعة الكلمة التي اختارها يقوم بطياعة الشكل الرسومي    
#10) الاهم | لقد عملت تحقق شرطي بين اختيار الكمبيوتر واختيار المستخدم لاضهار من هو الفائز منهم 

#*******************************< الكود . البرنامج >*******************************

import random


nump=["Rock","Paper","Scissors"]

    
    #********************************************
shcl1="""
       _______
  ---'    ____)______
             ________)
               ________)
              _______)
  ---.____________)
"""

shcl2="""
       __
      |--|_ _ _
  ---'  _______)
         _______)
         _______)
        _______)
  ---.________)
"""

shcl3="""
     _ _ __
----'   ____)_ _ ___
          _ __ _ _ __)
          _ _ _ _ _ ___)
        (_ __ _)
---.___(_ __ _)
"""


    #*************************************
    

print("Welcome to the Rock, Paper, Scissors game:")


name=input("Press Enter to continue or type (Help) for the rules:").capitalize()


if name=='Help':
    print("""
          *********** RULES ************
          1) You choose and the computer chooses
          2) Rock smashes Scissors --> Rock wins
          3) Scissors cut Paper --> Scissors win
          4) Paper covers Rock --> Paper wins
          """)
    
    
else:
    print()

entr=input("Enter your choice (rock, paper, scissors): ").capitalize()    



clo=random.choice(nump)

print()

#***************شرط التحقق واضهار الاشكال الرسومية ******************

if entr in nump:
    print("You chose:")
    print()
    if entr=="Rock":
        print(shcl2)
    elif entr=="Paper":
        print(shcl1)
    else:
        print(shcl3)
        
    print()
    

    print("Commputer chose:")
    print()
    if clo=="Rock":
        print(shcl2)
    elif clo=="Paper":
        print(shcl1)
    else:
        print(shcl3)
        
    print()
    
    #***************شرط لاضهار نتيجة اللعبة******************|
   
    if entr==clo:
        print("It's a tie! =")
    
    elif entr=="Paper" and clo=="Rock":
        print(f"Tou Won,😍 {clo} Stronger than {entr}")
        
    elif entr =="Rock" and clo=="Scissors":
        print(f"Tou Won,😍 {clo} Stronger than {entr}")
        
    elif entr =="Scissors" and clo=="Paper":
        print(f"Tou Won,😍 {clo} Stronger than {entr}")
    
    
    else:
        print(f"You, lese! {clo} beats {entr}")
    
else:
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
    
    
    

