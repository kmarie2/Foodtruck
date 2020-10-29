def customer():
    print("Welcome to my food truck! I hope you are very hungry!")
    name=input("What is your name, customer?")
    print("Happy to serve you today",name)
def order():
    print("I exclusively serve 3 food items; that may be a very small menu, but these items continue to attract and please all of my customers, so why add extra stuff, huh?")
    print("My three items are fish tacos, chicken stir-fry, and my famous curry that comes in different spices of your choice! Also, you get a free cookie for each meal, my way of thanks for coming to my food truck!")
    print("Ready to order? How many of each item do you want? You can say 0 if you don't want anything of something.")
def fishtacos():
    fish=int(input("Do you have a taste for some fish tacos? How many of each item do you want?"))
    if fish == 0:
             print("Don't have a taste for that, huh?")
    elif fish > 0:
             print("Fintastique! Since you ordered that much, I will give you the same number in cookies!")
             for arrow in range (fish):
                 print("Here's a cookie!")
def stirfry():
    fry=int(input("Do you want the chicken stirfry? How many of each item do you want?"))
    if fry == 0:
            print("Don't have a taste for that, huh?")
    elif fry > 0:
            print("Cool! Don't let your chicken friends see you eat that though...chicken stirfry is amazing. Since you ordered that much, I will give you the same number in cookies!")
            for arrow in range (fry):
                print("Here's a cookie!")
def curry():
    famous=int(input("Do you want to try my famous curry? How many of each item do you want?"))
    if famous == 0:
               print("Don't have a taste for that, huh?")
    elif famous > 0:
               print("Beautiful!")
               spice=input("What is your spice level? Mild? Medium? Spicy?")
               print("Nice. Keep on and curry on, that's my philosophy. Since you ordered that much, I will give you the same number in cookies!")
               for arrow in range (famous):
                   print("Here's a cookie!")
def total():
    num=input("Hey,I lost count of how much you have ordered.Numbers are not my thing sometimes. Can you tell me the total of food items you ordered?")
    print("Okay.Sorry about that.You have ordered",num,"items!")
    print("Thank you for visiting my food truck, I hope you enjoy the food. Have a nice day!")
def main():
    customer()
    order()
    fishtacos()
    stirfry()
    curry()
    total()
main()
