from flask import render_template
import db_connection

# App
connex_app = db_connection.connex_app

# Lendo o arquivo swagger.yml e configurando endpoints
connex_app.add_api("swagger.yml")

# Criando uma rota "/"
@connex_app.route("/")
def home():

    return render_template("guide.html")

if __name__ == "__main__":
    connex_app.run(debug=False)