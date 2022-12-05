import requests
from bs4 import BeautifulSoup
import json

    
def find_words():
    first_word = input('Ведите слово для поиска: ')
    second_word = input('Ведите слово для поиска: ')
    
    answer = {
        first_word: 0,
        second_word: 0
    }
    urls = open('urls.txt',encoding='utf-8')
    for line in urls:
        url = line.strip()
        r=requests.get(url) 

        soup = BeautifulSoup(r.text,'lxml')
        t = soup.findAll('p')
        for i in t:
            for word in i.text.split():
                if word == first_word:
                    answer[first_word] += 1
                elif word == second_word:
                    answer[second_word] += 1
                    
    
    with open('answer.json','w') as outfile:
        json.dump(answer, outfile)

if __name__ == '__main__':
    find_words()