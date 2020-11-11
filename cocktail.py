# input ingredients that you have
# output cocktails made from ingredients
import json


# def __is_recipe(url):
#     if 

with open('sitemap.json') as f:
    sitemap = json.load(f)

for url in sitemap['url']:
    if __is_recipe(url['loc']): 
        print(url['loc'])