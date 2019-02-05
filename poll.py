import time, os, requests

num = input( "\x1b[1;31;50m How many poll:\x1b[0m" )
if(int(num)):
    def pollcode():
        Proxy = {
            'http' : "socks5://127.0.0.1:9050",
            'https' :"socks5://127.0.0.1:9050"
        }
        Post = {'answer': '4'} # change answer
        url = 'https://vote.pollcode.com/21673531' # change url poll
        res = requests.post(url, proxies=Proxy, data=Post, timeout=100, verify=False)
        ip  = requests.get('http://icanhazip.com',proxies=Proxy)
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m ' + ip.text)
        os.system("killall -HUP tor")
        time.sleep(0.3)

    for i in range(0, num):
        pollcode()
