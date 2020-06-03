import enum
class Sems(enum.Enum):
    DEFAULT = enum.auto()
    MYSQL = enum.auto()
    NETWORK = enum.auto()
    REQUESTS = enum.auto()
    FIREFOX = enum.auto()
    AIOHTTP = enum.auto()
    CURL = enum.auto()
    WGET = enum.auto()
    TELETHON = enum.auto()
    DOMAIN = enum.auto()

sems_names = {name.name for name in Sems}

network = [Sems.REQUESTS.name, Sems.FIREFOX.name, Sems.AIOHTTP.name, Sems.CURL.name, Sems.WGET.name, Sems.TELETHON.name,
           Sems.DOMAIN.name]
sem_attrs = ['values']
task_attrs = ['tasks', 'todo', 'busy', 'done', 'error']
attrs = sem_attrs + task_attrs
class Sel:
    def __init__(sel):
        sel.names = {'DEFAULT', 'MYSQL', 'NETWORK', 'REQUESTS', 'FIREFOX', 'AIOHTTP', 'CURL', 'WGET', 'DOMAIN', 'TELETHON', 'icorating.com'}
        sel.tasks = {'DEFAULT': set(), 'MYSQL': set(), 'NETWORK': set(), 'REQUESTS': set(), 'FIREFOX': {'https://icorating.com/ico/all'},
                  'AIOHTTP': set(), 'CURL': set(), 'DOMAIN': set(), 'TELETHON': set(),
                  'WGET': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'},
                  'icorating.com': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'}}
        sel.todo = {'DEFAULT': set(), 'MYSQL': set(), 'NETWORK': set(), 'REQUESTS': set(), 'FIREFOX': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/', 'caca'},
                  'AIOHTTP': set(), 'CURL': set(), 'DOMAIN': set(), 'TELETHON': set(),
                  'WGET': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'},
                  'icorating.com': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'}}
        sel.busy = {'DEFAULT': set(), 'MYSQL': set(), 'NETWORK': set(), 'REQUESTS': set(), 'FIREFOX': {'https://icorating.com/ico/all'},
                  'AIOHTTP': set(), 'CURL': set(), 'DOMAIN': set(), 'TELETHON': set(),
                  'WGET': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'},
                  'icorating.com': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'}}
        sel.done = {'DEFAULT': set(), 'MYSQL': set(), 'NETWORK': set(), 'REQUESTS': set(), 'FIREFOX': {'https://icorating.com/ico/all'},
                  'AIOHTTP': set(), 'CURL': set(), 'DOMAIN': set(), 'TELETHON': set(),
                  'WGET': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'},
                  'icorating.com': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'}}
        sel.error = {'DEFAULT': set(), 'MYSQL': set(), 'NETWORK': set(), 'REQUESTS': set(), 'FIREFOX': {'https://icorating.com/ico/all'},
                  'AIOHTTP': set(), 'CURL': set(), 'DOMAIN': set(), 'TELETHON': set(),
                  'WGET': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'},
                  'icorating.com': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/', 'caca'}}
        sel.values = {'DEFAULT': set(), 'MYSQL': set(), 'NETWORK': set(), 'REQUESTS': set(), 'FIREFOX': {'https://icorating.com/ico/all'},
                  'AIOHTTP': set(), 'CURL': set(), 'DOMAIN': set(), 'TELETHON': set(),
                  'WGET': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'},
                  'icorating.com': {'https://icorating.com/ico/all', 'https://icorating.com/analytics/indepth/aidcoin-rating-review/'}}
self = Sel()

def where(name, unique=True):
    if unique:
        return {attr: {sem for sem in self.names for value in getattr(self, attr).get(sem) if name in value} for attr in
                task_attrs}
    else:
        return {attr: [sem for sem in self.names for value in getattr(self, attr).get(sem) if name in value] for attr in
                task_attrs}

def count(name):
    return {attr: len(value) for attr, value in where(name, False).items()}


def clean(name):
    if name in sems_names:
        for task_attr in task_attrs:
            getattr(self, task_attr)[name] = set()
    else:
        if name in self.names:
            self.names.remove(name)
            for attr in attrs:
                del getattr(self, attr)[name]
        for attr, sems in where(name).items():
            for sem in sems:
                for value in list(getattr(self, attr).get(sem)):
                    if name in value:
                        getattr(self, attr).get(sem).remove(value)


def end(name):
    c = count(name)
    if c['tasks'] and c['done'] and c['tasks'] == c['done']:
        clean(name)
        return True

def audit(name):
    c = count(name)
    if c['tasks'] != c['todo'] + c['busy'] + c['done']:
        clean(name)
        return True


print(where('icorating.com'))
print(where('icorating.com', False))
print(count('icorating.com'))
print(end('icorating.com'))
print(count('icorating.com'))

clean('icorating.com')
print(where('icorating.com', False))
print(where('icorating.com'))

print(count('icorating.com'))
print(count('caca'))

print(audit('icorating.com'))
print(count('icorating.com'))

print(audit('caca'))
print(count('caca'))



# clean('icorating.com')
# print(self.__dict__)
# print(count('icorating.com'))
# print(end('icorating.com'))