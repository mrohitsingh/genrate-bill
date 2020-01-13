from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1350x700+0+0")
		self.root.title("Billing Software")
		bg_color="#4d004d"
		title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

		#------------Variables-----------
		#------------Mobile-----------
		self.note_8=IntVar()
		self.m20=IntVar()
		self.pro_6=IntVar()
		self.q6=IntVar()

		#------------Laptop-----------
		self.tuf=IntVar()
		self.dell=IntVar()
		self.air=IntVar()
		self.hp=IntVar()

		#------------Mice-----------
		self.b170=IntVar()
		self.x1000=IntVar()
		self.M235=IntVar()
		self.N100=IntVar()

		#------------Total Price & Tax -----------
		self.mobile_price=StringVar()
		self.laptop_price=StringVar()
		self.mice_price=StringVar()

		self.mobile_tax=StringVar()
		self.laptop_tax=StringVar()
		self.mice_tax=StringVar() 

		#------------Customer-----------
		self.c_name=StringVar()
		self.c_phone=StringVar()
		self.bill_no=StringVar()
		x=random.randint(1000,9999) 
		self.bill_no.set(str(x))
		self.search_bill=StringVar()

		#----------Customer Detail Frame-----------------
		F1=LabelFrame(self.root,bd=10,text="Costmer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F1.place(x=0,y=80,relwidth=1)

		cname_lbl=Label(F1,text="Costmer Name:",bg=bg_color,fg="white",font=("times new roman", 15,"bold")).grid(row=0,column=0,padx=20,pady=5)
		cname_txt=Entry(F1,width=16,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

		cphn_lbl=Label(F1,text="Phone No.:",bg=bg_color,fg="white",font=("times new roman", 15,"bold")).grid(row=0,column=2,padx=20,pady=5)
		cphn_txt=Entry(F1,width=16,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

		c_bill_lbl=Label(F1,text="Bill No.:",bg=bg_color,fg="white",font=("times new roman", 15,"bold")).grid(row=0,column=4,padx=20,pady=5)
		c_bil_txt=Entry(F1,width=16,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

		bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bg=bg_color,fg="white",bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
		
		#----------Mobile Label Frame-------------------
		F2=LabelFrame(self.root,bd=10,text="Mobile",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F2.place(x=5,y=183,width=325,height=380)

		note_8_lbl=Label(F2,text="Redmi Note 8",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		note_8_lbl=Entry(F2,width=10,textvariable=self.note_8,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		m_20_lbl=Label(F2,text="Galaxy M20",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		m_20_lbl=Entry(F2,width=10,textvariable=self.m20,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		pro_6_lbl=Label(F2,text="Redmi 6 Pro",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		pro_6_lbl=Entry(F2,width=10,textvariable=self.pro_6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		q6_lbl=Label(F2,text="LG Q6",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		q6_lbl=Entry(F2,width=10,textvariable=self.q6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


		#----------Grossery Label Frame-------------------
		F3=LabelFrame(self.root,bd=10,text="Laptop",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F3.place(x=340,y=183,width=325,height=380)

		tuf_lbl=Label(F3,text="ASUS Gaming",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		tuf_lbl=Entry(F3,width=10,textvariable=self.tuf,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		dell_lbl=Label(F3,text="Dell Inspiron",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		dell_lbl=Entry(F3,width=10,textvariable=self.dell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		air_lbl=Label(F3,text="MacBook Air",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		air_lbl=Entry(F3,width=10,textvariable=self.air,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		hp_lbl=Label(F3,text="HP Pavilion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		hp_lbl=Entry(F3,width=10,textvariable=self.hp,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


		#----------Mice Label Frame-------------------
		F4=LabelFrame(self.root,bd=10,text="Mice",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F4.place(x=673,y=183,width=325,height=380)

		b170_lbl=Label(F4,text="Logitech B170",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		b170_lbl=Entry(F4,width=10,textvariable=self.b170,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		x1000_lbl=Label(F4,text="HP X1000",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		x1000_lbl=Entry(F4,width=10,textvariable=self.x1000,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		m235_lbl=Label(F4,text="Logitech M235",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		m235_lbl=Entry(F4,width=10,textvariable=self.M235,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		n100_lbl=Label(F4,text="Lenovo N100",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		n100_lbl=Entry(F4,width=10,textvariable=self.N100,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		#----------Bill Area----------------
		F5=LabelFrame(self.root,bd=10,relief=GROOVE)
		F5.place(x=1005,y=183,width=350,height=380)
		bill_title=Label(F5,text="Bill Area",bd=6,relief=GROOVE,font=("times new roman",13,"bold")).pack(fill=X)
		scrol_y=Scrollbar(F5,orient=VERTICAL)
		self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
		scrol_y.pack(side=RIGHT,fill=Y)
		scrol_y.config(command=self.txtarea.yview)
		self.txtarea.pack(fill=BOTH,expand=1)

		#--------Button Frame-----------

		F6=LabelFrame(self.root,bd=10,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F6.place(x=0,y=570,relwidth=1,height=140)

		menu1=Label(F6,text="Total Mobile Price:",font=("times new roman",13,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
		menu1_txt=Entry(F6,width=10,textvariable=self.mobile_price,font=("arial",13,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=3)

		menu2=Label(F6,text="Total Laptop Price:",font=("times new roman",13,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
		menu2_txt=Entry(F6,width=10,textvariable=self.laptop_price,font=("arial",13,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=3)
		
		menu3=Label(F6,text="Total Mice Price:",font=("times new roman",13,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
		menu3_txt=Entry(F6,width=10,textvariable=self.mice_price,font=("arial",13,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=3) 


		tax1=Label(F6,text="Mobile Tax:",font=("times new roman",13,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
		tax1_txt=Entry(F6,width=10,textvariable=self.mobile_tax,font=("arial",13,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=3)

		tax2=Label(F6,text="Grossery Tax:",font=("times new roman",13,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
		tax2_txt=Entry(F6,width=10,textvariable=self.laptop_tax,font=("arial",13,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=3)
		
		tax3=Label(F6,text="Mice Tax:",font=("times new roman",13,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
		tax3_txt=Entry(F6,width=10,textvariable=self.mice_tax,font=("arial",13,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=3) 


		btn_f=Frame(F6,bd=7,relief=GROOVE)
		btn_f.place(x=750,width=575,height=100)

		total_btn=Button(btn_f,command=self.total,text="Total",width=10,bg=bg_color,fg="white",bd=7,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)


		gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",width=10,bg="#000000",fg="white",bd=7,font="arial 12 bold").grid(row=0,column=1,padx=10,pady=15)


		clear_btn=Button(btn_f,text="Clear",width=10,bg=bg_color,fg="white",bd=7,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=15)


		exit_btn=Button(btn_f,text="Exit",width=10,bg=bg_color,fg="white",bd=7,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=15)
		self.w_bill()


	def total(self):
		self.m_n_p=self.note_8.get()*8999
		self.m_m_p=self.m20.get()*12999
		self.m_p_p=self.pro_6.get()*14999
		self.m_q_p=self.q6.get()*27999

		self.total_mobile_price=float(
										self.m_n_p+
										self.m_m_p+
										self.m_p_p+
										self.m_q_p
										)
		self.mobile_price.set("Rs. "+str(self.total_mobile_price))
		self.m_tax=round((self.total_mobile_price*0.05),2)
		self.mobile_tax.set(str(self.m_tax))



		self.l_t_p=self.tuf.get()*40599
		self.l_d_p=self.dell.get()*67999
		self.l_a_p=self.air.get()*78999
		self.l_h_p=self.hp.get()*59999
		self.total_laptop_price=float(
										self.l_t_p+
										self.l_d_p+
										self.l_a_p+
										self.l_h_p
										)
		self.laptop_price.set("Rs. "+str(self.total_laptop_price))
		self.l_tax=round((self.total_laptop_price*0.05),2)
		self.laptop_tax.set(str(self.l_tax))


		self.mi_b_p=self.b170.get()*799
		self.mi_x_p=self.x1000.get()*999
		self.mi_m_p=self.M235.get()*620
		self.mi_n_p=self.N100.get()*1299

		self.total_mice_price=float(
										self.mi_b_p+
										self.mi_x_p+
										self.mi_m_p+
										self.mi_n_p
										)
		self.mice_price.set("Rs. "+str(self.total_mice_price))
		self.mi_tax=round((self.total_mice_price*0.05),2)
		self.mice_tax.set(str(self.mi_tax))

		self.Total_bill=float(	self.total_mobile_price+
								self.total_laptop_price+
								self.total_mice_price+
								self.m_tax+
								self.l_tax+
								self.mi_tax
								)


	def w_bill(self):
		self.txtarea.delete('1.0',END)
		self.txtarea.insert(END,"    Welcome to the Mahi Kirana Store\n")
		self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
		self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
		self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
		self.txtarea.insert(END,f"\n =====================================")
		self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
		self.txtarea.insert(END,f"\n =====================================")

	def bill_area(self):

		if self.c_name.get()=="" or self.c_phone.get()=="":
			messagebox.showerror("Error","Customer Details are must")

		elif self.mobile_price.get()=="Rs. 0.0" and self.laptop_price.get()=="Rs. 0.0" and self.mice_price.get()=="Rs. 0.0":
			messagebox.showerror("Error","No product Purches")
		else:	
			self.w_bill()
			#--------------Mobile------------------
			if self.note_8.get()!=0:
				self.txtarea.insert(END,f"\n Note 8\t\t{self.note_8.get()}\t\t{self.m_n_p}")
			if self.m20.get()!=0:
				self.txtarea.insert(END,f"\n Glaxy M20\t\t{self.m20.get()}\t\t{self.m_m_p}")
			if self.pro_6.get()!=0:
				self.txtarea.insert(END,f"\n Note 6 PRO\t\t{self.pro_6.get()}\t\t{self.m_p_p}")
			if self.q6.get()!=0:
				self.txtarea.insert(END,f"\n LG Q6\t\t{self.q6.get()}\t\t{self.m_q_p}")


			#--------------Laptop------------------
			if self.tuf.get()!=0:
				self.txtarea.insert(END,f"\n ASUS Gaming\t\t{self.tuf.get()}\t\t{self.l_t_p}")
			if self.dell.get()!=0:
				self.txtarea.insert(END,f"\n Dell Inspiron\t\t{self.dell.get()}\t\t{self.l_d_p}")
			if self.air.get()!=0:
				self.txtarea.insert(END,f"\n MacBook Air\t\t{self.air.get()}\t\t{self.l_a_p}")
			if self.hp.get()!=0:
				self.txtarea.insert(END,f"\n HP Pavilion\t\t{self.hp.get()}\t\t{self.l_h_p}")


			#--------------Mice------------------
			if self.b170.get()!=0:
				self.txtarea.insert(END,f"\n Logitech B170\t\t{self.b170.get()}\t\t{self.mi_b_p}")
			if self.x1000.get()!=0:
				self.txtarea.insert(END,f"\n HP X1000\t\t{self.x1000.get()}\t\t{self.mi_x_p}")
			if self.M235.get()!=0:
				self.txtarea.insert(END,f"\n Logitech M235\t\t{self.M235.get()}\t\t{self.mi_m_p}")
			if self.N100.get()!=0:
				self.txtarea.insert(END,f"\n Lenovo N100\t\t{self.N100.get()}\t\t{self.mi_n_p}")


			self.txtarea.insert(END,f"\n -------------------------------------")
			if self.mobile_tax.get()!="Rs: 0.0":
				self.txtarea.insert(END,f"\n Mobile Tax\t\t\t\t{self.mobile_tax.get()}")

			if self.laptop_tax.get()!="Rs: 0.0":
				self.txtarea.insert(END,f"\n Laptop Tax\t\t\t\t{self.laptop_tax.get()}")

			if self.mice_tax.get()!="Rs: 0.0":
				self.txtarea.insert(END,f"\n Mice Tax\t\t\t\t{self.mice_tax.get()}")

			self.txtarea.insert(END,f"\n Total: \t\t\t\t{self.Total_bill}")
			self.txtarea.insert(END,f"\n -------------------------------------")
			self.save_bill()

	def save_bill(self):
		op=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
		if op>0:
			self.bill_data=self.txtarea.get('1.0',END)
			f1=open("bills/"+str(self.bill_no.get())+".txt","w")
			f1.write(self.bill_data)
			f1.close()
			messagebox.showinfo("saved",f"Bill no.: {self.bill_no.get()} saved successfully")
		else:
			return

	def find_bill(self):
		for i in os.listdir("bills/"):
			print(i)


root=Tk()
obj =Bill_App(root)
root.mainloop()