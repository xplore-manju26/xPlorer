from datetime import datetime

odds = [1, 3, 5, 7]

right_this_minute = datetime.today().minute

print(right_this_minute % 10)

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute..")

for x in range(10)
    print(x)
