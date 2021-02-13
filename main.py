import discord
import Cipher #pip install CipherModule
import string
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def fetch_message(self,message):
        if message.content == 'ping':
            await message.channel.send('pong1')



    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '&?ping':
            await message.channel.send('Pong')

        if message.content.startswith('&?caesar'):
            cont=message.content.split()
            encrypt=''
            for i in cont[2:]:
                encrypt=encrypt + " "+str(i)
            key=int(cont[1])            
            decrypt=Cipher.Caesar.decode(encrypt, key).replace('|',' ')
            await message.channel.send(f"`{decrypt}`")

        if message.content.startswith('&?b64'):
            cont=message.content.split()
            encrypt=''
            for i in cont[1:]:
                encrypt=encrypt + " " + str(i)          
            decrypt=Cipher.B64.decode(encrypt) #.replace('|',' ')
            await message.channel.send(f"`{decrypt}`")

        if message.content.startswith('&?a1z26'):
            alphabets=list(string.ascii_lowercase)
            cont=message.content.split()
            encrypt=''
            num_list=[]
            for i in cont[1:]:
                encrypt=encrypt + " " + str(i)
                num_list.append(int(i))                
            decrypt=''
            if cont[1].isalpha():
                for i in encrypt:
                    try:
                        decrypt=decrypt+' '+str(alphabets.index(i.lowercase()))
                    except:
                        decrypt=decrypt+str(i)
            else:

                for i in num_list:
                    decrypt=decrypt + " " + str(alphabets[i])
            
            
            await message.channel.send(f"`{decrypt}`")

        if message.content.startswith('&?atbash'):
            alphabets=list(string.ascii_lowercase)
            cont=message.content.split()
            encrypt=''
            num_list=[]
            for i in cont[1:]:
                encrypt=encrypt + " " + str(i)

            decrypt=''

            for i in encrypt:
                try:
                    decrypt=decrypt+(alphabets[25-alphabets.index(i.lower())])
                except:
                    decrypt=decrypt+str(i)
                    
            await message.channel.send(f"`{decrypt}`")


client = MyClient()
client.run(os.getenv('TOKEN'))