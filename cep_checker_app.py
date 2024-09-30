
"""
Projeto Consulta de CEP
Versão: 1.97
Autor: Prof. Sauer
Site: www.sauer.pro.br
Redes sociais:
    - Email: sauer@simplificatreinamentos.com.br
    - Instagram: https://www.instagram.com/prof.alesauer/
    - Facebook: https://www.facebook.com/prof.alesauer
    - YouTube: https://www.youtube.com/@prof.alesauer
    - LinkedIn: www.linkedin.com/in/alesauer

Este projeto utiliza Flask para criar uma interface web onde o usuário pode inserir um CEP, e a aplicação faz
uma consulta à API ViaCEP para retornar informações detalhadas sobre o endereço associado ao CEP.

Dependências:
    - Flask
    - requests
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Rota principal que exibe o formulário para inserção do CEP.
    Se o método for POST, faz a consulta à API ViaCEP e retorna os dados ou erros.
    """
    if request.method == "POST":
        # Recebendo o CEP enviado pelo formulário
        cep = request.form.get("cep")
        # Montando a URL da API ViaCEP para a consulta
        url = f"https://viacep.com.br/ws/{cep}/json/"
        
        try:
            # Fazendo a requisição GET à API com o CEP
            response = requests.get(url, proxies=proxy)
            if response.status_code == 200:
                # Se a resposta for bem-sucedida, renderizamos os dados
                data = response.json()
                return render_template("index.html", data=data)
            else:
                # Se houver erro na solicitação, exibimos uma mensagem de erro
                error = f"Erro na solicitação: {response.status_code}"
                return render_template("index.html", error=error)
        except Exception as e:
            # Em caso de falha de conexão ou outro erro, capturamos a exceção
            error = f"Erro de conexão: {e}"
            return render_template("index.html", error=error)

    # Caso seja um GET (primeira visita à página), apenas renderizamos o formulário
    return render_template("index.html")

if __name__ == "__main__":
    # Executa a aplicação Flask no modo de depuração
    app.run(debug=True, host='0.0.0.0')
