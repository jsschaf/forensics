
import httplib, urllib, urllib2
import requests;
import sys;
import re;

#get what the server says
def get_response(temp):

    url = "https://weratepups.xyz/";
    url = url  + str(temp);
    conn = requests.get(url);
    response = conn.text;
    return response


#main function
if __name__ == '__main__':

    temp = 9999;

    #if the response was a padding error:
    while True:
        #get new response from the server
        response = get_response(temp);
        if response != "Error 404 - Not found":
            print temp;
            break;
        temp += 1;
        print "loop";

