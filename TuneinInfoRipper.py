import re
import urllib2
import string
def getURL():
    ID = []
    url1 = raw_input("Please enter a URL from Tunein Radio: ");
    open_file = urllib2.urlopen(url1);
    raw_file = open_file.read();
    cut = raw_file.split("<label>AVAILABLE STREAMS</label>")
    try:
        Part = cut[1].split("</li>")
    except IndexError:
        print "Stream URL unavailable."
        getURL()
    logo_ = raw_file.split("http://cdn-radiotime-logos")
    logo = logo_[1].split("\"")
    Logo = "http://cdn-radiotime-logos" + logo[0];
    desc_ = raw_file.split("description\" content=\"")
    Desc_ = desc_[1].split("\" />")
    Description = Desc_[0]
    genre_ = raw_file.split("itemprop=\"genre\" content=\"")
    Genre_ = genre_[1].split("\"/>")
    Genre = Genre_[0]
    raw_title = re.findall(r"<title>(.*?) - Listen Online",raw_file);
    try:
        full_title = str(raw_title[0]);
    except IndexError:
        raw = re.findall(r"<title>Listen to (.*?) online</title>",raw_file);
        try:
            full_title = str(raw[0]);
        except IndexError:
            rawe = re.findall(r"<h3>Listen to (.*?) on your phone!</h3>",raw_file);
        else:
            title = "is non-existent";
            full_title = url1;
    else:
        try:
            short_title = re.findall(r"(.*?) -", full_title);
            title = str(short_title[0]);
        except IndexError:
            short_title = "is non-existent";
            title = "is non-existent";
        else:
            short_title = "is non-existent";
            title = "is non-existent";
    print "Logo: " + Logo
    print "Description: " + Description
    print "Genre: " + Genre
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
            #print raw_file
            ID.append(raw_file)
            key_content = raw_file
            raw_stream_url = re.findall(r"Url\": \"(.*?)\"", key_content);
            #bandwidth = re.findall(r"Bandwidth\":(.*?),", key_content);
            isPlaylist = re.findall(r"HasPlaylist\":(.*?),", key_content);
            codec = re.findall(r"MediaType\": \"(.*?)\",", key_content);
            tipe = re.findall(r"Type\": \"(.*?)\"", key_content);
            total = 0
            for element in raw_stream_url:
                total = total + 1
            total = 0
            if total > 1:
                print "I found " + str(total) + " streams.";
            else:
                print "I found only one stream.";
            for element in raw_stream_url:
                reliability = key_content.split('"Reliability":')
                reliability = re.findall(r"lity\":(.*?),", key_content);
                bandwidth = re.findall(r"Bandwidth\":(.*?),", key_content);
                print "== Stream =="
                print "Stream stats:";
                print "Full station name: " + full_title + ".";
                print "Shortened station name " + title + ".";
                try:
                    print "Bandwidth: " + str(bandwidth[i - 2]) + " kilobytes per second."
                except IndexError:
                    print "Bandwidth currently unavailable."
                try:
                    print "Reliability: " + str(reliability[i - 1]) + "%"
                except IndexError:
                    print "Reliability data currently unavailable."
                try:
                    print "HasPlaylist: " + str(isPlaylist[i - 1]) + "."
                except IndexError:
                    print "HasPlayist data currently unavailable."
                try:
                    print "Stream codec: " + str(codec[i - 1]) + "."
                except IndexError:
                    print "Stream codec data currently unavailable."
                try:
                   print "This audio stream is " + tipe[i - 1].lower() + "."
                except IndexError:
                    print "Audio stream type is unavailable."
                try:
                    print "Pure streaming URL: " + str(raw_stream_url[i - 2]) + ".";
                except IndexError:
                    print "Stream URL unavailable."
                print "Logo URL: " + Logo;
                print "Description: " + Description
                print "Genre: " + Genre
        i = i + 1
    
    getURL()
getURL()
