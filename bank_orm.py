import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class Customer(Base):   
    __tablename__ ="customer"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    bankaccount = Column(Integer)
    supply = Column(Integer)

    def __init__(self,**kwargs ):
        self.engine = create_engine('sqlite:///bank.db', echo=True)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        
        
    def insert_table(self,id_field,name_field,last_name_field,bank_account_field,supply_field):
        # i=0
        Base.metadata.create_all(self.engine)
        customers = self.session.query(Customer).all()
        for customer in customers:
            if id_field == customer.id:
                return False
        customer1=Customer(id=id_field,firstname=name_field,lastname=last_name_field,bankaccount=bank_account_field,supply=supply_field)
        self.session.add(customer1)
        self.session.commit()
        return True
        
    def open_search(self,id_search):
        intended_supply = self.session.query(Customer.supply).filter(Customer.id == id_search)
        for row in intended_supply: 
            if row != 0:
                return intended_supply
            else:
                return False
        
    def add_sheets(self,intended_data,id_search,sheet):
        for row in intended_data:
            select_row=list(row)
            sheet+=select_row[0]
            self.session.query(Customer).filter(Customer.id == id_search).update({Customer.supply: sheet})
            self.session.commit()

    def sub_sheets(self,intended_data,id_search,sheet):
        for row in intended_data:
            select_row=list(row)
            select_row[0]-=sheet
            if select_row[0]>0 :
                self.session.query(Customer).filter(Customer.id == id_search).update({Customer.supply: select_row[0]})
                self.session.commit()
                return True
            else:
                return False

    def withdraw(self,id_search):
        if self.session.query(Customer).filter(Customer.id == id_search).delete():
            self.session.commit()
            return True
        else:
            return False

    def show(self):
        list_user=[]
        all_list_user=[]
        data=self.session.query(Customer).all()

        for row in data:
            list_user.append(row.id)
            list_user.append(row.firstname)
            list_user.append(row.lastname)
            list_user.append(row.bankaccount)
            list_user.append(row.supply)
        all_list_user.append(list_user)
        return all_list_user