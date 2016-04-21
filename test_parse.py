import time, math, json

def parseData(data, lines):
    data_arr = []
    #get user data from _user.json
    data_file = open(data, 'r')
    lines_r = data_file.readlines()
    if(lines > 100):
        l = lines/100 + 1
    else:
        l = 1
    prog = 0
    for i in lines_r:
        dat = json.loads(i)
        data_arr.append(dat)

        prog = prog + 1
        #if((prog % l) == 0):
           # print str(prog/l) + "% parsed " + data
            #print dat['votes']

    return data_arr


if __name__ == "__main__":
    #user_dat = parseUser("yelp_user_test.json", 2)
    # number of lines of each set - change to run on subsets of the data
    user_lines = 552339
    tip_lines = 591864
    rev_lines = 2225213
    checkin_lines = 55569
    business_lines = 77445
    #user data
    user_data = parseData("yelp_academic_dataset_user.json", 552339)
    print "READ USER DATA"
    #tip data
    tip_data = parseData("yelp_academic_dataset_user.json", tip_lines)
    print "READ TIP DATA"
    #review data
    review_data  = parseData("yelp_academic_dataset_review.json", rev_lines)
    print "READ REVIEW DATA"
    #checkin data
    checkin_data = parseData("yelp_academic_dataset_checkin.json", checkin_lines)
    print "READ CHECKIN DATA"
    #business data
    business_data = parseData("yelp_academic_dataset_business.json", business_lines)
    print "READ BUSINESS DATA"
    print "SUCCESSFUL PARSED ALL DATA FROM JSONs"
