class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        # def __repr__(self):
        #     return f"First Name - {self.first_name} Last Name - {self.last_name} Email - {self.email} Age - {self.age} Rewards Member - {self.is_rewards_member} Points - {self.gold_card_points}"
        print(f"First Name - {self.first_name}")
        print(f"Last Name - {self.last_name}")
        print(f"Email - {self.email}")
        print(f"Age - {self.age}")
        print(f"Rewards Member - {self.is_rewards_member}")
        print(f"Points - {self.gold_card_points}")
        

    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            print("User is has been enrolled!")
        else:
            print("User is already enrolled!")
        
        self.gold_card_points = 200


    def spend_points(self, amount):
        self.gold_card_points -= amount
        if self.gold_card_points < 0:
            self.gold_card_points = 0
            print ("Insufficent funds, please try again later")
        print(self.gold_card_points)






user_eric = User("Eric","Liu","eric.liu82794@gmail.com", 28)
user_john = User("John","Jacob","johnjacobjingle@gmail.com", 18)
user_tony = User("Tony", "Stark", "tonystarkisthegreatestavenger.gmail.com", 45)

user_eric.spend_points(50)
user_john.enroll()
user_john.enroll()
user_eric.display_info()
user_john.display_info()
user_tony.display_info()
user_tony.spend_points(40)