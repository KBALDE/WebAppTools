# Introduction to HTML


HTML is the standard markup language for creating Web pages.

## What is HTML?
- HTML stands for Hyper Text Markup Language
- HTML is the standard markup language for creating Web pages
- HTML describes the structure of a Web page
- HTML consists of a series of elements
- HTML elements tell the browser how to display the content
- HTML elements label pieces of content such as "this is a heading", "this is a paragraph", "this is a link", etc.

```php
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

## Example Explained
- The **!DOCTYPE html** declaration defines that this document is an HTML5 document
- The **html** element is the root element of an HTML page
- The **head** element contains meta information about the HTML page
- The **title** element specifies a title for the HTML page (which is shown in the browser's title bar or in the page's tab)
- The **body** element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.
- The **h1** element defines a large heading
- The **p** element defines a paragraph

## What is an HTML Element?

An HTML element is defined by a start tag, some content, and an end tag:

``<tagname> Content goes here... </tagname>``

The HTML element is everything from the start tag to the end tag:
````php
<h1>My First Heading</h1>
<p>My first paragraph.</p>
````

**Note**: *Some HTML elements have no content (like the **br** element). These elements are called empty elements. Empty elements do not have an end tag!*


## Web Browsers
The purpose of a web browser (Chrome, Edge, Firefox, Safari) is to read HTML documents and display them correctly.

A browser does not display the HTML tags, but uses them to determine how to display the document.

## HTML Documents
All HTML documents must start with a document type declaration: **!DOCTYPE html**.

The HTML document itself begins with **html** and ends with **/html**.

The visible part of the HTML document is between **body** and **/body**.

## The <!DOCTYPE> Declaration
The **!DOCTYPE** declaration represents the document type, and helps browsers to display web pages correctly.

It must only appear once, at the top of the page (before any HTML tags).

The **!DOCTYPE** declaration is not case sensitive.

The **!DOCTYPE** declaration for HTML5 is: ``<!DOCTYPE html>``


## HTML Links
HTML links are defined with the **a** tag:

````php
<a href="https://www.w3schools.com">This is a link</a>
````
The link's destination is specified in the ``href`` attribute. 

Attributes are used to provide additional information about HTML elements.

You will learn more about attributes in a later chapter.

## HTML Images
HTML images are defined with the **img** tag.

The source file (src), alternative text (alt), width, and height are provided as attributes:

```php
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
```

## Empty HTML Elements
HTML elements with no content are called empty elements.

The **br** tag defines a line break, and is an empty element without a closing tag:

```php
<p>This is a <br> paragraph with a line break.</p>
```

## HTML is Not Case Sensitive
HTML tags are not case sensitive: **P** means the same as **p**.

The HTML standard does not require lowercase tags, but W3C recommends lowercase in HTML, and demands lowercase for stricter document types like XHTML.

## HTML Attributes
All HTML elements can have attributes
Attributes provide additional information about elements
Attributes are always specified in the start tag
Attributes usually come in name/value pairs like: name="value"

### The href Attribute
The **a** tag defines a hyperlink. The href attribute specifies the URL of the page the link goes to:

```php
<a href="https://www.w3schools.com">Visit W3Schools</a>
```

### The src Attribute
The **img** tag is used to embed an image in an HTML page. The src attribute specifies the path to the image to be displayed:

```php
<img src="img_girl.jpg">
```

### The width and height Attributes
The **img** tag should also contain the width and height attributes, which specify the width and height of the image (in pixels):

```php
<img src="img_girl.jpg" width="500" height="600">
```

### The alt Attribute
The required alt attribute for the **img** tag specifies an alternate text for an image, if the image for some reason cannot be displayed. This can be due to a slow connection, or an error in the src attribute, or if the user uses a screen reader.

```php
<img src="img_girl.jpg" alt="Girl with a jacket">

