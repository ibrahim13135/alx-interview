# Making HTTP Requests in Node.js

HTTP (Hypertext Transfer Protocol) requests are a fundamental part of web development, enabling the exchange of data between a client and a server. In Node.js, making HTTP requests to external services can be done using various modules and libraries. This article will discuss HTTP, the components of HTTP requests, and how to make these requests in Node.js using different methods. We'll also cover error handling.

## Prerequisites

- Node.js installed on your computer (Node v14.15.4 or above)
- Basic knowledge of JavaScript

## Understanding HTTP Requests

HTTP requests are used to exchange information between a client and a server. The client initiates the request, and the server responds accordingly. An HTTP request consists of several components:

1. **Method (GET, POST, PUT, DELETE, etc.)**: Defines the action to be performed on the server.
2. **URL**: The target where the request is sent.
3. **Protocol**: The name and version of the protocol (HTTP/1.1, HTTP/2, etc.).
4. **Headers**: Additional information sent with the request.
5. **Body**: Data sent with the request (used in POST, PUT methods).

### Example of a GET Request
```http
GET /home.html HTTP/1.1
Host: developer.mozilla.org
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

### Example of a POST Request
```http
POST /test HTTP/1.1
Host: foo.example
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

name=Victor&email=emailaddress
```

## Ways to Make HTTP Requests in Node.js

### 1. Using the HTTP Module

The built-in `http` and `https` modules in Node.js allow you to make HTTP requests. The `https` module is used for making requests to HTTPS URLs.

#### GET Request with `https` Module
```javascript
const https = require("https");

