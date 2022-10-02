import mysql.connector as my

class emp:
	
	con=my.connect(host='localhost',port='3306',user='root',passwd='1234',database='employee')
	print("connection sucessful")
	mycursor=con.cursor()
	query='create table if not exists employe(Eid int(20) primary key,Ename varchar(200),salery int(20),address varchar(20))'
	mycursor.execute(query)
	print("table created")	


	#insert coding
	def insert(self,Eid,Ename,salery,address):

		query="insert into employe(Eid,Ename,salery,address) values({},'{}',{},'{}')".format(Eid,Ename,salery,address)
		mycursor=self.con.cursor()
		mycursor.execute(query)
		self.con.commit()
		print('insertion sucessful')

	#fetching data

	def fetch_all(self):
		query="select * from employe"
		mycursor=self.con.cursor()
		mycursor.execute(query)
		for i in mycursor:
			print("Eid:",i[0])
			print("Ename:",i[1])
			print("salery:",i[2])
			print("address:",i[3])
			print()
			print()
		
	def delete(self,Eid):

		query="delete from employe where Eid={}".format(Eid)
		mycursor=self.con.cursor()
		mycursor.execute(query)
		self.con.commit()
		print("deleted ")

	def update(self,Eid,newname,newsalery,newaddress):

		query="update employe set Ename='{}',salery={},address='{}' where Eid={}".format(newname,newsalery,newaddress,Eid)
		#print(query)
		mycursor=self.con.cursor()
		mycursor.execute(query)
		self.con.commit()
		print("updated")
