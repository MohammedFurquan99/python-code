customer_name = input("Enter your name: ")
appointment_time = input("Enter appointment time: ")

if appointment_time == "(8:11) am":
    print("Appointment at 8:11 AM")

elif appointment_time == "(12:11) pm":
    print("Appointment at 12:11 PM")


barbers = ["sadiq", "zeeshan", "ali"]

count = 1

for barber in barbers:
    print(count, barber)
    count = count + 1

choice = int(input("Select your barber: "))
if choice == 1 or choice == 2 or choice == 3:
    selected_barber = barbers[choice - 1]
    print(selected_barber)
else:
    print("INVALID BARBER")
    exit()


services = ["haircut", "haircut with hairwash", "haircut with beard", "only beard"]

count = 1

for service in services:
    print(count, service)
    count = count + 1

service_choice = int(input("Enter your service: "))

if service_choice == 1 or service_choice == 2 or service_choice == 3 or service_choice == 4:
    selected_service = services[service_choice - 1]
    print(selected_service)
else:
    print("INVALID SERVICE")
    exit()


if service_choice == 1:
    price = 150
elif service_choice == 2:
    price = 250
elif service_choice == 3:
    price = 250
elif service_choice == 4:
    price = 100
else:
    print("INVALID")


print("----- BARBER PANEL -----")
print("1. Approve")
print("2. Reject")

approval = int(input("Barber choice: "))

if approval == 1:
    print("-------BOOKING APPROVED--------")
    print("Customer:", customer_name)
    print("Barber:", selected_barber)
    print("Service:", selected_service)
    print("Price:", price)
    print("Time:", appointment_time)

elif approval == 2:
    print("BOOKING REJECTED")

else:
    print("INVALID CHOICE")