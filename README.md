<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFH_logo.png?raw=true" style="margin: 0;">


## Milestone Project 3 - CodeInstitute
#### By Sascha Andeweg
This site is developed as the [third Milestone Project](https://ms3-ffh.herokuapp.com/) for the [CodeInstitute](https://codeinstitute.net), 
covering all modules up till and including Data Centric Development.


[Your food - Your identity: FoodFromHome](https://ms3-ffh.herokuapp.com/) is a website helping you find the 
food you had at home, the food you grew up with. The food you would show off when living in Ireland. 
Because it's part of who you are; your identity.

In Ireland it is not easy to find the products from your home country. But they can be found now. Users can 
add their find on FoodFromHome and add it to the database, making fellow nationals, or anyone else loving these 
types of food, very happy when searching for their favourites on FoodFromHome.

Starting with five countries of origin (The Netherlands, Belgium, France, Germany and Spain), the site can be 
easily extended to more countries of origin. And also, starting with Ireland as the country where the food should 
be sold, this also can be extended to many more countries of course.



## UX
The website has a homepage that starts with the full list of products from the database. The filter options 
are self explanatory: country of origin and category. The simple navigation on top of the site provides an about page, 
explaining the purpose of this site, the link to the page for adding products and a link to the page for editing 
products. Admin access needs no authentification since the site is for educational purposes only and provides 
creating, updating and deleting categories to the database (CRUD).
Adding a product to the database redirects the user to the add supplier page. Suppliers cannot be added to
the database without being linked to a product added.



## USER STORIES
1. A Dutch student looking for Calve peanutbutter searches in category food after selecting origin The Netherlands. 
The product card with basic information for Calve pindakaas is found and with a click on the plus-icon more information 
about the product is given. The name of the supplier is always visible. The entry date gives an indication of how likely 
it is the product is still to be found there.
2. A Dutch resident of Cork city found that a Polish shop sells Lays Paprika crisps (Walkers in Ireland, but paprika isn't 
a flavour sold in the republic). He goes onto FoodFromHome and adds the product with the details of the shop under the 
category Snacks. When entering the details he leaves a password for the entry, so he can later authenticate, edit or 
delete the product when he no longer finds his favourite crisps in this particular shop.
3. An Irish woman living in Longford has lived in Amsterdam for 15 years and has gotten very used to Dutch foods and 
drinks. But also Belgian beers were a very common product in Amsterdam. To bring back good memories and enjoy the 
unique taste of a nice Belgian beer she can go to FoodFromHome and select origin Belgian and select category Beverages. 
There she finds a nice selection. It will take a bit of driving to go to the supplier, but the experience is worth it. 
4. A shop in county Kerry keeps getting Dutch customers asking for Hagelslag (chocolate sprinkles). He manages to find a 
supplier to import the product and goes onto FoodFromHome to add the product and his shop's details so that the Dutch 
community in that part of the country can finally find their favourite sandwich spread.
5. A Spanish language student found her favourite Sangria in a Cork shop and had added the product in the database a week 
ago. However, the product seems to be a one off in the shop's stock and is no longer available. She goes to 
FoodFromHome and using her personal code she can remove the product again.



## WIREFRAME / DESIGN
The wireframe is made in Adobe XD which is also the design. With the principle of mobile first in mind, the full wireframe 
is built in mobile orientation and dimensions (375 x 812 px - iPhone X/XS/11 Pro). For design purposes, the home page is 
also designed in web dimensions 1920 x 1080 px).
The website is responsive, using the Materialize css framework.

<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/webFFHhome.png?raw=true" style="margin: 0;">


<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFHhome.png?raw=true" style="margin: 0;">


<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFHaddproduct.png?raw=true" style="margin: 0;">


<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFHeditproduct.png?raw=true" style="margin: 0;">


<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFHadmin.png?raw=true" style="margin: 0;">


<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFHabout.png?raw=true" style="margin: 0;">



## DESIGN CHOICES:

<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFH_logo.png?raw=true" style="margin: 0;">


The logo is a simple shape with rounded corners and slightly slanted in a lime green with in it the initials of FoodFromHome 
in dark blue for contrast. The full name beside it. All text in the logo is in type Lora which is used throughout the site 
for text in serif. A stylish serif, easy to read, pretty to look at.

This font type Lora comes from [Google Fonts](https://fonts.google.com/) and the sans-serif, Roboto, is the standard 
sans-serif in the [Materialize framework](https://materializecss.com).

The main image is a stock photo bought (free in a trial period) from [Adobe Stock](https://stock.adobe.com/ie). It shows a multicultural couple enjoying 
walking on a market. The asian looking girl pointing at something could be interpreted as someone finding that product she 
used to enjoy back home. By using a photo not necessarily linked to Ireland will make it easier in the future to expand to 
other markets.

The images used for the categories are also stock photos, bought from [Adobe Stock](https://stock.adobe.com/ie). I considered using product photos, but 
they are almost without exception under copyright. This would be too risky, would the site go live to the public.

Initially I set up the products in accordions to be folded out to view the product. However, using the cards from Materialize 
is a user friendly option where the products are more easily found and it makes the site look more appealing.

### The grid
I used the standard grid Materialize uses: small, medium, large viewports. This shows 4, 2 or 1 column of product cards on the page.

### The colours:
The light purple and dark blue give a good contrast and are soft and friendly. The site is providing a service, not selling 
goods. So without being pushy with screaming colours it should be a pleasant expierence for the user. The red (standard from the
Materialize framework) provides a nice balance with the girl's red scarf in the main picture.

The colours used are: 

<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/FFHcolours.png?raw=true" style="margin: 0;">



## THE DATABASE
For the project a NoSQL database MongoDB is used. MongoDB is known for it's flexibility and having no rigid requirements for tables and rows.
The project is suitable for this. However, initially I have set up the database in a slighly relational way, separating the suppliers from the products.
My thought was that products could eventually have several suppliers and suppliers could have multiple products. Also the countries of origin would
be the same for a large group of products and the same goes for the categories.

Working with this structure I learned that binding or aggregating is not an easy thing when handling data on the website. I managed to get filters
on categories and countries to work with products, but it was a very steep learning curve, costing a lot of time. Therefor, because of too much time spent
on these issues, linking the supplier-view to the product cards and adding category images to the product card are future features.

The database at the moment looks like this:

<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/MongoDB_FFH_Page_1.jpg?raw=true" style="margin: 0;">

<img src="https://github.com/Andeweg01/MS3-FoodFromHome/blob/master/static/img/MongoDB_FFH_Page_2.jpg?raw=true" style="margin: 0;">



## FEATURES
#### Existing features:

##### Navbar:
Provides the logo, and links to the 'about', 'add product', 'edit product' and 'administrator' pages. 
On small screens the navigation collapses into a hamburger menu (Materialize).

##### Selection options:
Two filters, providing the five countries of origin (The Netherlands, Belgium, France, Germany and Spain)
and the six existing categories (beverages, food, health, ingredienst, snacks and sweets.
The pages 'Add Product', 'Edit Product' and 'Administrator' provide CRUD (create, read, update and delete 
functionality) on the database for products, suppliers, countries and categories.

##### Product presentation:
The results are shown on the home page as Materialize cards with category image, product name, brand, and entry date. 
The bottom of the card shows the supplier and is always visible, also after clicking the plus-icon to read more: 
description, price and a line saying 'We like this in 'country'.

##### About:
A short description of the purpose and setup of this site and of the developer.

##### Add product:
Users can enter products they found with suppliers in Ireland within the available categories. By entering a personal 
code users can also edit their entries afterwards. Authentication is a future feature. 
After adding the product, the page redirects to 'add supplier'. The details for the Supplier name given for the product
will be stored. A future feature will be a view of the supplier details with Google Maps functionality.

##### Edit product:
Users can edit the products they added to the database. A future feature will be authentication with the personal user_code.

##### Administrator:
The administrator can add and edit categories if needed. A future feature will be authentication with the personal admin_code.



## FEATURES LEFT TO IMPLEMENT
In the process many unexpected issues arose (to be described later) and took more time than I had wished. 
Therefor quite a few wanted features are still missing:
1. Google Maps with markers for the supppliers.
2. Link to the supplier page, presenting supplier details and Google Maps functionality.
3. More categories and countries of origin can be added when the basic site proves successful.
4. The administrator section and editing by users will need authentication to be accessed by the administrator and 
appropriate users only.
5. The proper category image has to be added by the administrator in the MongoDB database manually. In future this will
be done when the user adds the product.
6. Form validation is not working properly. The Materialize validation options that should be working actually don't. 
Where on the first filters (origin and category) you can not filter unless a country of origin is selected, in the other forms
the functionality simply does not do what it's supposed to do. Therefor, unfortunately also, a future feature.



## TECHNOLOGIES USED

### Front-end
* [HTML5](https://en.wikipedia.org/wiki/HTML5) for the HTML structure.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) for styling and editing existing Materialize css-code
* [Materialize framework](http://materializecss.com) framework version 0.100.2 is used for the navbar, accordions, cards, forms and the majority of css code.  
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) version 3.2.1 is used to work with 
* [JQuery](https://jquery.com) which manipulates the DOM

### Back-end
* [Python](https://www.python.org/) (version 3.8.2) for running the python app
* [Flask](https://palletsprojects.com/p/flask/) (version 1.1.2) is used for the Jinja template structure and routing.
* [Python Mongo (pyMongo)](https://pymongo.readthedocs.io/en/stable/) is used for handling the MongoDB database with Python
* [Werkzeug](https://pypi.org/project/Werkzeug) version 1.0.1 a library within Flask with utilities for debugging, testing, etc.
* [MongoDB](https://www.mongodb.com/cloud/atlas) a cloud MongoDB service that runs the MondoDB NoSQL database for the site
* [Jinja](https://palletsprojects.com/p/jinja) for templating
* [GitHub](https://github.com) for version control and storing the repositories
* [GitPod](https://www.gitpod.io) the online IDE for coding, testing and debugging
* [Heroku](https://www.heroku.com) the cloud application platform used to deploy the Python application



## TESTING
Throughout the project some of the main methods for testing were
* before entering the Python development stage (design only), using Adobe Dreamweaver for it's live design functionality and very handy suggestions while designing
* the inspect functionality in Google Chrome for code errors
* running the Python app on GitPod and viewing the debugging in terminal
* deploying on Heroku to see how everything functions when deployed

Testing is done on Windows10, iPhone 7+, Samsung tablet 10", Android Phone.

The test were manual, testing the different filters and CRUD functionality and responsiveness.

### styling
The styling is responsive on all devices and sizes. Colours look good and images are as they're intended.

Found issues:
1. There is a strange problem in the footer on the filtered pages and about page which I haven't been able to figure out. The width does not fill the screen.
2. The + icon for more info on the products disappears when using the size class medium (Materialize). When not using the medium class the alignment of 
the cards goes overboard because of different heights.


### filtering
The filtering of countries and categories works well on all devices and browsers.

### editing products
The editing of products and categories works identically on all devices and browsers and edits the changes from the form.
However:

Found issues:
1. The manually added category images are deleted when updating the product details.

### adding products / suppliers / categories
Adding products, suppliers and categories works on all devices and in all browsers and the redirect to 
adding supplier after submitting also works.
No issues found.

### deleting products / categories
Deleting the products or categories works well on all devices and in all browsers.
No issues found.

### testing Python
It proved to be very usefull to work with print functions in the filtering route. In the Python interpreter (terminal)
it was easier to spot whether or not data was being fetched or filtered.
The error pages when Python fails to run gives clues about where to search for failing code.
The preview from GitPod CL was well used throughout the process.

### testing code
The Python code was checked with [Pep8](http://pep8online.com) and small issues were caught there.
The HTML and CSS was validated with the [W3 validator](https://validator.w3.org/) and with some minor changes no errors were found.


## DEPLOYMENT
In the design phase [Adobe Dreamweaver](https://www.adobe.com/ie/products/dreamweaver.html) was used to speed up the 
design process and make good use of the handy live view. 
The HTML/CSS design during this process was also deployed and tested on a live server (Strato - domain Tradtracker.com). 

In the process I found issues with combining Bootstrap and Materialize. In their css they use the same naming in the CSS 
code for several navigation elements. Inspecting with Google Chrome on the live server proved to be very usefull to find 
the issues and create workarounds in my own code. After finding more and more issues that seemed impossible to overcome I decided
to stop using Bootstrap en continue with Materialize only.

I used the GitPod IDE for testing in the required environment for the CodeInstitute courses. The HTML/CSS files 
are pushed to the GitHub repository to handle the version control.

The Flask/Python part of the project is built within the GitPod IDE and once linked to the MongoDB database, 
deployment is done on Heroku.

### The process:
* In GitHub a repository with full template by the CodeInstitute is generated for use with GitPod.
* In GitPod a site structure is built with a static folder, as required for Flask project, a templates folder and
* files to load and set the libraries, environment variables, configuration files:
   dnspython==1.16.0  
   Flask==1.1.2  
   Flask-PyMongo==2.3.0  
   heroku==0.1.4  
   pymongo==3.10.1  
   python-dateutil==1.5  
   Werkzeug==1.0.1  

   These are stored in the file requirements.txt by using the command: `pip3 freeze --local > requirements.txt`
   So these requirements can easily be loaded again by typing `pip3 install -r requirements.txt`
* In Heroku the app has to be created to be able to run later. 
* It's important to have the variables 'IP' and 'HOST' set and also the Mongo URI key to be able to use the database with Heroku
* In GitPod an env.py file is created to store that same Mongo URI variable. The env.py is stored in the .gitignore so that it doesn't push to the remote servers.
* A Procfile is created to show that app.py will be the Python file to run and we're good to go. Type `echo web: python app.py > Procfile`
* In GitPod login to Heroku by typing `heroku login` and pressing the spacebar. In the preview screen the login can be done.
* In GitPod the remote app is selected by typing `heroku git:remote -a myappname`
* The app has to start running on Heroku by typing `heroku ps:scale web=1`
* The normal process to push files to remote server can be used: `git add .` and `git commit . -m "comments"` and then `git push heroku master` to push to the master branch of our Heroku app.

To run the app.py locally we have to run the Python server `python3 -m http.server` and run `python3 app.py`.
You can now either open a browser or the preview in GitPod.


## Issues in the process
As mentioned before, the conflicts using both Materialize and Bootstrap caused me a lot of problems. 
As I decided to go for Materialize, and based on recommendations in the course material, version 0.100.2 instead of the latest, I ran into more problems.
Materialize seems to be not very well tested or ready for updated browsers. The issues I have not been able to solve are
* The footer width on the filtered products page and the about page.
* The button for more information in the product card that changes layer as the size for the cards is set.
* The validation on forms that does not work in Chrome, and possibly other device/browser combinations.

Only a few days before the submission date I found out that MDBootstrap would have been a very welcome alternative. But time wasn't on my side.
Also the schema I initially made, turned out to be not the best choice. Since suppliers would have been quite unique per product, I could have included them
in the product collection. This would have made it possible to easily create a view of the supplier with the product. Some changes in the add_products and add_supplier
pages and code would have been enough to make that work.

## Credits
#### Content
The content of this site is my own. The products placed in the database are fictional since the site is for educational purposes only.
The photographs are bought licenses from Adobe Stock.
The logo is my own design.

#### Support
The Slack community has been helpful finding answers to many issues.
StackOverflow is a lifesaver and teaches a lot about possibilities and limitations.
The Tutor Support and Mentor from CodeInstitute was awesome. I couldn't have done it without them.
A big thank you for CodeInstitute for their patience and support.