<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFH_logo.png?raw=true" style="margin: 0;">

## Milestone Project 3 - CodeInstitute
#### By Sascha Andeweg
Your food - Your identity: FoodFromHome is a website helping you find the food you had at home, the food you grew up with. The food you would show off with when living in Ireland. Because it's part of who you are; your identity.

In Ireland it is not easy to find the products from your home country. But they can be found now. Users can add their find on FoodFromHome and add it to the database, making fellow nationals, or anyone else loving these types of food, very happy when searching for their favourites on FoodFromHome.

Starting with five countries of origin (The Netherlands, Belgium, France, Germany and Spain), the site can be easily extended to more countries of origin. And also, starting with Ireland as the country where the food should be sold, this also can be extended to many more countries of course.

## UX
The website has a homepage that starts with the full list of products from the database. The selection options are self explanatory: country of origin, sorting by category. The simple navigation provides an about page, explaining the purpose of this site, the link to the page for adding products and a link to the page for editing products. Admin access needs no authentification since the site is for educational purposes only and provides updating and adding categories to the database (CRUD).

## USER STORIES
A Dutch student looking for Calve peanutbutter searches in category food after selecting origin The Netherlands. The product card with basic information for Calve pindakaas is found and with a click on the plus-icon more information about the product is given. The name of the supplier is always visible. The entry date gives an indication of how likely it is the product is still to be found there.

A Dutch resident of Cork city found that a Polish shop sells Lays Paprika crisps (Walkers in Ireland, but paprika isn't a flavour sold in the republic). He goes onto FoodFromHome and adds the product with the details of the shop under the category Snacks. When entering the details he leaves a password for the entry, so he can later authenticate, edit or delete the product when he no longer finds his favourite crisps in this particular shop.

An Irish woman living in Longford has lived in Amsterdam for 15 years and has gotten very used to Dutch foods and drinks. But also Belgian beers were a very common product in Amsterdam. To bring back good memories and enjoy the unique taste of a nice Belgian beer she can go to FoodFromHome and select origin Belgian and select category Beverages. There she finds a nice selection. It will take a bit of driving to go to the supplier, but the experience is worth it. 

A shop in county Kerry keeps getting Dutch customers asking for Hagelslag (chocolate sprinkles). He manages to find a supplier to import the product and goes onto FoodFromHome to add the product and his shop's details so that the Dutch community in that part of the country can finally find their favourite sandwich spread.

A Spanish language student found her favourite Sangria in a Cork shop and had added the product in the database a week ago. However, the product seems to be a one off in the shop's stock and is no longer available. She goes to FoodFromHome and using her personal code she can remove the product again.

## WIREFRAME / DESIGN
The wireframe is made in Adobe XD which is also the design. With the principle of mobile first in mind, the full wireframe is built in mobile orientation and dimensions (375 x 812 px - iPhone X/XS/11 Pro). For design purposes, the home page is also designed in web dimensions 1920 x 1080 px).
The website will be responsive, using the Materialize css framework.

img...:

## DESIGN CHOICES:
The logo is a simple shape with rounded and slightly slanted corners in a lime green with in it the initials of FoodFromHome in dark blue for contrast. The full name beside it. All text in the logo is in type Lora which is used throughout the site for text in serif. A stylish serif, easy to read, pretty to look at.

The chosen font Lora is taken from Google Fonts (https://fonts.google.com/) and the other, Roboto is a font that is the standard sans-serif in Materialize framework.

The main image is a stock photo bought (free in a trial period) from Adobe Stock. It shows a multicultural couple enjoying walking on a market. The asian looking girl pointing at something could be interpreted as someone finding that product she used to enjoy back home. By using a photo not necessarily linked to Ireland will make it easier in the future to expand to other markets.

The images used for the products are also stock photos, bought from Adobe Stock. I considered using product photos, but they are almost without exception under copyright. This would be too risky, would the site go public.

Initially I set up the products in accordions to be folded out to view the product. However, using the cards from Materialize is a user friendly option where the products are more easily found and it makes the site look more appealing.

### The colours:
The light purple and dark blue give a good contrast and are soft and friendly. The site is providing a service, not selling goods. So without being pushy with screaming colours it should be a pleasant expierence for the user. The navigation on mobile sizes uses transparancy to visually  'stay in touch' with the main page of the site.

The colours used are: 
* Light purple: CCCCFF
* Dark blue: 333399

## FEATURES
#### Existing features:

##### Navbar:
Provides the logo, and links to the 'about', 'add product', 'edit product', 'administrator' and 'contact' pages. On small screens the navigation collapses into a hamburger menu (Materialize).

##### Selection options:
Searching a database for products originating from a selection of countries, presented in a collapsible dropdown with text and the flags of the countries, and known to be all time favourites and sold within the republic of Ierland. The second dropdown selects categories 'beverages', 'food', 'health', 'ingredienst', 'snacks' and 'sweets'.

##### Product presentation:
The results are shown on the same page as basic cards with category image, product name, brand, and entry date. The bottom of the card shows the supplier and is always visible, also after clicking the plus-icon to read more: description, price and a line saying 'We like this in <country>.

##### About:
A short description of the purpose and setup of this site and of the developer.

##### Add product:
Users can enter products they found with suppliers in Ireland within the available categories. By entering a personal code users can also edit their entries afterwards. After adding the product, the page redirects to 'add supplier' if there's a new supplier to be added.

##### Edit product:
Users can edit the products they added to the database, as a later addition only by using the provided user_code.

##### Administrator:
The administrator can add and edit categories if needed, as a later addition only using his personal credentials.


## FEATURES LEFT TO IMPLEMENT
At a later stage Google Maps with markers for the supppliers can be added.
More categories and countries of origin can be added when the basic site proves to be a success.
The administrator section and editing by users will need authentication to be accessed by the administrator and appropriate users only.


## TECHNOLOGIES USED
The navbar and accordion bars css base are taken from the Materialize framework (http://materializecss.com). Bootstrap (http://getbootstrap.com) is used for a lot of the HTML/CSS structure and customised for FoodFromHome.
Flask (https://palletsprojects.com/p/flask/) is used for the Jinja template structure and routing.
An extra library is used for handling the MongoDB database with Python: Python Mongo (pyMongo) (https://pymongo.readthedocs.io/en/stable/).
JavaScript (https://developer.mozilla.org/en-US/docs/Web/JavaScript) is used to work with the GoogleMaps API returning the locations of suppliers as a marker on a map.
JQuery ?

## TESTING


## DEPLOYMENT
In the design phase Adobe Dreamweaver was used to speed up the design process and make good use of the handy live view. The HTML/CSS design during this process was also tested on a live server (Strato - domain Tradtracker.com). In the process I found an issue with Bootstrap and Materialize using the same names in the CSS code for navigation elements. Inspecting in Google Chrome on the live server proved to be very usefull to find the issues and create workarounds in my own code.

The GitPod IDE is used for testing in the required environment for the CodeInstitute courses. The HTML/CSS files are pushed to the GitHub repository to handle the version control.

The Flask/Python part of the project is built within the GitPod IDE and once linked to the MongoDB database, deployment is done on Heroku.

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
#### Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X
