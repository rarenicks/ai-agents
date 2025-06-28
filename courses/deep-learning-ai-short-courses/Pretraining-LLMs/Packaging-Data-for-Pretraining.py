#!/usr/bin/env python
# coding: utf-8

# # Lesson 3: Data Packaging
# ## 1. Tokenizing and creating input_ids
# 
# Start by loading the dataset from the previous lesson:

# In[1]:


import datasets

dataset = datasets.load_dataset(
    "parquet", 
    data_files="./data/preprocessed_dataset.parquet", 
    split="train"
)
print(dataset)


# Use the `shard` method of the Hugging Face `Dataset` object to split the dataset into 10 smaller pieces, or *shards* (think shards of broken glass). You can read more about sharding at [this link](https://huggingface.co/docs/datasets/en/process#shard).

# In[2]:


dataset = dataset.shard(num_shards=10, index=0)
print(dataset)


# Load the tokenizer and try it out:

# In[3]:


from transformers import AutoTokenizer
model_path_or_name = "./models/SOLAR-10.7B-v1.0"
tokenizer = AutoTokenizer.from_pretrained(
    model_path_or_name, 
    use_fast=False
)


# In[4]:


tokenizer.tokenize("I'm a short sentence")


# Create a helper function:

# In[5]:


def tokenization(example):
    # Tokenize
    tokens = tokenizer.tokenize(example["text"])

    # Convert tokens to ids
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Add <bos>, <eos> tokens to the front and back of tokens_ids 
    # bos: begin of sequence, eos: end of sequence
    token_ids = [
        tokenizer.bos_token_id] \
        + token_ids \
        + [tokenizer.eos_token_id
    ]
    example["input_ids"] = token_ids

    # We will be using this column to count the total number of tokens 
    # in the final dataset
    example["num_tokens"] = len(token_ids)
    return example


# Tokenize all the examples in the pretraining dataset:

# In[6]:


dataset = dataset.map(tokenization, load_from_cache_file=False)
print(dataset)


# In[7]:


sample = dataset[3]

print("text", sample["text"][:30]) # 
print("\ninput_ids", sample["input_ids"][:30])
print("\nnum_tokens", sample["num_tokens"])


# Check the total number of tokens in the dataset:

# In[8]:


import numpy as np
np.sum(dataset["num_tokens"])


# ## 2. Packing the data

# ![Packing data for training](./data_packing.png)

# Concatenate input_ids for all examples into a single list:

# In[9]:


input_ids = np.concatenate(dataset["input_ids"])
print(len(input_ids))


# In[10]:


max_seq_length = 32


# In[11]:


total_length = len(input_ids) - len(input_ids) % max_seq_length
print(total_length)


# Discard extra tokens from end of the list so number of tokens is exactly divisible by `max_seq_length`:

# In[12]:


input_ids = input_ids[:total_length]
print(input_ids.shape)


# In[13]:


input_ids_reshaped = input_ids.reshape(-1, max_seq_length).astype(np.int32)
input_ids_reshaped.shape  


# In[14]:


type(input_ids_reshaped)


# Convert to Hugging Face dataset:

# In[15]:


input_ids_list = input_ids_reshaped.tolist()
packaged_pretrain_dataset = datasets.Dataset.from_dict(
    {"input_ids": input_ids_list}
)
print(packaged_pretrain_dataset)


# ## 3. Save the packed dataset to disk

# In[16]:


packaged_pretrain_dataset.to_parquet("./data/packaged_pretrain_dataset.parquet")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




