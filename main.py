import phonenumbers
from phonenumbers import timezone, geocoder, carrier
print("☎️ Phone Number Information Finder")
while True:
    Number = input("Enter the number with country code :(+91-)")
    if(Number.lower()=="q"):
        print("📵Exiting... Goodbye!")
        break
    else:
        phone = phonenumbers.parse(Number)
        time = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone,"en")
        reg = geocoder.description_for_number(phone,"en")
        print(f"Parsed Number: {phone}")
        print(f"timezone : {time}")
        print(f"carrier : {car}")
        print(f"Region : {reg}")
        print("❤️Goodbye!")