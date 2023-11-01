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

