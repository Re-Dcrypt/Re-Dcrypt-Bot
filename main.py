import discord
import Cipher #pip install CipherModule
import string
import os

class MyClient(discord.Client):
    async def on_ready(self):
        activity = discord.Game(name="&?help")
        await client.change_presence(activity=activity)
       # await client.change_presence(activity=discord.Activity(activity=discord.Game(name="&?help")))
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

         
            
            
        if message.content.startswith('&?b64_decode'):
            encrypt=message.content.split()
            '''
            for i in cont[1:]:
                encrypt=encrypt + " " + str(i)         
            
            decrypt=Cipher.B64.decode(encrypt) #.replace('|',' ')
            
            # Don't need dependencies
            '''
            # Check for padding issues
            padding_needed = len(encrypt) % 4
            if padding_needed:
                encrypt += '===' # See https://stackoverflow.com/a/49459036/14437456
            
            decrypt = base64.b64decode(encrypt).decode('utf-8')
            await message.channel.send(f"`{decrypt}`")
        
        
        
        
        
        if message.content.startswith('&?b64_encode'):
            to_encrypt = ' '.join(message.content.split()[1:])
            message_bytes = to_encrypt.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            await message.channel.send(f'`{base64_message}`')
        
        
        

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

            
            
            
        if message.content.startswith('&?feedback'):
            cont=message.content.replace('&?feedback ','')
            channel=client.get_channel(810404758706716672)
            embed=discord.Embed(title="New Feedback", description=cont, color=0x39ff14)
            embed.set_author(name=message.author)
            mess = await channel.send(embed=embed)
            emoji1='\N{THUMBS UP SIGN}'
            emoji2='\N{THUMBS DOWN SIGN}'
            await mess.add_reaction(emoji1)
            await mess.add_reaction(emoji2)
            #await channel.send(f'{message.author} sent a feedback: {cont}')
            await message.channel.send('Feedback sent')
            
            
            
            
            
        if message.content.startswith('&?help'):
            embed=discord.Embed(title="Re-Dcrypt Bot Help", description="Re-Dcrypt Bot is a bot that will help you decode many ciphers like caesar , base64, A1Z26 & Atbash.", color=0x39ff14)
            embed.set_author(name="Re-Dcrypt", icon_url="https://i.imgur.com/ynad6vI.png")
            embed.set_thumbnail(url="https://i.imgur.com/ynad6vI.png")
            embed.add_field(name="Prefix", value="&?", inline=False)
            embed.add_field(name="Commands", value="Below are the commands you can use with this bot", inline=False)
            embed.add_field(name="Caesar Cipher Decode", value="&?caesar [key] [code]", inline=False)
            embed.add_field(name="a1z26", value="&?a1z26 [code] (can be numbers/alphabets)", inline=False)
            embed.add_field(name="Base64 Decode", value="&?b64decode [code]", inline=False)
            embed.add_field(name="Base64 Encode", value="&?b64encode [code]", inline=False)
            embed.add_field(name="Atbash", value="&?atbash [code]", inline=False)
            embed.add_field(name="Feedback/Suggestion", value="&?feedback [your feedback/suggestion]", inline=False)
            embed.add_field(name="Invite", value="&?invite", inline=False)
            embed.set_footer(text="Re-dcrypt Bot v0.5 Beta")
            embed2=discord.Embed(title="Community Server", url="https://discord.gg/hpyJ5A2tXY", description="Join our community server", color=0x39ff14)
            embed2.set_author(name="Re-Dcrypt", icon_url="https://i.imgur.com/ynad6vI.png")
            embed2.set_thumbnail(url="https://i.imgur.com/ynad6vI.png")
            embed2.set_footer(text="Re-dcrypt Bot v0.5 Beta")
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            
            
            
            
        if message.content.startswith('&?invite'):
            await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=775629409494630410&permissions=67451968&scope=bot')


client = MyClient()
client.run(os.getenv('TOKEN'))
