## Google Mass Search(gms) - written by Kousthub Raja.

import urllib2

banner1="Google Mass Search"
banner2="Written by Kousthub Raja"
print banner1.center(70)
print banner2.center(70)
print '\n'
#Gets the required inputs from user
query=raw_input("Enter the search query : ")
rescount=int(raw_input("How many results? : "))
fname=raw_input("Output file name : ")

opt=raw_input("Any additional options like hl=en? :")
incl=raw_input("Any strings to include in url? : ")
excl=raw_input("Any strings to exclude in url? : ")
cust_useragent=raw_input("Have a custom user agent? :")
cust_url=raw_input("Do you have a custom url?(Don't type anything if you dont know what it is)")
res=""
resfound=0

#Sets the headder to fool google search ;)
if cust_useragent.strip()!="":
	headder=cust_useragent
else:
	headder = {'User-Agent': 'Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1'}

#Open a file if a filename specified
if fname!="":
	fil=open(fname,"a+")
	fil.write("\n"+"_"*50+"\n\n")

query=query.replace(' ',"+")

#Loop to retrieve each page
for n in range(0,rescount,10):
    pno=str(n)
    print "\nPage : "+ pno
    if cust_url.strip()!="":
		url=cust_url+"?q="+query+"&start=" + pno
    else :
		url="http://www.google.com/search?"+opt+"&q="+query+"&start=" + pno
    print url
    req=urllib2.Request(url,headers=headder)
    page=urllib2.urlopen(req)
    string= page.read()
    endpos=0
    startpos=0
    string.replace("<b>","")
    count=string.count("u=")
    print str(count)+" Results"
	
	#Loop to retrieve each results in a page
    for i in range(count):
        startpos=string.find("u=",endpos)
        endpos=string.find("&amp;",startpos+3)
        temp=string[startpos+2:endpos]
        if res.find(temp)==-1:
            if incl=="" and excl=="":
                res+= temp+"\n"
		resfound+=1
	    elif (incl!="" and temp.find(incl)!=-1) and excl=="":
                res+= temp+"\n"
		resfound+=1
	    elif incl=="" and (excl!="" and temp.find(excl)==-1):
                res+= temp+"\n"
		resfound+=1
	    elif (incl!="" and temp.find(incl)!=-1) and (excl!="" and temp.find(excl)==-1):
                res+= temp+"\n"
		resfound+=1
	
    print res
    if fname!="":
        fil.write(res)
    res=""


res=res+ "\n"+str(resfound) + " Reasults Total"
#print res

if fname!="":
	fil.write(res)
	fil.close()

raw_input("Everything Complete! Press enter to exit...")
