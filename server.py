"""
This module is responsible for starting the server and handling requests to the server.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from repository import get_all, retrieve, create, delete, update

METHODS_MAPPER = {
    "GET": get_all,
    "RETRIEVE": retrieve,
    "POST": create,
    "PUT": update,
    "DELETE": delete
}

class HandleRequests(BaseHTTPRequestHandler):
    """
    Controls the functionality of any GET, PUT, POST, DELETE requests to the server.
    """

    def parse_url(self, path):
        """
        Parses the URL path and returns the resource, id, and query parameters.
        """
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = url_components.query.split("&")
        resource = path_params[0]
        _id = None

        try:
            _id = int(path_params[1])
        except (IndexError, ValueError):
            pass

        return (resource, _id, query_params)

    def do_GET(self):
        """
        Handles GET requests to the server.
        """
        (resource, _id, _) = self.parse_url(self.path)

        if _id is not None:
            response = retrieve(resource, _id)  # Call the retrieve function
        else:
            response = get_all(resource)  # Call the get_all function

        if response is not None:
            self._set_headers(200)
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            response = "Resource not found."
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """
        Handles POST requests to the server.
        """
        self._set_headers(201)
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, _id, _) = self.parse_url(self.path)

        new_item = None

        if resource == "orders":
            if all(key in post_body for key in ("metalId", "sizeId", "styleId")):
                self._set_headers(201)
                new_item = create(post_body)  # Call the create function from repository
            else:
                self._set_headers(400)
                error_message = "Please provide a metal, size, and style."
                self.wfile.write(json.dumps(error_message).encode())

        if new_item is not None:
            self.wfile.write(json.dumps(new_item).encode())

    def do_DELETE(self):
        """
        Handles DELETE requests to the server.
        """
        self._set_headers(204)
        (resource, _id, _) = self.parse_url(self.path)

        if resource == "orders":
            delete(resource, _id)  # Call the delete function from repository

        self.wfile.write("".encode())

    def do_PUT(self):
        """
        Handles PUT requests to the server.
        """
        self._set_headers(400)
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, _id, _) = self.parse_url(self.path)

        if resource == "orders":
            self._set_headers(204)
            error_message = "Order Production has begun. Cannot be modified."
            self.wfile.write(json.dumps(error_message).encode())

    def _set_headers(self, status):
        """
        Sets the status code, Content-Type, and Access-Control-Allow-Origin headers on the response.
        """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        """
        Sets the options headers.
        """
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Accept")
        self.end_headers()

def main():
    """
    Starts the server on port 8088 using the HandleRequests class.
    """
    host = ""
    port = 8088
    server = HTTPServer((host, port), HandleRequests)
    print(f"Server running on {host}:{port}")
    server.serve_forever()

if __name__ == "__main__":
    main()
