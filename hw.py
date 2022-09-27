from datetime import datetime as dt
from abc import ABC, abstractmethod

class User():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on = dt.utcnow()
    
    def edit_f_name():
        pass
    def edit_l_name():
        pass

    @property
    #def full_name(self):
        #return self.first_name + " " + self.last_name
    
    def __str__(self):
        return f"<User | {self.full_name}"
    def __repr__(self):
        return f"<User | {self.last_name} {self.created_on.strftime('%c')}>"
    def __hash__(self):
        return hash(self.full_name + self.created_on.strftime("%c"))
    def __eq__(self, __o):
        return self.email == __o.email



class Employee(User):
    def __init__(self, department, security_level, first_name, last_name, email, home_address): #employ_id
        super().__init__(self, first_name, last_name, email)
        self.department = department
        self.security_level = security_level
        #self.employ_id = employ_id
        self.home_address = home_address
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def employ_id(self):
        return self.full_name + self.department 
    
    def edit_dept():
        pass
   
        

class Customer(User):
    def __init__(self, first_name, last_name, email, shipping_address, billing_address, purchase_history):
        super().__init__(self, first_name, last_name, email)

        self.shipping_address = shipping_address
        self.billing_address = billing_address 
        self.purchase_history = purchase_history

    def cust_id(self):
        return self.email + self.shipping_address

    def edit_billing():
        pass

    def edit_shipping():
        pass
    

matt = Customer(first_name="bob", last_name="steve", email="mj@gmail.com",shipping_address="123 street street", billing_address="123 feefefe",purchase_history=["water","strawberries","ice cream"])

