# saas_subscription_system.py
#OOPS topics involved:
#This program uses Inheritance (FreePlan, ProPlan, EnterprisePlan inherit from Subscription) and Polymorphism (same calculate_price() method behaves differently for each plan).

class Subscription:
    def __init__(self, user_name, base_price):
        self.user_name = user_name
        self.base_price = base_price

    def calculate_price(self):
        raise NotImplementedError


class FreePlan(Subscription):
    def calculate_price(self):
        return 0


class ProPlan(Subscription):
    def calculate_price(self):
        gst = self.base_price * 0.18
        return self.base_price + gst


class EnterprisePlan(Subscription):
    def __init__(self, user_name, base_price, support_fee):
        super().__init__(user_name, base_price)
        self.support_fee = support_fee

    def calculate_price(self):
        gst = self.base_price * 0.18
        return self.base_price + gst + self.support_fee


# Main
print("---- SaaS Subscription System ----")
print("1. Free Plan")
print("2. Pro Plan")
print("3. Enterprise Plan")

choice = input("Choose plan: ")
name = input("Enter user name: ")

if choice == "1":
    plan = FreePlan(name, 0)
elif choice == "2":
    price = float(input("Enter base price: "))
    plan = ProPlan(name, price)
elif choice == "3":
    price = float(input("Enter base price: "))
    support = float(input("Enter support fee: "))
    plan = EnterprisePlan(name, price, support)
else:
    print("Invalid choice")
    exit()

print("Final Subscription Price:", plan.calculate_price())
