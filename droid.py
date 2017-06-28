from gopigo import *
import urllib
import urllib2
import json
import time
import logging
 
def main():
   
    status = getStatus()
   
    if status == 'gopi':
        # Execute robot command
        print("execute robot")
        skynet()
        normal()    #return back to waiting
        main()      #recursive method
    if status == 'nope':
        time.sleep(10)   # Delay for 1 minute (60 seconds). (JUST WAITING AROUND)
        main()
    if status == 'quit':
        print "These are not the droids you were looking for"
def skynet():
    
    enc_tgt(1,1,90)
    fwd()
    time.sleep(10)
    enc_tgt(1,1,8)
    left_rot()
    enc_tgt(1,1,8)
    left_rot()
    #compass adjustment
    time.sleep(5)
    enc_tgt(1,1,90)
    fwd()
def normal():
    url_path = 'https://bluepen.herokuapp.com/?type=set&getValue=nope'
        
    # Send HTTP POST request
    request = urllib2.Request(url_path)
   
    #Temp code - proxy
    #proxy = urllib2.ProxyHandler({'https': 'go-proxy.fpl.com:8080'})
    #opener = urllib2.build_opener(proxy)
    #urllib2.install_opener(opener)
    #Temp code - proxy
       
    response = urllib2.urlopen(request)
    parsed_json = json.load(response)
   
    #droid_status = parsed_json['status'];   
    print "return to normal"
def getStatus():
    #module that calls a web service to see if its time to move forward
    #https://bluepen.herokuapp.com/?type=get
    #https://bluepen.herokuapp.com/?type=set&getValue=gopi
    #python -m pip install SomePackage --proxy go-proxy.fpl.com:8080
    url_path = 'https://bluepen.herokuapp.com/?type=get'
    
    # page id query
    query_args = { 'type':'get'}
   
    # urlencode data (need urllib)
    data = urllib.urlencode(query_args)
       
    # Send HTTP POST request
    request = urllib2.Request(url_path)
   
    #Temp code - proxy
    #proxy = urllib2.ProxyHandler({'https': 'go-proxy.fpl.com:8080'})
    #opener = urllib2.build_opener(proxy)
    #urllib2.install_opener(opener)
    #Temp code - proxy
       
    response = urllib2.urlopen(request)
    parsed_json = json.load(response)
   
    droid_status = parsed_json['status'];
    print droid_status
    return droid_status
 
main()