from flask import Flask, render_template, request, redirect, url_for

# Inicializa a aplicação Flask
app = Flask(__name__)

# --- ROTAS DE AUTENTICAÇÃO E PÁGINA INICIAL ---

@app.route('/')
def index():
    """Página inicial (landing page)"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de Login. Se o método for POST, 'loga' o usuário e redireciona."""
    if request.method == 'POST':
        # Aqui você colocaria sua lógica de verificação de login
        # Como é um exemplo, vamos apenas redirecionar para o dashboard
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Página de Cadastro. Se o método for POST, 'cadastra' e redireciona."""
    if request.method == 'POST':
        # Aqui você colocaria sua lógica de salvar o novo usuário
        # Redireciona para o dashboard após o cadastro
        return redirect(url_for('dashboard'))
    return render_template('cadastro.html')

@app.route('/recuperar_senha', methods=['GET', 'POST'])
def recuperar_senha():
    """Página de recuperação de senha."""
    if request.method == 'POST':
        # Lógica de enviar email de recuperação
        # Redireciona para a página de aviso
        return redirect(url_for('aviso_recuperacao'))
    return render_template('recuperar_senha.html')

@app.route('/aviso_recuperacao')
def aviso_recuperacao():
    """Página que avisa que o email de recuperação foi enviado."""
    return render_template('aviso_recuperacao.html')

# --- ROTAS DO PAINEL DO USUÁRIO (DASHBOARD) ---

@app.route('/dashboard')
def dashboard():
    """Página principal após o login, mostrando os salões."""
    return render_template('dashboard.html')

@app.route('/servicos')
def servicos():
    """Página que lista os serviços."""
    return render_template('servicos.html')

@app.route('/funcionarios')
def funcionarios():
    """Página que lista os funcionários (exemplo)."""
    return render_template('funcionarios.html')

@app.route('/agendar')
def agendar():
    """Página com o formulário de agendamento rápido."""
    return render_template('agendar.html')

@app.route('/perfil')
def perfil():
    """Página de perfil do usuário. O formulário de 'agendar' redireciona para cá."""
    # Você pode capturar os dados do agendamento via request.args
    # ex: salao = request.args.get('salao')
    return render_template('perfil.html')

# --- Executa o aplicativo ---
if __name__ == '__main__':
    app.run(debug=True)
