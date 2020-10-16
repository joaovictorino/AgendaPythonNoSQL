app = None
config = None

from agenda.adapter.repositoryContato import RepositoryContato

def createRepository():
    return RepositoryContato(config['DEFAULT']['mongodb'])