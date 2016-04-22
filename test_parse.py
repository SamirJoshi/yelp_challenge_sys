import time, math, json
import os.path

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
    # number of lines of each set - change to run on subsets of the data
    user_lines = 552339
    tip_lines = 591864
    rev_lines = 2225213
    checkin_lines = 55569
    business_lines = 77445
    #filenames and paths
    user_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yelp_academic_dataset_user.json"))
    tip_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yelp_academic_dataset_tip.json"))
    rev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yelp_academic_dataset_review.json"))
    check_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yelp_academic_dataset_checkin.json"))
    bus_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yelp_academic_dataset_business.json"))
    
    #Reading in/ parsing data
    #user data
    start = time.clock()
    user_data = parseData(user_path, user_lines)
    end = time.clock()
    # user_data = parseData(os.path.dirname(__file__) + "/../yelp_academic_dataset_user.json", 552339)
    print "READ USER DATA in " + str(end - start) + " seconds"
    #tip data
    start = time.clock()
    tip_data = parseData(tip_path, tip_lines)
    end = time.clock()
    print "READ TIP DATA in " + str(end - start) + " seconds"
    #review data
    start = time.clock()
    review_data  = parseData(rev_path, rev_lines)
    end = time.clock()
    print "READ REVIEW DATA in " + str(end - start) + " seconds"
    #checkin data
    start = time.clock()
    checkin_data = parseData(check_path, checkin_lines)
    end = time.clock()
    print "READ CHECKIN DATA in " + str(end - start) + " seconds"
    #business data
    start = time.clock()
    business_data = parseData(bus_path, business_lines)
    end = time.clock()
    print "READ BUSINESS DATA in " + str(end - start) + " seconds"
    print "SUCCESSFUL PARSED ALL DATA FROM JSONs"
