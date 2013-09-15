import lxml.html
import pickle
import time





def yeast_download(url, producer, yeast_list):
    url = url
    producer = producer
    yeast_list = yeast_list

    tree = lxml.html.parse(url)
    root = tree.getroot()
     

    for e in root.cssselect("tr"):
        if not producer in e.text_content():
            item = e.text_content()
            item = item.splitlines()
            item = [w.replace("\t", '') for w in item]
            yeast_list[item[0]] = (
                                  {'producer': producer,
                                   'id_code': item[1], 
                                   'attenuation': item[2], 
                                   'flocculation': item[3],
                                   'ferment_temp': item[4],
                                   'alcohol_yield': item[5]}
                                  )

    return yeast_list


yeast_dict = {}
url_dict = {'White Labs': 'http://www.brewersfriend.com/yeast-whitelabs/',
            'Wyeast': 'http://www.brewersfriend.com/yeast-wyeast/',
            'Fermentis': 'http://www.brewersfriend.com/yeast-fermentis/'}

for company, site in url_dict.iteritems():
    yeast_download(site, company, yeast_dict)
print yeast_dict

filename = open('yeast_list.pkl', 'wb')

pickle.dump(yeast_dict, filename)
filename.close
