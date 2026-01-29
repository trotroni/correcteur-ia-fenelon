from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from correcteur import corriger

class Serveur(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/web/index.html"

        try:
            with open(self.path[1:], "rb") as f:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f.read())
        except:
            self.send_error(404, "Fichier non trouvé")

    def do_POST(self):
        if self.path == "/corriger":
            longueur = int(self.headers['Content-Length'])
            donnees = self.rfile.read(longueur)
            texte = json.loads(donnees)["copie"]

            resultat = corriger(texte)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(resultat).encode())

if __name__ == "__main__":
    serveur = HTTPServer(("localhost", 8000), Serveur)
    print("Serveur lancé sur http://localhost:8000")
    serveur.serve_forever()
