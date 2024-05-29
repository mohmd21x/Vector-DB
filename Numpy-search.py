import numpy as np
import time
# Lengths of DB
lengths = [10, 100, 1000, 10000, 100000, 500000]

array1 = np.random.rand(1, 512)
search_time_np = []
for len in lengths:
  data = np.random.rand(len, 512)
  start_time = time.time()
  # Calculate the L2 distance
  l2_distance = np.linalg.norm(array1 - data, axis=1)
  end_time = time.time() - start_time
  search_time_np.append(end_time)
  print('Time Of Search(numpy)', end_time)