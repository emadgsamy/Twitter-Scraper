from ntscraper import Nitter
import json 

#the attributes of the tweets are:
num_of_mentions = 0
accounts = input("Enter accounts(separated by space): ").split()
ticker = input("Enter ticker: ")
st_date = input("Enter start date(yyyy-mm-dd): ")
end_date = input("Enter end date(yyyy-mm-dd): ")

#loop through the accounts and get the tweets
for account in accounts:
    npa = 0 #numper of mentions per account
    print("=============",account,"=============")
    tweets = Nitter().get_tweets(f"{account}", mode="user",since= st_date, until= end_date, number=60) #fetching all tweets of an account in a specified interval
    #saving the tweets to a json file
    with open(f"{account}.json", "w") as file:
        json.dump(tweets, file)
    #looping through the tweets to check if the ticker is mentioned
    for tweet in tweets["tweets"]:
        if ticker in tweet["text"]:
            num_of_mentions += 1
            npa += 1
    #printing number of mentions per account
    print(account," has ", npa, " tweets with ", ticker)
    
#printing total number of mentions
print(ticker," was used ", num_of_mentions, " times in the time between ", st_date, " and ", end_date)



