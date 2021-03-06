# Ashleigh Baking School

## Introduction
This is an e-commerce website for a small baking school to sell their baking courses.  The initial thought of this project was initiated by the thought of many small businesses that are struggling to pitch to wider population due to lack of digital platform and relying in many cases on words of mouth or in newspaper advertisements.

It uses HTML, CSS, Javascript, Python and Django as taught by Code Institute to bring the real world e-commerce website.

### A. Objectives
The objectives of creating this app are:

Users:

- to allow users to browse through courses, place bookings and complete payment online.

- to allow users to buy gift cards as special gifts for special occasions.

- able to get to know the team that runs the school and location of the school.

- able to submit any inquiry through the contact page.

B. Owner of this baking school:

- to add, update or delete courses and gift cards through admin area.

- able to advertise next coming event to draw customers’ attention on the homepage.

- to able to add or edit member info.

- able to track and modify orders and check on inquiries submitted.

### B. Wireframes

[wireframe-desktop1](static/img/wireframes/Desktop1.png)

[wireframe-desktop2](static/img/wireframes/Desktop2.png)

[wireframe-desktop3](static/img/wireframes/Desktop3.png)

[wireframe-desktop4](static/img/wireframes/Desktop4.png)

[wireframe-desktop5](static/img/wireframes/Desktop5.png)

[wireframe-mobile1](static/img/wireframes/mobile1.png)

[wireframe-mobile2](static/img/wireframes/mobile2.png)

[wireframe-mobile3](static/img/wireframes/mobile3.png)

### C. User Stories

**Homepage**

The Jumbotron is of food image to give impression of this app is about food.  The overlay with a big heading of ‘Welcome’ inviting user at first sight to explore the app.  The paragraph on ‘It is never too late to learn or up-skills’ encourages user to learn a new skill.  There is an ‘Browse Courses’ button which leads to all courses page for user to browse.

Below the Jumbotron showed the next event with date and time and a button of course name which user can click on leading directly to that course.

On the same page, there are a few past students’ feedbacks as reference of the courses they had did.  These may help to guide generally about courses offered by the baking school.

Footer showed that this baking school can be followed on social medias, the venue where courses will be run and contact’s link that bring user to the contact page directly.

**Have a Browse page**

This page displays all products in the database with links to individual product page using the ‘More Info’ button.  Jumbotron gives general information about baking courses. The pagination is clearly shown on the bottom if there are more than six courses in the database.  If less than six courses, no pagination will be shown.  In addition, I can also filter the categories of products  through the category buttons. 

**Single Course/Gift Card Page**

This page shows the individual product’s details and add to basket button if user wants to purchase. It also allows increasing or decreasing the quantity of course and a message will appear just below the basket icon on the top right corner if product is added or updated.  The grand total amount will be reflected on the basket icon on the navbar.  It also showed the person image and name who will conduct that particular course.

Gift card page shows the image of gift card and general information about it such as validity and free postage.

**Shopping Basket**

This page shows the items that are added from browsing the courses or gift cards.  It include the image of the product, date and time as well as the price.  The grand total is clearly showed on the top right corner above the basket table.  In the basket table, user can update the quantity of similar item or remove item through update or remove button.
At the bottom of the table, there is button for secure checkout or continue browsing to help to guide user what he or she can do next.

**Secure Checkout**

This page are forms that required users to enter their information including their personal details, delivery address, personal message to be inserted in gift card and payment details at the bottom.  Users  either can complete the order by clicking on complete order or adjust basket if they change their mind.  Grand total is clearly showed above the payment as well as text in red about amount of payment will be charged to card is also shown just right below ‘complete button’.

**Success Checkout**

A confirmation of success checkout if payment successful will be displayed along side with item information and order number.

**Our Team Page**

This page is about chefs who run the baking school and general information on their baking qualification.

**Our Kitchen Page**

This gives information about the location and how to reach the venue as well as a peek of the kitchen through the kitchen image.

**FAQ**

