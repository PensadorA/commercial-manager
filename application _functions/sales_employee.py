from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview


class Sales:
    def __init__(self):
        self.__frame_cart_sales_var = None
        self.__frame_option_sales_var = None
        self.__frame_list_sales_var = None
        self.__root_sales = Tk()
        self.__root_sales.title('Vendas')
        self.__root_sales.geometry("1000x800")
        self.__root_sales.resizable(False, False)
        self.frame_list_sales()
        self.frame_option_sales()
        self.frame_cart_sales()
        self.__root_sales.mainloop()

    # setting the stock treeview



    def frame_list_sales(self):
        self.__frame_list_sales_var = Frame(self.__root_sales, bg='#7267CB')
        self.__frame_list_sales_var.place(relheight=1, relwidth=0.49, rely=0, relx=0)

        columns = ('first_name', 'last_name', 'email')

        tree = Treeview(self.__frame_list_sales_var, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            tree.insert('', END, values=contact)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))

        tree.bind('<<TreeviewSelect>>')

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = Scrollbar(self.__root_sales, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def frame_option_sales(self):
        self.__frame_option_sales_var = Frame(self.__root_sales, bg='#7267CB')
        self.__frame_option_sales_var.place(relheight=0.49, relwidth=0.5, rely=0, relx=0.5)

    def frame_cart_sales(self):
        self.__frame_cart_sales_var = Frame(self.__root_sales, bg='#7267CB')
        self.__frame_cart_sales_var.place(relheight=0.50, relwidth=0.5, rely=0.50, relx=0.5)


Sales()
