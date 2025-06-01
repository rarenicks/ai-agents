#!/usr/bin/env python
# coding: utf-8

# # OpenAI Function Calling
# 

# **Notes**:
# - LLMs don't always produce the same results. The results you see in this notebook may differ from the results you see in the video.
# - Notebooks results are temporary. Download the notebooks to your local machine if you wish to save your results.
# - OpenAI has announced the release of an updated GPT-3.5-Turbo model and the deprecation of the ```gpt-3.5-turbo-0613``` model. The gpt-3.5-turbo-0613 model, which has been utilized in this Short Course since its launch in October 2023, will be replaced by the ```gpt-3.5-turbo``` model.

# In[1]:


import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


# In[2]:


import json

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


# In[3]:


# define a function
functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]


# In[4]:


messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston?"
    }
]


# In[5]:


import openai


# > Note: This notebook was updated in June 2024. Consequently, we are now using the ```gpt-3.5-turbo model``` instead of the ```gpt-3.5-turbo-0613``` model featured by the instructor in the video lesson.

# In[6]:


# Call the ChatCompletion endpoint
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions
)


# > Note: The following result may differ slightly from the one shown by the instructor in the video lesson due to the model being updated.

# In[7]:


print(response)


# In[8]:


response_message = response["choices"][0]["message"]


# In[9]:


response_message


# In[10]:


response_message["content"]


# In[11]:


response_message["function_call"]


# In[12]:


json.loads(response_message["function_call"]["arguments"])


# In[13]:


args = json.loads(response_message["function_call"]["arguments"])


# In[14]:


get_current_weather(args)


# * Pass a message that is not related to a function.

# In[15]:


messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]


# > Note: This notebook was updated in June 2024. Consequently, we are now using the ```gpt-3.5-turbo model``` instead of the ```gpt-3.5-turbo-0613``` model featured by the instructor in the video lesson.

# In[16]:


response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
)


# In[17]:


print(response)


# * Pass additional parameters to force the model to use or not a function.

# In[18]:


messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="auto",
)
print(response)


# * Use mode 'none' for function call.

# In[19]:


messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="none",
)
print(response)


# * When the message should call a function and still uses mode 'none'.

# In[20]:


messages = [
    {
        "role": "user",
        "content": "What's the weather in Boston?",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="none",
)
print(response)


# * Force calling a function.

# In[21]:


messages = [
    {
        "role": "user",
        "content": "hi!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call={"name": "get_current_weather"},
)
print(response)


# * Final notes.

# In[22]:


messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston!",
    }
]
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call={"name": "get_current_weather"},
)
print(response)


# In[23]:


messages.append(response["choices"][0]["message"])


# In[24]:


args = json.loads(response["choices"][0]["message"]['function_call']['arguments'])
observation = get_current_weather(args)


# In[ ]:


messages.append(
        {
            "role": "function",
            "name": "get_current_weather",
            "content": observation,
        }
)


# In[ ]:


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
print(response)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




