from logging import exception
import tweepy
import time
import random
client = tweepy.Client(consumer_key='UawWPXt9ilHLPnY2pHzHToE93',
                       consumer_secret='yMesVkvUIwUiRg8cSaZgv3W40nmB812MSkcCRAqhfBhW64cdMu',
                       access_token='1585345500508659712-E1RYkhytfU3gnKMNrtbaKzQztSrabe',
                       access_token_secret='XTQeeaPpLfDnYVsxpEy8yeGJsz8trhYoAOGeY1LpNCcUv')
nouns = ["Gay people", "Furries", "Fortnite players", "Minimum wage workers", "Alpha males", "Celebrities", "VTubers", "Non-binary people", "Lesbians", "Beat Saber players", "Femboys", "OSU! players", "College representatives", "Pedophiles", "Zoophiles", "Protogens", "PNGTubers", "Police officers", "Newborns", "Dream stans", "Elementary school teachers", "Old people", "Tik Tokers", "Minecraft players", "Pansexuals", "Friday Night Funkin' players", "Gimmick accounts", "My kids", "ADOFAI players", "Cat posting accounts"]
auth = tweepy.OAuthHandler("UawWPXt9ilHLPnY2pHzHToE93", "yMesVkvUIwUiRg8cSaZgv3W40nmB812MSkcCRAqhfBhW64cdMu") 
auth.set_access_token("1585345500508659712-E1RYkhytfU3gnKMNrtbaKzQztSrabe", "XTQeeaPpLfDnYVsxpEy8yeGJsz8trhYoAOGeY1LpNCcUv") 
api = tweepy.API(auth)
lastchoice = ''
filename = "m.jpg"
while True:
    choice = (random.choice(nouns))
    if choice != lastchoice:
        api.update_status_with_media(filename = filename, status = f"{random.choice(nouns)} when I bash their head in with a metal rod")
        nouns.remove(choice)
        print(len(nouns))
        time.sleep(86400) #86400 = 1day
    elif choice == lastchoice:
       new = random.choice(nouns)
       api.update_status_with_media(filename = filename, status = f"{random.choice(new)} when I bash their head in with a metal rod")
       nouns.remove(new)
       print(len(nouns))
       time.sleep(86400) #86400 = 1day
    
    if len(nouns) == 0:
        print("Out of nouns. Exiting")
        exit()

    lastchoice = choice