This gives general information for users about courses and if more information required, user can simply contact the baking school by clicking on button 'contact us' just below FAQ.

**Contact**

This page mainly gives information on ways to contact the baking school, either through email, post or phone.  Users can also fill in inquiry form for the baking school admin team to call or respond to them.

**My Account**

User can register or login through the My Account on the top of the navbar.  Any fields that are not  filled in will be prompted to fill in or if password features not unique will prompt user to consider other passwords before submitting.  After logged in, user can update their addresses through the update button in My Account page and view any previous order history.  This website allows user to complete purchase without registering.



###  D. FEATURES

- **Top NavBar** - This is non-collapsible Navbar features so that in the small screen, the name of the baking school, My account’s dropdown as well as Basket icon are still visible on the top.

- **Navbar** - This feature uses Bootstrap Navbar toggles and collapsible features which allow when in smaller screen to toggle and collapse, featuring  like a dropdown for easier navigation.

- **Footer** - The footer is simple with ‘Follow Me’ wording which clearly indicates to users that they can also follow the baking school on social medias. This uses font awesome social media icons.  It also shows the kitchen’s address and contact methods.  The contact is using font awesome icons that when user clicks will direct them to the contact page.

- **Message Pop-up** - A message with different colour will appear just right under basket icon whenever user add new item, update item, delete or completed order successfully.  This uses bootstrap’s toast feature.  This also works whenever user login or register successfully.

- **Homepage** - Bootstrap 4 Jumbotron with responsive heading used in the top section as shoutout to welcome user to browse through this baking school website.  Button feature is used so user can click on ‘Browse Courses’ leading to ‘Have a Browse’ page.


Below the jumbotron is a section to display the next course event that helps user to quickly reach the detail of the course by clicking on the course name button.  This information is fetched from the backend if the admin ticked on ‘next_event’ field.


Right under that section is a section which uses bootstrap 4 grid system and card decks for responsiveness and displaying the students’ feedbacks. These however are static.

- **Have a Browse Page** - This page uses card decks group components from Bootstrap 4 to display all products in the database.  It also uses button features for filtering categories.  Each card shows the course image, title, date, time and price fetched from the database. Django pagination feature is used here if card decks more than 6 in a page for ease of navigation.
’More Info’ button at the bottom of each card leads to individual product page.

- **Individual product page** - Each of these pages showed details of the product.  All information are fetched from the database.  The quantity decreasing and increasing button utilising javascript features.

- **Shopping Basket** - This uses bootstrap table features.  The increase and decreasing button is performed by javascript features.  Subtotal can be updated through the update button.  These all done through Django.

- **Secure Checkout** - This page uses Django form features as well as crispy form feature for the appearance of the form.  Payment method is utilising Stripe payment installation.

- **Our Team** - The member displayed in the team section are all fetched from database.  If more members joining the school, this can be easily added through admin and display in the our team page.

- **Contact Page**- The ‘Make An Inquiry’ is a button that if clicked on will bring on a modal.  This uses Bootstrap Modal features.  Form in the contact uses Django form feature as well as crispy form features.

- **Register/Login** - This uses Django All-auth library with some adjustment by CSS.  User details can also be saved into database if ‘save information’ is clicked.

**_Features to implement in future_**

1.  To able to incorporate event calendar for ease of selecting courses according to months.
2.  To create blogs that owner can provide information such as new recipes or event feedbacks.
3.  User to be abled to modify date of courses bought within 14 days of purchases without charges.

### E.Technologies Used

