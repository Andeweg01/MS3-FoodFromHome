<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFH_logo.png?raw=true" style="margin: 0;">

## Milestone Project 3 - CodeInstitute
#### By Sascha Andeweg
Your food - Your identity: FoodFromHome is a website helping you find the food you had at home, the food you grew up with. The food you would show off with when living abroad. Because it's part of who you are; your identity.
In Ireland it is not easy to find the products from your home country. But they can be found now. Users can add their find on FoodFromHome and add it to the database, making fellow nationals,or anyone else loving these food types, very happy when searching for their favourites on FoodFromHome.
Starting with five countries of origin, the site can be easily extended to more countries of origin. And also, starting with Ireland as the country where the food should be sold, this also can be extended to many more countries.

## UX
The website has a homepage that starts with the full list of products from the database. The selection and sorting options are self explanatory: country of origin, sorting on name, brand, category, location, the entry date and supplier. The simple navigation provides an about page, explaining the purpose of this site and the link to the page for adding products. Admin access is open since the site is for educational purposes only and provides updating and adding categories to the database.

## USER STORIES
A Dutch student looking for Calve peanutbutter searches for category food on the origin-page The Netherlands and sorts on brand. The product Calve pindakaas is found and with a click on the product name the accordion unfolds the product with name and location of the supplier and location marker on a Google maps map. Also the date added gives an indication of how likely it is still to be found there.
A Dutch resident of Cork city found that a Polish shop sells Lays Paprika crisps (Walkers in Ireland, but paprika isn't a flavour sold in the republic). He goes onto FoodFromHome and adds the product with the details of the shop under the category Snacks. When entering the details he leaves a password for the entry, so he can later identify and delete the product when he no longer finds his favourite crisps in this particular shop.
An Irish woman living in Longford has lived in Amsterdam for 15 years and has gotten very used to Dutch foods and drinks. But also Belgian beers were a very common product in Amsterdam. To bring back good memories and enjoy the unique taste of a nice Belgian beer she can go to FoodFromHome and select origin Belgian and select category Beverages. There she finds a nice selection. It will take a bit of driving to go to the supplier, but the experience is worth it. 
A shop in county Kerry keeps getting Dutch customers asking for Hagelslag (chocolate sprinkles). He manages to find a supplier to import the product and goes onto FoodFromHome to add the product and his shop's details so that the Dutch community in that part of the country can finally find their favourite sandwich spread.

## WIREFRAME / DESIGN
The wireframe is made in Adobe XD which is also the design. With the principle of mobile first in mind, the full wireframe is built in mobile orientation and dimensions (375 x 812 px - iPhone X/XS/11 Pro). For design purposes, the home page is also designed in web dimensions 1920 x 1080 px).
The website will be responsive, using Bootstrap and Materialize css.

img...:

## DESIGN CHOICES:
The chosen fonts are taken from Google Fonts (https://fonts.google.com/) and are:
Noto Sans, a neat sans type in the same style as Droid and Roboto optimized for readability on small devices and designed to have full Unicode support in multiple languages.
Lora, a  well balanced comtemporary serif that suits the style I was looking for to contrast the sans-serif Noto Sans and give the site a friendly look and link to food as a feel-good product.
The main image is a stock photo bought from Adobe Stock. It shows a multicultural couple enjoying walking on a market. The asian looking girl pointing at something could be interpreted as someone finding that product she used to enjoy back home. By using a photo not necessarily linked to Ireland will make it easier in the future to expand to other markets.
The colours:
The light purple, green and dark blue give a good contrast and are soft and friendly. The site is providing a service, not selling goods. So without being pushy with screaming colours it should be a pleasant expierence for the user.
The colours used are:
img...:

## FEATURES
####Existing features:

##### Navbar:
Provides the logo, and links to the 'about', 'add product', 'edit product', 'administrator' and 'contact' pages. On small screens the navigation collapses into a hamburger menu (Materialize).

##### Selection options:
Searching a database for products originating from a selection of countries, presented as the flags and initials of the countries, and known to be all time favourites and sold within the republic of Ierland. Click the flag to select country of origin.
Select categories 'beverages', 'food', 'health', 'ingredienst', 'snacks' and 'sweets'.
Sort the selected by 'brand', 'name', 'supplier', 'location' and 'entry date'.

##### Product presentation:
The results are shown on the same page by unfolding the accordion with products. The product is shown with name, brand, an image of the product, a description and the found supplier, with address, location on GoogleMaps (coordinates will be entered by the administrator to avoid mistakes) and the date of entry. Chances of finding the product are obviously better with recent additions.

##### About:
A short description of the purpose and setup of this site and of the developer.

##### Add product:
Users can enter products they found with suppliers in Ireland within the available categories. By entering a personal code users can also edit their entries afterwards.

##### Edit product:
Users can edit the products they added to the database, but only by using the provided user_code.

##### Administrator:
The administrator can add and edit categories if needed and can add the coordinates for GoogleMaps.

##### Contact:
A simple email form for users to leave comments, suggestions or ask questions.


## FEATURES LEFT TO IMPLEMENT
At a later stage the Google Maps functionality can be extended to search products on location and proximity.
More categories and countries of origin can be added when the basic site proves to be a success.
The administrator section will need authentication to be accessed by the administrator only.


## TECHNOLOGIES USED
The navbar and accordion bars css base are taken from the Materialize framework (http://materializecss.com). Bootstrap (http://getbootstrap.com) is used for a lot of the HTML/CSS structure and customised for FoodFromHome.
Flask (https://palletsprojects.com/p/flask/) is used for the Jinja template structure and routing.
An extra library is used for handling the MongoDB database with Python: Python Mongo (pyMongo) (https://pymongo.readthedocs.io/en/stable/).
JavaScript (https://developer.mozilla.org/en-US/docs/Web/JavaScript) is used to work with the GoogleMaps API returning the locations of suppliers as a marker on a map.
JQuery ?

## TESTING


## DEPLOYMENT
The GitPod IDE is used for all the coding and GitHub repositories handle the version control.
Deployment is done on Heroku.
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