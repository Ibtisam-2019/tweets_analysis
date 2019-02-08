import twitter 
# Enter your keys/secrets as strings in the following fields
import sys



api = twitter.Api(
consumer_key='',
  consumer_secret='',
  access_token_key='',
  access_token_secret='')

 
 

def checkUserName(user):
	'''
	The purpose of this function is to check if the user exists or not  
	'''
	try:
		output = api.GetUser(screen_name=user)
		return True
	except:

		return False

def searchUserTweets(user_name,words):
	user = checkUserName(user_name)
	link_tweets = ''
	full_tweets = ''
	followers_count = ''
	friends_count = ''
	tweets_date = ''
	store_it_to_dict = dict()
	count = 0
	#if the user exists
	if user:

		#now will get the tweest till 1000 times 
		t = api.GetUserTimeline(screen_name=user_name,count=100000)
		
		#will put the tweets in arrays
		tweets = [i.AsDict() for i in t]
	
		count = 0
		# it going to loop and get all the tweets
		for t in tweets:
			#it will check if the count vaiarble is 0 will do the following vairables to store 
			if count == 0:

				#now will store the information
				try:
					location = t['user']['location']
				except:
					location = "unkown"
				followers_count = t['user']['followers_count']
				friends_count = t['user']['friends_count']
				store_it_to_dict['location'] = location
				store_it_to_dict['followers_count'] = followers_count
				store_it_to_dict['friends_count'] = friends_count
			#if word in tweet
			if words in t['text']:

				idd = t['id_str']

				#the date of tweet created
				store_it_to_dict['created_at'] = t['created_at']
				#the link of the tweet
				store_it_to_dict['link'] =  "https://twitter.com/"+user_name+"/status/" + idd
				#the full tweet that has the bad word
				store_it_to_dict['full_tweets'] = t['text']
			count = count + 1

		#it will store the information as a dictionary 
		return store_it_to_dict
					
	else:
		#don't do anything
		pass


