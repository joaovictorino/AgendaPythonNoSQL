import common
from flask import jsonify, request, render_template
app = common.app
config = common.config
from agenda.application.agendaService import AgendaService
from agenda.domainModel.exception.contatoJaCadastrado import ContatoJaCadastrado

@app.route("/")
def index():
    pagina = open("./src/agenda/presentation/view/index.html", "r")
    return pagina.read()

@app.route("/contato/criar", methods=["POST"])
def criarContato():
    applicationService = createService()
    try:
        applicationService.inserir(request.form["nome"], request.form["numero"])
    except ContatoJaCadastrado:
        response = jsonify('Contato já cadastrado')
        response.status_code = 500
        return response
    except ValueError as exc:
        response = jsonify(str(exc))
        response.status_code = 500
        return response

    return 'OK', 201

def createService():
    repository = common.createRepository()
    return AgendaService(repository)
