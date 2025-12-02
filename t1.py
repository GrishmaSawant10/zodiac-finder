from tkinter import*
from tkcalendar import*

root=Tk()
root.title ("Know Your Zodiac Sign By Grishma Sawant")
root.geometry("750x550+230+100")
f=("TIMES NEW ROMAN",30,"bold")

def zodiac_sign(date,month):
	if (month==1 and date>=20) or (month==2 and date<=18):
		return "Aquarius"
	elif (month==2 and date>18) or (month==3 and date<=20):
		return "Pisces"
	elif (month==3 and date>=21) or (month==4 and date<=19):
        	return "Aries"
	elif (month==4 and date>=20) or (month==5 and date<=20):
        	return "Taurus"
	elif (month==5 and date>=21) or (month==6 and date<=20):
        	return "Gemini"
	elif (month==6 and date>=21) or (month==7 and date<=22):
        	return "Cancer"
	elif (month==7 and date>=23) or (month==8 and date<=22):
        	return "Leo"
	elif (month==8 and date>=23) or (month==9 and date<=22):
        	return "Virgo"
	elif (month==9 and date>=23) or (month==10 and date<=22):
        	return "Libra"
	elif (month==10 and date>=23) or (month==11 and date<=21):
        	return "Scorpio"
	elif (month==11 and date>=22) or (month==12 and date<=21):
        	return "Sagittarius"
	elif (month==12 and date>=22) or (month==1 and date<=19):
        	return "Capricorn"
def show_zodiac():
	selected_date = cal.get_date()
	day = selected_date.day
	month = selected_date.month
	sign = zodiac_sign(day, month)
	lab_zodiac.config(text=f" Your Zodiac Sign is {sign} ", bg='lightblue', font=f, anchor='center')

lab_header= Label(root,bg='lightpink',text=" Wanna Know Your Zodiac Sign? ",font=f, anchor='center')
lab_header.place(x=80,y=50)

lab_ent= Label(root,bg='lightgreen',text=" Enter Your Birthdate!!! ",font=f, anchor='center')
lab_ent.place(x=150,y=135)

cal = DateEntry(root, width=20, background='darkblue', foreground='white', borderwidth=20,font=f, anchor='center')
cal.pack(padx=125, pady=220)

btn_submit=Button(root,text="Show Zodiac",font=f,width=12,anchor='center',command=show_zodiac)
btn_submit.place(x=220,y=290)

lab_zodiac = Label(root, wraplength=600, anchor='center')
lab_zodiac.place(x=150,y=390)

root.mainloop()