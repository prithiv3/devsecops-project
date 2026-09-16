from http.server import BaseHTTPRequestHandler, HTTPServer


class DevSecOpsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            message = """
            <html>
                <head>
                    <title>DevSecOps Project</title>
                </head>
                <body>
                    <h1>DevSecOps Pipeline is Running!</h1>
                    <p>Application deployed using Docker and Kubernetes.</p>
                    <p>Jenkins + Trivy + Ansible + Terraform + Minikube</p>
                </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(message.encode())

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8080), DevSecOpsHandler)

print("DevSecOps application running on port 8080")

server.serve_forever()
