# declaring or creating new class
# title
class User:
    # defining & initializing the constructor syntax+("self", attributes)
    def __init__(self, fname, lname, email, age):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.age = age
        # default attributes we dont get them from the user we intiate them here
        self.is_rewards_member = False
        self.gold_card_points = 0

    # after the constructor we go with methods 
    def display_info(self):
        print("First name: "+self.first_name)
        print("Last name: "+self.last_name)
        print("Email adress: "+self.email)
        print("Age: "+str(self.age))
        if self.is_rewards_member:
            print("He is good user and his total gold card points is", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("This member is already enrolled!!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient balance!")
        else:
            self.gold_card_points -= amount

# creating a new instance
acc1 = User("sedik", "tlich", "tedik@com", 25)
# displaying his info
# acc1.display_info()
# enroll
acc1.enroll()
acc1.spend_points(50)

# redisplay for test
# acc1.display_info()

# creating more intances
acc2 = User("sof", "naj", "sofnaj@com", 28)
acc2.enroll()
acc2.spend_points(80)

acc3 = User("dhia", "abdel", "mouola@com", 30)

acc1.display_info()
acc2.display_info()
acc3.display_info()

# Bonus logical tests
acc1.enroll()
acc3.spend_points(40)