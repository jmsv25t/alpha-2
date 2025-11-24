from flask import Flask
# Importa os Blueprints
from .auth import auth as auth_bp
from .main import main as main_bp

# 1. Inicializa o aplicativo Flask
app = Flask(__name__)

# Configurações de Segurança (ESSENCIAL)
# A chave secreta é usada para sessões e segurança.
app.config['SECRET_KEY'] = 'SUA_CHAVE_SECRETA_MUITO_FORTE_AQUI'

# Registra os Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# --- EXECUÇÃO ---

if __name__ == '__main__':
    # Roda o servidor.
    app.run(debug=True)
