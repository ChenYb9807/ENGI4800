import json
from datasets import load_dataset
dataset = load_dataset("teven/pseudo_crawl_en_seeds")

# This include most of the pseudocrawl dataset in English in BigScience.(ABC Australia not included)
# It's a little bit messy
# Teven https://huggingface.co/teven who belongs to huggingface contributes this dataset.

# For example, if we are trying to fetch news from
# Dataset Card for pseudocrawl-filtered_497_www_straitstimes_com(straitstimes is a pretty famous newspaper in Singapore)

straitstimes = {}
news_resources = dataset['train']
for i,news in enumerate(news_resources):
    if 'straitstimes' in news_resources[i]['meta']['url']:
        straitstimes[i]=news
with open('straitstimes.json','w') as f:
    json.dump(straitstimes,f)

# There are 572,281 pieces of news in straitstimes, pretty promising(1.71G json file).