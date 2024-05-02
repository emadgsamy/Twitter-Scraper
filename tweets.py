from ntscraper import Nitter
import json 

num_of_mentions = 0



accounts = input("Enter accounts(separated by space): ").split()
ticker = input("Enter ticker: ")
st_date = input("Enter start date(yyyy-mm-dd): ")
end_date = input("Enter end date(yyyy-mm-dd): ")
for account in accounts:
    npa = 0
    print("=============",account,"=============")
    tweets = Nitter().get_tweets(f"{account}", mode="user",since= st_date, until= end_date, number=60)
    with open(f"{account}.json", "w") as file:
        json.dump(tweets, file)
    for tweet in tweets["tweets"]:
        if ticker in tweet["text"]:
            num_of_mentions += 1
            npa += 1
    print(account," has ", npa, " tweets with ", ticker)
    

print(ticker," was used ", num_of_mentions, " times in the time between ", st_date, " and ", end_date)



