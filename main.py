import discord
#import Cipher #pip install CipherModule
import string
import os
import base64
import binascii
from art import *

alphabet = string.ascii_lowercase
alphabet_upper = alphabet.upper()


def caesar(text,s): 
    result = "" 

    for i in range(1,len(text)): 
        char = text[i] 
        if char.isalpha():
            if char != " ":
                if (char.isupper()): 
                    result += chr((ord(char) + s-65) % 26 + 65) 
        
                else: 
                    result += chr((ord(char) + s - 97) % 26 + 97) 
            else:
                result=result+ char
        else:
            result += char
    return result


def vignere(text, key, mode):
  lowercase = text.lower()
  encrypted = ''
  index = None
  counter = 0
  alphabet = string.ascii_lowercase
  alphabet_upper=alphabet.upper()
  # First do the shifting thingy
  for char in lowercase:
    # Make sure the index does not exceed the key's length
    if counter == len(key): counter = 0

    if char not in alphabet:
      encrypted += char
    else:
      index = alphabet.index(char)
      
      if mode == 'encrypt':
        index += alphabet.index(key[counter])
      else:
        index -= alphabet.index(key[counter])

      index %= len(alphabet)
      encrypted += alphabet[index]
      counter += 1
  
  # Restore cases
  for x in range(len(encrypted)):
    encrypted = list(encrypted)
    if text[x] in alphabet_upper:
      encrypted[x] = encrypted[x].upper()
    
  return ''.join(encrypted)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-' , ' ':'/'} 

tap_code_dict={'A':'. .' , 'B':'. ..', 'C':'. ...','K':'. ...', 'D':'. ....' , 'E':'. .....'
            ,'F':'.. .','G':'.. ..', 'H':'.. ...', 'I':'.. ....' , 'J':'.. .....'
            ,'L':'... .','M':'... ..', 'N':'... ...', 'O':'... ....' , 'P':'... .....'
            ,'Q':'.... .','R':'.... ..', 'S':'.... ...', 'T':'.... ....' , 'U':'.... .....'
            ,'V':'..... .','W':'..... ..', 'X':'..... ...', 'Y':'..... ....' , 'Z':'..... .....', ' ':'/ /'}

def morse_encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else: 
            cipher += ' / '
  
    return cipher 

def morse_decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        i=0
        if (letter != ' '):   
            i = 0
            
            citext += letter 
        else:
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher 

def tap_encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += tap_code_dict[letter.upper()] + ' '
        else: 
            cipher += ' / '
  
    return cipher 

def tap_decrypt(message): 
    message=message.replace("/"," / / ")
    message_pair=[]
    i=0
    while i < (len(message.split())-1):
        temp_str=message.split()[i] + " "+message.split()[i+1]
        message_pair.append(temp_str)
        i=i+2
    decipher = '' 
    for letter in message_pair: 
            decipher += list(tap_code_dict.keys())[list(tap_code_dict .values()).index(letter)]   
    return decipher 

bacon_dict_complete = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB', 'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA', 'Z': 'BBAAB'}


bacon_dict_standard = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAA', 'K': 'ABAAB', 'L': 'ABABA', 'M': 'ABABB', 'N': 'ABBAA', 'O': 'ABBAB', 'P': 'ABBBA', 'Q': 'ABBBB', 'R': 'BAAAA', 'S': 'BAAAB', 'T': 'BAABA', 'U': 'BAABB', 'V': 'BAABB', 'W': 'BABAA', 'X': 'BABAB', 'Y': 'BABBA', 'Z': 'BABBB'}



def bacon_encode(text, mode):
    if mode == 'standard':
        bacon_dict = bacon_dict_standard
    else:
        bacon_dict = bacon_dict_complete

    text = text.upper()
    ciphertext = ''
    for char in text:
        try:
            ciphertext += bacon_dict[char] + " "
        except:
            ciphertext += char + " "

    return ciphertext


def bacon_decode(text, mode):

  if mode == 'standard':
    bacon_dict = bacon_dict_standard
  else:
    bacon_dict = bacon_dict_complete

  text = text.split()
  bacon_dict = dict((v,k) for k,v in bacon_dict.items()) # See https://stackoverflow.com/a/50232911/14437456
  plaintext = ''

  for item in text:
    plaintext += bacon_dict[item]

  return plaintext

