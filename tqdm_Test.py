# coding=utf-8
# @Author   : zpchcbd HG team
# @Time     : 2021-08-31 17:50

from time import sleep
import random
from tqdm import tqdm
from multiprocessing import Pool, freeze_support, RLock

L = list(range(24))  # works until 23, breaks starting at 24


def progresser(n):
    text = f'#{n}'

    sampling_counts = 10
    with tqdm(total=sampling_counts, desc=text, position=n + 1) as pbar:
        for i in range(sampling_counts):
            sleep(random.uniform(0, 1))
            pbar.update(1)


if __name__ == '__main__':
    freeze_support()
    p = Pool(processes=None, initargs=(RLock(),), initializer=tqdm.set_lock)
    p.map(progresser, L)
    print('\n' * (len(L) + 1))
