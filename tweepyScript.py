class GetTweets:
    """
    The GetTweets class builds the two primary object lists used in the TweetAnalysis class. The
    first function, get_christmas_tweets, builds a list of all the tweets that inlcudes one of the
    four hashtags specified in the christmas_hashtags list. The second function, get_hanukkah_tweets,
    builds a list object that inlcudes all of the tweets that used one of the four hashtags initiated
    in the hanukkah_hashtags list.
    """
    def get_christmas_tweets():
        """
        This function builds a list object using the authentication of twitters API. It
        fills the list based on the four tweets initiated in the list that are found in tweets
        for the last second. These hashtags are more relevant to Christmas.
        """
        import tweepy #Used to connect to the Twitter API

        #Authentication tokens
        consumer_key = 'yourkeyhere'
        consumer_secret = 'yourkeyhere'
        access_token = 'yourkeyhere'
        access_token_secret = 'yourkeyhere'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        # Variable Lists used to match in tweets found
        christmas_hashtags = ["#MerryChristmas", "#ChristmasDinner", "#ChristmasLights", "#FamilyChristmas"]
        hashtags_list = []
        seconds=1
        # Using an API to track and record the hashtags in our hashtags list being Tweeted out, and adding them to a separate list to be later transposed into a text file
        for i in range(1):
            hol_tweets_0 = api.search(christmas_hashtags[0], counts=seconds)
            for tweet in hol_tweets_0:
                hashtags_list.append(tweet.text)
            hol_tweets_1 = api.search(christmas_hashtags[1], counts=seconds)
            for tweet in hol_tweets_1:
                hashtags_list.append(tweet.text)
            hol_tweets_2 = api.search(christmas_hashtags[2], counts=seconds)
            for tweet in hol_tweets_2:
                hashtags_list.append(tweet.text)
            hol_tweets_3 = api.search(christmas_hashtags[3], counts=seconds)
            for tweet in hol_tweets_3:
                hashtags_list.append(tweet.text)

            return(hashtags_list) #Object used in analysis

    def get_hanukkah_tweets():
        """
        This function builds a list object using the authentication of twitters API. It
        fills the list based on the four tweets initiated in the list that are found in tweets
        for the last second. These hashtags are more relevant to Hanukkah.
        """
        import tweepy
        #Authentication to Twitter API
        consumer_key = "0Kv3XUgyYL43VeD2b2I6gcRvj"
        consumer_secret = "eI0XfCCAy9SIxIvqDlRyM3Ubs58J9eUlKC6OhnrP7yTaSiRa4f"
        access_token = "803856264195375104-Q0eDjYiVxzXwB2Y8KeramMdwypBSYyz"
        access_token_secret = "LSL94aUV5U1kRl6XyCZb8GgJ0LLnWNJMlf8MN17HxbExx"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        # Variable Lists
        hanukkah_hashtags = ["#HappyHanukkah", "#Hanisim", "#Gelt", "#FamilyHanukkah"]
        hashtags_list1 = []

        seconds = 1
        for i in range(1):
            hol_tweets_0 = api.search(hanukkah_hashtags[0], counts=seconds)
            for tweet in hol_tweets_0:
                hashtags_list1.append(tweet.text)
            hol_tweets_1 = api.search(hanukkah_hashtags[1], counts=seconds)
            for tweet in hol_tweets_1:
                hashtags_list1.append(tweet.text)
            hol_tweets_2 = api.search(hanukkah_hashtags[2], counts=seconds)
            for tweet in hol_tweets_2:
                hashtags_list1.append(tweet.text)
            hol_tweets_3 = api.search(hanukkah_hashtags[3], counts=seconds)
            for tweet in hol_tweets_3:
                hashtags_list1.append(tweet.text)

            return(hashtags_list1) #Object used in analysis
