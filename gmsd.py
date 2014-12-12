import urllib2
headder = {'User-Agent': 'Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1'}

query=raw_input("Enter the search query : ")
rescount=int(raw_input("How many results? : "))
fname=raw_input("Output file name : ")
incl=raw_input("Any strings to include in url? : ")
excl=raw_input("Any strings to exclude in url? : ")

res=""
resfound=0
fil=open(fname,"a+")
fil.write("\n_________________________________________________________\n\n")

query=query.replace(' ',"+")

for n in range(0,rescount,10):
    pno=str(n)
    print "\nPage : "+ pno
    url="http://www.google.com/search?q="+query+"&start=" + pno
    print url
    req=urllib2.Request(url,headers=headder)
    page=urllib2.urlopen(req)
    string= page.read()
    endpos=0
    startpos=0
    string.replace("<b>","")
    count=string.count("u=")
    print str(count)+" Results"
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

    fil.write(res)
    print res
    res=""


res=res+ "\n"+str(resfound) + " Reasults Total"
#print res

fil.write(res)
fil.close()    
