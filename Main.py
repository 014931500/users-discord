import requests,random
from requests import get,post

Token= str(input("Please Enter Token : "))
num= int(input("Enter The number of usernames ? :"))
discord= "https://discordapp.com/api/webhooks/1121345141966381056/CtuF92VkTLXgIGm4rKcTN2j6hXn7fw6Bi8ruqOpnc55SkiqPpGeZxx41JFIchL31jQOa"
gif = "https://i.pinimg.com/originals/c2/32/7f/c2327f218eb515211a15bd513fe4265f.gif"

fuser= "jpno"
while True:
    chars="qw_ertyuiopa.123456789.0sdfghjkl_z.xc_vbn_mqwer.t_yuiopasd0123466.559856_fghjkl.zxcvbnmqwert000.yuio_pasdf.ghjklzxc.vbnmqw.ertyuiopasd_fghj.klzx.cvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890.";user=""
    for user in range(1):
        user=""
        for item in range(num):
            user+=random.choice(chars)

        url= "https://discord.com/api/v9/users/@me/relationships"
        headers={
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"en-US,en;q=0.9,ar;q=0.8",
            "Authorization":f"{Token}",
            "Content-Length":"20",
            "Content-Type":"application/json",
            "Cookie":"__dcfduid=cf576c80336511ed920e3f458d8db9d4; __sdcfduid=cf576c81336511ed920e3f458d8db9d445af67e5e809f3f17ebcad3cf9d3d3295abc987db2fd05b8c5acae99c5a09236; __cfruid=1e59b0d1a6360972d9c60b3f2fb4360a1447d790-1687415491; __cf_bm=7w8LP6W7baOkDGyEdDgjnk_9LwQ8cPYJMTWOBERjdPo-1687415499-0-Ae7ISf9drWNcKJClysmuojhko0SXhI3O/mWPiu/UoKZdbP977boAVUDAmmvL5b0hrA==",
            "Origin":"https://discord.com",
            "Referer":"https://discord.com/channels/@me",
            "Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Sec-Ch-Ua-Mobile":"?0",
            "Sec-Ch-Ua-Platform":"Windows",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "X-Debug-Options":"bugReporterEnabled",
            "X-Discord-Locale":"en-US",
            "X-Discord-Timezone":"Asia/Riyadh",
            "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIwNzQ3MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        data={
            "username":user
        }
        req = requests.post(url=url, headers=headers, data=data)
        if req.status_code==429:
            print(f"This username Available @{user} "+req.text)
            data = {}
            data["embeds"] = [{"description": f"\n • New username’s Claimed : @{user}","color": random.choice([0x8f12e3,0x6e09b3]),"thumbnail": {"url": gif},"author": {"name": "Discord ."}}]
            post(url=discord, json=data)
        else:print(req.text)
