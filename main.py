       # დავალება #1
# საბანკო ანგარიშის მართვა:
# შექმენით კლასი სახელწოდებით BankAccount, რომელიც წარმოადგენს მარტივ საბანკო ანგარიშს ისეთი ატრიბუტებით, როგორიცაა account_number, holder_name და ბალანსი.
# განახორციელეთ დეპოზიტის, ამოღებისა და ბალანსის შემოწმების მეთოდები. ჩართეთ შეცდომის სათანადო დამუშავება არასწორი ტრანზაქციებისთვის (მაგ., ბალანსზე მეტის ამოღების მცდელობა).


class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = int(balance)
        print(f"{self.holder_name}ს ანგარიშზე საწყის თანხაა: {self.balance} ლარი")

    def Deposite(self, deposited_amount):
        self.deposited_amount = int(deposited_amount)
        self.new_balance_pluse = self.balance + self.deposited_amount
        return f"ბალანსის შევსების შემდეგ თქვენს ანგარიშზე არის: {self.new_balance_pluse} ლარი"

    def Balance_Withdrawing(self, withdraw):
        self.withdraw = int(withdraw)
        if self.withdraw <= self.new_balance_pluse:
            self.new_balance_minus = self.new_balance_pluse - self.withdraw
            return f"თქვენს ანგარიშზე დარჩა: {self.new_balance_minus} ლარი"
        else:
            return f"ანგარიშზე არ არის მოთხოვნილი თანხა"


BankAccount1 = BankAccount("GE08GB65406640464406404", "Tariel", 5000)
deposite = 3000
withdraw = 4000


print(BankAccount1.Deposite(deposite))
print(BankAccount1.Balance_Withdrawing(withdraw))

        # დავალება #2
# ინვენტარის მართვა:
# შექმენით პროდუქტის კლასი ისეთი ატრიბუტებით, როგორიცაა სახელი, ფასი და რაოდენობა. დანერგეთ მეთოდები რაოდენობის განახლებისთვის,
# მიიღეთ მარაგში არსებული პროდუქტების მთლიანი ღირებულება და შეამოწმეთ პროდუქტი მარაგშია თუ არა.


class Inventarisation():
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = int(price)
        self.quantity = int(quantity)

    def full_price(self):
        return f"საწყობში არსებული {self.quantity} ცალი {self.product_name}ს ღირებულებაა - {self.price * self.quantity} ლარი"

    def quantity_change(self, change):
        # change - მიღების დროს არის დადდებითი, გაცემის დროს უარყოფითი
       self.change = int(change)
       new_quantity = self.quantity + self.change

       if new_quantity >= 0:
            return f"{self.change} ცალი  {self.product_name}ს გაყიდვის შემდეგ საწყობში  დარჩა  {new_quantity} ცალი {self.product_name}"
       return f"საწყობში არ არის {self.product_name} მოთხოვნილი რაოდენობა"




product1 = Inventarisation("სკამი", 30, 130)
change = 30
#
print(product1.full_price())
print(product1.quantity_change(change))


#      დავალება #3
# ონლაინ საყიდლების კალათა:
# შექმენით კლასები პროდუქტის, საყიდლების კალათისა და მომხმარებლისთვის, ონლაინ შოპინგის გამოცდილების სიმულაციისთვის.
# დანერგეთ კალათიდან პროდუქტების დამატების/ამოღების, მთლიანი ფასის გამოთვლისა და გამოწერის მეთოდები.


class Shop():
    def __init__(self, product_name, price, quantity):
        # self.purchased_quantity = None
        self.product_name = product_name
        self.price = int(price)
        self.quantity = int(quantity)
        print(f"მაღაზიაში გვაქვს: {quantity} ცალი {product_name}, რომლის საერთო ღირებულებაა {price*quantity} ლარი")

    def bayer(self, purchased_quantity):
        # self.product_name = product_name
        self.purchased_quantity = int(purchased_quantity)
        amount_price = self.price * self.purchased_quantity
        self.quantity = self.quantity - self.purchased_quantity
        if self.quantity >= 0:
            return f"გაყიდული {self.purchased_quantity} {self.product_name}ს ღირებულებაა:  {amount_price} ლარი, \n მაღაზიაში დარჩა {self.quantity} {self.product_name} \n"
        else:
            return f"მაღაზიაში არ არის {self.product_name}-ს მოთხოვნილი რაოდენობა"


product2 = Shop("ტელეფონი", 1200, 25)
product3 =Shop("ტელევიზორი", 1500, 12)
# # shop_product = Shop.bayer("ტელეფონი", 800)
#
# purchased_quantity =  5
# bayer1 = Shop.bayer("ტელეფონი", 5)
print(product2.bayer(3), product3.bayer(1))
print(product2.bayer(10))
print(product3.bayer(12))