[Adobe](https://www.adobe.com/ie/products/xd.html?promoid=PYPVQ3HN&mv=other/)

Why it is being used:  Recommended by my mentor and it gives a good idea of wireframes even to the details of colours and images.

[Bootstrap v 4.4](https://getbootstrap.com/)

Why it is being used: As mobile digitals are increasing and so widely used, Bootstraps has been chosen for mobile first -approach for the design of the webpages so that it can be easily made responsive with many different features offered.

**Bootstrap own Javascript, jQuery and Popper.js**
(https://getbootstrap.com/docs/4.3/getting-started/introduction/)

 Why it is being used: As many of bootstrap v4.3 required use of Javascript, jQuery and Popper.js, these technologies were also incorporated into this project.    
     
**HTML5**
 
 Why it is being used: Using up-to-date features offered which is HTML5 through Cloud9 IDE for programming languages.

**CSS3**

Why is being used: Using the latest Cascading Style Sheets to support for responsive designs and styling.


[W3C Markup Validation Service](https://validator.w3.org/)
Why it is being used: to help to validate codes


[Font awesome](https://fontawesome.bootstrapcheatsheets.com/)
why it is being used: to add icons

[Python 3](https://www.python.org/downloads/)
why it is being used: back-end programming languages

[Django 3.0.7](https://www.djangoproject.com/)

[Jinja 2.11.x](https://jinja.palletsprojects.com/en/2.11.x/)
why it is being used: templating languages for Python for fetching backend data to the front-end.

[Heroku](https://www.heroku.com/)
why it is being used: cloud based application allowing me to build and run my application.

**Other packages or dependencies installed**:

_boto-3 1.14.9_

_dj-database-url_

_django-allauth_

_django-countries_

_django-cripsy-forms_

_django-storages_

_gunicorn_

_pillow_

_psycopg2-binary_

## DATABASES used:

_Postgres_ in deployment

_SQlite_ in development

## VERSION CONTROL:

- _Github_ : remote repository used in this project and hosted in _Heroku_

### F. Testing

In the process of developing this project, **Chrome Development Tool** was used to assess responsiveness as well as designing and debugging.  HTML validator was used to validate the codes.

##### **Manual testings:**

[W3 HTML validator](https://validator.w3.org/)

Deployed project tested on multiple devices including iphoneSE, iPhone 7, iPad and MacAir.  
Chrome Development Tool used for desktop version.

Each features in the project has been tested in all these devices by making single or multiple purchases of courses and gift cards and all successfully completed the checkout process and orders appear in admin area.  Inquiries submitted also appeared in contact in admin area.

Login and Register features also tested. Admin area accessed by superuser account created.

### G. Local Deployment

1. An IDE will be needed to run this project locally.

2. In [Github](https://github.com/capel82/ashleigh_baking_school), choose the ashleigh_baking_school repository and on the right top corner, click on *code* green button to clone the codes. 

3. Copied the URL  *https://github.com/capel82/ashleigh_baking_school.git* and at the IDE terminal type in `git clone https://github.com/capel82/ashleigh_baking_school.git` to clone into chosen working directory.

4.  Create env.py to insert all secret keys required.

import OS

os.environ[“SECRET_KEY”] = “Password”

os.environ[“STRIPE_PUBLIC_KEY”] = “Password”

os.environ[“STRIPE_SECRET_KEY”] = “Password”

os.environ[“STRIPE_WH_SECRET”] = “Password”

os.environ[“DATABASE_URL”] =“Password”

5. import env.py in settings.py

6. create requirements.txt with command:

`pip3 install -r requirements.txt`

7. run the project with command: 

`pip3 manage.py runserver`

8. you should be able to open the browser through expose port.

### G. Deployment to Heroku

1. Create Heroku App at www.heroku.com.  Log in heroku.com or register a new account if first time using.  At the top right corner, create ‘New app’ button and give the app a name.  In this project is ‘ashleigh-baking-school’ and choose Europe region.

2. Under Resources tab, insert ‘Heroku Postgres - using “Hobby Dev-Free” ’ as Add-ons. 

3. In Gitpod IDE, install _dj_database_url_and _psycopg2-binary_ with pip commands as below:

	`pip3 install dj_database_url`
	`pip3 install psycopg2-binary`

4.  Then, update requirements.txt

	`pip3 freeze > requirements.txt`

5. in project setting.py, insert following:

	a. import dj_database_url 

	(just under import os at the top of this setting.py)

	b. under Databases, insert if and else statement:

	```
	if ‘DATABASE_URL’ in os environ:
		DATABASES = {
			‘default’: dj_database_url.parse(os.environ.get(‘DATABASE_URL’))
			}
	else:
		DATABASES = {
			‘default’: {
			‘ENGINE’: ‘django.db.backends.sqlite3’,
			‘NAME’: os.path.join(BASE_DIR, ‘db.sqlite3’),
			}
	```
	

6. In Heroku app, replace config vars with postgres url

7. Once all the settings in placed, in order to get all databases set up in postgres, migrations need to be done by following commands in terminal:

	`python3 manage.py showmigrations`

	`python3 manage.py migrate`

	`python3 manage.py loaddata` (if there is JSON files)

8. Create super user with command in terminal:

	`python3 manage.py createsuperuser`

	-which will prompt for username, password and email.

9. Install Unicorn:

	`pip3 install unicorn`

10. Update requirements.txt:
	
	`pip3 freeze > requirements.txt`

11. Create Procfile in the root of project.  Insert 

	web: unicorn ashleigh_baking.wsgi:application

12. Login Heroku from terminal:

	`heroku login -i`

13. Disabled collectstatic:

	`heroku config:set DIASABLE_COLLECTSTATIC = 1 - - ashleigh-baking-school`

14. Under settings.py, insert allowed hosts:

	`ALLOWED_HOSTS= [‘ashleigh-baking-school.herokuapp.com', ‘localhost’]`

15. Update codes by git add/commit/push as well as heroku:

	`heroku git:remote -a ashleigh-baking-school`

	`git push heroku master`

16. Create django secret key generator from website https://miniwebtool.com/django-secret-key-generator/. Then, enter into config file in Heroku.

17.  Connecting to AWS amazon.com S3:

	a. create an account at aws.amazon.com and under S3, create bucket and choose allow public access.
		i. properties : ON:static website hosting
		ii. permission: CORS configuration
		iii. bucket policy:
			- select policy generator
				type: S3 bucket policy
				ARN:
			- generate policy then copy into bucket policy 
	b. create user identity to assess the bucket:
	IAM (Identity and Access Management(IAM)
		i. create a group by giving it a name
		ii. create policy
			- under JSON tab: 
				SELECT import manage policies
				SELECT S3 import Amazon S3 Full Access

		iii. create user

18.  Connect Django to S3:

	i. in terminal,

		`pip3 install boto3`

		`pip3 install django-storages`

	ii. in settings.py,

		`INSTALLED_APP : ‘django_storages’`

19. Git add . git commit and git push to deploy project to Heroku.



### H.Credits

**Codes**

Codes for Basket and Checkout Apps were taken from Boutique Ado Video Tutorials by **Chris Z** in Code Institute lessons. These include signals, webhooks, stripe, email and forms features taught by Chris Z.

Codes for pagination were taken from **Brad Traversy** tutorial on ‘Python Django Dev to Deployment’ in Udemy.

**Images**

1. Images :

	a. ‘Churros with powdered sugar’ - by Pixabay at [pexels](www.pexels.com)

	b. ‘Baked bread platter on tabletop’ - by Lucie Liz at [pexels](www.pexels.com)

	c. ‘Berry closed up cooking’ by Mali Maeder at [pexels](www.pexels.com)

	d. ‘Men’s White Dress Shirt’ by Mentatdgt at [pexels](www.pexels.com)

	e. ‘Brown haired girl in sleeveless dress' at [pexels](www.pexels.com)

	f. ‘contact’ at [pexels](www.pexels.com)

2. Kitchen image: by Lisa R at www.biencuitglutenfree/residentialclass/cookery-kitchen-3/

3. All courses images : [bbcgoodfood.com]www.bbcgoodfood.com

4. All gift cards images : [Amazon EU](www.amazon.com)(giftcards)


### I. Acknowledgement

A special thanks to my mentor **Maranatha Ilesanmi** who has very kindly encouraged, guided and taught me with so much patience towards me in finishing this third milestone project.

Not forget the tutors in Code Institute who had faithfully helping to solve any problems arising in completing this project.