import re
import urllib2
import string
def getURL():
    ID = []
    url1 = raw_input("Please enter a URL from Tunein Radio: ");
    open_file = urllib2.urlopen(url1);
    raw_file = open_file.read();
    cut = raw_file.split("<label>AVAILABLE STREAMS</label>")
    Part = cut[1].split("</li>")
    #print "Part[0]:"
    #print Part[0];
    i = 0;
    i = i + 1
    #print i
    Piece = Part[0].split("?streamid=")
    #print "Piece 0: " + str(Piece[0])
    #print "Piece 1: " + str(Piece[1])
    brek = "<a "
    i = 0
    for brek in Part[0]:
        i = i + 1
    #print "brek was in Part[0] " + str(i) + " times."
    Cutt = Part[0].split("<a ")
    Cuttt = str(Cutt).split("a>")
    #Chop = Cutt[i].split("a>")
    Piece[0] = Piece[1].split('</li>')
    #print "Piece 0: " + str(Piece[0])
    i = 0
    for items in Cutt:
        #print "Stream " + str(i)
        #print Cutt[i]
        i = i + 1
    Amount = i
    i = 0
    for items in Cutt:
        #print "Cutt " + str(i)
        #print Cutt[i]
        streamid = Cutt[i].split('data-streamid="')
        #streamid[0] = streamid[0].split('"')
        #print streamid[0]
        Streamid = str(streamid[0]).split('href="?streamid=')
        #print "0" + Streamid[0]
        #print str(Streamid)
        NStreamid = str(Streamid).split(" '")
        #print NStreamid[1]
        NNStreamid = str(NStreamid[1]).split('"')
        #print NNStreamid[0]
        if i is not 0:
            open_file = urllib2.urlopen("http://stream.radiotime.com/listen.stream?streamIds=" + str(NNStreamid[0]));
            raw_file = open_file.read();
            print raw_file
            ID.append(raw_file)
        i = i + 1
    getURL()
getURL()
