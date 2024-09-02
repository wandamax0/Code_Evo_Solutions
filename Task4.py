import http.server
import socketserver
import pyqrcode
import os
import webbrowser
from PIL import Image
import io
import png

def generate_qr_code(ip_address, port):
    """Generates a QR code for the given IP address and port."""
    qr_code = pyqrcode.create(f"http://{ip_address}:{port}")
    qr_code.png("qr_code.png", scale=6)

def start_server(port):
    """Starts the HTTP server on the specified port."""
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Serving at port:", port)
        httpd.serve_forever()

def main():
    """Main function to orchestrate the file-sharing app."""
    port = 8000  # You can change the port number
    user_name = "priyagaude"  # Replace with your name

    # Get the local IP address
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    generate_qr_code(ip_address, port)

    # Open the QR code in a web browser
    webbrowser.open("qr_code.png")

    # Start the HTTP server
    start_server(port)

if __name__ == "__main__":
    main()