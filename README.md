# Luna Pottery - Project 5

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/lunapottery.jpg">

Live link to Application: (https://luna-pottery.herokuapp.com/)

Luna Pottery is an e-commerce online store application built with Django and Python. It allows users to create their own accounts, and experience a full online shopping experience whereby they can purchase items of ceramics and pottery. The application is intended as a template for all small-to-medium arts and crafts people to use to drive sales of their products and to better market their output using a modern, functional web storefront. The application also provides customer engagement by allowing the user to rate or review the products they have purchased.

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


## Wireframes
The following images show wireframes of the 2 primary designs of the application. These wireframes were created using Balsamiq Wireframes.

### Wireframe of Home Page of Application
This wireframe details the homepage of the site, showing the layout of a welcoming slideshow image of some pottery products, some welcome information text, and a couple of call-to-action panels allowing the customer to either view the products or book a pottery class.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/Homepage.png">

### Wireframe of the Product List Page
This wireframe shows how the list of products will appear, with various utilities to sort the display of products in specific orders.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/Products.png">

### Wireframe of the Product Detail Page
This wireframe shows how an individual product page will look after selecting from previous list.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/IndividualProduct.png">

<hr>

# System Design
Once the system requirements from the Site Users perspective was finalized, a design of information flow was completed to demonstrate how the required data models were needed for the backend of this application. The following entity relationship (ER) diagram displays the relationship between the various data models.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/LunaPotteryERDiagram.png">