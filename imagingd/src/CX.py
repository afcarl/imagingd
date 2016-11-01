
import json
import itertools

class Network:

    def __init__(self, CX):
        self.raw = json.loads(CX)
        self.meta_data = [ MetaData(meta_data) for meta_data in self.getAspect('metaData') ]
        self.nodes = [ Node(node) for node in self.getAspect('nodes') ]
        self.edges = [ Edge(edge) for edge in self.getAspect('edges') ]
        self.network_attributes = [ NetworkAttribute(attribute) for attribute in self.getAspect('networkAttributes') ]
        self.node_attributes = [ NodeAttribute(attribute) for attribute in self.getAspect('nodeAttributes') ]
        self.edge_attributes = [ EdgeAttribute(attribute) for attribute in self.getAspect('edgeAttributes') ]

    def getAspect(self, name):
        return self.flatten([ element[name] for element in self.raw if name in element ])

    def flatten(self, aspect):
        return list(itertools.chain.from_iterable(aspect))

class MetaData:

    def __init__(self, CX):
        self.id_counter = CX.get('idCounter')
        self.element_count = CX.get('elementCount')
        self.checksum = CX.get('checkSum')
        self.consistency_group = CX['consistencyGroup']
        self.last_update = CX['lastUpdate']
        self.name = CX['name']
        self.properties = CX['properties']
        self.version = CX['version']

class Node:

    def __init__(self, CX):
        self.id = CX['@id']

class Edge:

    def __init__(self, CX):
        self.id = CX['@id']
        self.source_id = CX['s']
        self.target_id = CX['t']
        self.interaction = CX['i']

class NetworkAttribute:

    def __init__(self, CX):
        self.name = CX['n']
        self.value = CX['v']

class NodeAttribute:

    def __init__(self, CX):
        self.node_id = CX['po']
        self.name = CX['n']
        self.value = CX['v']

class EdgeAttribute:

    def __init__(self, CX):
        self.edge_id = CX['po']
        self.name = CX['n']
        self.value = CX['v']
