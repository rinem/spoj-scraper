from bs4 import BeautifulSoup
import requests

def create_url_list():
    url_list = []                                                   #List holding the links of problems
    p_counter = 0                                                   #Page Number counter->Increased by 50 each time
    main_url = 'https://www.spoj.com/problems/classical/sort=6'     #Url for problem sorted by difficulty

    print("How many problems do you want to store ?")
    n = int(input())

    while (p_counter != ((n//50)+1)*50):
        if (p_counter != 0):
            main_url = main_url+',start='+str(p_counter)
        res = requests.get(main_url, timeout = 5)
        soup = BeautifulSoup(res.content, "lxml")
        spoj = main_url[:20]                                        #SPOJ link
        link = soup.find_all('td')

        for i in range(1, 300, 6):
            problem_link = spoj+link[i].find('a')['href']           #Concatenating problem link to end of SPOJ link
            url_list.append(problem_link)
        p_counter += 50

    f = open("url-list.txt", "w+")
    for i in url_list:
        f.write(i+'\n')
    f.close();
