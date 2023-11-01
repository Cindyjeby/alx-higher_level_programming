<h1>JAVASCRIPT - WEB JQUERY</h1>
<h2>What is JavaScript?</h2>
<p>It is a scripting language that enables you to create dynamically updating content, control multimedia, animate images.<p>
<h2>Selectors</h2>
<h3>The #id selector</h3>
<p>It is used to locate a desired element.<br>It should be unique, so you should only use this selector when you wish to locate a unique element.<br>To locate an element with a specific ID, write a hash charachter followed by the id of the element you wish to locate, eg:<br>#divTest</p>
<h3>The .class selector</h3>
<p>Element s with a specific class can be matched by writing a fulstop(.) character followed by the name of the class.<br>example:<br>
<ul><br>
	<li class="bold">Test 1</li><br>
	<li>Test 2</li><br>
	<li class="bold">Test 3</li><br>
</ul><br>
<script type="text/javascript"><br>
$(function()<br>
{<br>
	$(".bold").css("font-weight", "bold");<br>
});<br>
</script>
<h3>The element selector</h3>
<p>you can also match elements based on their tag names. for example:<br>you can match links with "a" or dives with "div".
<h2>DOM manipulation</h2>
<p>DOM - Document Object Model manipulation is the process of using programming to interact with and modify the structure and content of a web pages's document object model.
<h3>Getting and Setting content[text(), html() and vai()]</h3>
<h4>text()</h4>
<p>this method is used to get or set the text context of an HTML element.<br>When used iyou retrieve the text within an element or you can set new text to replace the existing content.<br>it works with elements that contain plain text ike headinds paragraphs and span elements.<br>Example:<br>(element).text():retrieves the text content of the selected element.<br>(element).text("New Text"):sets the text content of the selected element to "new Text".</p>
<h4>html</h4>
<p>this method is used to get or set the html content of HTML.When used you can access the content within an element including the HTML tags in it.<br>you can also replace the existing content with new html content.<br> example<br>(element).html(): retrieves the HTML content of the selected element<br>(element).html("<p>New HTML content</p>"):sets the html content of the selected element to the new content</p>
<h4>val()</h4>
<p>is used with form elements like text input fields,checkboxes and radio buttons.when used you can access the value of the form element.<br> Example<br>if you have an input field with the value john, it will return "John".<br> when setting,it can be used to change the value of the text input field to jane by ".val("jane")"</p>
<h3>Getting and setting CSS classes</h3>
<p>
