import aiohttp
import asyncio
import colorama
import os
import time

def _exit():
    time.sleep(5)
    exit()

async def check_hook(hook):
    async with aiohttp.ClientSession() as session:
        async with session.get(hook) as response:
            info = await response.text()
            return "\"message\": \"Unknown Webhook\"" not in info

async def send_message(webhook, name, message):
    async with aiohttp.ClientSession() as session:
        async with session.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://cdn.discordapp.com/attachments/1351896657142485135/1352946159966228520/IMG_0708.jpeg?ex=67dfdccd&is=67de8b4d&hm=224496bef074d6a44513af5f7c06b642f25a3f32a1a1fab112bb9f9762871770&"}) as response:
            if response.status == 204:
                print(f"{colorama.Back.CYAN} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")

async def main(webhook, name, delay, amount, message, hook_deleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            await send_message(webhook, name, message)
        except Exception as e:
            print(f"Error: {e}")
        await asyncio.sleep(float(delay))
        counter += 1
    if hook_deleter.lower() == "y":
        async with aiohttp.ClientSession() as session:
            await session.delete(webhook)
            print(f'{colorama.Fore.CYAN}Webhook deleted!')
    print(f'{colorama.Fore.GREEN}All tasks complete.')
    _exit()

async def initialize():
    print(f"""{colorama.Fore.CYAN}


███╗   ██╗ ██████╗  ██████╗████████╗██╗   ██╗██████╗ ███╗   ██╗███████╗    ██╗   ██╗ ██╗
████╗  ██║██╔═══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝    ██║   ██║███║
██╔██╗ ██║██║   ██║██║        ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗      ██║   ██║╚██║
██║╚██╗██║██║   ██║██║        ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝      ╚██╗ ██╔╝ ██║
██║ ╚████║╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗     ╚████╔╝  ██║
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝      ╚═══╝   ╚═╝
                                                                                       
                                       -by solowwprime
     """)
    webhook = input("Enter the webhook > ")
    name = input("Enter custom webhook name > ")
    message = input("Enter the message to be spammed > ")
    delay = input("Enter the delay between messages [int/float] (0.1 recommended) > ")
    amount = input("Enter the amount of messages to be spammed [int/inf] (100 recommended) > ")
    hook_deleter = input("Delete webhook after spam? (fast delete btw.) [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not await check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hook_deleter.lower() != "y" and hook_deleter.lower() != "n"):
        _exit()
    else:
        await main(webhook, name, delay, amount, message, hook_deleter)

if __name__ == '__main__':
    os.system('cls')
    os.system('title x_x - meowhook')
    colorama.init()
    asyncio.run(initialize())