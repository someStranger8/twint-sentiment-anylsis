
"""
  A bot that will lable every
  michael reeves post on twitter
  good or bad.
"""

# import
from textblob import TextBlob
import twint, os, csv

# clear screen
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# user
user = "michaelreeves"

# config
c = twint.Config()
c.Username = user
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

# csv
with open('data.csv', 'x', encoding='UTF8') as f:
  # writer
  wr = csv.writer(f)
  wr.writerow(["user", "tweet", "sentiment"])

  # loop through tweets
  for tweet in tweets:
    # list
    l = []

    # get sentiment
    if TextBlob(tweet.tweet).sentiment.polarity > 0: out = "Positive"; pos_count += 1
    else: out = "Negative"; neg_count += 1

    print("["+ str(count) + "] " + tweet.tweet + "  :: " + out + "\n")

    # add to list
    l.append(user)
    l.append(tweet.tweet)
    l.append(out)

    # write to csv
    wr.writerow(l)

    # increment count
    count += 1


# enter to exit
print("\n\n\n")
print("[*] Total tweets collected: " + str(len(tweets)))
print(f"[*] Total tweets anylised: {str(pos_count + neg_count)}")
print(f"[*] {str(pos_count)} of the tweets were positive")
print(f"[*] {str(neg_count)} of the tweets were negative\n")
input("[*] Press enter to continue...")
