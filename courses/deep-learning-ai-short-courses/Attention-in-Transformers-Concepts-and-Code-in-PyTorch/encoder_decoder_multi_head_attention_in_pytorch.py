#!/usr/bin/env python
# coding: utf-8

# # Coding Attention in PyTorch!!!
# 
# By Josh Starmer

# <p style="background-color:#fff6e4; padding:15px; border-width:3px; border-color:#f5ecda; border-style:solid; border-radius:6px"> ⏳ <b>Note <code>(Kernel Starting)</code>:</b> This notebook takes about 30 seconds to be ready to use. You may start and watch the video while you wait.</p>

# ---- 
# 
# In this tutorial, we will code a class that is capable of all **3** types of **Attention** that we have studied, **Self-Attention**, **Masked Self-Attention**, and **Encoder-Decoder Attention**. We'll also code a few lines that will make **Multi-Headed Attention** work.
# 
# In this tutorial, you will...
# 
# - **[Code an Attention Class!!!](#attention)** This class will be able to perform **Self-Attention**, **Masked-Self Attention**, and **Encoder-Decoder Attention**.
# 
# - **[Calculate Encoder-Decoder Attention Values!!!](#calculate)** We'll then use the class that we created, Attention, to calculate **Encoder-Decoder Attention** values for some sample data.
#  
# - **[Code Multi-Head Attention!!!](#multi)** We'll code **Multi-Head Attention**.
# 
# - **[Calculate Mult-Head Attention!!!!](#calcMulti)** Lastly, we calculate **Multi-Head Attention** values for some sample data.
# 

# ----

# # Import the modules that will do all the work

# In[1]:


import torch ## torch let's us create tensors and also provides helper functions
import torch.nn as nn ## torch.nn gives us nn.module() and nn.Linear()
import torch.nn.functional as F # This gives us the softmax()


# <p style="background-color:#fff6ff; padding:15px; border-width:3px; border-color:#efe6ef; border-style:solid; border-radius:6px"> 💻 &nbsp; <b>Access <code>requirements.txt</code> file:</b> 1) click on the <em>"File"</em> option on the top menu of the notebook and then 2) click on <em>"Open"</em>. For more help, please see the <em>"Appendix - Tips and Help"</em> Lesson.</p>

# ----

# # Code Attention
# <a id="attention"></a>

# In[2]:


class Attention(nn.Module): 
                            
    def __init__(self, d_model=2,  
                 row_dim=0, 
                 col_dim=1):
        
        super().__init__()
        
        self.W_q = nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        self.W_k = nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        self.W_v = nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        
        self.row_dim = row_dim
        self.col_dim = col_dim


    ## The only change from SelfAttention and attention is that
    ## now we expect 3 sets of encodings to be passed in...
    def forward(self, encodings_for_q, encodings_for_k, encodings_for_v, mask=None):
        ## ...and we pass those sets of encodings to the various weight matrices.
        q = self.W_q(encodings_for_q)
        k = self.W_k(encodings_for_k)
        v = self.W_v(encodings_for_v)

        sims = torch.matmul(q, k.transpose(dim0=self.row_dim, dim1=self.col_dim))

        scaled_sims = sims / torch.tensor(k.size(self.col_dim)**0.5)

        if mask is not None:
            scaled_sims = scaled_sims.masked_fill(mask=mask, value=-1e9)
            
        attention_percents = F.softmax(scaled_sims, dim=self.col_dim)

        attention_scores = torch.matmul(attention_percents, v)

        return attention_scores


# # BAM!

# ----

# # Calculate Encoder-Decoder Attention
# <a id="calculate"></a>

# In[3]:


## create matrices of token encodings...
encodings_for_q = torch.tensor([[1.16, 0.23],
                                [0.57, 1.36],
                                [4.41, -2.16]])

encodings_for_k = torch.tensor([[1.16, 0.23],
                                [0.57, 1.36],
                                [4.41, -2.16]])

encodings_for_v = torch.tensor([[1.16, 0.23],
                                [0.57, 1.36],
                                [4.41, -2.16]])

## set the seed for the random number generator
torch.manual_seed(42)

## create an attention object
attention = Attention(d_model=2,
                      row_dim=0,
                      col_dim=1)

## calculate encoder-decoder attention
attention(encodings_for_q, encodings_for_k, encodings_for_v)


# ----

# # Code Mutli-Head Attention
# <a id="multi"></a>

# In[4]:


class MultiHeadAttention(nn.Module):

    def __init__(self, 
                 d_model=2,  
                 row_dim=0, 
                 col_dim=1, 
                 num_heads=1):
        
        super().__init__()

        ## create a bunch of attention heads
        self.heads = nn.ModuleList(
            [Attention(d_model, row_dim, col_dim) 
             for _ in range(num_heads)]
        )

        self.col_dim = col_dim
        
    def forward(self, 
                encodings_for_q, 
                encodings_for_k,
                encodings_for_v):

        ## run the data through all of the attention heads
        return torch.cat([head(encodings_for_q, 
                               encodings_for_k,
                               encodings_for_v) 
                          for head in self.heads], dim=self.col_dim)


# ----

# # Calcualte Multi-Head Attention
# <a id="calcMulti"></a>

# First, verify that we can still correctly calculate attention with a single head...

# In[5]:


## set the seed for the random number generator
torch.manual_seed(42)

## create an attention object
multiHeadAttention = MultiHeadAttention(d_model=2,
                                        row_dim=0,
                                        col_dim=1,
                                        num_heads=1)

## calculate encoder-decoder attention
multiHeadAttention(encodings_for_q, encodings_for_k, encodings_for_v)


# Second, calculate attention with multiple heads...

# In[6]:


## set the seed for the random number generator
torch.manual_seed(42)

## create an attention object
multiHeadAttention = MultiHeadAttention(d_model=2,
                                        row_dim=0,
                                        col_dim=1,
                                        num_heads=2)

## calculate encoder-decoder attention
multiHeadAttention(encodings_for_q, encodings_for_k, encodings_for_v)


# # TRIPLE BAM!!
