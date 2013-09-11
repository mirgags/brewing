class Hop(object):

    def __init__(self, name):
        self.name = name


    def aau(self):
        hops = []
        hop_name = self.name.upper()
        with open('hop_list.txt') as hop_list:
            for line in hop_list:
                hops.append({line.rstrip()})
        for hop in hops:
            hops[hops.index(hop)]['name']
            if hop_name.startswith(hop[len(hop)-1]['name'].upper):
                return hops['aau']


    def origin(self):
        with open('hop_list.txt') as hop_list:
            hops = []
            for line in hop_list:
                hops.append(line.rstrip())
        for hop in hops:
            if self.name.upper == startswith(hop['name'].upper):
                return hops['origin']