```
### The style Attribute
The style attribute is used to add styles to an element, such as color, font, size, and more.

```php
<p style="color:red;">This is a red paragraph.</p>
```

### The lang Attribute
You should always include the lang attribute inside the **html** tag, to declare the language of the Web page. This is meant to assist search engines and browsers.

The following example specifies English as the language:

```php
<!DOCTYPE html>
<html lang="en">
<body>
...
</body>
</html>
```
Country codes can also be added to the language code in the lang attribute. So, the first two characters define the language of the HTML page, and the last two characters define the country.

The following example specifies English as the language and United States as the country:

```php
<!DOCTYPE html>
<html lang="en-US">
<body>
...
</body>
</html>
```

### The title Attribute
The title attribute defines some extra information about an element.

The value of the title attribute will be displayed as a tooltip when you mouse over the element:

```php
<p title="I'm a tooltip">This is a paragraph.</p>
```

## HTML Headings
HTML headings are defined with the h1 to h6 tags.

h1 defines the most important heading. h6 defines the least important heading.

### Headings Are Important
Search engines use the headings to index the structure and content of your web pages.

Users often skim a page by its headings. It is important to use headings to show the document structure.

h1 headings should be used for main headings, followed by h2 headings, then the less important h3, and so on.

### Bigger Headings
Each HTML heading has a default size. However, you can specify the size for any heading with the style attribute, using the CSS font-size property:

```php
<h1 style="font-size:60px;">Heading 1</h1>
```
### HTML Horizontal Rules
The **hr** tag defines a thematic break in an HTML page, and is most often displayed as a horizontal rule.

The **hr** element is used to separate content (or define a change) in an HTML page:

```php
<h1>This is heading 1</h1>
<p>This is some text.</p>
<hr>
<h2>This is heading 2</h2>
<p>This is some other text.</p>
<hr>
```

### HTML Line Breaks
The HTML **br** element defines a line break.

Use **br**  if you want a line break (a new line) without starting a new paragraph:

```php
<p>This is<br>a paragraph<br>with line breaks.</p>
```

### The HTML <pre> Element
The HTML **pre** element defines preformatted text.

The text inside a **pre** element is displayed in a fixed-width font (usually Courier), and it preserves both spaces and line breaks:

```php
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

### The HTML Style Attribute
Setting the style of an HTML element, can be done with the **style** attribute.

The HTML style attribute has the following syntax:
```php
<tagname style="property:value;">
```
The property is a CSS property. The value is a CSS value.


### Background Color
The CSS background-color property defines the background color for an HTML element.

```php
<body style="background-color:powderblue;">

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>

// Set background color for two different elements:
<body>

<h1 style="background-color:powderblue;">This is a heading</h1>
<p style="background-color:tomato;">This is a paragraph.</p>

</body>

```

### Text Color
The CSS color property defines the text color for an HTML element:
```php
<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```

### Fonts
The CSS font-family property defines the font to be used for an HTML element:

```php
<h1 style="font-family:verdana;">This is a heading</h1>
<p style="font-family:courier;">This is a paragraph.</p>
```

### Text Size
The CSS font-size property defines the text size for an HTML element:
```php
<h1 style="font-size:300%;">This is a heading</h1>
<p style="font-size:160%;">This is a paragraph.</p>
```


### Text Alignment
The CSS text-align property defines the horizontal text alignment for an HTML element:

```php
<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>
```

### HTML Formatting Elements
Formatting elements were designed to display special types of text:

**b** - Bold text
**strong** - Important text
**i** - Italic text
**em** - Emphasized text
**mark** - Marked text
**small** - Smaller text
**del** - Deleted text
**ins** - Inserted text
**sub** - Subscript text
**sup** - Superscript text

Example
```php
<b>This text is bold</b>
```

### HTML Quotation

**blockquote**,**q**, **abbr**, **address** **cite**, and **bdo** HTML elements.

- The HTML **blockquote** element defines a section that is quoted from another source.
- The HTML **q** tag defines a short quotation.
- The HTML **abbr** tag defines an abbreviation or an acronym, like "HTML", "CSS", "Mr.", "Dr.", "ASAP", "ATM".
- The HTML **address** tag defines the contact information for the author/owner of a document or an article.
- The HTML **cite** tag defines the title of a creative work (e.g. a book, a poem, a song, a movie, a painting, a sculpture, etc.)
- The HTML **bdo** tag is used to override the current text direction. BDO stands for Bi-Directional Override.

# HTML Comment Tag
You can add comments to your HTML source by using the following syntax:
```php
<!-- Write your comments here -->
```
You can hide more lines

