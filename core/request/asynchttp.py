# coding=utf-8
# @Author   : zpchcbd HG team
# @Time     : 2021-08-27 22:06

import asyncio
from typing import Union, Tuple, Any

import aiohttp
import random
import ssl
import certifi


# @ Harvester
class AsyncFetcher:

    @staticmethod
    def getUserAgent():
        userAgents = [
            'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
            'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
        ]
        return random.choice(userAgents)

    @staticmethod
    async def fetch(session, url, params='', json=False) -> Union[str, dict, list]:
        try:
            if params != '':
                # sslcontext = ssl.create_default_context()
                async with session.get(url, verify_ssl=False, params=params, timeout=15) as response:
                    await asyncio.sleep(2)
                    return await response.text() if json is False else await response.json()
            else:
                # sslcontext = ssl.create_default_context()
                async with session.get(url, verify_ssl=False, timeout=15) as response:
                    await asyncio.sleep(2)
                    return await response.text() if json is False else await response.json()
        except Exception as e:
            # print('An exception has occurred, {}'.format(e.__str__()))
            return ''

    @staticmethod
    async def fetch2(session, url, params=''):
        headers = {'User-Agent': AsyncFetcher.getUserAgent()}
        try:
            if params != '':
                sslcontext = ssl.create_default_context(cafile=certifi.where())
                async with session.get(url, ssl=sslcontext, headers=headers, params=params, timeout=10) as response:
                    # print(response)
                    await asyncio.sleep(2)
                    return response
            else:
                sslcontext = ssl.create_default_context(cafile=certifi.where())
                async with session.get(url, ssl=sslcontext, headers=headers, timeout=10) as response:
                    await asyncio.sleep(2)
                    return response
        except Exception as e:
            # print('An exception has occurred, {}'.format(e.__str__()))
            return ''

    @staticmethod
    async def fetch4(session, urlaprams = '', json=False) -> Union[str, dict, list]:
        pass

    @staticmethod
    async def fetch3(session, url, params='', json=False) -> Union[str, dict, list]:
        try:
            if params != '':
                async with session.get(url, verify_ssl=False, params=params) as response:
                    await asyncio.sleep(2)
                    return await response.text() if json is False else await response.json()
            else:
                async with session.get(url, verify_ssl=False) as response:
                    await asyncio.sleep(2)
                    return await response.text() if json is False else await response.json()
        except Exception as e:
            # print('An exception has occurred, {}'.format(e.__str__()))
            return ''

    @classmethod
    async def postFetch(cls, url, headers='', data='', params='', json=False):
        if len(headers) == 0:
            headers = {'User-Agent': AsyncFetcher.getUserAgent()}
        timeout = aiohttp.ClientTimeout()
        try:
            if params == '':
                async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
                    async with session.post(url, data=data) as resp:
                        await asyncio.sleep(3)
                        return await resp.text() if json is False else await resp.json()
            else:
                async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
                    sslcontext = ssl.create_default_context(cafile=certifi.where())
                    async with session.post(url, data=data, ssl=sslcontext, params=params) as resp:
                        await asyncio.sleep(3)
                        return await resp.text() if json is False else await resp.json()
        except Exception as e:
            # print('An exception has occurred, {}'.format(e.__str__()))
            return ''

    @staticmethod
    async def postFetch2(session, url, data='', params='', json=False):
        try:
            if params == '':
                async with session.post(url, data=data) as resp:
                    await asyncio.sleep(3)
                    return await resp.text() if json is False else await resp.json()
            else:
                sslcontext = ssl.create_default_context(cafile=certifi.where())
                async with session.post(url, data=data, ssl=sslcontext, params=params) as resp:
                    await asyncio.sleep(3)
                    return await resp.text() if json is False else await resp.json()
        except Exception as e:
            # print('An exception has occurred, {}'.format(e.__str__()))
            return ''

    @staticmethod
    async def postFetch3(session, url, data='', params='', json=False):
        try:
            if params == '':
                async with session.post(url, data=data) as resp:
                    await asyncio.sleep(3)
                    return await resp.text() if json is False else await resp.json()
            else:
                sslcontext = ssl.create_default_context(cafile=certifi.where())
                async with session.post(url, data=data, ssl=sslcontext, params=params) as resp:
                    await asyncio.sleep(3)
                    return await resp.text() if json is False else await resp.json()
        except Exception as e:
            # print('An exception has occurred, {}'.format(e.__str__()))
            return ''

    @staticmethod
    async def takeoverFetch(session, url) -> Union[Tuple[Any, Any], str]:
        try:
            url = f'http://{url}' if str(url).startswith(('http:', 'https:')) is False else url
            async with session.get(url, timeout=10) as response:
                await asyncio.sleep(2)
                return url, await response.text()
        except Exception:
            return url, ''

    @staticmethod
    async def takeoverFetch2(session, url) -> Union[Tuple[Any, Any], str]:
        try:
            url = f'http://{url}' if str(url).startswith(('http:', 'https:')) is False else url
            async with session.get(url) as response:
                await asyncio.sleep(2)
                await response.text()
        except Exception:
            return ''

    @classmethod
    async def fetchAll(cls, urls, headers='', params='', json=False, takeover=False) -> list:
        timeout = aiohttp.ClientTimeout()
        if len(headers) == 0:
            headers = {'User-Agent': AsyncFetcher.getUserAgent()}
        if takeover:
            async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
                tuples = await asyncio.gather(*[AsyncFetcher.takeoverFetch(session, url) for url in urls])
                return tuples
        if len(params) == 0:
            async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
                texts = await asyncio.gather(*[AsyncFetcher.fetch(session, url, json=json) for url in urls])
                return texts
        else:
            async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
                texts = await asyncio.gather(*[AsyncFetcher.fetch(session, url, params, json) for url in urls])
                return texts
