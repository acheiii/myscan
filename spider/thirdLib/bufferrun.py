# coding=utf-8
# @Author   : zpchcbd HG team
# @Time     : 2021-08-26 21:25
from core.setting import HTTP_PROXY
from spider.thirdLib.public import *
from spider.thirdLib import BaseThird


class Bufferover(BaseThird):
    """
    bufferover third spider
    """
    def __init__(self, domain):
        super().__init__()
        self.domain = domain
        self.addr = "http://dns.bufferover.run/dns?q=.{}"
        self.source = 'bufferover'

    async def getSubdomain(self, proxy):
        try:
            # proxies = {'http': f'http:{proxy}', 'https': f'https:{proxy}'}
            # resList = []
            # scraper = cfscrape.create_scraper()  # 绕Cloudflare验证码
            # resp = scraper.get(url=self.addr.format(self.domain), headers=self.headers, verify=False,
            #                    timeout=self.reqTimeout, proxies=proxies)
            # text = resp.text
            # FDNS_A_value = json.loads(text)['FDNS_A']
            # if FDNS_A_value:
            #     for _ in FDNS_A_value:
            #         subdomain = _.split(',')[-1]
            #         resList.append(subdomain)
            #     return resList
            # else:
            #     print('bufferover API No Subdomains.')
            async with aiohttp.ClientSession(headers=self.headers) as session:
                proxies = 'http://{}'.format(proxy)
                resList = []
                async with session.get(url=self.addr.format(self.domain), verify_ssl=False, timeout=10, proxy=proxies) as response:
                    text = await response.text(encoding='utf-8')
                    FDNS_A_value = json.loads(text)['FDNS_A']
                    if FDNS_A_value:
                        for _ in FDNS_A_value:
                            subdomain = _.split(',')[-1]
                            resList.append(subdomain)
                        return resList
                    else:
                        print('[-] bufferover No data query.')
        except TimeoutError:
            print('[-] curl dns.bufferover.run error, the error is Timeout.')
        except ConnectionRefusedError:
            print('[-] curl dns.bufferover.run error, the error is ConnectionRefused.')
        except Exception as e:
            print('[-] curl dns.bufferover.run error, the error is {}'.format(e.args))

    async def spider(self):
        async def getProxy():
            url = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000'
            try:
                async with aiohttp.ClientSession(headers=self.headers) as session:
                    async with session.get(url=url, verify_ssl=False, timeout=self.reqTimeout, proxy=HTTP_PROXY) as response:
                        if response is not None:
                            text = await response.text()
                            if text:
                                proxyList = [x for x in text.split('\r\n') if x != '']
                                print('[+] curl api.proxyscrape.com grabbed proxy success.')
                                return proxyList
                            else:
                                print('[-] curl api.proxyscrape.com grabbed proxy fail.')
            except aiohttp.ClientHttpProxyError:
                print('[-] curl api.proxyscrape.com need outer proxy.')
                return []
            except asyncio.TimeoutError:
                print("[-] curl api.proxyscrape.com timeout, check your proxy.")
                return []
            except Exception as e:
                print("[-] curl api.proxyscrape.com error, thr error is {}".format(e.args))
                return []
        print('[+] Load bufferover api ...')
        t = asyncio.create_task(getProxy())
        proxyList = await t
        if proxyList:
            taskList = []
            for _ in proxyList:
                taskList.append(asyncio.create_task(self.getSubdomain(_)))
            res = await asyncio.gather(*taskList)
            for aList in res:
                if aList is None:
                    continue
                self.resList.extend(aList)
            self.resList = list(set(self.resList))
            print('[+] [{}] [{}] {}'.format(self.source, len(self.resList), self.resList))
        return self.resList


async def do(domain):
    bufferover = Bufferover(domain)
    res = await bufferover.spider()
    return res


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(do('nbcc.cn'))
