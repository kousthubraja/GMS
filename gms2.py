## Google Mass Search(gms) - written by Kousthub Raja.

import urllib2

def getshortfname(longurl):
	tmp=longurl.split("/")
	tmp=tmp[-1]
	if tmp.find('.')==-1:
		tmp=tmp+'.html'
	return tmp

def formaturl(longurl):
	if longurl.find('http')==-1 and longurl.find('ftp')==-1:
		longurl='http://'+longurl
	if longurl[-1]=="/":
		longurl=longurl[0:-1]
	return longurl

def download(longurl):
	longurl=formaturl(longurl)
	fname=getshortfname(longurl)
	headder = {'User-Agent': 'Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1'}
	req=urllib2.Request(longurl,headers=headder)
	con2=urllib2.urlopen(req)
	sfn=getshortfname(longurl)
	output = open(sfn,'wb')
	output.write(con2.read())
	print "Saved file : " + sfn
	output.close()
	con2.close()

	
def main():
  banner1="Google Mass Search"
  banner2="Written by Kousthub Raja"
  print banner1.center(70)
  print banner2.center(70)
  print '\n'
  #Gets the required inputs from user
  query=raw_input("Enter the search query : ")
  rescount=int(raw_input("How many results? : "))
  fname=raw_input("Output file name : ")
  down=raw_input("Do you want to download the contents of the links (May takes time.)[y/n] : ")

  adv_opt=raw_input("Want advanced options?[y/n] : ")
  adv_opt=adv_opt.strip()
  opt=incl=excl=cust_useragent=cust_url=""

  if adv_opt=="y":	
    opt=raw_input("Any additional options like hl=en? :")
    incl=raw_input("Any strings to include in url? : ")
    excl=raw_input("Any strings to exclude in url? : ")
    cust_useragent=raw_input("Have a custom user agent? :")
    cust_url=raw_input("Do you have a custom url?(Don't type anything if you dont know what it is)")

  down=down.strip()
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
      pno=str(n/10)
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
      if down=="y":
        download(temp)
        elif (incl!="" and temp.find(incl)!=-1) and excl=="":
                  res+= temp+"\n"
      resfound+=1
      if down=="y":
        download(temp)
        elif incl=="" and (excl!="" and temp.find(excl)==-1):
                  res+= temp+"\n"
      resfound+=1
      if down=="y":
        download(temp)
        elif (incl!="" and temp.find(incl)!=-1) and (excl!="" and temp.find(excl)==-1):
                  res+= temp+"\n"
      resfound+=1
      if down=="y":
        download(temp)
    
      print res
      if fname!="":
          fil.write(res)
      res=""


  res=res+ "\n"+str(resfound) + " Results Total"
  #print res

  if fname!="":
    fil.write(res)
    fil.close()

  raw_input("Everything Complete! Press enter to exit...")

if __name__=='__main__':
  main()
