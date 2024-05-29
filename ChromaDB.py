import random
import string
import numpy as np
import time
import chromadb

lengths = [10, 100, 1000, 10000]
array1 = np.random.rand(512)
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

client = chromadb.Client()
collection = client.create_collection("test2")
db_time_chroma = []
search_time_chroma = []
for len in lengths:
  data = np.random.rand(len, 512).astype('float32')
  idz = [generate_random_string(16) for i in range(len)]
  strt = time.time()
  collection.add(
      ids=idz,
      embeddings=data,
  )
  end = time.time() - strt
  db_time_chroma.append(end)
  print('Create Database Time(): ', end)
  strt = time.time()
  results = collection.query(array1.reshape((1, 512)),
      n_results=100)
  end = time.time() - strt
  search_time_chroma.append(end)
  print('Search Time (ChromaDB) :', end)

# Create Db for 100,000 vectors
  
from tqdm import tqdm
collection = client.create_collection("test0")
strt = time.time()
for len in tqdm(range(5)):
  data = np.random.rand(20000, 512).astype('float32')
  idz = [generate_random_string(16) for i in range(20000)]
  collection.add(
      ids=idz,
      embeddings=data,
  )
end = time.time() - strt
db_time_chroma.append(end)
print('Create Database Time(): ', end)

strt = time.time()
results = collection.query(array1.reshape((1, 512)),
    n_results=100)
end = time.time() - strt
search_time_chroma.append(end)
print('Search Time (ChromaDB) :', end)

# Part3: create DB for 500,000 vectors

collection = client.create_collection("test7")
strt = time.time()
for len in tqdm(range(20)):
  data = np.random.rand(25000, 512).astype('float32')
  idz = [generate_random_string(16) for i in range(25000)]
  collection.add(
      ids=idz,
      embeddings=data,
  )
end = time.time() - strt
db_time_chroma.append(end)
print('Create Database Time(): ', end)

strt = time.time()
results = collection.query(array1.reshape((1, 512)),
    n_results=100)
end = time.time() - strt
search_time_chroma.append(end)
print('Search Time (ChromaDB) :', end)