#!/usr/bin/env python3
"""Serveur HTTP statique — ALLO BRISE DE GLACE (aperçu Emergent).

Sert le contenu de /app/frontend/dist sur le port 3000.
En production, Nginx remplace ce serveur (voir README.md).
"""
import http.server
import os
import socketserver

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
PORT = int(os.environ.get("PORT", "3000"))

SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


class StaticHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST, **kwargs)

    def log_message(self, *args):
        pass

    def end_headers(self):
        for key, value in SECURITY_HEADERS.items():
            self.send_header(key, value)
        if self.path.startswith("/assets/"):
            self.send_header("Cache-Control", "public, max-age=604800")
        else:
            self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            try:
                with open(os.path.join(DIST, "404.html"), "rb") as handle:
                    body = handle.read()
            except OSError:
                body = b"<h1>Page introuvable</h1>"
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


class ThreadingServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with ThreadingServer(("0.0.0.0", PORT), StaticHandler) as server:
        print(f"ALLO BRISE DE GLACE — serving {DIST} on 0.0.0.0:{PORT}")
        server.serve_forever()
