# Luna Pottery - Project 5

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/lunapottery.jpg">

Live link to Application: (https://luna-pottery.herokuapp.com/)

Luna Pottery is an e-commerce online store application built with Django and Python. It allows users to create their own accounts, and experience a full online shopping experience whereby they can purchase items of ceramics and pottery. The application is intended as a template for all small-to-medium arts and crafts people to use to drive sales of their products and to better market their output using a modern, functional web storefront. The application also provides customer engagement by allowing the user to rate or review the products they have purchased.

<hr>

# Table of Contents

- [UX (User Experience)](#ux--user-experience-)
  * [Target Audience](#target-audience)
  * [User Flow Diagram](#user-flow-diagram)
  * [User Stories](#user-stories)
    + [User Stories for Admin User](#user-stories-for-admin-user)
    + [User Stories for Customer User](#user-stories-for-customer-user)
    + [User Stories for Future Version](#user-stories-for-future-version)
  * [Wireframes](#wireframes)
    + [Wireframe of Home Page of Application](#wireframe-of-home-page-of-application)
    + [Wireframe of the Product List Page](#wireframe-of-the-product-list-page)
    + [Wireframe of the Product Detail Page](#wireframe-of-the-product-detail-page)
  * [Agile Methodology](#agile-methodology)
- [System Design](#system-design)
  * [Entity Relationships](#entity-relationships)
- [Application Features](#application-features)
  * [Base Template](#base-template)
    + [Header Section](#header-section)
    + [Footer Section](#footer-section)
  * [Welcome Page](#welcome-page)
    + [Image Slideshow](#image-slideshow)
    + [Call to Action Panels](#call-to-action-panels)
  * [The Products Page](#the-products-page)
  * [Single Product Page](#single-product-page)
  * [Wishlist Page](#wishlist-page)
  * [Shopping Cart Page](#shopping-cart-page)
  * [Checkout Page](#checkout-page)
  * [Profile Page](#profile-page)
  * [Message Alerts](#message-alerts)
- [Technologies Used](#technologies-used)
- [Code Validation](#code-validation)
  * [HTML Validation](#html-validation)
  * [CSS Validation](#css-validation)
  * [Javascript / JQuery Validation](#javascript---jquery-validation)
    + [JQuery code in Cart.html page](#jquery-code-in-carthtml-page)
    + [JQuery code in Products, Add Product and Update Product HTML pages](#jquery-code-in-products--add-product-and-update-product-html-pages)
    + [Javscript code in stripe_elements.js](#javscript-code-in-stripe-elementsjs)
  * [Python Validation](#python-validation)
- [Testing](#testing)
  * [Cross Browser Testing](#cross-browser-testing)
  * [Compatibility Testing](#compatibility-testing)
  * [Responsiveness Testing](#responsiveness-testing)
    + [One column layouts](#one-column-layouts)
    + [The header section](#the-header-section)
    + [The Products/Search Results/Wishlist Pages](#the-products-search-results-wishlist-pages)
    + [The Single Product Page](#the-single-product-page)
    + [The Cart Page](#the-cart-page)
    + [The Checkout Page](#the-checkout-page)
    + [The Profile Page](#the-profile-page)
    + [The Page Footer](#the-page-footer)
  * [Performance Testing](#performance-testing)
  * [User Testing - AUTOMATED](#user-testing---automated)
  * [User Testing - MANUAL](#user-testing---manual)
- [SEO and Marketing Strategies](#seo-and-marketing-strategies)
  * [SEO (Search Engine Optimization)](#seo--search-engine-optimization-)
  * [Social Media](#social-media)
    + [Email Marketing](#email-marketing)
- [Bugs, Errors & Solutions](#bugs--errors---solutions)
  * [Error in Popup Message on Cart quantity adjustment](#error-in-popup-message-on-cart-quantity-adjustment)
  * [Error with Rating of Products](#error-with-rating-of-products)
  * [Account Setup and Password Reset Emails Not Arriving](#account-setup-and-password-reset-emails-not-arriving)
  * [Sorting Products by Average Rating Not Working](#sorting-products-by-average-rating-not-working)
  * [Display Error of Product Stock Warning Colours](#display-error-of-product-stock-warning-colours)
  * [Errors on First Heroku Deployment](#errors-on-first-heroku-deployment)
  * [Cart Quantity Form Validation Error](#cart-quantity-form-validation-error)
- [Future Application Improvements](#future-application-improvements)
- [Deployment of Application](#deployment-of-application)
    + [To successfully deploy the application to Heroku, I undertook the following steps in this sequence:](#to-successfully-deploy-the-application-to-heroku--i-undertook-the-following-steps-in-this-sequence-)
  * [Amazon Web Services Deployment](#amazon-web-services-deployment)
  * [Connect Django to AWS S3 Bucket](#connect-django-to-aws-s3-bucket)
- [Credits](#credits)

<hr>

# UX (User Experience)

## Target Audience
The target audience for this application are lovers of arts and crafts, in particular people who love ceramics and pottery. This target persona will also engage with the application by providing feedback on the ceramic products on offer. This audience may also include those who wish to learn how to create their own pottery by way of the pottery classes that can be booked using the web storefront. These requirements informed the UX strategy for the application, thus needing to display the 2 options of either buying pottery or taking classes clearly on the homepage. This is seen in both the wireframes and final design of the app, with respect to the landing/home page of the site.

## User Flow Diagram
This diagram shows the typical flow of user interactions through the application, and gave a good guidelines as to what user stories were needed to satisfy these user flows.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/UserFlowDiagram.jpg">

## User Stories
There are 2 classifications of user that can use this site, the Customer and the Administrator. The Customer can carry out all expected tasks of a modern web storefront such as purchashing, adding items to cart, reviewing items and placing them on a wishlist. The Administrator is concerned with adding the store products to the store, with all the required details and data. The Admin may also edit or delete the products. The user stories for both user classes are as follows:

### User Stories for Admin User

+ [[#18](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/18)] Add A Product: The Admin user can use the front end form to add a new product with all relevant product details.
+ [[#19](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/19)] Edit A Product: The Admin user can navigate to the individual product page [[#2](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/2)], and click on the Edit button to be directed to a form page where updating can be completed
+ [[#20](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/20)] Delete A Product: The Admin user can follow same path as previous user story, and choose to click the Delete button. A modal popup appears to confirm that the deletion of the product will take place.

### User Stories for Customer User

+ [[#4](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/4)] Create New Account: The Customer can create new account using Sign Up page, choosing email address, username and valid password.
+ [[#6](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/6)] Receive Account Signup Email: The Customer is validated as a user by receiving an email where they click a link and confirm their account, this link forwards user back to application where they see a messsage of confirmation.
+ [[#7](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/7)] Recover Password: The Customer can recover or change their password by selecting the desired link on the Login page [[#5](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/5)]
+ [[#5](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/5)] Login / Logout: The Customer can safely log in and out of the application using their previously validated credentials.
+ [[#8](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/8)] Product Search: The Customer can use the top search bar to find products that interest them by keyword, the search terms searching both product name and description.
+ [[#1](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/1)] View List of Products: The Customer can view a list of all ceramic products by clicking on the relevant link on the homepage menu.
+ [[#10](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/10)] Sort List of Products: The Customer can sort the previously accessed list of products by either clicking in links in dropdowns on the navbar, or by clicking on the dropdown menu futher down page. Items can be sorted by Price, Category, Rating or by Name.
+ [#2](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/2) View Single Product: The Customer can choose a single product from the previously accessed list, either sorted or not [#1](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/1) [#10](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/10), and will be directed to a dedicated page for that product where they can access further info and utilities associated with that product.
+ [#21](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/21) Comment on Product: The Customer can leave a review on the item by commenting using the comment form at bottom of single product page.
+ [[#22](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/22)] Add Product to Wishlist: The Customer can add an individual item to their wishlist by clicking on the heart icon on the single product page.
+ [[#25](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/25) View Wishlist: The Customer can view their wishlisted items by using the heart icon menu item on main navbar, this will direct them to their own unique wishlist page.
+ [[#23](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/23)] Remove Product from Wishlist: The Customer can access their wishlisted items [[#25](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/25)] and choose the one they want to remove by clicking on the desired DELETE button.
+ [[#24](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/24)] Rate a Product: The Customer can give a rating from 0 to 5 for an item by selecting from the drop down menu on the single product page and clicking the RATE button. Customer can only rate an item once.
+ [[#12](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/12)] Add To Cart: The Customer can access the add to cart utility on the single product page. Quantity of items can be modified here also before adding.
+ [[#13](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/13)] View Cart Items: The customer can view current cart items either by clicking the GO TO SECURE CHECKOUT button on the notification popup, or by clicking the Cart icon in main navbar.
+ [[#14](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/14)] Edit Cart Contents: The Customer can modify their cart contents by navigating to the cart page [[#13](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/13)], either by clicking the GO TO SECURE CHECKOUT button on the notification popup, or by clicking the Cart icon in main navbar. Customer can then alter quantities, or delete from cart altogether.
+ [[#3](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/3)] View Cart Total: The Customer can view the total price in cart at any time by viewing the amount underneath the cart icon in the main navbar.
+ [[#15](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/15)] Pay for Cart Items: The Customer can pay for their cart items by navigating to the checkout page and entering delivery info and payment details.
+ [[#16](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/16)] View Order Confirmation: The Customer can verify the order has been completed by viewing order confirmation page after payment.
+ [[#17](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/17)] Order Confirmation Email: The Customer can view a confirmation email, further confirming the order details are correct and completed
+ [[#26](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/26)] View Profile: The Customer can access their own unique user profile page by navigating to relevant link on navbar. Delivery details can be modified, or previous order details can be viewed here.

### User Stories for Future Version
There are a number of unrealised user stories that due to time constraints could not be completed for this application, but would be ideal improvements for future more expansive versions of the project:
+ [[#27](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/27)] Edit A Product Rating: The Customer could alter their previously chosen rating on a product.
+ [[#28](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/28)] Edit Product Review: The Customer could edit their review of a product
+ [[#29](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/29)] Delete Product Review: The Customer can delete the review of a product.


## Wireframes
The following images show wireframes of the 3 primary designs of the application. These wireframes were created using Balsamiq Wireframes.

### Wireframe of Home Page of Application
This wireframe details the homepage of the site, showing the layout of a welcoming slideshow image of some pottery products, some welcome information text, and a couple of call-to-action panels allowing the customer to either view the products or book a pottery class.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/Homepage.png">

### Wireframe of the Product List Page
This wireframe shows how the list of products will appear, with various utilities to sort the display of products in specific orders.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/Products.png">

### Wireframe of the Product Detail Page
This wireframe shows how an individual product page will look after selecting from previous list.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/IndividualProduct.png">

## Agile Methodology

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/agileboard.jpg">

I used the Kanban board in Github to layout the Agile approach of this application. Each user story was submitted as an issue, and as I finished a sprint of work I then moved across the board from Todo, to In Progress, to Done as required. Some of the issues were flagged as Bugs, and returned to once these bugs were resolved. A number of undone features still remain in the Todo section, as they will be for a future version of the application. 

The live link to the project board can be [viewed here.](https://github.com/users/kevinjohnkiely/projects/2)

<hr>

# System Design
Once the system requirements from the Site Users perspective was finalized, a design of information flow was completed to demonstrate how the required data models were needed for the backend of this application. The following entity relationship (ER) diagram displays the relationship between the various data models.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/LunaPotteryERDiagram.png">

## Entity Relationships
The relationships between the data models in this application are as follows:
+ Product - Review (1 to Many): A Product can have many reviews
+ Product - Rating (1 to Many): A Product can have many ratings
+ Product - Wishlist (1 to Many): A Product can be added to many users wishlists
+ Category - Products (1 to Many): A Category can contain many Products
+ User - Review (1 to Many): A User can review many Products
+ User - Rating (1 to Many): A User can rate many Products
+ User - Wishlist (1 to Many): A User can add many Products to Wishlist
+ User - Order (1 to Many): A User can submit many Orders
+ Order - Order Line Item (1 to Many): An Order can have multiple Order Line Items
+ Order Line Item - Product (1 to 1): An Order Line Item can have just one Product

<hr>

# Application Features

## Base Template
The base template provides a structure to the application in that it holds the 2 main features of the application that are common to all views, the header and footer sections. A "base.html" file was created in Django to hold these elements, and also contain the various css and javascript links and files needed for inital loading of the application.

### Header Section
<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/header.jpg">
The header section consists of 4 elements, a logo which stacks to the upper left, a search bar which appears on upper center, and an icon menu which stacks to upper right, which contains the links for logging in/out, wishlist and cart. Underneath this section there is a second row which houses the main bootstrap menu for the product, the various links allowing the user to search products by price, by category and so on. Just below the header section is an information bar, showing the current logged in users email and a message about free postage.

### Footer Section
<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/footer.jpg">
The footer section is the location for 2 important social media aspects of the application, the facebook link in the left column, and the MailChimp signup form on the right. Underneath this in a separate row is some copyright information and a link to the Privacy Policy.

## Welcome Page
This page is the landing page of the application, what the user first sees on login/signup. As well as the previously detailed header and footer, the homepage consists of the following features:

### Image Slideshow

A visually engaging image slideshow of 3 pottery images to enhance the overall visually aspect of the application and showcase what kind of product is on offer. Some introductory text is placed underneath to welcome the user to the site and give a brief explanation of the business.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/slideshow.jpg">

### Call to Action Panels

Underneath the slideshow and welcome text are 2 call-to-actions panels, designed to further showcase the Potterys products. The panel on the left links to all the ceramic products, while the panel on the right links to the pottery classes that are on offer.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/call-to-actions.jpg">

## The Products Page

This view appears on either searching for a product, or by choosing one of the links on the bootstrap menu to filter or show all of the products. The products appear in a 4 column grid on large screens, with some basic information and the image acting as a link to the single product page with more information. Some stock information is also present, with some colour coded messages alerting the user if this item is either low in stock or sold out.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/products.jpg">

## Single Product Page

This view is for an individual product selected by the customer. It shows all the information already shown from products page but also extra essential information such as description, and the ability to rate, review or add item to the cart. A comment panel also appears underneath is section if the user is logged in, the rating and wishlist buttons are also disabled if the user is not logged in. For the site admin user, an extra panel appears in dotted red outline, enabling the superuser to edit the product if needed.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/single-product.jpg">

## Wishlist Page

This view shows the items added to the wishlist by the user, following a similar design layout to the products page, with a 4 column grid layout on large screens. The customer can click on the blue DELETE button to remove item from wishlist.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/wishlist.jpg">

## Shopping Cart Page

This page is the cart page that appears when the user has added items to the cart and navigated to it. Items appear in rows with option to change quantity before purchase. In the bottom row of this page are the totals, subtotals, and links to either continue shopping or to proceed to the Checkout page.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/cart.jpg">

## Checkout Page

The customer is directed to this view once they click the checkout link in the cart page, and are presented with a summary of the items they are about to buy on the right side column, with a form on the left for entering delivery and payment details.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/checkout.jpg">

## Profile Page

This is the profile page view for each customer where they can update their delivery information using the form in the left column, or view their previous orders in the right hand column.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/profile.jpg">

## Message Alerts

A message alert box pops up at the top right of the screen, or center of screen on mobile devices, which give feedback on actions just performed by the user, such as adding items to cart, or rating/reviewing an item. The popup box is closed by clicking on the X button.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/features/messages.jpg">

<hr>

# Technologies Used

The following is a list of the various technologies employed to build this application

+ HTML5 - Hypertext markup language used to give the website its overall structure and semantic value.
+ CSS3 - Cascading Style Sheets used to apply consistent styles across all sections of the application.
+ Bootstrap 4.6.2 - CSS framework to assist in rapid site front end development.
+ Javascript/JQuery - Front end coding language used in a number of templates to provide specific functions.
+ Git/Gitpod - Gitpod used as development platform to build incremental versions of the application and Git commands to backup these changes to Github.
+ Heroku - Platform used for hosting the deployed application.
+ PostgreSQL - This was used as the database storage for the application, it was added as a Resource in the Heroku hosting platform settings.
+ Django - Python based web application framework used to build the application.
+ Font Awesome - Fontawesome toolkit imported into HTML files and its icons used to show button icons and logo.
+ Balsamiq Wireframes - Downloadable software to create the wireframe mockups.
+ Draw.io - Downloadable software to help create UX features such as user flow and ER Diagrams.
+ Stripe - Online payment processor to handle the payments for stock items.
+ AWS S3 - Cloud hosting platform used to store the product images.

<hr>

# Code Validation

## HTML Validation
I used the online validator at (https://validator.w3.org/) to check the HTML of the application. All of the applications frontend views were checked, with the same errors as follows appearing across all pages in the application:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/html-errors.jpg">

+ Error no.1 was corrected by adding a semantic <menu> tag to enclose the list items.
+ Errors no.2 and 3 were solved by changing the ID of "logo-text" to "logo-text-mobile" on the mobile menu HTML section
+ Error no.8 and 9 were corrected by deleting the width and height attributes of the images in question. Width and height is determined by Bootstrap grid and screen size, thus these sizes are not needed on the img tag.
+ A non fatal warning error also appeared, saying that the type attribute of a Javascript tag is not needed, so these tags were replaced as script tags with the src attribute only required.

After correcting these errors, I ran the site through validator again and it passed successfully:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/html-errors-fixed.jpg">

## CSS Validation

There was no need to test the Bootstrap supplied css of this project, however I used a custom css file to supplement these rules located at static/css/base.css. I used the online CSS Validator at (https://jigsaw.w3.org/css-validator) to test the CSS of the application, using the "by direct input" option to copy and paste in the CSS code. As seen below, no errors were reported in the custom CSS:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/css-valid.jpg">

## Javascript / JQuery Validation

I used the online validator at (https://jshint.com/) to test the various JQuery code snippets that appear throughout the application. The results are as follows:

### JQuery code in Cart.html page
+ WARNING: Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. ($)
+ UNDEFINED VARIABLE: $
+ Missing semicolons

The first warning refers to a loop which format I needed to leave as is, to acheive the functionality I required for the shopping cart to function properly, so I was prepared to note this warning but ignore on this occasion. The second warning refers to the $ symbol used by JQuery, and since this is necessary I was prepared to ignore similar warnings in future code snippets.

### JQuery code in Products, Add Product and Update Product HTML pages
+ No warnings or errors

### Javscript code in stripe_elements.js
+ Missing semicolons.

A couple of warnings were supressed when I added the code /*jshint esversion: 6*/ at the top of the JSHint validator. These had to do with template literals which I use sparingly in my code.

## Python Validation
At the time of testing, the online Python validator at (http://pep8online.com/) was offline. As a result, I took a more hands-on approach to validating the python files in this application. In the gitpod development terminal I typed in the command "python3 -m flake8" which output a comprehensive list of how to improve the Python code:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/flake-8.jpg">

The above image shows a typical output from the flake8 command, the only errors showing up as "lines too long", and some unused imports which come from files that were automatically generated on application creation. I meticulously got rid of all the "line too long" issues, and as a result most of these errors now do not appear. In a few instances, the effort to break lines in 2 resulted in some bugs, so I accepted that some of these "line too long" errors were necessary to the overall working product.

<hr>

# Testing

## Cross Browser Testing
The application was functionally tested across the 3 web browsers, Google Chrome, Microsoft Edge & Mozilla Firefox. The site loaded consistently across all 3 and no issues were detected on any browser.

## Compatibility Testing
I tested the site across different devices, such as the Nokia 4.2 smartphone with Android 11, Lenovo Ideapad 3 laptop with different browsers on Windows 11, and on a Dell Studio laptop with different browsers on a Linux Mint operating system. No issues were reported between these devices.

## Responsiveness Testing
I tested this application both during and after development on multiple screen sizes using Google Chromes Developer Tools to ensure that all elements scaled correctly across all viewports. The Bootstrap framework helped a great deal in ensuring a responsive application, but I also had to introduce some of my own CSS rules within Media Queries in the custom CSS file, for any edge cases. The responsiveness testing produced the following results:

### One column layouts
All sections of the application with just one Bootstrap column display as expected across all screen sizes as no stacking or moving of the rows or columns are needed. Some margin or padding values may have had to be altered to suit the screen size. As a result, sections like the homepage slideshow, introductory text, product comment form/reviews, and the login/register page are consistent on all devices.

### The header section
+ On medium and smaller screen sizes, the Bootstrap menu changes to a burger icon and dropdown menu items, as is default on a Bootstrap template. Also, the search box disappears and is replaced instead by a search icon which joins the other icon menu, and generates a drop down search box.
+ On Smaller screen sizes, as the screen gets smaller, the Bootstrap burger button and Site Logo stack beside each other, and underneath the icon menu appears on the next row.
+ On extra small screen sizes, paddings and margins are adjusted and also so save space, the text values of the icon menu items are hidden, leaving just the icons, which are self-explanatory on their own.

### The Products/Search Results/Wishlist Pages
+ The products are displayed in a 4 column grid on larger screen sizes, and as the screen size reduces, the columns become 3, 2 and finally a one column layout for extra small screens. All relevant product information is still visible.
+ The page heading text, the sorting box and the product amount text all stack vertically on extra small screens.

### The Single Product Page
+ This layout moves from a 2 column layout on large and medium screens, to a one column grid on smaller screens, with the image appearing on top and the product information and cart buttons appearing underneath.
+ The second row on small screens with the information and buttons needed to be adjusted with paddings and margins, as the default layout that appeared on smaller screens looked inconsistent and messy.

### The Cart Page
+ On large and medium screens, the tabular format of the cart page displays well, just slightly resizing its table cell widths as the screen size reduced.
+ This layout needed a lot of adjustments for smaller screens. The table layout did not scale well on small screens, everything was too tightly packed with some information not even viewable without scrolling sideways. I decided to create a different table layout with some colspans and rowspans attributes to get the desired result.
+ The cart details HTML table was hidden on smaller screens, and the alternative mobile HTML table was hidden on larger screens. A lot of extra code, but was the solution I chose to make this part of application responsive.

### The Checkout Page
+ This page was another example of a 2 column grid becoming a one column layout on medium and small screen sizes.
+ On small devices, the form for entering delivery and payment details appear first, with the cart details summary appearing below. Some necessary paddings and margins needed adjustment to suit the viewport.

### The Profile Page
+ Again this appeared as a 2 column layout on larger screens
+ On smaller to medium screen sizes, the form for changing delivery details appeared in the top row, with the order history details appearing below.

### The Page Footer
+ On large screens the footer was a 2 column layout, with the facebook link to the left and the Mailchimp signup form to the right.
+ Once the viewport switched to medium/small screen sizes, this layout changed to a one column grid, with the Mailchimp form appearing on the second row.
+ The Mailchimp form and section needed some custom CSS to fit the overall site theme. This needed some time to fix as this section came with its own image and css, so I needed to make it look as I wished. The Mailchimp logo needed to be resized for extra small screen sizes.

<hr>

## Performance Testing

Coming towards the finalization of development of the application, I tested the performance using Google Chromes Lighthouse feature, the results seen below:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/lighthouse-before.jpg">

Obviously the Accessibilty was the most urgent in need of improving so I set to work by checking the suggested improvements from Lighthouse.

+ Fixed the number of duplicate aria ID labels
+ Created more meaningful semantic elements, such as adding a Section element instead of "div id='xyz'"
+ Fixed the hierarchy of heading elements. For example on one page I had a H1, followed further down in the content by a H2, and then a H5. Changing the H5 to a heading size 3 made more sense.
+ In the mobile version of the navbar, there were list item tags with no parent tag, thus I added a Menu tag to house them.

Once I created these fixes, I noticed that the scores for Performance and SEO improved slightly also. I further improved these by reducing the quality on some of the slideshow images for Performance, and added a Meta Description tag to improve SEO. Overall I am much happier with the following scores:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/lighthouse-after.jpg">

## User Testing - AUTOMATED
Due to time constraints on this project, I adopted a manual only testing approach and was unable to carry out automated testing also.

## User Testing - MANUAL

In order to verify that this application was working correctly, I wanted to thoroughly test all user journeys manually, 21 of which would be undertaken by the Customer, 3 of which by the Admin user. I asked a friend to stand in as the Customer User, and I would personally test the Admin actions.

1. Create New Account - Test User had no issues signing up for account. Because I did not want the user to supply their personal email for this process, I created a fake email at (https://temp-mail.org/en/) for testing purposes. Once the user informed me that she had signed up and received a notifcation on screen that their email had to be verified, I checked this temp email inbox.

2. Receive Account Signup Email - From the previous user story, I copied and pasted the verification link, and returned this to the test user. She was able to click this link and was forwarded back to the live application where she saw the message that her email was now verified.

3. Recover Password - This process worked perfectly for the test user, using the same temp email from the previous user journey. User was able to reset password and log back in to the application.

4. Login / Logout - Test User was able to login and logout correctly. I asked the User to enter invalid details on login form, and the required error messages clearly appeared. User was happy with login/logout process.

5. Product Search - Test User found the product search bar very quickly on the desktop screen, but took a little longer to find on mobile due to the different layout. I decided this slight delay wasn't enough to influence a re-design of that section. I asked the user to enter the keyword "clay" in the test and also a keyword of their choice, and the 4 expected pottery items appeared below in page.

6. View List of Products - User reported that it was quite easy to find a list of all available products, finding the 'All Products' dropdown menu and find the desired link beneath. Again, it took slightly longer on the Bootstrap mobile menu, but was again easy to find.

7. Sort List of Products - Test User found it easy to sort the products, and commented that it was extra helpful to have 2 methods to achieve this, both by using the links in the Bootstrap menu, and also the dropdown list box above the product list.

8. View Single Product - Test User was asked to choose to view a single product details, and they found it easy to click on the image to do this. They commented that it was best to have the link on the image as this was the largest item to click and thus the easiest to do promptly. User also commented that it was very useful to have the stock quantities available and more importantly, the colour coded messages about stock running low or being empty.

9. Comment on Product - I asked the Test User to try give a product a review without any instructions as to how to do it. They found it easy to do, however they commented that perhaps a link should appear near top of the product page nearby the rating or wishlist buttons, that would then scroll the page down to the comment form, as it doesnt appear when the page loads. I considered this, but already found that area of page too cluttered with items, so was happy to leave page as is.

10. Add Product to Wishlist - Test User was easily able to add item to their wishlist by clicking the heart icon, although commented that the icon could be a little larger. They commented that the popup notification message at top right hand corner was a nice touch.

11. View Wishlist - The Test User was quickly and easily able to find their own wishlisted items by clicking the icon in the navbar. They commented that this was very clearly labelled and easy to find.

12. Remove from Wishlist - The User found it very easy to remove items from wishlist by simply clicking delete buttons underneath each. Again they commented in positive terms about this section.

13. Rate a Product - The Test User found it quite easy to rate a piece, and commented that it was also useful to have the small text message 'You rated this product' appear where the rating form used to be, to inform the user that they have already rated the piece they are viewing. Also it was verified that the average rating of the product now updated correctly.

14. Add to Cart - Test User was easily able to find how to add items to the cart, and specify a change of quantity before doing so. Again user was pleased to see popup message verifying what they just completed.

15. View Cart Items - The Test User reported that it was very clear what the shopping cart icon in the icons menu navbar was meant to portray, and clicking on it would take the user to the shopping cart page as expected.

16. Edit Cart Contents - This test threw up some errors that I had to fix. The Test User was easily able to delete items from their cart page, and also use the +/- icon buttons to change and update quantities. However, I asked the user to manually add a number into the quantity box that was greater than the amount remaining in stock, and this was still possible. This obviously was an error that I had to fix, and did so with some extra JQuery code in the cart page template. Now, if the user adds too large a number, a red warning box will appear instead of the update quantity link, thus they will not be able to proceed to add a quantity that is greater than stock amounts.

17. View Cart Total - Test User was quickly and easily able to view their cart total on the icon button in navbar. In mobile screens, the cart amount total is hidden so the user was able to click the icon and be taken to cart page where total is clearly visible in large text at bottom of page as "Grand Total"

18. Pay For Cart Items - Test User reported no issues undertaking this task, reporting it as a very similar and recognisable process to other e-commerce payment flows that they experienced.

19. View Order Confirmation - The Test User was happy to see a clear order confirmation of their purchase with everything appearing to be in order.

20. Order Confirmation Email - I checked the temp email that I supplied to the test user and verified that this was working correctly, with all details appearing to be correct.

21. View Profile - I asked the Test User to find how to view their personal profile page, and they found this quite quickly by navigating to the My Account icon button on navbar and selecting relevant dropdown link.

22. Add A Product - I personally tested this user flow, by logging in as the superuser "heroku-admin". I confirmed that the "Add Product" link on the icon navbar under My Account was only viewable by me the Admin user. The Product form worked correctly, with all relevant form validations working in the case of empty fields, or invalid data, for example Postcode needing to be all numbers instead of letters.

23. Edit A Product - I navigated to the Single Product page to find a small Admin panel under the Product description, only viewable to the Admin user. I confirmed that the Update button in this panel takes me to the Product update form which works correctly like the Add Product form does.

24. Delete A Product - On the same Admin panel, I clicked the Delete button and was presented with a modal popup confirming if I want to delete this item. On clicking yes, I confirmed that the correct product had indeed been deleted, which was the case.

<hr>

# SEO and Marketing Strategies

In order to employ an efficient marketing strategy to this application, I undertook a three-pronged approach to acheiving this, by way of SEO techniques, Social Media, and Email marketing.

## SEO (Search Engine Optimization)
As I neared the end of the development of this application, I began to consider how to improve its quality in terms of SEO efficiency. I achieved this by using the following methods:

+ Meta HTML Tags - I added the meta description and keywords tags to the head of the base.html document, with the suitable phrases and keywords to assist the SEO. Also I added the title tag to the head of the document, thus these tags appearing on all pages across the site.
+ Hierarchical Heading Content - I ensured that I used h1, h2 and h3 heading tags in the correct order in the page content, with meaningful content related to the sites keywords within these tags.
+ Image Alternative Text - I ensured that all image content in the site had alt tags to further enhance SEO visibility but also to give assistive technologies the data they need for screen readers etc.
+ External Link - I included an external link to a similar business in the footer of the site, with the rel attribute to suit.
+ Effective Keyword Placement - I re-structured some text content in the homepage, to make sure that the websites most relavant keywords appear where they should, and not be hidden from the SEO web crawlers.

## Social Media
I created a facebook page for this project, with the url for this page linked in the site footer for clear and easy access. The page is [linked here](https://www.facebook.com/profile.php?id=100085932773680), and in case Facebook shuts down this inactive page in near future, some screenshots are available below:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/fb/fb-1.jpg">

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/fb/fb-2.jpg">

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/fb/fb-3.jpg">

### Email Marketing
The third and final marketing aspect was an email marketing form, again placed in the footer of the site for convenient access. An account was created with MailChimp, and a form created there. The HTML of this form was then copied into my base.html page, and I modified the design and CSS to suit. I tested out the form with my own gmail address and it works as expected. The form was already shown in the [features section](#footer-section)

<hr>

# Bugs, Errors & Solutions
During development of the application I encountered a number of bugs and errors, the following list which I was able to find a solution for:

## Error in Popup Message on Cart quantity adjustment
This was not a serious operational error, but one I wanted to fix nonetheless. During testing I discovered the following message appeared in the Popup Message when adjusting the cart quantity items - 'Updated Holy Water Font quantity to {cart[item_id]}'.

Obviously the django code was appearing where a number should be instead, so on examining the code I found that during my refactoring to get rid of the "line too long" warning, I broke the following line into 2 and this caused the error:
    messages.success(request, f'Updated {product.name} ' + 
    ' quantity to {cart[item_id]}')

To fix this I undid the line break and accepted the linting warning, happy that this popup message now showed the correct number format.

## Error with Rating of Products
During the browsing of some of the products, the following error appeared when I would load an individual product page:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/errors/rating-error.jpg">

I noticed that this only appeared for some products, and narrowed it down to an issue with the ratings added by the user for that item. When the user would click the rating form without selecting any value from 1 to 5, the form would send a NONE value to the backend, instead of the expected value of zero. Thus, I added some code to the Products views.py file, in the add_rating method as follows to handle this:

    if rating.rating is None:
            rating.rating = 0

This solved the issue and then to complete the fix I had to go into the django admin site and manually delete all ratings which were recorded as NONE instead of zero.

## Account Setup and Password Reset Emails Not Arriving
During early testing of the Account setup I noticed that no emails were arriving to my Temp Mail accounts, nor could I receive emails to rest passwords. The error returned back was as follows:

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/errors/signup-error.jpg">

 I carefully checked all the required setup steps and code and could find no errors. However, I finally found the error in the Heroku Config Vars section, where I had the environment variable entered there as EAIL_HOST_PASS, instead of EMAIL_HOST_PASS, a simple typo issue. Once I fixed this typo, the emails worked as expected.

## Sorting Products by Average Rating Not Working
Having added products and sorting to the application, I noticed that the products were sorting fine for all methods, except for the average rating. On further investigation, I realised that it was an issue with the name of the rating that I originally applied in the Products model, which was 'avg_rating'.

The problem with this was that the format of sorting worked ideally with the following  JQuery code:

    var sort = selectedVal.split("_")[0];
    var direction = selectedVal.split("_")[1];

Due to the fact that the option value in the HTML code also contained one underscore, my adding of 'avg_rating' as a model field would mean 2 underscores, whereby the above code would fail. After much unsuccessful refactoring of both HTML and JQuery code, I found the easiest solution was to just rename the avg_rating in the Model file to 'rating'. This along with running databaes migrations was in the end an easy fix, and the sorting of ratings now worked fine.

## Display Error of Product Stock Warning Colours
In both the Products page and single product views, I have a stock warning utility where over the images of the products there is a small box with a background colour of green if there is plenty stock left, a warning colour of orange if stocks are running low (less than or equal to 5), or a danger warning of red if no stock remains. During testing I noticed that these displayed all fine, except for if a stock remaining value was 5, then the orange warning did not appear. I discovered in the code that it was a simple logical error in the python code within the HTML page as follows:

    {% if product.in_stock_amount == 0 %}
        <span class="bg-danger p-2 text-white"><strong>SOLD OUT!</strong></span>
    {% elif product.in_stock_amount < 5 %}
        <span class="bg-warning p-2 text-white">Only {{ product.in_stock_amount }} left in stock!</span>
    {% elif product.in_stock_amount > 5 %}
        <span class="bg-success p-2 text-white">{{ product.in_stock_amount }} left in stock</span>
    {% endif %}

I forgot to put "<= 5" in line 3, thus ensuring that the case of stock being equal to 5 would be never reached. I fixed this simple issue by adding the equals symbol.

## Errors on First Heroku Deployment
After the first deployment to Heroku, I received the following error messages in the logs:

    remote: ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects
    remote:  ! Push rejected, failed to compile Python app.

I researched this issue and after consulting with some Slack channel posts about similar issues, I decided to uninstall the backports-zoneinfo package, as this only seemed to work with versions of Python less than 3.9, and my project runs on Python version 4+. Deleting the package, and regenerating the requirements.txt file solved this issue, and deployment worked fine.

## Cart Quantity Form Validation Error
On the cart page, the user is able to adjust the quantity of their item before purchase, and I had some validation to prevent the user selecting a number higher than the amount of that item in stock. This worked fine using the stock amount coming from the model being set as the max value of the input field, however a user could still bypass this by manually typing in a large number, clicking update quantity, and then going to the cart page with an quantity amount not reflecting the stock amount remaining. I wrote some extra JQuery code to fix this issue:

    $('.qty_input').change(function (e) {
        var id = $(this).data('item_id');

        var x = parseInt($(this).val());
        var y = parseInt($(this).attr("max"));
        if (x > y) {
            $('.update-link-' + id).hide();
            $('.qty-error-info-' + id).show();
        } else {
            $('.update-link-' + id).show();
            $('.qty-error-info-' + id).hide();
        }
    });

The basic operation of this code is a change listener that fires when the user attempts to enter too large a number into the input box. The code checks if this value is larger than the max value, and either allows the update link to be available, or in its place displays a red error box saying "Not Enough Stock". While this fixed the issue, I noticed that this would only work for one input box in the cart, so if mulitple items were in the cart, the red warning notice would appear for unrelated cart items, which was not ideal. As a result I added the following extra code to ensure that the change handler was fired only by the input box that required it:

    for (let x = 0; x <= 50; x++) {
        $('.qty-error-info-' + x).hide();
    }

This is not an ideal solution as the 50 in the for loop refers to the number of different products in stock, so if this was increased the developer would have to remember to find this line of code and update accordingly. Also, this method creates a lot of extra potentially avoidable processing loops which may slightly slow down the loading of the cart page. However, given the timeframe constraints I am happy with this fix but recognise with more time I may have come up with a more elegant and future-proofed solution.

<hr>

# Future Application Improvements

During the development of this application I began to consider a number of potential future improvements given a more lengthy timeframe. In the Agile Kanban board, I already listed 3 items as 'Todo' for future iterations of the project, they are:

+ Allow the Customer to change a Product Rating
+ Allow the Customer to delete a Product Review
+ Allow the Customer to edit a Product Review

There are also a few more enhancements to this application that could improve it overall:
+ Have an image gallery for each single product page by using a carousel similar to site homepage. This would be ideal for the customer as some products would need multiple image views to get a feel of their quality, given the items 3 dimensional nature. This could also work as a pinch-and-zoom image utilty on mobile devices.
+ Implement a 'rewards' utility where the Customers could earn points with every purchase and result in possible discounts on future purchases. This points total could be accessed on the current User Profile page.
+ Creation of some video content for the Pottery Classes page, to give the viewer a better feel for what is taught and further entice interested customers to purchases some classes. Such extra content creation would also benefit the sites Social Media and SEO strategies.
+ Allow the user to sort products by stock amounts, so they can quickly ignore what items are sold out, or what items have a plentiful supply in stock.

<hr>

# Deployment of Application

### To successfully deploy the application to Heroku, I undertook the following steps in this sequence:

1. Create a new app on Heroku with a suitable name
2. On Resources tab in Heroku, provision a new database by selecting the Heroku Postgres free plan database.
3. In Gitpod, install dj_database-url and psycopg2-binary packages, and freeze the requirements.txt file to ensure Heroku install these on deployment
4. In settings.py file, import the dj_database_url and add the required database URL from Heroku. Database URL is found in the Config Vars setting in Heroku.
5. Run migrations once more because we are now connecting to a new database on Heroku.
6. Create an if/else statement in settings.py file, determining which database is being connected to
    if "DATABASE_URL" in os.environ:
        DATABASES = {
        'default': dj_database_url.parse('postgres://bydautguzdijlc:bda52676988bc7d0af64907579f2d0760f075a912dea7fa4c28fcefde75e8215@ec2-54-228-125-183.eu-west-1.compute.amazonaws.com:5432/da8ju8pb7nn6i7')
        }
    else:
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
7. Create a DATABASE_URL environmental variable in the Gitpod variables.
8. Create a superuser account that can now login into application connecting to Heroku Database.
9. Ensure Gitpod is connected to local database, and perform dumpdata commands on the models that I require:
    python3 manage.py dumpdata products > products.json
    python3 manage.py dumpdata categories > cats.json
10. Ensure the connected Database is now the Heroku version
11. Transfer the data over by the following commands, and in this order due to foreign key constraints:
    python3 manage.py loaddata products.json
    python3 manage.py loaddata cats.json
12. Remove DATABASE_URL from Gitpod variables
13. Install the gunicorn package to act as web server, and generate requirements.txt file
14. Create Procfile locally for Heroku web dyno to serve the application.
15. In terminal type command: heroku config:set DISABLE_COLLECTSTATIC=1
16. In settings.py, add the heroku app hostname and localhost to ALLOWED_HOSTS collection
17. Use git commands to add and push to github, then type the command of 'git push heroku main' to deploy to heroku
18. Set automatic deployments by navigating to Deploy tab in Heroku, search for and connect to repository and select 'Enable Automatic Deploys'
19. In settings.py, set DEBUG to True only if there is environmental variable called DEVELOPMENT.
20. In settings.py, remove SECRET_KEY and set it to get this from environmental variable instead, setting its default to empty string.

## Amazon Web Services Deployment
21. Create a new AWS account at aws.amazon.com, selecting username and password and then open the S3 service.
22. Create new s3 bucket to match app name in project, and turn on static web hosting in Properties.
23. In Permissions tab, set relevant CORS configuration
24. Generate a new security policy for the bucket, copying in ARN (Amazon Resource Name) from previous step
25. In Access Control List, select List Object to enable access for everyone
26. Open IAM service in AWS and create a new Group in User Groups section.
27. Select the user group created, and on Permissions tab open Add Permissions and click attach policy.
28. Select the polic and click Add Permissions.

## Connect Django to AWS S3 Bucket
29. In Gitpod workspace install boto3 and django-storages packages, and freeze requirements.txt
30. In settings.py, add 'storages' to INSTALLED_APPS collection
31. Check if USE_AWS is in the environment variables and if so add the variables as follows:
    AWS_STORAGE_BUCKET_NAME = 'luna-pottery'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
32. In Heroku admin, add keys listed in step 31 to Config variables. Also add USE_AWS variable and set to True, and remove the DISABLE_COLLECTSTATIC variable
33. In Gitpod application root folder, create new file custom_storages.py and add following code:
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

    class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

    class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
34. In settings.py, add the following code:
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
35. Perform git push and build project, all static files will be collected succesfully and also appear in static folder in AWS s3 bucket
36. Go to s3 folder in AWS and create new folder called media, select all product images.
37. In Manage Public Permissions, select Grant Public Read Access to this object(s), and click upload
38. Add Stripe API keys STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to Heroku Config vars
39. Add new webhook endpoint in Stripe to reflect heroku endpoint URL, choosing to receive all events
40. Reveal webhook signing secret and add to Heroku config variables as STRIPE_WH_SECRET.

<hr>

# Credits
+ Some image content for this application came from Pexels (https://www.pexels.com/). All product image content was my own property.
+ Diagnosis and error solutions were greatly helped by consulting the Code Institute Slack Community.
+ Expert guidance on the subject matter given by my Code Institute mentor, Adegbenge Adeye.
+ Icons supplied by [Font Awesome](https://fontawesome.com/v4/)
+ The Code Institute project walkthrough Boutique Ado provided the foundation for the design of this application.
+ Countless tips and solutions accessed on [Stack Overflow](https://stackoverflow.com/)
+ The offical [Django documentation](https://docs.djangoproject.com/en/4.1/) was a big help in some aspects of this project