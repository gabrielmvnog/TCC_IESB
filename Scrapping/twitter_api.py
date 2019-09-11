import tweepy
import csv
import pandas as pd
from tqdm import tqdm
from datetime import datetime

class TwitterAPI():

    def __init__(self):
        CONSUMER_KEY = "hePIf2ssrcXj66w7FSbqlCHW1"
        CONSUMER_SECRET = "vVVpFeZLWlbWIJ3NvhQQbSA4yOTCDAmIyqNRyrZyvxynIV7MYC"
        ACCESS_TOKEN = "98022990-jgx2gcI666p05mkSoGBzOjBIPg2IVxaGm4tWfRvWy"
        ACCESS_TOKEN_SECRET = "b3vdXsNWoM3yvrsmECoYMBHXHiL2Fkfp1PJehuYLnXZzj"

        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def search_tweets(self, keywords, limit=1000):

        with open("depression_text_" + str(datetime.now()).split('.')[0] + ".csv", "w") as write_file:
            writer = csv.writer(write_file)

            for keyword in keywords:

                print(f"\n## Iniciando busca: {keyword} ##\n")
                

                for tweet in tqdm(tweepy.Cursor(self.api.search, q=keyword, lang="pt",  tweet_mode='extended').items(limit)):
                    writer.writerow([tweet.full_text])



if __name__ == "__main__":
    api = TwitterAPI()
        
    words = ["suicidio", "me matar", "carta de suicidio", "nota de suicidio", "acabar com a minha vida", "acabar minha vida", 
            "não aguente mais", "não dá para viver", "a vida não vale a pena", "pronto para morrer", "pronto para saltar", 
            "dormir para sempre", "quero morrer", "morrer", "melhor morrer", "melhor morto", "morrer sozinho", "dormir para sempre", 
            "não quero estar vivo", "pacto de suicidio", "plano de suicidio", "plano de morte", "desisto de tudo", "desisto da vida", "cansei de viver",
            "cansei dessa vida", "viver não vale a pena"]

    api.search_tweets(words, limit= 5000 // len(words))
