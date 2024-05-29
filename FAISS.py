import faiss
import numpy as np
import time
from statistics import mean
# Lengths of DB
lengths = [10, 100, 1000, 10000, 100000, 500000]

db_time_faiss = []
search_time_faiss = []
for len in lengths:
  data = np.random.rand(len, 512).astype('float32')
  start_time = time.time()
  index = faiss.IndexFlatL2(512) # L2 distance index
  index.add(data)
  end_time = time.time() - start_time
  db_time_faiss.append(end_time)
  print('Create Database Time(FAISS): ', end_time)
  query_vector = np.random.rand(1, 512).astype('float32')
  k = index.ntotal
  start_time = time.time()
  distances, indices = index.search(query_vector, k)
  end_time = time.time() - start_time
  search_time_faiss.append(end_time)
  print('Time Of Search(FAISS)', end_time)

print('Avg Create Time DB(FAISS) :', mean(db_time_faiss))
print('Avg Search Time (FAISS) :', mean(search_time_faiss))