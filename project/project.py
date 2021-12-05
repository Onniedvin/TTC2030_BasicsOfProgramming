import datetime

def alarm_clock(alarm):
    if len(alarm) != 8:
        return "Wrong format, try again."
    else:
        if int(alarm[0:2]) > 23:
            return "Wrong hour format, try again."
        elif int(alarm[3:5]) > 59:
            return "Wrong minute format, try again."
        elif int(alarm[6:8]) > 59:
            return "Wrong second format, try again."
        else:
            return "valid"

while True:
    alarm = input("Enter your desired time to wake up in the following format \"HH:MM:SS\" \nWake up time: ")
    validate = alarm_clock(alarm)
    if validate != "valid":
        print (validate)
    else:
        print(f"\nYour alarm is set for the time {alarm}")
        break

alarm_hour = int(alarm[0:2])
alarm_min = int(alarm[3:5]) 
alarm_sec = int(alarm[6:8])

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("\nWake up!")
                print("\nDo you want to save your last set alarm time on a text file? \"y, n\"")

                file_list = ["\nYour last alarm was set for the time",  alarm]

                filewrite = input()
                if filewrite == "y":
                    file = open("last_alarm.txt", "a")
                    for thingy in file_list:
                        file.write("\n" + thingy)
                    file.close()
                    print("\nThe text file will be found in the folder where the program was run")
                else:
                    print("\nOK, no file will be written")
                break