```php
<p>This is a paragraph.</p>
<!--
<p>Look at this cool image:</p>
<img border="0" src="pic_trulli.jpg" alt="Trulli">
-->
<p>This is a paragraph too.</p>
```

### Hide Inline Content
Comments can be used to hide parts in the middle of the HTML code.

```php
<p>This <!-- great text --> is a paragraph.</p>
```

## HTML Colors
HTML colors are specified with predefined color names, or with RGB, HEX, HSL, RGBA, or HSLA values.

In HTML, a color can be specified by using a color name. 
Color names are: Tomato, Orange, DodgerBlue, MediumSeaGreen, Gray, SlateBlue, Violet, LightGray.
And more..; There are 140.

### Background Color
You can set the background color for HTML elements:
```php
<h1 style="background-color:DodgerBlue;">Hello World</h1>
<p style="background-color:Tomato;">Lorem ipsum...</p>
```

### Text Color
You can set the color of text:
```php
<h1 style="color:Tomato;">Hello World</h1>
<p style="color:DodgerBlue;">Lorem ipsum...</p>
<p style="color:MediumSeaGreen;">Ut wisi enim...</p>
```

### Border Color
You can set the color of borders:
```php
<h1 style="border:2px solid Tomato;">Hello World</h1>
<h1 style="border:2px solid DodgerBlue;">Hello World</h1>
<h1 style="border:2px solid Violet;">Hello World</h1>

```

## HTML Styles - CSS

CSS stands for Cascading Style Sheets.

CSS saves a lot of work. It can control the layout of multiple web pages all at once.

### What is CSS?
Cascading Style Sheets (CSS) is used to format the layout of a webpage.

With CSS, you can control the color, font, the size of text, the spacing between elements, how elements are positioned and laid out, what background images or background colors are to be used, different displays for different devices and screen sizes, and much more!

### Using CSS
CSS can be added to HTML documents in 3 ways:

Inline - by using the style attribute inside HTML elements
Internal - by using a style element in the head sectiond
External - by using a link element to link to an external CSS file

The most common way to add CSS, is to keep the styles in external CSS files.
However, in this tutorial we will duse inline and internal styles, because this is easier to demonstrate, and easier for you to try it yourself

### Inline CSS
An inline CSS is used to apply a unique style to a single HTML element.

An inline CSS uses the style attribute of an HTML element.

The following example sets the text color of the **h1** element to blue, and the text color of the **p** element to red:

```php
<h1 style="color:blue;">A Blue Heading</h1>

<p style="color:red;">A red paragraph.</p>
```

### Internal CSS
An internal CSS is used to define a style for a single HTML page.

An internal CSS is defined in the **head** section of an HTML page, within a **style** element.

The following example sets the text color of ALL the **h1** elements (on that page) to blue, and the text color of ALL the **p** elements to red. In addition, the page will be displayed with a "powderblue" background color: 
```php
<!DOCTYPE html>
<html>

<head>
<style>
	body {background-color: powderblue;}
	h1   {color: blue;}
	p    {color: red;}
</style>
</head>

<body>
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
</body>

</html>
```
### External CSS
An external style sheet is used to define the style for many HTML pages.

To use an external style sheet, add a link to it in the **head** section of each HTML page:

```php
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

The external style sheet can be written in any text editor. The file must not contain any HTML code, and must be saved with a .css extension.

Here is what the "styles.css" file looks like:

```php

body {
  background-color: powderblue;
}
h1 {
  color: blue;
}
p {
  color: red;
}

```
### CSS Colors, Fonts and Sizes
Here, we will demonstrate some commonly used CSS properties. You will learn more about them later.

- The CSS color property defines the text color to be used.

- The CSS font-family property defines the font to be used.

- The CSS font-size property defines the text size to be used.

```php
<!DOCTYPE html>
<html>
<head>

<style>
h1 {
  color: blue;
  font-family: verdana;
  font-size: 300%;
}
p {
  color: red;
  font-family: courier;
  font-size: 160%;
}
</style>

</head>

<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

### CSS Border
The CSS border property defines a border around an HTML element.

Tip: You can define a border for nearly all HTML elements.
```php
p {
  border: 2px solid powderblue;
}
```
### CSS Padding
The CSS padding property defines a padding (space) between the text and the border.

