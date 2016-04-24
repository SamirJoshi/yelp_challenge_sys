import time, math
import os

from test_parse import *

def averageRating():
    (user_p, user_l) = filePaths('user')
    user_data = getFiles(user_p, user_l)
    num = len(user_data)
    sum = 0
    for i in range(0, num):
        curr = user_data[i]
        u_avg = curr['average_stars']
        sum = sum + u_avg

    avg = sum / num
    return avg

if __name__ == "__main__":
    avg = averageRating()
    print "AVERAGE STARS " + str(avg) 
