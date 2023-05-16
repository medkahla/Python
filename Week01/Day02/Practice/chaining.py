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
            print("He is good member and his total gold card points is", self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("This member is already enrolled!!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient balance!")
        else:
            self.gold_card_points -= amount
        return self


acc1 = User("sedik", "tlich", "tedik@com", 25)
acc2 = User("sof", "naj", "sofnaj@com", 28)
acc3 = User("dhia", "abdel", "mouola@com", 30)
acc1.enroll().spend_points(50).display_info().enroll()
acc2.enroll().spend_points(80).display_info()
acc3.display_info().spend_points(40)