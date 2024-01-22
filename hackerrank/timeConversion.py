
def timeConversion(time_str):
    sufex = time_str[-2:]
    hour = time_str[0:2]
    minutes = time_str[3:5] 
    seconds = time_str[6:8]
    #print(hour)
    #print(sufex)
    # print(minutes)
    #print(seconds)
    removed_sufex = time_str.replace(sufex, '')

    if sufex == "AM" and hour != 0:
        return removed_sufex
    
        # Convert to 24-hour format
    if sufex == 'PM' and hour != 12:
        hour += 12
    elif sufex == 'AM' and hour == 12:
        hour = 0
     
    #print(removed_sufex)
    l = time_str.split(":")
    hour_24 = str(int(l[0]) +12)
    return hour_24+ ':' + minutes + ':'+ seconds


if __name__ == "__main__":

    time_str = "12:32:23AM"
    result = timeConversion(time_str)

    print(result)
