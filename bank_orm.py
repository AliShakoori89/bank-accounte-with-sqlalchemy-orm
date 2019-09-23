import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

global i
i=0
Base = declarative_base()
engine = create_engine('sqlite:///bank.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
class Customer(Base):
    __tablename__ ="customer"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    bankaccount = Column(Integer)
    supply = Column(Integer,nullable=False)
    # def __init__(self,id,firstname,lastname,bankaccount,supply):
    #     self.id=id
    #     self.firstname=firstname
    #     self.lastname=lastname
    #     self.bankaccount=bankaccount
    #     self.supply=supply


    def insert_table(self,data_list,id_field):
        global i
        
        customers = session.query(Customer).all()
        for customer in customers:
            # print(f'{customer.id} was released on {customer.firstname}')
            if id_field == customer.id:
                return False
            
        Base.metadata.create_all(engine)
        customer1=Customer(id=data_list[i],firstname=data_list[i+1],lastname=data_list[i+2],bankaccount=data_list[i+3],supply=data_list[i+4])
        session.add(customer1)
        session.commit()
        return True
        
    
    def open_search(self,id_search):
        customers = session.query(Customer).all()
        for customer in customers:
            if id_search == customer.id:
                return customer.id
    
    def add_sheets(self,intended_data,id_search,sheet):
        l=list(intended_data)
        new_suply=l[0]+sheet
        customer=session.query(Customer).filter(id==id_search).first()
        print(customer.fetchall())


        
