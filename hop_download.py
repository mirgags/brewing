import xml.etree.ElementTree as ET
import pickle


tree = ET.parse('List_of_hop_varieties.xml')
root = tree.getroot()
hop_list = {} 
filename = open('hop_list.pkl', 'wb')


for name in root:
    if name[0].text is not None:
        hop_list[name[0].text.upper()] = (
                                         {'aau': name[2].text,
                                          'origin': name[1].text}
                                         )

#for hop in hop_list:
#    print "**************"
#    print "Name: %s" % hop['name']
#    print "Alpha Acid: %s" % hop['aau']
#    print "Country: %s" % hop['origin']
pickle.dump(hop_list, filename)
filename.close
