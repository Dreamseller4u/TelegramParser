from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError


import asyncio
import csv
import traceback
import random


api_id = 000000
api_hash = ''
main_accoutn = '+62895416029826'
accounts = ['+62895416029826','+62895416029826','+62895416029826']
users =[]   


async def chooce_tareget_group(client):
    async with client:
        me = await client.get_me()
        
        print('Working with', me.first_name)
        
        global target_group_entity 
        chats = []
        groups = []

        result = await client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=202,
                hash=0,
            ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue
        
        print('Выберите номер группы из перечня:')
        i = 0
        for g in groups:
            print(str(i) + '- ' + g.title)
            i += 1

        g_index = input('Choose the group')
        
        target_group_entity = groups[int(g_index)]

async def create_user_list():
    with open('users.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for i in data:
        users.append(i[0])
    print(f'Data ready to use .')

async def work(client):
    async with client:
        me = await client.get_me()
        
        print('Working with', me.first_name)

        # Add user to target group
        n = 0
        for user in users:
            n += 1
            if n % 50 == 0:
               await asyncio.sleep(900)
            try:
                user_to_add = await client.get_input_entity(user)
                # await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                print(f'{me.first_name} added user {user} to {target_group_entity.title}')
                print("Waiting for 60-180 Seconds...")
                users.remove(user)
                print(f'Lenght of users must me cutted check it out : {len(users)}')
                await asyncio.sleep(random.randint(60,80))
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print(f'-------------------------- {user}----------------------------')
            except UserPrivacyRestrictedError:
                print("The user's privacy settings do not allow you to do this. Skipping.")
            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue

        

async def main():
    tasks = [work(TelegramClient(phone, api_id, api_hash)) for phone in accounts]
    await chooce_tareget_group(TelegramClient(main_accoutn, api_id, api_hash))
    await asyncio.gather(
        create_user_list(),
        *tasks,
    )

asyncio.run(main())