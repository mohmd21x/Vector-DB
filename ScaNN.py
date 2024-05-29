import scann
import numpy as np
import time
from statistics import mean
# Lengths of DB
lengths = [10, 100, 1000, 10000, 100000, 500000]
# creating searcher
array1 = np.random.rand(512)
db_time_scann = []
search_time_scann = []
for len in lengths:
  data = np.random.rand(len, 512).astype('float32')
  k = int(np.sqrt(data.shape[0]))
  start_time = time.time()
  searcher = scann.scann_ops_pybind.builder(data, 10, "squared_l2").tree(
      num_leaves=k, num_leaves_to_search=int(k/20), training_sample_size=2500).score_brute_force(2).reorder(20).build()
  end_time = time.time()
  scann_time = end_time - start_time
  db_time_scann.append(scann_time)
  print('Create Database Time(): ', scann_time)
  start_time = time.time()
  neighbors, distances = searcher.search(array1, final_num_neighbors=20)
  end_time = time.time()
  scann_time = end_time - start_time
  search_time_scann.append(scann_time)
  print('Time Of Search', scann_time)