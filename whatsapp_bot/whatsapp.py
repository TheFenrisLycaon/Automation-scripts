from datetime import datetime

import pywhatkit

now = datetime.now()

chour = now.strftime("%H")
mobile = input("Enter Mobile No of Receiver : ")
message = input("Enter Message you wanna send : ")
hour = int(chour) + int(input("Enter hour : "))
minute = int(input("Enter minute : "))

pywhatkit.sendwhatmsg(mobile, message, hour, minute)
