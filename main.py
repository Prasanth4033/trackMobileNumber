import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from phonenumbers.phonenumberutil import number_type
num=input("enter the number you want to track:")
phone = phonenumbers.parse(num)
time= timezone.time_zones_for_number(phone)
carrier = carrier.name_for_number(phone,'en')
registration= geocoder.description_for_number(phone,'en')

print(phone)
print(time)
print("companyname:",carrier)
print("country is:",registration)
'''import json
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from phonenumbers.phonenumberutil import number_type
import pycountry
from tkinter import Tk, Label, Button, Entry
from phone_iso3166.country import phone_country


class Location_Tracker:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="#3f5efb")
        self.window.resizable(False, False)

        # ___________Application menu_____________
        Label(App, text="Enter a phone number", fg="white", font=("Times", 20), bg="#3f5efb").place(x=150, y=30)
        Label(App, text="(Add country code at the start)", fg="white", font=("Times", 8), bg="#3f5efb").place(x=180, y=70)
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
        self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
        self.country_label = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
        self.timezone = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
        self.carrier = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")


        # ___________Place widgets on the window______
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.country_label.place(x=100, y=280)
        self.timezone.place(x=150, y=300)
        self.carrier.place(x=200, y=320)

        # __________Linking button with countries ________
        self.track_button.bind("<Button-1>", self.Track_location)
        # 255757294146

    def Track_location(self, event):
        phone_number = self.phone_number.get()
        country = "Country is Unknown"
        if phone_number:
            tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
            print(tracked)
            if tracked:
                if hasattr(tracked, "official_name"):
                    country = tracked.official_name
                    carrier = tracked.name

                else:
                    country = tracked.name
        self.country_label.configure(text=country)
        self.carrier.configure(text=carrier)



PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()'''

