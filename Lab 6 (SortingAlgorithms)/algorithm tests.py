import random
from comparison_sort import selection_sort, quick_sort
import time

lst_size = [1000, 2000, 4000, 8000, 16000]
for i in lst_size:
    random.seed(1)
    alist = random.sample(range(1000000), i)
    alist.sort()
    random.seed(1)
    flist = random.sample(range(1000000), i)
    selection_sort(flist)
    self.assertEqual(flist, alist)
    
