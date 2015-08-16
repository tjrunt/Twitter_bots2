#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.4.3


import tweepy, time, sys, os, random,  datetime, shutil 

#rgfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



pathRun = 'images\run'
pathDone = 'images\Done'
productLinkFile = 'links.txt'

# affilate id
affliteID = 'rf=XXXXXXXXXX'




curentTime = time.time()
print('curentTime : ', curentTime)



def readFile(linkPath):
    # read product links
    filename=open(linkPath,'r')
    f=filename.readlines()
    filename.close()
    return f

# add affilate id and choose between ? or &
def formatPost(f, affliteID):
    posts = []
    for i in f:
        i = i.strip()
        if '?' in i:
            link = i + '&' + affliteID
            posts.append(link)
        else:
            link = i + '?' + affliteID
            posts.append(link) 
    return posts


def writeLinksToNewFile():
    return


def uploadPost(postText, imagesDir):
    count = 1
    for i in postText:
        try:
            image = '0' + str(count) + '.png'
            imagePath = imagesDir + '\\' + image
            #post image and status
            print('this is the text for -i- to post:' , i)
            print('imagePath to post:' , imagePath)
            api.update_with_media(imagePath, status= i)
            count = count + 1
            time.sleep(50)
        except:
            pass

def getDirName(rootDir):
    for root, dirs, files in os.walk('images', topdown=False):        
        for name in dirs:
            myDir = (os.path.join(root, name))
            if  "images\\run\\"  in myDir:
                #os.move(myDir)
                print('myDir: ', myDir)
                dest = myDir.replace('run', 'Done')
                print('dest ', dest)
                return myDir, dest 
                
def moveDir(src, dest):
    print('moving: ' , src, dest)
    shutil.move(src, dest)


general_messages = ['check it out!!! ', 'sweet design ', 'cool stuff ', ' ' , ' ', ' ']


mydirs = getDirName('images')
linkPath= mydirs[0] + '\\' +'links.txt'
f_text = readFile(linkPath)
### use if I need to add affilate Id also change argument in doPost()
#myPosts = formatPost(f_text, affliteID)
doPost = uploadPost(f_text, mydirs[0])
moveDir(mydirs[0], mydirs[1])

