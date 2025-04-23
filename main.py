#!/usr/bin/env python
# coding: utf-8

# In[1]:


# main.py
import datetime

def log_time():
    now = datetime.datetime.now()
    with open("log.txt", "a") as file:
        file.write(f"Script ran at: {now}\n")
    print("Logged the time successfully.")

if __name__ == "__main__":
    log_time()

