
"""
  A bot that will lable every
  michael reeves post on twitter
  good or bad.
"""

# import
from textblob import TextBlob
import twint, os

# clear screen
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# config
c = twint.Config()
c.Username = "michaelreeves"
c.Store_object = True
c.Hide_output = True
c.Limit = 200
c.Media = False
c.Links = "exclude"


# run
twint.run.Search(c)

# tweets
tweets = twint.output.tweets_list

clear()


# count
count = 1
pos_count = 0
neg_count = 0

# loop through tweets
for tweet in tweets:

  # get sentiment
  if TextBlob(tweet.tweet).sentiment.polarity > 0: out = "Positive"; pos_count += 1
  else: out = "Negative"; neg_count += 1

  print("["+ str(count) + "] " + tweet.tweet + "  :: " + out + "\n")
  count += 1


# enter to exit
print("\n\n\n")
print("[*] Total tweets collected: " + str(len(tweets)))
print(f"[*] Total tweets anylised: {str(pos_count + neg_count)}")
print(f"[*] {str(pos_count)} of the tweets were positive")
print(f"[*] {str(neg_count)} of the tweets were negative\n")
input("[*] Press enter to continue...")
