import xml.etree.ElementTree as ET


tree = ET.parse('List_of_hop_varieties.xml')
root = tree.getroot()
hop_list = []
filename = open('hop_list.txt', 'w')


for name in root:
    hop_list.append({'name': name[0].text,
                     'aau': name[2].text,
                     'origin': name[1].text
                   })


for hop in hop_list:
#    print "**************"
#    print "Name: %s" % hop['name']
#    print "Alpha Acid: %s" % hop['aau']
#    print "Country: %s" % hop['origin']
    filename.write("%s\n" % hop)

filename.close
