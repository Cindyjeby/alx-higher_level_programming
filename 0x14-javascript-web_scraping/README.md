<h1>JavaScript-web scraping</h1>
<p><strong>JavaScript Object Notation (JSON)</strong> is a standard text-based format for representing structured data based on javaScript object syntax.<br>It is widly used for data exchange between a server and web application, configuration files and data storage.</p>
<p>JSON exists as a string.</p>
<h2>JSON Structure</h2>
<h3>Key-Value pairs</h3>
<p>JSON data is represented as a set of key-value pairs, where keys are strings enclosed in double quotes, followed by a colon, and then the corresponding value. Values can be strings, numbers, objects, arrays, booleans, or null. Here's an example of a simple JSON object:</p>
<p>
{
  "name": "John",
  "age": 30,
  "isStudent": false,
  "city": "New York"
}
</p>
<h3>Objects</h3>
<p>JSON objects are enclosed in curly braces {} and can contain multiple key-value pairs. Keys must be unique within an object. In the example above, the entire structure is a JSON object.</p>
<h3>Arrays</h3>
<p>JSON arrays are ordered lists of values enclosed in square brackets []. Elements in an array can be of different types, including other arrays and objects. Here's an example:</p>
<p>
{
  "fruits": ["apple", "banana", "cherry"]
}
</p>
<h3>Nested Structures</h3>
<p>JSON allows nesting of objects and arrays within other objects and arrays. This enables the representation of complex data structures. For example:</p>
<p>
{
  "person": {
    "name": "Alice",
    "address": {
      "street": "123 Main St",
      "city": "Los Angeles"
    },
    "hobbies": ["reading", "swimming"]
  }
}
</p>
<h3>Boolean and Null Values</h3>
<p>JSON supports boolean values (true and false) and a special null value. For example:</p>
<p>
{
  "isStudent": true,
  "isEmployed": false,
  "middleName": null
}
</p>
<h3>Whitespace</h3>
<p>JSON allows for whitespace (spaces, tabs, line breaks) for formatting and readability, but it's not required. The following JSON is equivalent to the previous example:</p>
<p>
{
  "isStudent": true,
  "isEmployed": false,
  "middleName": null
}
</p>
<h3>Array of objects</h3>
<p>As stated earlier arrays are in cloded in [] while objects are inclode in {} so in this the object is inside the array. for example:</p>
<p>
[<br>
  {<br>
    "name": "John",<br>
    "age": 30,<br>
    "city": "New York"<br>
  },<br>
  {<br>
    "name": "Alice",<br>
    "age": 25,<br>
    "city": "Los Angeles"<br>
  }<br>
]
</p>

<h2>How to manipulate JSON data</h2>
<p>Manipulating JSON data typically involves reading, modifying, and writing JSON data using a programming language. Here's a general overview of how to manipulate JSON data using Python as an example:</p>
<h3>Reading JSON Data</h3>
<p>You can read JSON data from a file or an API response using Python's json module. Here's an example of reading JSON data from a file:<br>
import json
<br>
with open('data.json', 'r') as file:<br>
    data = json.load(file)
<br>If you have JSON data as a string, you can use json.loads() to parse it into a Python data structure.</p>
<h3>Accessing JSON data</h3>
<p>Once you have the JSON data as a Python dictionary or list, you can access and manipulate its values like you would with any other Python data structure. For example:<br>
print(data['name'])  # Access a specific value by key<br>
data['age'] = 31     # Modify a value</p>
<h3>Modifying JSON data</h3>
<p>To modify JSON data, simply access the values you want to change and update them as needed. You can add new key-value pairs, delete entries, or modify existing values.Example:<br>
data['new_key'] = 'new_value'  # Add a new key-value pair<br>
del data['old_key']           # Delete a key-value pair</p>
<h3>Converting back to json</h3>
<p>After making changes to your data, you can convert it back to JSON format using json.dumps() if you want to save it to a file or send it to an API. For example:<br>modified_json = json.dumps(data)</p>
<h3>Writing JSON data to a file</h3>
<p>To save the modified JSON data to a file, use json.dump():<br>
with open('modified_data.json', 'w') as file:<br>
    json.dump(data, file)
</P>

<h2>How to use request and fetch API</h2>
<p>requests and the Fetch API are both commonly used to make HTTP requests in different programming environments. I'll provide an overview of how to use each of them.</p>
<h3>Using requests in python</h3>
<p>The requests library is widely used for making HTTP requests in Python. It provides a simple and intuitive API for sending HTTP requests and handling responses. You can use it to send GET, POST, PUT, DELETE, and other types of HTTP requests.<br>Here's a basic example of how to use requests to make a GET request:<br>
import requests<br>

# Make a GET request to a URL<br>
response = requests.get("https://api.example.com/data")<br>

# Check if the request was successful (status code 200)<br>
if response.status_code == 200:<br>
    # Parse the response content (assuming it's JSON)<br>
    data = response.json()<br>
    print(data)<br>
else:<br>
    print(f"Request failed with status code {response.status_code}")
</p>
<h3>To Install<h3>
<p>pip install requests</p>
<h3>Using the Fetch API in JavaScript (Front-end):</h3>
<p>The Fetch API is a modern JavaScript API for making network requests in the browser. It's widely used for fetching data from APIs and resources on the web. Here's a basic example of how to use the Fetch API to make a GET request in JavaScript:<br>
// Make a GET request using the Fetch API<br>
fetch("https://api.example.com/data")<br>
  .then((response) => {<br>
    // Check if the response status is OK (status code 200)<br>
    if (response.ok) {<br>
      // Parse the response as JSON<br>
      return response.json();<br>
    } else {<br>
      throw new Error(`Request failed with status: ${response.status}`);<br>
    }<br>
  })<br>
  .then((data) => {<br>
    console.log(data);<br>
  })<br>
  .catch((error) => {<br>
    console.error(error);<br>
  });</p>

<h2>How to read and write a file using fs module</h2>
<p>To read and write files using the Node.js fs module, you can follow these steps. First, you need to require the fs module in your Node.js script:<br>
<strong>const fs = require('fs');</strong></p>
<h3>Reading a File:</h3>
<p>To read a file, you can use the <strong>fs.readFile</strong> method. This method reads the contents of a file and provides a callback function with the content or an error if the file can't be read.<br>
fs.readFile('example.txt', 'utf8', (err, data) => {<br>
  if (err) {<br>
    console.error(err);<br>
  } else {<br>
    console.log(data);<br>
  }<br>
});<br>
In this example, example.txt is the name of the file you want to read. The 'utf8' argument specifies the encoding for the file content (usually set to 'utf8' for text files)</p>
<h3>Writing to a File:</h3>
To write to a file, you can use the <strong>fs.writeFile</strong> method.<br>This method writes data to a file or creates a new file if it doesn't exist.<br>It also provides a callback function to handle success or error.<br>
const content = 'This is the content to write to the file.';<br>
fs.writeFile('output.txt', content, (err) => {<br>
  if (err) {<br>
    console.error(err);<br>
  } else {<br>
    console.log('File written successfully.');<br>
  }<br>
});<br>
In this example, output.txt is the name of the file to which you want to write the content. The content variable contains the data to be written.</p>
<h3>Appending to a File</h3>
<p>If you want to add content to an existing file, you can use the <strong>fs.appendFile</strong> method.<br>It works similarly to fs.writeFile but appends content to the end of the file.</p>
