import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
os.listdir('C:/Users/zahid/Desktop/DL_Projects/Chatterbot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data')
x = ChatBot('Robot')
trainer = ChatterBotCorpusTrainer(x)
trainer.train("chatterbot.corpus.english")
while True:
    message=input('Me:')
    if message.strip()!= 'Bye':
       reply=x.get_response(message)
    
    print('Robot:', reply)
    if message.strip()=='Bye!':
        
        print('Robot: Bye')
        break
    
    
    