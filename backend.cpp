#include <bits/stdc++.h>
#include "httplib.h" // Assuming you are using cpp-httplib library

void handle_request(const httplib::Request& req, httplib::Response& res) {
    // Your backend logic goes here
    res.set_content("Hello from C++ backend!", "text/plain");
}

int main() {
    httplib::Server svr;

    svr.Get("/hello", handle_request); // Define endpoint

    svr.listen("localhost", 8080); // Start the server

    return 0;
}
