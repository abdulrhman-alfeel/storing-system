from tkinter import *
import time

# # Assuming `df` is your DataFrame
# df['Total Cost'] = df['Total Cost'].apply(lambda x: int(x.replace(',', '')))

# # Now we can filter the rows based on the `Total Cost` column
# filtered_df = df[df['Total Cost'] < 50000]

def AppConvex(conves,oprtion=None):
        global activity_indicator
        global farming
        farming = conves
        activity_indicator = Canvas(conves,  height=100, bd=0, highlightthickness=0)
        # .activity_indicator.place(x=100, y=50)
        if oprtion is None:
            activity_indicator.grid(row=1, column=5, padx=55, pady=5, sticky="nsew")
        elif oprtion == 'addpack':
            activity_indicator.grid(row=0,column=0,padx=10,pady=10)
        else:
            activity_indicator.grid_forget()
        # Frameing = ttk.Frame(.activity_indicator)
        activity_indicator.create_text(150, 150,text="الرجاء الانتظار",font=("Tajawal",30), fill="#fff", width=0)
        # text_awaite.grid(row=0,column=0)
        conves.after(0, animate)
def animate():
        for i in range(30):
            activity_indicator.itemconfig(activity_indicator.find_all()[0],fill="#a9d8f8")
            farming.update()
            time.sleep(0.01)
            activity_indicator.itemconfig(activity_indicator.find_all()[0], fill="#007fff")
            farming.update()
            time.sleep(0.01)
            activity_indicator.itemconfig(activity_indicator.find_all()[0], fill="#333333")
            farming.update()
            time.sleep(0.01)
        activity_indicator.grid_forget()
