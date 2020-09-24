class TweetAnalysis:
    """
    The TweetAnalysis class is used to form the analysis of the two list objects initiated in the
    GetTweets class. The first two functions each search for four different words in the output file
    and make a bar graph to shoe the counts for what is found in comparison between christmas and
    hanukkah. The third and fourth functions are used to look at a dataframe of the last 100 tweets
    using "MerryChristmas" or "HappyHanukkah". There are three ways to look at the data for each which
    are kept constant so that we can compare the results in the final report.
    """
    def christmasAnalysis():
        """
        The ChristmasAnalysis function is used to send the output of the christmas tweets
        list to the file, Christmas.txt. The function then looks for four keywords in the file
        line by line to find the count of each so that a bar graph can be made showcasing the
        counts.
        """
        from tweepyScript import GetTweets #imports the object class
        import pandas as pd #used for bar graphs
        import matplotlib.pyplot as plot #used for bar graphs

        # Creates a Christmas file containing the tweets
        christmas_file = open('Christmas.txt', 'w')
        for i in GetTweets.get_christmas_tweets():
            christmas_file.write(i)
        christmas_file.close()

        #Opens the christmas file containing the tweets
        christmas_analytics = open('Christmas.txt')

        # Christmas Data Visualization
        #Set counts to 0
        count_love = 0
        count_lights = 0
        count_travel = 0
        count_hashtag = 0

        #Keeps count of each word in the christmas_file
        for line in christmas_analytics:
           if 'love' in line:
               count_love += 1
           if 'lights' in line:
               count_lights += 1
           if 'travel' in line:
               count_travel += 1
           if '#' in line:
               count_hashtag += 1

        #Creates a data frame of all the words and their counts in the file
        christmas_df = pd.DataFrame(
           {"love": [count_love],
            "lights": [count_lights],
            "travel": [count_travel],
            "total hashtags": [count_hashtag]},
           index=[1])

        print(christmas_df)

        # Creates the Christmas Tweets bar graph
        christmas_df.plot.bar()
        plot.title("Holiday Terms Used In Christmas Tweets")
        plot.ylabel('Number of Tweets')
        plot.xlabel('Holiday Terms')
        plot.show()


    def hanukkahAnalysis():
        """
        The hanukkahAnalysis function is used to send the output of the hanukkah tweets
        list to the file, hanukkah.txt. The function then looks for four keywords in the file
        line by line to find the count of each so that a bar graph can be made showcasing the
        counts.
        """
        from tweepyScript import GetTweets #Imports the object class
        import pandas as pd #used for bar graphs
        import matplotlib.pyplot as plot #used for bar graphs

        #Creates a Hanukkah file containing the tweets
        hanukkah_file = open('hanukkah.txt', 'w')
        for x in GetTweets.get_hanukkah_tweets():
           hanukkah_file.write(x)
        hanukkah_file.close()

        #Opens the file for analysis
        hanukkah_analytics = open("hanukkah.txt")

        # Hanukkah Data Visualization
        count_gelt = 0
        count_lights = 0
        count_love = 0
        count_hashtag = 0

        # Counts the amount of times the following four words appear in the file
        for line in hanukkah_analytics:
           if 'Gelt' in line:
               count_gelt += 1
           if 'lights' in line:
               count_lights += 1
           if 'love' in line:
               count_love += 1
           if '#' in line:
               count_hashtag += 1
        #Creats a dataframe of the word and how many times it appears in the file
        hanukkah_df = pd.DataFrame(
           {"Gelt": [count_gelt],
            "lights": [count_lights],
            "love": [count_love],
            "total hashtags": [count_hashtag]},
           index=[1])

        print(hanukkah_df)

        # Creates the Hanukkah Tweets bar graph
        hanukkah_df.plot.bar()
        plot.title("Holiday Terms Used In Hanukkah Tweets")
        plot.ylabel('Number of Tweets')
        plot.xlabel('Holiday Terms')
        plot.show()

    def toDataFrameChristmas():
        """
        This function uses twitter authentication to search for "MerryChristmas" in the last
        100 tweets. It then creates a dataframe full of data about each tweet it collected which
        is used to perform three different data anaylis. This includes the descriptive statistics of
        the retweets and amount of followers of each user. The third analyis allows the team to compare
        the location geographically of each tweet between "MerryChristmas" and "HappyHanukkah".
        """
        import tweepy
        import pandas as pd
        import numpy as np
        from tweepyScript import GetTweets
        import pandas as pd
        import matplotlib.pyplot as plot

        #Twitter Authentication
        consumer_key = "RL4pgPIV8SaCXXwAmkg07M0fl"
        consumer_secret = "EyaB325pTuLeoS5rlW9dmVlfw6k9N0m19ndx4MyAUyDTEYasTu"
        access_token = "1602024776-fXXhqaBFJ3u8bxuYoodseQxHseXO8CitE7jJlAR"
        access_token_secret = "Md6qcYxvymRCpuuKLvtpRWVoOGkDR4taUDQBZHWrcFDAg"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        #Adds each of the 100 tweets to a results list
        results = [ ]
        for tweet in tweepy.Cursor(api.search, q='%23MerryChristmas').items(100):
            #%23 used to specify '#'

            results.append(tweet)

        DataSet = pd.DataFrame() #Create an empty data frame

        DataSet['tweetID'] = [tweet.id for tweet in results]
        DataSet['tweetText'] = [tweet.text for tweet in results]
        DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in results]
        DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in results]
        DataSet['tweetSource'] = [tweet.source for tweet in results]
        DataSet['tweetCreated'] = [tweet.created_at for tweet in results]
        DataSet['userID'] = [tweet.user.id for tweet in results]
        DataSet['userScreen'] = [tweet.user.screen_name for tweet in results]
        DataSet['userName'] = [tweet.user.name for tweet in results]
        DataSet['userCreateDt'] = [tweet.user.created_at for tweet in results]
        DataSet['userDesc'] = [tweet.user.description for tweet in results]
        DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in results]
        DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in results]
        DataSet['userLocation'] = [tweet.user.location for tweet in results]
        DataSet['userTimezone'] = [tweet.user.time_zone for tweet in results]
        #print(DataSet)

        #Statisitcs
        print("The following Statisitcs are for tweets related to ""MerryChristmas""")
        print("The Descriptive Statistics of the Retweets are:\n", DataSet['tweetRetweetCt'].describe())
        print("The Descriptive Statistics of the followers of each user:\n", DataSet['userFollowerCt'].describe())
        print("The user locations of all the tweets and their counts:\n", DataSet['userLocation'].value_counts())



    def toDataFrameHanukkah():
        """
        This function uses twitter authentication to search for "HappyHanukkah" in the last
        100 tweets. It then creates a dataframe full of data about each tweet it collected which
        is used to perform three different data anaylis. This includes the descriptive statistics of
        the retweets and amount of followers of each user. The third analyis allows the team to compare
        the location geographically of each tweet between "MerryChristmas" and "HappyHanukkah".
        """
        import tweepy
        import pandas as pd
        import numpy as np
        from tweepyScript import GetTweets
        import pandas as pd
        import matplotlib.pyplot as plt

        #Twitter Authentication
        consumer_key = "RL4pgPIV8SaCXXwAmkg07M0fl"
        consumer_secret = "EyaB325pTuLeoS5rlW9dmVlfw6k9N0m19ndx4MyAUyDTEYasTu"
        access_token = "1602024776-fXXhqaBFJ3u8bxuYoodseQxHseXO8CitE7jJlAR"
        access_token_secret = "Md6qcYxvymRCpuuKLvtpRWVoOGkDR4taUDQBZHWrcFDAg"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        #Adds each of the 100 tweets to a results list
        results = [ ]
        for tweet in tweepy.Cursor(api.search, q='%23HappyHanukkah').items(100):
            #%23 used to specify '#'

            results.append(tweet)

        DataSet = pd.DataFrame() #Creates an empty dataframe

        DataSet['tweetID'] = [tweet.id for tweet in results]
        DataSet['tweetText'] = [tweet.text for tweet in results]
        DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in results]
        DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in results]
        DataSet['tweetSource'] = [tweet.source for tweet in results]
        DataSet['tweetCreated'] = [tweet.created_at for tweet in results]
        DataSet['userID'] = [tweet.user.id for tweet in results]
        DataSet['userScreen'] = [tweet.user.screen_name for tweet in results]
        DataSet['userName'] = [tweet.user.name for tweet in results]
        DataSet['userCreateDt'] = [tweet.user.created_at for tweet in results]
        DataSet['userDesc'] = [tweet.user.description for tweet in results]
        DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in results]
        DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in results]
        DataSet['userLocation'] = [tweet.user.location for tweet in results]
        DataSet['userTimezone'] = [tweet.user.time_zone for tweet in results]
        #print(DataSet)

        #Statistics
        print("The following Statisitcs are for tweets related to ""HappyHanukkah""")
        print("The Descriptive Statistics of the Retweets are:\n",DataSet['tweetRetweetCt'].describe())
        print("The Descriptive Statistics of the followers of each user\n", DataSet['userFollowerCt'].describe())
        print("The user locations of all the tweets and their counts:\n", DataSet['userLocation'].value_counts())

#Used to call the program from the command line
if __name__ == "__main__":
    TweetAnalysis.christmasAnalysis()
    TweetAnalysis.hanukkahAnalysis()
    TweetAnalysis.toDataFrameChristmas()
    TweetAnalysis.toDataFrameHanukkah()