class MyClient(discord.Client):
    async def on_ready(self):
        activity = discord.Game(name="&?help")
        await client.change_presence(activity=activity)
        print('Logged on as', self.user)



    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        #print (message.guild)
        if message.guild == None:
            prefix=''
        else:
            prefix="&?"
        #print (message.channel.id)

        if message.content.startswith(prefix):
            if message.content == f"{prefix}ping"  or message.content.startswith("&?ping"):
                await message.channel.send('Pong')
                
            
            elif message.content.startswith(f"{prefix}vignere_encrypt") or message.content.startswith("&?vignere_encrypt"):
                text = message.content.split()
                key = text[1]
                text = ' '.join(text[2:])
                enc = vignere(text, key, 'encrypt')
                await message.channel.send(f'```{enc}```')
                
                
            elif message.content.startswith(f"{prefix}vignere_decrypt") or message.content.startswith("&?vignere_decrypt"):
                text = message.content.split()
                key = text[1]
                text = ' '.join(text[2:])
                dec = vignere(text, key, 'decrypt')
                await message.channel.send(f'```{dec}```')

            elif message.content.startswith(f"{prefix}reverse")  or message.content.startswith("&?reverse"):
                cont=message.content.split()
                encrypt=''
                for i in cont[1:]:
                    encrypt=encrypt + " "+str(i)
                rev=encrypt[::-1]
                await message.channel.send(f"```{rev}```")

            elif message.content == f"{prefix}stats":
                await message.channel.send(f"Currently I'm in {len(client.guilds)} servers")

            elif message.content.startswith(f"{prefix}caesar")  or message.content.startswith("&?caesar"):
                cont=message.content.split()
                     
                try:
                    encrypt=''
                    for i in cont[2:]:
                        encrypt=encrypt + " "+str(i)
                    key=int(cont[1])     
                    decrypt=caesar(encrypt,26-key)
                    await message.channel.send(f"```{decrypt}```")
                except:
                    output_l=[]
                    encrypt=''
                    for i in cont[1:]:
                        encrypt=encrypt + " "+str(i)
                    for i in range(1,27):
                        decrypt=caesar(encrypt,26-i)
                        output_l.append(f"Key = {i}: {decrypt}")
                    outp=''
                    for i in output_l:
                        outp=outp+i+"\n"
                    await message.channel.send(f"```{outp}```")


               
            elif message.content.startswith(f'{prefix}bacon_encrypt') or message.content.startswith('&?bacon_encrypt'):
                msg=''
                if message.content.split()[1].lower() != 'complete':
                    for i in message.content.split()[1:]:
                        msg=msg + " " + i
                    mode='standard'
                else:
                    for i in message.content.split()[2:]:
                        msg=msg + " " + i
                    mode='complete'
                
                await message.channel.send(f'```{bacon_encode(msg, mode)}```')

            elif message.content.startswith(f'{prefix}bacon_decrypt') or message.content.startswith('&?bacon_decrypt'):
                msg=""
                if message.content.split()[1].lower() != 'complete':
                    for i in message.content.split()[1:]:
                        msg=msg + " " + i
                    mode='standard'
                else:
                    for i in message.content.split()[2:]:
                        msg=msg + " " + i
                    mode='complete'
                
                await message.channel.send(f'```{bacon_decode(msg, mode)}```')       
            
            elif message.content.startswith(f"{prefix}b64_decode") or message.content.startswith("&?b64_decode"):
                cont=message.content.split()
                encrypt=''
                for i in cont[1:]:
                    encrypt=encrypt + " " + str(i)         

                padding_needed = len(encrypt) % 4
                if padding_needed:
                    encrypt += '===' # See https://stackoverflow.com/a/49459036/14437456
                
                decrypt = base64.b64decode(encrypt).decode('utf-8')
                await message.channel.send(f"```{decrypt}```")
            

            elif message.content.startswith(f"{prefix}b64_encode")  or message.content.startswith("&?b64_encode"):
                to_encrypt = ' '.join(message.content.split()[1:])
                message_bytes = to_encrypt.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                await message.channel.send(f'```{base64_message}```')

            elif message.content.startswith(f"{prefix}a1z26")  or message.content.startswith("&?a1z26"):
                alphabets=list(string.ascii_lowercase)
                cont=message.content.split()
                encrypt=''
                num_list=[]
                for i in cont[1:]:
                    encrypt=encrypt + " " + str(i)
                    try:
                        num_list.append(int(i))                
                    except:
                        pass
                decrypt=''
                if cont[1].isalpha():
                    for i in encrypt:
                        try:
                            z=i.lower()
                            decrypt=decrypt+' '+str(alphabets.index(z)+1)
                        except:
                            decrypt=decrypt+str(i)
                else:
                    for i in num_list:
                        decrypt=decrypt + " " + str(alphabets[i-1])
                
                
                await message.channel.send(f"``` {decrypt} ```")

            elif message.content.startswith(f"{prefix}atbash")  or message.content.startswith("&?atbash"):
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
                        
                await message.channel.send(f"```{decrypt}```")
        
            elif message.content.startswith(f"{prefix}morse") or message.content.startswith("&?morse"):
                cont=message.content.split()
                encrypt=''
                for i in cont[1:]:
                    encrypt=encrypt + " " + str(i)
                try:
                    await message.channel.send(f"```{morse_decrypt(encrypt[1:])}```")
                except:
                    await message.channel.send(f"```{morse_encrypt(encrypt[1:])}```")

            elif message.content.startswith(f"{prefix}tap") or message.content.startswith("&?tap"):
                cont=message.content.split()
                encrypt=''
                for i in cont[1:]:
                    encrypt=encrypt + " " + str(i)
                if len(encrypt.split())==1:
                    await message.channel.send(f"```{tap_encrypt(encrypt[1:])}```")                    
                else:
                    try:
                        await message.channel.send(f"```{tap_decrypt(encrypt)}```")
                    except:
                        await message.channel.send(f"```{tap_encrypt(encrypt[1:])}```")                    

            elif message.content.startswith(f"{prefix}feedback") or message.content.startswith("&?feedback"):
                cont=message.content.replace('&?feedback ','')
                channel=client.get_channel(810404758706716672)
                embed=discord.Embed(title="New Feedback", description=cont, color=0x39ff14)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                mess = await channel.send(embed=embed)
                emoji1='\N{THUMBS UP SIGN}'
                emoji2='\N{THUMBS DOWN SIGN}'
                await mess.add_reaction(emoji1)
                await mess.add_reaction(emoji2)
                #await channel.send(f'{message.author} sent a feedback: {cont}')
                await message.channel.send('Feedback sent')
                
            elif message.content.startswith(f"{prefix}help") or message.content.startswith("&?help"):
                embed=discord.Embed(title="<a:redcryptexcited:781090077748494336> Re-Dcrypt Bot Help <a:redcryptexcited:781090077748494336>", description="Re-Dcrypt Bot is a bot that will help you decode many ciphers like caesar , base64, A1Z26 & Atbash.", color=0x39ff14)
                embed.set_author(name="Re-Dcrypt", icon_url="https://i.imgur.com/ynad6vI.png")
                embed.set_thumbnail(url="https://i.imgur.com/ynad6vI.png")
                embed.add_field(name="Prefix", value="&?", inline=False)
                embed.add_field(name="Commands", value="Below are the commands you can use with this bot", inline=False)
                embed.add_field(name="Caesar Cipher Decode", value=f"{prefix}caesar [key] [code] \n{prefix}caesar [code]  (This will bruteforce with all keys)", inline=False)
                embed.add_field(name="Bacon/Baconian Cipher", value=f'{prefix}bacon_encrypt [text] \n{prefix}bacon_decrypt [code] \n{prefix}bacon_encrypt [complete] [text] \n{prefix}bacon_decrypt [complete] [code] \n**Note**: By default Bacon cipher will decrrypt/encrypt in the standard form. If you need to encrypt/decrypt in complete form of bacon cipher then you need to mention it. ', inline=False)
                embed.add_field(name="Vignere Cipher", value=f'{prefix}vignere_encrypt [key] [code] \n{prefix}vignere_decrypt [key] [code]', inline=False)
                embed.add_field(name="a1z26", value=f"{prefix}a1z26 [code] (can be numbers/alphabets)", inline=False)
                embed.add_field(name="Base64 Decode", value=f"{prefix}b64_decode [code] \n{prefix}b64_encode [code]", inline=False)
                embed.add_field(name="Atbash", value=f"{prefix}atbash [code]", inline=False)
                embed.add_field(name="Morse Code", value=f"{prefix}morse [code/text] (This will automatically decode the morse & encode the text)", inline=False)
                embed.add_field(name="Tap Code", value=f"{prefix}morse [code/text] (This will automatically decode the tap code & encode the text)", inline=False)
                embed.add_field(name="Text reverse", value=f"{prefix}reverse [text]", inline=False)
                embed.add_field(name="Feedback/Suggestion", value=f"{prefix}feedback [your feedback/suggestion]", inline=False)
                embed.add_field(name="Invite", value=f"{prefix}invite", inline=False)
                embed.add_field(name="Note:", value="The Prefix  `&?` is only required in servers. All the commands will work without the prefix in the bots DM.", inline=False)
                embed.set_footer(text="Re-dcrypt Bot v0.7 Beta")
                embed2=discord.Embed(title="Community Server", url="https://discord.gg/c68aWWMruT", description="<a:BlobDiscord:779402415916580864> Join our community server <a:redcryptexcited:781090077748494336>", color=0x39ff14)
                embed2.set_author(name="Re-Dcrypt", icon_url="https://i.imgur.com/ynad6vI.png")
                embed2.set_thumbnail(url="https://i.imgur.com/ynad6vI.png")
                embed2.set_footer(text="Re-dcrypt Bot v0.7 Beta")
                await message.channel.send(embed=embed)
                await message.channel.send(embed=embed2)
                
            elif message.content.startswith(f"{prefix}invite")  or message.content.startswith("&?invite"):
                await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=775629409494630410&permissions=67451968&scope=bot')
            
            else:
                e404 = text2art("404","banner3")
                embed2=discord.Embed(title="Well that's unfortunate. The command that you entered couldn't be found", url="https://bit.ly/3dhfRHD", description=f"```{e404}```", color=0x39ff14)
                embed2.set_author(name="Re-Dcrypt", icon_url="https://i.imgur.com/ynad6vI.png")
                embed2.set_thumbnail(url="https://i.imgur.com/ynad6vI.png")
                embed2.set_footer(text="Re-dcrypt Bot v0.7 Beta")
                #await message.channel.send(f"```Well that's unfortunate. The command that you entered couldn't be found```")
                await message.channel.send(embed=embed2)

client = MyClient()
