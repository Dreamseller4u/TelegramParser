from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputPhoneContact
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest, AddContactRequest
import sys
import csv
import traceback
import time
import random


api_id = 000000
api_hash = ''
phone = '+62895416029826'

client = TelegramClient(phone, api_id, api_hash)


async def main():
    me = await client.get_me()

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

    g_index = input("Input group1 index : ")
    target_group = groups[int(g_index)]

    print('Try to find all users ...')
    users = await client.get_participants(target_group);

    utu = []
    with open('users.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=' ', lineterminator='\n')
        for user in users:
            if user.username and user.bot == False and user.access_hash:
                username = user.username
                if username not in utu:
                    utu.append(username)
                    writer.writerow([f'{username}'])
                else:
                    continue
 
    print('Complite')





with client:
    client.loop.run_until_complete(main())