```php
p {
  border: 2px solid powderblue;
  padding: 30px;
}
```
### CSS Margin
The CSS margin property defines a margin (space) outside the border.
```php
p {
  border: 2px solid powderblue;
  margin: 50px;
}
```
### Link to External CSS
External style sheets can be referenced with a full URL or with a path relative to the current web page.
```php
<link rel="stylesheet" href="https://www.w3schools.com/html/styles.css">
```
This example links to a style sheet located in the html folder on the current web site: 
```php
<link rel="stylesheet" href="/html/styles.css">
```

## HTML Favicon
A favicon is a small image displayed next to the page title in the browser tab.

### How To Add a Favicon in HTML
You can use any image you like as your favicon. You can also create your own favicon on sites like https://www.favicon.cc.

To add a favicon to your website, either save your favicon image to the root directory of your webserver, or create a folder in the root directory called images, and save your favicon image in this folder. A common name for a favicon image is "favicon.ico".

Next, add a **link** element to your "index.html" file, after the **title** element, like this:

```php
<!DOCTYPE html>
<html>
<head>
  <title>My Page Title</title>
  <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```	

## HTML Tables
HTML tables allow web developers to arrange data into rows and columns.
```php
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>
```

- Each table cell is defined by a **td** and a slash **td** tag. td stands for table data.
- Each table row starts with a **tr** and ends with a **tr** tag. tr stands for table row.
- Sometimes you want your cells to be table header cells. In those cases use the **th** tag instead of the **td** tag. th stands for table header.

By default, the text in **th** elements are bold and centered, but you can change that with CSS.

## HTML Lists
HTML lists allow web developers to group a set of related items in lists.

### Unordered HTML List
An unordered list starts with the **ul** tag. Each list item starts with the **li** tag.

The list items will be marked with bullets (small black circles) by default:
```php
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

```

### Ordered HTML List
An ordered list starts with the **ol** tag. Each list item starts with the **li** tag.

The list items will be marked with numbers by default:

```php
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```
### HTML Description Lists
HTML also supports description lists.

A description list is a list of terms, with a description of each term.

The **dl** tag defines the description list, the **dt** tag defines the term (name), and the **dd** tag describes each term:

```php
<dl>
  <dt>Coffee</dt>
  <dd>- black hot drink</dd>
  <dt>Milk</dt>
  <dd>- white cold drink</dd>
</dl>
```
## HTML Block and Inline Elements
Every HTML element has a default display value, depending on what type of element it is.

There are two display values: block and inline.

### Block-level Elements
A block-level element always starts on a new line, and the browsers automatically add some space (a margin) before and after the element.

A block-level element always takes up the full width available (stretches out to the left and right as far as it can).

Two commonly used block elements are: **p** and **div**.

The **p** element defines a paragraph in an HTML document.

The **div** element defines a division or a section in an HTML document.

```php
<p>Hello World</p>
<div>Hello World</div>
```

### Inline Elements
An inline element does not start on a new line.

An inline element only takes up as much width as necessary.

This is a **span** element inside a paragraph.

```php
<span>Hello World</span>
```
### The <div> Element
The **div** element is often used as a container for other HTML elements.

The **div** element has no required attributes, but style, class and id are common.

When used together with CSS, the **div** element can be used to style blocks of content:
```php
<div style="background-color:black;color:white;padding:20px;">
  <h2>London</h2>
  <p>London is the capital city of England. It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>
</div>
```	
### The <span> Element
The **span** element is an inline container used to mark up a part of a text, or a part of a document.

The **span** element has no required attributes, but style, class and id are common.

When used together with CSS, the **span** element can be used to style parts of the text:
```php
<p>My mother has <span style="color:blue;font-weight:bold;">blue</span> eyes and my father has <span style="color:darkolivegreen;font-weight:bold;">dark green</span> eyes.</p>

```

## HTML class Attribute
The HTML class attribute is used to specify a class for an HTML element.

Multiple HTML elements can share the same class.

Using The class Attribute
The class attribute is often used to point to a class name in a style sheet. It can also be used by a **JavaScript** to access and manipulate elements with the specific class name.

