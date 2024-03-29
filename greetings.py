import time

timestamp = time.strftime('%H') # Hour (24-hour clock) as a decimal number [00,23]

# print(type(timestamp))

if int(timestamp) < 12:
    print("Good Morning!!!")

elif int(timestamp) >= 12 and int(timestamp) <= 17:
    print("Good Afternoon!!!")

else:
    print("Good Evening!!!")