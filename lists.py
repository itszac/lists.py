#list command line app
#makes lists by: python lists.py newlist listtitle list contents
#add to lists by: python lists.py listname add stuff to add
#delete list : python lists.py listname delete stuff to delte
#preint list by python litsts.py listname

import sys
import json
#open file, big json list [[listtitle, things, in, list], [listtitle, things, in, list]]
try:
    f = open('lists.txt', 'r')
        
except:
    f = open('lists.txt', 'w')
try:
    everything = json.load(f)
except:
    everything = []

#extract list titles


#get arguments and do stuff

length = len(sys.argv)
if length <= 1:
    print 'need more arguments: lists.py action stuff, action can be listslists newlist listname add delte'
elif sys.argv[1] == 'newlist':
    newlist = []
    newlist.append(unicode(sys.argv[2]))
    listitems = sys.argv[3:]
    for i in listitems:
        newlist.append(unicode(i))
    everything.append(newlist)
    print 'list added'
    print newlist
elif sys.argv[1] == 'listlists':
    listtitles = [listy[0] for listy in everything]
    print listtitles
    sys.exit()
else:

    listtitles = [listy[0] for listy in everything]
    listtitle = sys.argv[1]
    if listtitle not in listtitles:
        print 'bad list name, available lists are'
        print listtitles
        sys.exit()
    else:
        l = everything[listtitles.index(listtitle)]
    if length == 2:
        print l
    elif sys.argv[2] == add:
        for i in sys.argv[3:]:
            l.append(i)
        print l
    elif sys.argv[2] == delete:
        for i in sys.argv[3:]:
            l.delete(i)
    else:
        print 'confused'
print everything
with open('lists.txt','w') as f:
    json.dump(everything, f)
