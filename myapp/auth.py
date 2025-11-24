from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from functools import wraps

# Cria o Blueprint de Autenticação
auth = Blueprint('auth', __name__)

# Decorador de Login (Pode ser em um arquivo utils.py ou no main.py)
def login_required(f):
    """Verifica se o usuário está na sessão."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # flash('Você precisa estar logado para acessar esta página.')
            return redirect(url_for('auth.login')) # Redireciona para a rota de login
        return f(*args, **kwargs)
    return decorated_function

# Exemplo de Rota de Login aprimorada:
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        # 1. VERIFICAÇÃO REAL (BD)
        # user = verificar_credenciais_no_bd(email, senha) 
        
        # Simulação de Login BEM SUCEDIDO
        if email == 'teste@exemplo.com': # Apenas para simulação
            session['user_id'] = 1  # Armazena algo único do usuário na sessão
            session['user_email'] = email
            # flash('Login realizado com sucesso!')
            return redirect(url_for('main.dashboard'))
        else:
            # flash('Email ou senha incorretos.', 'error')
            return redirect(url_for('auth.login'))
            
    return render_template('login.html')

# Rota de Logout (ESSENCIAL)
@auth.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove o 'user_id' da sessão
    session.pop('user_email', None)
    # flash('Você foi desconectado.')
    return redirect(url_for('auth.index')) # Redireciona para a tela inicial
