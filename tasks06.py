
'''
Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"
'''

def whatday(num):
    # Put your code here
    weekends = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 1 <= num <= 7:
        return weekends[num - 1]
    else:
        return "Wrong, please enter a number between 1 and 7"