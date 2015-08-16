#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.4.3
import random, math
import tweepy, time, sys


def twitterAppInit(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET ):
    #enter the corresponding information from your Twitter application:
    CONSUMER_KEY = CONSUMER_KEY
    CONSUMER_SECRET = CONSUMER_SECRET
    ACCESS_KEY = ACCESS_KEY
    ACCESS_SECRET = ACCESS_SECRET
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)  
    return api
def readFile(myFile):
    f= open(myFile,'r')
    f_text= f.readlines()
    f.close()
    return f_text
def postTweet(api, tweet):
    api.update_status(status= tweet)
    return
def randNum(r):
    x = random.randrange(0,r)
    return x
def tweetBuilder( baseTweet, addHash ='', addDeal =''):
    return str(addDeal)+ ' ' + baseTweet +' ' + str(addHash)
def sleeper(sleepTime):
    time.sleep(sleepTime)
    return
#keep track of lines tweeted
def wasTweeted(currentTweet, oldTweets = []):
    return oldTweets.append(currentTweet)
def getTetweetId(api, getUserTweet):
   userTweet = api.user_timeline(getUserTweet, count = 1)
   print()
   print('user ', getUserTweet,' tweeted: ', userTweet[0].text)  
   return userTweet[0].id_str
def myRetweet(api, idToTweet ):
   #x[1].status.id_str
   #api.retweet(id)
   api.retweet(idToTweet)
   return
def myFav(api, user, idToTweet):
   api.create_favorite(idToTweet)
   return
def followNewfollowers(toFollow, api):
    count = 0
    for i in toFollow:
        Follow = api.get_user(i)
        if (Follow.following != True):
            #newFolowers.append(toFollow)
            Follow.follow()
            count = count + 1
            print('you are now following ' , i)
    print('total of: ', count, 'new acounts')
def getUserNames(userName, api):
    #follow followers
    fol = api.followers(userName)
    userNames= []
    for i in fol:
        userNames.append(i.screen_name)
    return userNames

# tweet must be less  than 140 characters

#remove '\n'

# build link add affilite

# build link add search words
def runRandomRETWEETER(api, my_fav_accounts):

    rendUser = randNum(len(my_fav_accounts))
    theUser =my_fav_accounts[rendUser]
    tweet_id = getTetweetId(api, theUser)
    reTweet = myRetweet(api,tweet_id )
def runRandomFAV(api, my_fav_accounts):
    rendUser = randNum(len(my_fav_accounts))
    theUser =my_fav_accounts[rendUser]
    tweet_id = getTetweetId(api, theUser)
    reFav = myFav(api, theUser, tweet_id )        
#twitterAccount is APPI
def runTweetBot(text, hashTags, affliateLinks, addDealMessage, twitterAccount, repeater = 10):
    staleTweets = []
    count = 0
    count2 = 0
    

    while count < repeater:

        for i in affliateLinks:
            print('count2  ',count2)
            if count2 == 3 or count2 == 8:
                runRandomFAV(twitterAccount, my_fav_accounts)
            if count2 == 5 or count2 == 10:
                runRandomRETWEETER(twitterAccount, my_fav_accounts)
            count2 = count2 + 1
            if len(i) < 3:
                randHashIndex = randNum(len(hashTags))
                randQuoteIndex = randNum(len(text))
                myPosTweet = text[randQuoteIndex]
                myPosHashIndex = hashTags[randHashIndex]
                # to do dont use a stale tweet in a session
                staleTweet = wasTweeted(randQuoteIndex, staleTweets )
                toTweet = tweetBuilder(myPosTweet, addHash=myPosHashIndex)
                if len(toTweet) <= 140:
                    print('true')
                    postTweet(twitterAccount, toTweet)
                    print('toTweet  ', toTweet)
                    mySleepTime = randNum(8000)
                    sleeper(mySleepTime)
                    

                else:
                    
                    #try post with no hashtags
                    print('myPosTweet: ', myPosTweet)
                    postTweet(twitterAccount, myPosTweet)
                    print('myPosTweet  ', myPosTweet)
                    mySleepTime = randNum(8000)
                    sleeper(mySleepTime)
                    
            else:
                # post link
                randDealMessage = randNum(len(addDealMessage))
                toTweet = tweetBuilder(i, addDeal=addDealMessage[randDealMessage])
                print('toTweet : ', toTweet)
                postTweet(twitterAccount, toTweet)
                
                mySleepTime = randNum(4000)
                sleeper(mySleepTime)
                
        count = count + 1
        




#############
        #####
        #####
        #####
#
# THis  runs the main  first follows new peeps then it starts the tweet robot


#todo write into classes, simplify, handle errors, loggong, dont repeat random posts, add machine gun posts w/impages, add dir message, add query
#
#
##test works
#account_babyRobot.update_status(status= "In order to succeed, we must first believe that we can. -Nikos Kazantzakis")


# zazzle store links
myLinks =readFile("Store_links.txt")

# Positize quoates
positiveQuoates = readFile("positiveQuoates.txt")


# 50% off all cases - How can you resist that! | USE CODE: FUNNEWCASE4U


# "10% Off with Code:TENTH4ZAZZLE","" ,"","How fun Zazzle's 10th Bday SAVE 10% Code:TENTH4ZAZZLE" "Up to 50% Off zazzle Code:TENTH4ZAZZLE ",
dealMessages = ["50% off all cases - How can you resist that! | USE CODE: FUNNEWCASE4U","","50% off all cases Use Code: READY4SCHOOL Good stuff"," Cool stuff &50% off all cases Code: FUNNEWCASE4U","choose your color, Recrop, resize, personalize and customize",
           "20% off Use upto 50% off dorm decor Use Code: READY4SCHOOL ","50% off all cases Use Code: READY4SCHOOL" ]

positveHashTags = ['#loveyourself #positivity #inspired','#nevergiveup #positivity','#positivelife','#optimism #inspire','#motivation #gettingthere','#Positivity',
                   '#positivity #motivation','#motivation','#enjoylife','#happy #positivelife','#happiness ' ,'#growth',
                   '','#persistent','#bepositive','#positivelife #nevergiveup','#positivevibes','#StayPositive','#inspirational #bepositive','#motivation','#Positizum',
                   '#GoodThoughts #Inspiration','#Inspiration','#positive', '#inspired #happy', '#good #positivelife', '#growth #happiness #inspired' , '#inspirational #positive']

#authentication info
account_babyRobot = twitterAppInit('xxx', 'xxx',
                                   'xxxx','xxxx' )

my_fav_accounts = ['@best1health', '@JerrySeinfeld','@GoldsGym', '@ConanOBrien', '@ConanOBrien',
               '@SethMacFarlane', '@BackpackerMag', '@visitmontana', '@drdrew', '@CanyonlandsNPS',
               '@MarketWatch', '@OlympicNP', '@BigBendNPS', '@GreatSmokyNPS', '@ArchesNPS', '@GrandCanyonNPS',
               '@neiltyson', '@jimmykimmel', '@bobsaget','@WhitneyCummings',
               '@Marvel', '@StarWars_VII', '@bcgoldthwait','@StarWars7783',
               '@ClassicStarWars', '@StarWarsJunk', '@pattonoswalt' ]

# I dont need this currently?
user = account_babyRobot.me()
# follow new followers
name = user.screen_name
myFollowers = getUserNames(name, account_babyRobot)
followNewfollowers(myFollowers, account_babyRobot)

baby = runTweetBot(positiveQuoates, positveHashTags, myLinks,  dealMessages, account_babyRobot )
