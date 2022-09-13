#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from PIL import Image, ImageDraw, ImageFont


# In[16]:


data = "results.csv"


# In[17]:


df = pd.read_csv(data)


# In[94]:


data = df.to_dict(orient='records')


# In[95]:


font = ImageFont.truetype("Agrandir-wide.otf", size=40)


# In[96]:


def makeCards(data):
    template = Image.open("template.png")
    draw = ImageDraw.Draw(template)

    draw.text((730, 320), str(data['Name'].upper()), font=font, fill='white')
    draw.text((730, 440), str(data['Uni Roll No.']), font=font, fill='white')
    draw.text((730, 560), str(data['Roll No.']), font=font, fill='white')
    draw.text((730, 670), str(data['1st']), font=font, fill='white')
    draw.text((730, 785), str(data['2nd']), font=font, fill='white')
    draw.text((730, 900), str(data['3rd']), font=font, fill='white')
    draw.text((730, 1010), str(data['CGPA']), font=font, fill='white')
    draw.text((730, 1120), str(data['Status']), font=font, fill='white')

    return template


# In[102]:


for record in data:
    card = makeCards(record)
    card = card.convert('RGB')
    card.save(f"results/{record['Roll No.']}.jpg")

