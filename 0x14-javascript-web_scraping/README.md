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
