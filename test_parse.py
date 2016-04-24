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

def filePaths(file_name):
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

    numlines = {'user' : user_lines, 'tips' : tip_lines, 'reviews' : rev_lines, 'checkin' : checkin_lines, 'business' :  business_lines}
    path = {'user' : user_path, 'tips' : tip_path, 'reviews' : rev_path, 'checkin' : check_path, 'business' : bus_path}

    return (path[file_name], numlines[file_name])

def getFiles(path, lines):

    start = time.clock()
    data = parseData(path, lines)
    end = time.clock()
    print "PARSED " + str(lines) + " of " + path + " in " + str(end - start) + "seconds" 
   
    return data

def parseAll():
    (user_p, user_l) = filePaths('user')
    user_data = getFiles(user_p, user_l)
    
    (tip_p, tip_l) = filePaths('tips')
    tip_data = getFiles(tip_p, tip_l)
    
    (rev_p, rev_l) = filePaths('reviews')
    rev_data = getFiles(rev_p, rev_l)
    
    (checkin_p, checkin_l) = filePaths('checkin')
    checkin_data = getFiles(checkin_p, checkin_l)
    
    (bus_p, bus_l) = filePaths('business')
    bus_data = getFiles(bus_p, bus_l)

    return 0
if __name__ == "__main__":
    f =parseAll()
    

