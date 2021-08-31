import datetime
def convert24(time):

    if time[-2:] == "AM" and time[:2] == "12":

        return "00" + time[2:-2]

    elif time[-2:] == "AM":

        return time[:-2]
       
    elif time[-2:] == "PM" and time[:2] == "12":

        return time[:-2]
          
    else:

        return str(int(time[:2]) + 12) + time[2:8]
    

def convertDateTime(dateTime):

    slash = '/'
    hyphen = '-'
    if slash in dateTime:

        date, time, timeMeridian = dateTime.split(' ')
        time = convert24(time + " " + timeMeridian)
                                                       # hours    # minutes 
        return datetime.datetime.strptime(date + " " + time[:2] + time[3:5], "%m/%d/%Y %H%M") # ignore seconds

    elif hyphen in dateTime:

        date, time = dateTime.split(' ')
        if(len(time) == 4):

            time = '0' + time

        return datetime.datetime.strptime(date[0:2] + '-' + date[3:5] + '-' +'20' + date[-2:] + " " + time[:2] + time[3:], '%m-%d-%Y %H%M')

# testing purpose date[3:5] + date[0:2]
if __name__ == "__main__":

    print(convertDateTime('04-02-15 6:31'))