from flask import render_template, Blueprint
from .auth import login_required # Importa o decorador

# Cria o Blueprint Principal
main = Blueprint('main', __name__)

# Rota principal (Tela de Pré-Cadastro/Login)
@main.route('/')
def index():
    return render_template('index.html')

# Rota do Dashboard (Listagem de Salões)
@main.route('/dashboard')
@login_required # Garante que só usuários logados acessem
def dashboard():
    return render_template('dashboard.html')

# ... demais rotas pós-login, também com @login_required
