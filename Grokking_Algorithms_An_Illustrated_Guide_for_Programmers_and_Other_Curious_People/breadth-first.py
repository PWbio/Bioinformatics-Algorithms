graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque

def person_with_Y(name):
    return name[-1] == 'y'

def search_name_end_with_y(name):
    ''' Search for first person name ended with y. '''
    search_quene = deque()
    search_quene += graph[name]
    searched = []
    while search_quene:
        person = search_quene.popleft()
        if not person in searched:
            if person_with_Y(person):
                print (person, 'end with y.')
                return True
            else:
                search_quene += graph[person]
                searched.append(person)
    return False

search_name_end_with_y('you')