https.get("https://reqres.in/api/users", (resp) => {
  let data = "";

  // A chunk of data has been received.
  resp.on("data", (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on("end", () => {
    console.log(JSON.parse(data));
  });
}).on("error", (err) => {
  console.log("Error: " + err.message);
});
```

#### POST Request with `https` Module
```javascript
const https = require("https");

const data = JSON.stringify({
  name: "Victor",
  email: "emailaddress"
});

const options = {
  hostname: 'yourapi.com',
  port: 443,
  path: '/todos',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
};

const req = https.request(options, (resp) => {
  let data = '';

  resp.on("data", (chunk) => {
    data += chunk;
  });

  resp.on("end", () => {
    console.log(JSON.parse(data));
  });
});

req.on("error", (err) => {
  console.log("Error: " + err.message);
});

req.write(data);
req.end();
```

### 2. Using Axios

Axios is a promise-based HTTP client for the browser and Node.js. It simplifies making HTTP requests by automatically handling JSON responses and providing features like request/response interception and cancellation.

#### Installing Axios
```bash
$ npm install axios
```

#### GET Request with Axios
```javascript
const axios = require('axios');

async function getUsers() {
  try {
    const response = await axios.get("https://reqres.in/api/users");
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

getUsers();
```

#### POST Request with Axios
```javascript
const axios = require('axios');

async function createUser() {
  try {
    const response = await axios.post("https://reqres.in/api/users", {
      name: "Victor",
      job: "developer"
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

createUser();
```

## Error Handling

Handling errors in HTTP requests is crucial for building robust applications. Here’s how you can handle errors in different methods.

### Error Handling with the `https` Module
```javascript
https.get("https://invalid.url", (resp) => {
  // Handle response
}).on("error", (err) => {
  console.error("Error: " + err.message);
});
```

### Error Handling with Axios
```javascript
async function getUsers() {
  try {
    const response = await axios.get("https://invalid.url");
    console.log(response.data);
  } catch (error) {
    console.error("Error: " + error.message);
  }
}

getUsers();
```

## Conclusion

Making HTTP requests in Node.js is a common task for web developers. Whether using the built-in `http`/`https` modules or third-party libraries like Axios, understanding the components of an HTTP request and how to handle errors is essential. This article provided an overview of HTTP requests and demonstrated how to make GET and POST requests using different methods in Node.js.







### 1. Using the HTTP Module

The `http` and `https` modules in Node.js can be used to create HTTP requests. Here’s how you can use them.

#### GET Request with `https` Module
```javascript
const https = require("https");

https.get("https://reqres.in/api/users", (resp) => {
  let data = "";

  // A chunk of data has been received.
  resp.on("data", (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on("end", () => {
    console.log(JSON.parse(data));
  });
}).on("error", (err) => {
  console.error("Error: " + err.message);
});
```

**Expected Output:**
```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    // More users...
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

#### POST Request with `https` Module
```javascript
const https = require("https");

const data = JSON.stringify({
  name: "Victor",
  job: "writer"
});

const options = {
  hostname: 'reqres.in',
  port: 443,
  path: '/api/users',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
};

const req = https.request(options, (resp) => {
  let data = '';

  resp.on("data", (chunk) => {
    data += chunk;
  });

  resp.on("end", () => {
    console.log(JSON.parse(data));
  });
});

req.on("error", (err) => {
  console.error("Error: " + err.message);
});

req.write(data);
req.end();
```

**Expected Output:**
```json
{
  "name": "Victor",
  "job": "writer",
  "id": "210",
  "createdAt": "2022-03-26T14:07:58.464Z"
}
```

### 2. Using Axios

Axios is a promise-based HTTP client for the browser and Node.js. It simplifies HTTP requests and handles JSON responses automatically.

#### Installing Axios
```bash
$ npm install axios
```

#### GET Request with Axios
```javascript
const axios = require('axios');

async function getUsers() {
  try {
    const response = await axios.get("https://reqres.in/api/users");
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

getUsers();
```

**Expected Output:**
```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    // More users...
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

#### POST Request with Axios
```javascript
const axios = require('axios');

const data = {
  name: "Victor",
  job: "writer"
};

async function addUser(data) {
  try {
    const response = await axios.post("https://reqres.in/api/users", data);
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

addUser();
```

**Expected Output:**
```json
{
  "name": "Victor",
  "job": "writer",
  "id": "210",
  "createdAt": "2022-03-26T14:07:58.464Z"
}
```

### 3. Using Got

Got is another HTTP client library that works similarly to Axios but offers additional features like Stream and Pagination APIs. It is a native ESM, so you need to use `import` rather than `require`.

#### Installing Got
```bash
$ npm install got
```

#### GET Request with Got
```javascript
import got from 'got';

async function getUsers() {
  try {
    const response = await got.get('https://reqres.in/api/users').json();
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}

getUsers();
```

**Expected Output:**
```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    // More users...
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

#### POST Request with Got
```javascript
import got from 'got';

const data = {
  name: "Victor",
  job: "writer"
};

async function addUser(data) {
  try {
    const response = await got.post('https://reqres.in/api/users', {
      json: data
    }).json();
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}

addUser();
```

**Expected Output:**
```json
{
  "name": "Victor",
  "job": "writer",
  "id": "210",
  "createdAt": "2022-03-26T14:07:58.464Z"
}
```

### 4. Using Node-Fetch

Node-Fetch is a lightweight HTTP library that mirrors the Fetch API in the browser, making it a consistent option for both server-side and client-side code.

#### Installing Node-Fetch
```bash
$ npm install node-fetch
```

#### GET Request with Node-Fetch
```javascript
import fetch from 'node-fetch';

async function getUsers() {
  const response = await fetch('https://reqres.in/api/users');
  const data = await response.json();
  console.log(data);
}

getUsers();
```

**Expected Output:**
```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    // More users...
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

#### POST Request with Node-Fetch
```javascript
import fetch from 'node-fetch';

const data = {
  name: "Victor",
  job: "writer"
};

async function addUser(data) {
  const response = await fetch('https://reqres.in/api/users', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const responseData = await response.json();
  console.log(responseData);
}

addUser(data);
```

**Expected Output:**
```json
{
  "name": "Victor",
  "job": "writer",
  "id": "210",
  "createdAt": "2022-03-26T14:07:58.464Z"
}
```

## Handling Responses and Errors

When making HTTP requests, handling responses and errors is crucial for robust application

 development.

### Handling Responses with Axios
Axios simplifies response handling by returning a promise that resolves with the response data:
```javascript
axios.get('https://reqres.in/api/users')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error("Error: " + error.message);
  });
```

### Handling Errors with Axios
Axios provides built-in error handling:
```javascript
axios.get('https://reqres.in/api/users')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error("Error: " + error.message);
  });
```

### Handling Responses and Errors with Got
Got also handles responses and errors similarly:
```javascript
got.get('https://reqres.in/api/users').json()
  .then(response => {
    console.log(response);
  })
  .catch(error => {
    console.error("Error: " + error.message);
  });
```

### Handling Responses and Errors with Node-Fetch
With Node-Fetch, you need to manually check the response status and handle errors:
```javascript
fetch('https://reqres.in/api/users')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("Error: " + error.message);
  });
```

## Conclusion

Making HTTP requests in Node.js is a common and necessary task for web development. Whether using the built-in `http`/`https` modules or third-party libraries like Axios, Got, or Node-Fetch, each method has its benefits. Choose the one that best fits your needs and workflow. This article provided an overview of how to make GET and POST requests using different methods in Node.js, along with handling responses and errors effectively.



## 5. SuperAgent

SuperAgent is a VisionMedia project with over 29 million downloads per month. It is a composable and promise-based API that retries on failure, follows redirects, handles gzip, has a JSON mode, and can also cancel requests. 

You can install SuperAgent with this command: 

```bash
$ npm install superagent
```

### Making a GET Request with SuperAgent

Let us make a call to our API with SuperAgent using an async function:

```javascript
const superagent = require('superagent');

async function getUsers() {
    try {
        const res = await superagent.get('https://reqres.in/api/users');
        console.log(res.body); // Logging the response body
    } catch (err) {
        console.error(err);
    }
}

getUsers();
```

**Expected Output:**

```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    ...
  ]
}
```

This almost looks like Axios if you remember, most especially the response gotten from the API. It also provides a text field along with JSON. Since SuperAgent is a promise-based API, we have to use a try/catch to handle errors.

### Making a POST Request with SuperAgent

Sending data to the server works cleanly too, but you have to add the `.send()`:

```javascript
const superagent = require('superagent');

const data = {
  "name": "victor",
  "job": "writer"
}

async function addUser(data) {
    try {
        const res = await superagent.post('https://reqres.in/api/users').send(data);
        console.log(res.body); // Logging the response body
    } catch (err) {
        console.error(err);
    }
}

addUser(data);
```

**Expected Output:**

```json
{
  "name": "victor",
  "job": "writer",
  "id": "210",
  "createdAt": "2022-03-26T14:07:58.464Z"
}
```

### Extending SuperAgent with Plugins

SuperAgent is also easily extendable with plugins such as `no-cache`, `superagent-mocker`, `superagent-node-http-timing`, and a few others. To use any of them, you import them and use the `.use()` method to call them.

```javascript
const nocache = require('superagent-no-cache');
const superagent = require('superagent');
const prefix = require('superagent-prefix')('/static');

superagent
  .get('/some-url')
  .use(prefix) // Prefixes *only* this request
  .use(nocache) // Prevents caching of *only* this request
  .end((err, res) => {
    if (err) {
      console.error(err);
    } else {
      console.log(res.body);
    }
  });
```

### Handling Errors

Handling errors in HTTP requests will vary according to the application and even the client library used, but we still have to factor in some things in our requests. For example, if you make a request to a wrong URL with Axios, you get an unmanageable response with a response field of undefined. In that case, you can handle it by adding a try/catch block to your code. 

```javascript
async function talkToMe(reqBody) {
  try {
    let res = await axios({
      method: 'post',
      url: 'https://api.com/to',
      data: reqBody
    });

    let data = res.data;
    return data;
  } catch (error) {
    console.log(error.response); 
    return error.response;
  }
}
```

Whatever error is caught in the try section is caught in the catch section instantly. Or if you are working with callbacks, then you use the `.catch()` method. 

```javascript
axios.get('/user/:victor')
  .catch(function (error) {
    if (error.response) {
      console.error(error.response);
    }
  });
```

There are also more errors that may occur, like when the site is down and you get a 50X error. Most libraries provide options to handle errors effectively.

### Conclusion

We have sampled five ways of making HTTP requests in Node.js, and from observations, they basically do the same thing but some of them handle the bottlenecks for you, most especially Axios and SuperAgent. This article is not intended to tell you which is better but to show you all the common ways and allow you to pick the most convenient. 

The main goal of HTTP requests is to communicate between computers, and the method, target, and protocol should be taken into consideration. So, make use of this article by picking the most suitable one for your project.
