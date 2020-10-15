import configparser

from agenda.adapter.repositoryContato import RepositoryContato
from agenda.application.agendaService import AgendaService
from agenda.presentation.agenda import Agenda

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    repository = RepositoryContato(config['DEFAULT']['mongodb'])
    application = AgendaService(repository)
    agenda = Agenda(application)
    agenda.executar()