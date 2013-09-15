import lxml.html
import pickle


tree = lxml.html.parse('http://www.onebeer.net/grainchart.html')
root = tree.getroot()
grain_list = {} 
filename = open('grain_list.pkl', 'wb')

for e in root.cssselect("tr"):
    item = e.text_content()
    item = item.splitlines()
    item = [w.replace("\t", '') for w in item]
    if 'Crystal Malt' in item[0]:
        grain_list["%s %s" % (item[0], item[1])] = (
                                                 {'lovibond': item[1], 
                                                  'gravity': item[2], 
                                                  'character': item[3]}
                                                 )
    else:
        grain_list[item[0]] = (
                              {'lovibond': item[1], 
                               'gravity': item[2], 
                               'character': item[3]}
                              )

pickle.dump(grain_list, filename)
filename.close
