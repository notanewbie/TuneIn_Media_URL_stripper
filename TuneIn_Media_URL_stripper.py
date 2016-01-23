import re
import urllib2
import string
def getURL():
    url1 = raw_input("Please enter a URL from Tunein Radio: ");
    open_file = urllib2.urlopen(url1);
    raw_file = open_file.read();
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
    API_key = re.findall(r"StreamUrl\":\"(.*?),",raw_file);
    #print API_key;
    #print "The API key is: " + API_key[0];
    #print "The API key is " + API_key[0] + ".";
    try:
        use_key = urllib2.urlopen(str(API_key[0]));
    except ValueError:
        print "I can't find stream URLs from stations where TuneIn wants to launch an external player because TuneIn doesn't know the URL, so how could I ask them what it is? Sorry. Try another station."
        getURL();
    logo_ = raw_file.split("http://cdn-radiotime-logos")
    logo = logo_[1].split("\"")
    Logo = "http://cdn-radiotime-logos" + logo[0];
    desc_ = raw_file.split("description\" content=\"")
    Desc_ = desc_[1].split("\" />")
    Description = Desc_[0]
    genre_ = raw_file.split("itemprop=\"genre\" content=\"")
    try:
        Genre_ = genre_[1].split("\"/>")
        Genre = Genre_[0]
    except IndexError:
        Genre = "Unknown"
    key_content = use_key.read();
    raw_stream_url = re.findall(r"Url\": \"(.*?)\"", key_content);
    bandwidth = re.findall(r"Bandwidth\":(.*?),", key_content);
    reliability = re.findall(r"lity\":(.*?),", key_content);
    isPlaylist = re.findall(r"HasPlaylist\":(.*?),", key_content);
    codec = re.findall(r"MediaType\": \"(.*?)\",", key_content);
    tipe = re.findall(r"Type\": \"(.*?)\"", key_content);
    total = 0
    for element in raw_stream_url:
        total = total + 1
    i = 0
    if total > 1:
        print "I found " + str(total) + " streams.";
    else:
        print "I found only one stream.";
    for element in raw_stream_url:
        print "Stream #" + str(i + 1);
        print "Stream stats:";
        print "Full station name: " + full_title + ".";
        print "Shortened station name " + title + ".";
        print "Bandwidth: " + str(bandwidth[i]) + " kilobytes per second."
        print "Reliability: " + str(reliability[i]) + "%"
        print "HasPlaylist: " + str(isPlaylist[i]) + "."
        print "Stream codec: " + str(codec[i]) + "."
        print "This audio stream is " + tipe[i].lower() + "."
        print "Pure streaming URL: " + str(raw_stream_url[i]) + ".";
        print "Logo URL: " + Logo;
        print "Description: " + Description
        print "Genre: " + Genre
        i = i + 1
    getURL();
getURL();
