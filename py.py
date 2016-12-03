import requests
import lxml.etree
from lxml import html
import urllib.request



def varsha(imdbID):


    url = "http://www.imdb.com/title/" + imdbID +"/episodes?season=1"
    response = urllib.request.urlopen(url)
    page_source = response.read()

    tree= html.fromstring(page_source)

    foo = tree.xpath('//h3[@id="nextEpisode"]/span/text()')

    if foo == []:
        print('Show has ended or show is between seasons.\n')
    else:
        print(foo[0][6:-1])




def get():


    while True:

        epTitle = input('Search by Title: ')
        year = input('Year: ')
        
        # search by title and year
        
        #r = requests.get('http://imdbapi.poromenos.org/js/?name=' + epTitle + '&year=' + year)
        #return r.json()

        w = requests.get('http://www.omdbapi.com/?type=series&s=' + epTitle + '&year=' + year)


        if int(w.json()['totalResults']) > 1:
            verb = 'are'
            result = 'results.'
        else:
            verb = 'is'
            result = 'result.'
            
        print('There are',w.json()['totalResults'],result)


        list_of_eps = []
        option = 0
        
        for eachDict in w.json()['Search']:
            print(str(option) +': ',(eachDict['Title']))
            option+=1
            

            
            list_of_eps += [[eachDict['Title'],eachDict['imdbID']]]
            #Also access each poster image using eachDict['Poster']

        num = int(input('Select an option: '))
        
        imdbID= list_of_eps[num][1]

        varsha(imdbID)
    
        again = input('Enter another search?\n')
        affirm = ['yes', 'sure', 'y', 'ok', 'okay']
    
        if again.lower() not in affirm:
            break
    