In the following example we have three **div** elements with a class attribute with the value of "city". All of the three **div** elements will be styled equally according to the .city style definition in the head section:
```php
<!DOCTYPE html>
<html>
<head>
<style>
.city {
  background-color: tomato;
  color: white;
  border: 2px solid black;
  margin: 20px;
  padding: 20px;
}
</style>
</head>
<body>

<div class="city">
  <h2>London</h2>
  <p>London is the capital of England.</p>
</div>

<div class="city">
  <h2>Paris</h2>
  <p>Paris is the capital of France.</p>
</div>

<div class="city">
  <h2>Tokyo</h2>
  <p>Tokyo is the capital of Japan.</p>
</div>

</body>
</html>
```

### HTML id Attribute
The HTML id attribute is used to specify a unique id for an HTML element.

You cannot have more than one element with the same id in an HTML document.

Using The id Attribute
The id attribute specifies a unique id for an HTML element. The value of the id attribute must be unique within the HTML document.

The id attribute is used to point to a specific style declaration in a style sheet. It is also used by JavaScript to access and manipulate the element with the specific id.

The syntax for id is: write a hash character (#), followed by an id name. Then, define the CSS properties within curly braces {}.

In the following example we have an **h1** element that points to the id name "myHeader". This **h1** element will be styled according to the #myHeader style definition in the head section:

```php
<!DOCTYPE html>
<html>
<head>
<style>
#myHeader {
  background-color: lightblue;
  color: black;
  padding: 40px;
  text-align: center;
}
</style>
</head>
<body>

<h1 id="myHeader">My Header</h1>

</body>
</html>

```

### Difference Between Class and ID
A class name can be used by multiple HTML elements, while an id name must only be used by one HTML element within the page:


### HTML Iframes
An HTML iframe is used to display a web page within a web page.

The HTML **iframe** tag specifies an inline frame.

An inline frame is used to embed another document within the current HTML document.
```php
<iframe src="url" title="description"></iframe>
```
Tip: It is a good practice to always include a title attribute for the **iframe**. This is used by screen readers to read out what the content of the iframe is.

### Iframe - Target for a Link
An iframe can be used as the target frame for a link.

The target attribute of the link must refer to the name attribute of the iframe:

```php
<iframe src="demo_iframe.htm" name="iframe_a" title="Iframe Example"></iframe>

<p><a href="https://www.w3schools.com" target="iframe_a">W3Schools.com</a></p>
```

## HTML JavaScript
JavaScript makes HTML pages more dynamic and interactive.

### The HTML <script> Tag
The HTML script tag is used to define a client-side script (JavaScript).

The script  element either contains script statements, or it points to an external script file through the src attribute.

Common uses for JavaScript are image manipulation, form validation, and dynamic changes of content.

To select an HTML element, JavaScript most often uses the document.getElementById() method.

This JavaScript example writes "Hello JavaScript!" into an HTML element with id="demo":

``` php
<script>
document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>

```

###The HTML noscript Tag
The HTML noscript tag defines an alternate content to be displayed to users that have disabled scripts in their browser or have a browser that doesn't support scripts:

```php
<script>
document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>
<noscript>Sorry, your browser does not support JavaScript!</noscript>
```

## Respinsive Web Site
### Setting The Viewport
To create a responsive website, add the following **meta** tag to all your web pages:

```php
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
And For images to be Responsive

```php
<img src="img_girl.jpg" style="width:100%;">
```
## HTML <code> For Computer Code
The HTML **code** element  is used to define a piece of computer code. The content inside is displayed in the browser's default monospace font.

```php
<pre>
<code>
x = 5;
y = 6;
z = x + y;
</code>
</pre>
```
### HTML <var> For Variables
The HTML **var** element  is used to define a variable in programming or in a mathematical expression. The content inside is typically displayed in italic.
```php
<p>The area of a triangle is: 1/2 x <var>b</var> x <var>h</var>, where <var>b</var> is the base, and <var>h</var> is the vertical height.</p>
```

## HTML Entities
Some characters are reserved in HTML.

If you use the less than (<) or greater than (>) signs in your text, the browser might mix them with tags.

Character entities are used to display reserved characters in HTML.

A character entity looks like this:
```
&entity_name;
OR

&#entity_number;
```
## The HTML charset Attribute
To display an HTML page correctly, a web browser must know the character set used in the page.

This is specified in the **meta** tag:

```<meta charset="UTF-8">```
