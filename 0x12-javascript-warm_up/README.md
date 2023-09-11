JAVASCRIPT WARM UP

JavaScript - this is a programming language that can add interactivity to a website.

Variables
   - these are containers that store values.
   - we declare variables using "var", "let", "set"
   - LET: - we use let keyword followd by the name then semicolon
          - eg: let myname;
          - we can also declear and give it a value say: my name = "cindy";
          - or you can just do them on the same line
          - eg: let myname = "cindy";
          - you call the variable by calling: myname; also you can change the value by: myname = "jeby"
   - Variables can hold values of different data types.
   - Eg: . string -> sequence of text enclodes in either double or single quotes
         . numbers
         . boolean -> this is a true or false value
         . Array -> this is a structure that allows you to store multiple values in a single reference.eg: myname = ['cindy', 'jeby']
         . object -> this is everything and anything. like all the above.

Comments
   - these  are description of the code or anything that are ignored by the browser
   - just like in CSS they are enclosed in [/* */]

Operators
   - just like in other languages these are ,ath symbol that produce a result
   - add (+), sub(-), mult( * ), div (/) assign (=), equality(===), not(!), not equal(!==)

Conditionals
   - this are code structures used to test if an expression returns true or not.
   - common form of conditionals is the (if...else)

Functions
   - this is a way of packaging functionality that you wish to reuse.it executes when it is called
   - so functions look like variables but are followed by parentheses()
   - eg: let myvariable = document.querySelectore("h1");
   - here the document.querySelector("h1");is an inbuilt function
   - what is in the parentheses is called an argument
   - we can also create our own funtions eg:
          function multipy(num1, num2) {
            let result = num1 * num2;
            return result;
          }

Events
   - these are code structures that listen for activity in the browser and run code in esponse.
   - we have anonymous functions like addEventListener() this is because it doesnt have a name, it can also be written using the arrow function ()=>
  - so like instead of writing this: document.querySelector("html).addEventListener("click", function () {}; you can write it like this: document.querySelector("html").addEventListener("click", () => {}

Note: When linking a javascript to a html file you can either link it in the head or in the body just before the closing tag.
- if the js file is supposed to affect the Html file it is advisable to add it at the body to avoid problems in the code as the browser reads code in the order it appears in the file.
