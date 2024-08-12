from tkinter import *
import tkinter.messagebox as msg
import pandas as pd


df = pd.read_csv('allbooks.csv')
allbooks=df.to_dict('records')
class Multiple():
    def __init__(self, root):

        self.root = root
        self.root.geometry("400x400")
        self.root.title("Library mangement system")
        self.root.config(bg="powderblue")
        self.admin_table=[]+allbooks
        self.user_table = []

        title = Label(self.root, text="Home Page",bg="powderblue", font=('bold', '25'))
        title.pack()

        book_button = Button(self.root, text="Book", command=self.book_page)
        book_button.place(x=150, y=90)

        admin_button = Button(self.root, text="Library",command=self.admin_page)
        admin_button.place(x=150, y=150)

        user_button = Button(self.root, text="User",command=self.user_page)
        user_button.place(x=150, y=200)

    def book_page(self):
            window0 = Tk()

            window0.title("Book Page")
            window0.geometry("400x200")
            window0.config(bg="powderblue")

            book_ISBN_label = Label(window0, text="ISBN", bg="powderblue", font=('bold', '15'))
            book_ISBN_label.place(x=20, y=40)

            self.book_ISBN = Entry(window0)
            self.book_ISBN.place(x=100, y=40)

            book_add = Button(window0, text="Add_Copy",command=self.add_copy)
            book_add.place(x=20 , y=100)

            book_remove = Button(window0, text="Remove_copy", command=self.remove_copy)
            book_remove.place(x=100, y=100)

            book_info = Button(window0, text="Show_Info.", command=self.show_info)
            book_info.place(x=200, y=100)

    def add_copy(self):
        j=0
        for i in range(len(self.admin_table)):

            if self.admin_table[i]["ISBN"]==int(self.book_ISBN.get()):
                j = 1
                self.admin_table[i]["quantity"] = self.admin_table[i]["quantity"] + 1
                msg.showinfo("Success","Added Copy")
                break
        if j==0:
            msg.showinfo("Failed","No such Book exists")

    def remove_copy(self):
        j = 0
        for i in range(len(self.admin_table)):

            if self.admin_table[i]["ISBN"] == int(self.book_ISBN.get()):
                j = 1
                self.admin_table[i]["quantity"] = self.admin_table[i]["quantity"] - 1
                msg.showinfo("Success", "Removed Copy")
                break
        if j == 0:
            msg.showinfo("Failed", "No such Book exists")

    def show_info(self):
        j = 0
        for i in range(len(self.admin_table)):

            if self.admin_table[i]["ISBN"] == int(self.book_ISBN.get()):
                j = 1
                msg.showinfo("Success",f"Book is having title {self.admin_table[i]['book_name']} with author as {self.admin_table[i]['author_name']} , ISBN {self.admin_table[i]['ISBN']} and was Published on {self.admin_table[i]['Pub_Year']} and quantity available is {self.admin_table[i]['quantity']}")
                break
        if j == 0:
            msg.showinfo("Failed", "No such Book exists")



    def admin_page(self):
            window = Tk()

            window.title("Library Page")
            window.geometry("400x400")
            window.config(bg="powderblue")
            book_name_label = Label(window, text="Book Name:", bg="powderblue", font=('bold', '15'))
            book_name_label.place(x=20, y=40)

            author_label = Label(window, text="Author Name:", bg="powderblue", font=('bold','15'))
            author_label.place(x=20, y=80)

            ISBN_label = Label(window, text="ISBN", bg="powderblue", font=('bold', '15'))
            ISBN_label.place(x=20, y=120)

            Publication_year_label = Label(window, text="Pub._Year:", bg="powderblue", font=('bold', '15'))
            Publication_year_label.place(x=20, y=160)

            qty_label = Label(window, text="Quantity", bg="powderblue", font=('bold', '15'))
            qty_label.place(x=20, y=200)

            self.book_entry = Entry(window)
            self.book_entry.place(x=150, y=40)

            self.author_entry = Entry(window)
            self.author_entry.place(x=150, y=80)

            self.ISBN = Entry(window)
            self.ISBN.place(x=150, y=120)

            self.pub_year= Entry(window)
            self.pub_year.place(x=150, y=160)

            self.qty_entry = Entry(window)
            self.qty_entry.place(x=150, y=200)

            admin_submit = Button(window, text="Submit",command=self.admin_sub)
            admin_submit.place(x=120 , y=240)

            tocsv_submit = Button(window, text="To_File", command=self.lis_tocsv)
            tocsv_submit.place(x=40, y=240)

    def lis_tocsv(self):
        df=pd.DataFrame(self.admin_table)
        df.to_csv('Library.csv',index=False)
        msg.showinfo("Success", "Converted in Library.csv")

    def admin_sub(self):
        j=0

        for i in range(len(self.admin_table)):

            if self.admin_table[i]["ISBN"] == int(self.ISBN.get()):
              j=1
              if self.admin_table[i]["book_name"]== self.book_entry.get() and self.admin_table[i]["author_name"]==self.author_entry.get() and self.admin_table[i]["Pub_Year"]==int(self.pub_year.get()):
                  self.admin_table[i]["quantity"] = self.admin_table[i]["quantity"] + int(self.qty_entry.get())
                  msg.showinfo("Success", "Added copies to existing book")
                  break
              else:
                  msg.showinfo("Error", "Wrong Info w.r.t ISBN")
                  break
        if j==0:
            self.admin_table.append({"book_name":self.book_entry.get(),"author_name":self.author_entry.get(),"ISBN":int(self.ISBN.get()),"Pub_Year":int(self.pub_year.get()),"quantity":int(self.qty_entry.get())})
            print(self.admin_table)
            msg.showinfo("Success", "Added Successfully")


    def user_page(self):
        window1 = Tk()

        window1.title("User page")
        window1.geometry("300x300")
        window1.config(bg="powderblue")

        user_book_label = Label(window1, text="Book Name:", bg="powderblue", font=('bold', '15'))
        user_book_label.place(x=20, y=40)

        user_author_Label = Label(window1, text="Author:", bg="powderblue", font=('bold', '15'))
        user_author_Label.place(x=20, y=100)

        self.user_book_entry = Entry(window1)
        self.user_book_entry.place(x=150, y=40)

        self.author_book_entry = Entry(window1)
        self.author_book_entry.place(x=150, y=100)


        user_add = Button(window1, text="Add",command=self.user_add)
        user_add.place(x=130, y=200)

        user_return = Button(window1, text="Return", command=self.user_ret)
        user_return.place(x=50, y=200)

        user_csv = Button(window1, text="to_file", command=self.user_tocsv)
        user_csv.place(x=180, y=200)


    def user_tocsv(self):
        df=pd.DataFrame(self.user_table)
        df.to_csv('allusers.csv',index=False)
        msg.showinfo("Success", "Converted in allusers.csv")

    def user_add(self):

            j=0
            for i in range(len(self.admin_table)):
                if self.admin_table[i]["book_name"]== self.user_book_entry.get() and self.admin_table[i]["author_name"]==self.author_book_entry.get() and self.admin_table[i]["quantity"]>=1:
                    j=1
                    if (len(self.user_table)) <= 2:#after 2, only 1 more book allowed
                        self.user_table.append({"book_name":self.user_book_entry.get(),"author_name":self.author_book_entry.get(),"ISBN":self.admin_table[i]["ISBN"],"Pub_Year":self.admin_table[i]["Pub_Year"]})
                        self.admin_table[i]["quantity"]=self.admin_table[i]["quantity"]-1
                        print(self.admin_table,self.user_table)
                        msg.showinfo("Success","Given to User")
                        break
                    else:
                        msg.showinfo("Error", "Borrow Limit Exceeded")
                        break

            if j==0:
                msg.showerror("Error","Sorry book not Available")




    def user_ret(self):

        k=0
        for i in range(len(self.user_table)):
            if self.user_table[i]["book_name"]==self.user_book_entry.get() and self.user_table[i]["author_name"]==self.author_book_entry.get():
             self.user_table.pop(i)
             k=1
             for i in range(len(self.admin_table)):
                 if self.admin_table[i]["book_name"] == self.user_book_entry.get() and self.admin_table[i]["author_name"] == self.author_book_entry.get():
                     self.admin_table[i]["quantity"] = self.admin_table[i]["quantity"] + 1
                     print(self.admin_table)
                     print(self.user_table)
                     break

        if k==0:
            msg.showinfo("Error", "Returning Unborrowed book")





root = Tk()
obj = Multiple(root)
root.mainloop()






