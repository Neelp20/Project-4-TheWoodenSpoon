# The Wooden Spoon

The Wooden Spoon is a fictional restaurant, which has a amazing setting and heartfelt hospitality promise a dining experience as memorable as the view.
Our each dish crafted from the freshest ingredient sourced and we honour the flavour of the region in every bite.
The live link can be found here: [Live Site - The Wooden Spoon](https://the-wooden-spoon-cfb803cde318.herokuapp.com/)

![Mock Up](docs/readme_images/mockup.webp)

## Table of Contents
- [Sizzle and Steak](#sizzle-and-steak)
  - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
  - [Credits](#credits)


# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed to help restaurant staff to easily manage the menus displayed on the website, as well as keeping track of upcoming bookings and capacity, editing and deleting as neccessary. 

The site also aims to provide customers with a simple, hassle free way to make reservations online or by calling the restaurant. They will also be able to cancel their bookings or update when needed.

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. spaced out evenly over four weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have."Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/Neelp20/projects/17/views/1) and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

![Kanban image](docs/readme_images/kanban.webp)

#### Epics

The project had 7 main Epics (milestones):

**EPIC 1 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

**EPIC 2 - Stand alone Pages**

The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

**EPIC 3 - Authentication Epic**

The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it the staff would not be able to managed the bookings securely without regular site visitors also being able to see and perform actions.

**EPIC 4 - Menu**

The menu epic is for all stories that relate to the creating, deleting, editing and viewing of menus. This allows for regular users to view menus and for staff to manage them with a simple UI interface.

**EPIC 5 - Bookings**

The booking epic is for all stories that relate to creating, viewing, updating and deleting bookings. This allows the staff to easily view upcoming bookings, manage the bookings and also for customers to book and manage their own reservations.

**EPIC 6 - Deployment Epic**

This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

**EPIC 7 - Documentation**

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.


#### User Stories

The following user stories (by epic) were completed:

**EPIC 1 - Base Setup**

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

As a developer, I need to create static resources so that images, css and javascript work on the website

As a developer, I need to set up the project so that it is ready for implementing the core features

As a developer, I need to create the footer with social media links and contact information

As a developer, I need to create the navbar so that users can navigate the website from any device

**EPIC 2 - Stand alone Pages**

As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist

As a developer, I need to implement a 500 error page to alert users when an internal server error occurs

As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views

As a restaurant owner, I would like a home page so that customers can view information on my restaurant

**EPIC 3 - Authentication Epic**

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

As a Site Owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used.

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling.

**EPIC 4 - Menu**

As a staff user, I want to be able to create a new menu/menu items when we have new dishes to offer

As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant

As a staff user, I want to be able to edit a menu/menu items when updates are needed

As a staff member, I would like to receive feedback when I create or update menus so that I can see they have worked

As a staff user, I want to be able to delete a menu when it is no longer used

**EPIC 5 - Booking**

As a user, I would like to be able to create a new booking when I want to visit the restaurant

As a user, I would like to view my bookings when I need to check the information

As a user, I would like to be able to edit a booking so that I can make changes when needed

As a user, I would like to receive feedback when I create a booking or edit one so I know it was completed successfully

As a staff user, I want to be able to search a booking by name/email or date to save time searching

As a user I would like to delete a booking when I no longer require it

**EPIC 6 - Deployment Epic**

As a developer, I need to set up whitenoise so that my static files are served in deployment

As a developer, I need to deploy the project to heroku so that it is live for customers

**EPIC 7 - Documentation**

Tasks:

* Complete readme documentation
* Complete testing documentation write up

## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality on Menu and Bookings
* Restricted role based features
* Home page with restaurant information

## The-Structure-Plane

### Features

``USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device``

Implementation:

**Navigation Menu**

 The Navigation contains links for Home, Menu, Bookings and has allauth options.

 The following navigation items are available on all pages:
  * Home -> index.html - Visible to all
  * Bookings (Drop Down):
    * Create Booking -> bookings.html - Visible to logged in users
    * Upcoming BookingS -> manage_bookings.html - Visible to logged in users
    * Past BookingS -> past_bookings.html - Visible to logged in users
    * All Bookings(Admin) --> admin_manage_bookings.html - visible to admin only
  * Menus (Drop Down):
    * View Menus -> menu.html - Visible to all
    * Create Menu -> create_menu.html - Visible to staff
    * Create Menu Item -> create_menu_items.html - Visible to staff
    * Create Allergy Label -> create_allergy_label.html - Visible to staff
    * Manage Menu -> manage_menu.html - Visible to staff
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](docs/readme_images/navbar1.webp)
![Navbar](docs/readme_images/navbar2.webp)
![Navbar](docs/readme_images/navbar3.webp)

``USER STORY - As a restaurant owner, I would like a home page so that customers can view information on my restaurant``

Implementation:

**Home Page**

The home page contains a hero image of a restaurant and the restaurant information at the top of the page. This will immediately make it evident to the user, what the purpose of the website is.

Under the information section, the opening hours of the restaurant and address with contact details, which will allow the user to locate the restaurant and operating times. and there are two buttons, 'View Menu' and 'Reserve a table'. These buttons will allow the user a quick way to the respective pages if they wish to view menu or make a booking.

![Hero Image](docs/readme_images/homepage.webp)

![About and Find Us](docs/readme_images/homepage1.webp)

``USER STORY - As a developer, I need to create the footer with social media links so that the customer can follow us``

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a Twitter, Instagram and Facebook link so that users can follow the restaurant on social media if they want to keep up to date with special offers not advertised on the website. These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.

![Footer](docs/readme_images/footer.webp)

``USER STORY - As a Site Admin I can create or update the menu page content so that it is available on the site``

Implementation:

**Create Menu/Menu items Page**

A create menu page was implemented to allow staff users to create new menus via the UI without having to use the backend admin panel. This will allow staff the ability to quickly update menu/menu items when they have made changes to the food being offered.

![Create Menu](docs/readme_images/createmenuitem.webp)

``USER STORY -As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant``

Implementation:

**View Menu Page**

A menu page has been implemented to allow users to see the current active menus and decide whether they are interested in the food we offer before booking. This is visible to all users regardless of logged in state as it is not user friendly to restrict core information from users to force them into signing up.

![View Menus](docs/readme_images/menupage.webp)

``USER STORY - As a admin user I can edit the menu/menu items so that updated version will be available``

`` USER STORY - As a staff user I can delete the menu/menu items so that Customer can view only what is available up to date``

Implementation:

**Edit Menu Page**

On the manage menus page a button was added to allow staff members to edit a menu when changes need to be made.

![Edit Menu](docs/readme_images/managemenu_admin.webp)

``USER-STORY - As a user, I would like to be able to create a new booking when I want to visit the restaurant``

Implementation:

**Create booking page**

A booking page was implemented with a form that takes in the customer details and enables the user to easily make a booking through the UI. 

Extensive logic was added to the form validation to ensure that not only is there a table available for the users chosen time and date but also that it has enough seats for the amount of guests. If the form is successful with validation on the front end, logic is in place to find the lowest capacity table to seat the guests for the given date and time.

This allows for seat optimisation to ensure we do not have small amounts of guests at tables that could of been booked for larger groups. Ensuring table optimisation and revenue for the restaurant.

![Create Booking](docs/readme_images/create_booking.webp)

``USER-STORY - As a user, I would like to view my bookings when I need to check the information``

``USER-STORY - As a user I would like to delete my booking when no longer require it``

Implementation:

**Upcoming bookings page**

A upcoming bookings page was implemented with validation checks on the user. This shows all of the users bookings. This will allow the user to view their upcoming bookings when needed.

For restaurant staff users, all bookings will be available to display so that staff can easily view numbers and future bookings.

![Empty Upcoming Bookings](docs/readme_images/empty_upcomingbooking.webp)

![Upcoming Bookings](docs/readme_images/upcoming_bookings1.webp)

Implementation:

**Edit Booking Page**

``USER-STORY - As a user I would like to be able to edit a booking so that i can make changes when needed``

On the manage bookings page an edit button is present that allows the user to direct to a form and update their booking when required. This will allow the user to easily manage their own booking.

For staff users, they can also edit bookings from the All bookings (admin) page, even if they did not create the reservation. This will allow restaurant staff to ammend details as needed.

![Edit Bookings](docs/readme_images/booking_edited.webp)

Implementation:

**Delete Booking**

``USER-STORY - As a user I would like to delete my booking when no longer require it``

![Delete Booking](docs/readme_images/sure_delete_booking.webp)

![Post Delete Booking](docs/readme_images/afterdelete_booking.webp)

``USER-STORY - As a staff user I want to be able to search a booking by name/date to save searching time``

Implementation:

**Searchbox**

A search box was added to the manage bookings page that is only visible to staff users. This will allow the staff members to easily locate a booking by name/email or date if they need to find it quickly.

![Search Boxes](docs/readme_images/search_bookings.webp)

``USER-STORY - As a staff user, As a Staff User I would like to view/edit/manage customer's bookings so that Customer can get help from our side too``

Implementation:

**All Bookings(Admin)**

All Bookings (Admin) page was added to the manage bookings and that is only visible to staff users. This will allow the staff members to easily perform view/edit/delete on the bookings made customer as well as admin.

![All Bookings (Admin)](docs/readme_images/admin_manageallbookings.webp)

Favicon
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon](docs/readme_images/favicon.webp)

### Features Left To Implement
- In a future release I would like to implement a page which displays a table map of the restaurant with information displayed on each table of upcoming bookings. This feature would allow staff to easily see if there are any upcoming bookings on the each table and plan accordingly. 
- I will also like to add multiple menu pages.

## The-Skeleton-Plane

### Wireframes

- Home page


![Home Page](docs/wireframes/homepage_wireframes.png)

- Signup page


![Sign up Page](docs/wireframes/signup_wireframe.png)

- Log in

![Login Page](docs/wireframes/login_wireframe.png)

- Log Out

![Logout Page](docs/wireframes/logout_wireframe.png)

- Create Booking

![Create Booking](docs/wireframes/createbooking_wireframe.png)

- Edit Booking 

![Edit Booking](docs/wireframes/edit_booking_wireframe.png)

- Upcoming Bookings

![Upcoming Bookings](docs/wireframes/upcomingbooking_wireframe.png)

- Delete Booking 

![Delete Booking](docs/wireframes/deletebooking_wireframe.png)

- Create Menu 

![Create Menu](docs/wireframes/createmenu_wireframe.png)

- Create Allergy Label

![Create Allergy Label](docs/wireframes/createallergy_wireframe.png)

- Edit Menu 

![Edit Menu](docs/wireframes/editmenu_wireframe.png)

- View Menu 

![View Menu](docs/wireframes/menu_wireframe.png)


- Manage Menus

![Manage Menu](docs/wireframes/managemenu_wireframe.png)

- Delete Menu 

![Delete Menu](docs/wireframes/deletemenu_wireframe.png)

### Security

Views were secured by using the django class based view mixin, UserPassesTextMixin. A test function was created to use the mixin and checks were ran to ensure that the user who is trying to access the page is authorized. Any staff restricted functionality, user edit/delete functionality listed in the features was secured using this method.

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository. In production, these variables were added to the heroku config vars within the project.

### Imagery

The Website logo was downloaded from google free source and Header/Footer colour was choosen to match website logo.

The hero image was taken from Pexels which is a royalty free image site.

## Technolgies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
<!-- - JavaScript
  - JavaScript was used to make the custom slider on the menu page change and the bootstrap date picker. -->
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- Google
  - This was used to download the logo in header 
- freeconvert.com
  - This was used to compress the images used in the website for optimal load times

**Python Modules Used**

* Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
* Mixins (LoginRequiredMixin, UserPassesTestMixin) - Used to enforce login required on views and test user is authorized to perform actions
* messages - Used to pass messages to the toasts to display feedback to the user upon actions
* reverse_lazy - Used to define redirect URLs (like success_url) in class-based views without causing circular import issues.
* date - Date was used in order to search for objects by date.
* method_decorator - Used to wrap them with access restrictions.
* staff_member_required - Used to restrict access to certain views only for staff users(bookings)

**External Python Modules**

* asgiref==3.8.1 - Used internally by Django to support asynchronous features
* bleach==6.2.0 - HTML sanitizing library that cleans user-generated content; useful for rich text editors like Summernote
* certifi==2025.6.15 - Used to secure HTTP requests by providing up-to-date SSL certificates
* cffi==1.17.1 - Used for calling C code from Python - required by cryptography
* charset-normalizer==3.4.2 - Used to detect and normalize text encoding; required by requests
* cloudinary==1.36.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* crispy-bootstrap5==0.7 - This was used to allow bootstrap5 use with crispy forms
* cryptography==45.0.4 - Installed as dependency with another package
* defusedxml==0.7.1 - Installed as dependency with another package
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.2.23 - Framework used to build the application
* django-allauth==0.57.0 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* django-crispy-forms==2.4 - Used to style the forms on render
* django-summernote==0.8.20.0 - Used for menu page since its a integrated rich text editor for content creation
* gunicorn==20.1.0 - Installed as dependency with another package
* idna==3.10 - Installed as dependency with another package
* oauthlib==3.3.1 - Installed as dependency with another package
* psycopg2==2.9.10 - Needed for heroku deployment
* pycparser==2.22 - Installed as dependency with another package
* PyJWT==2.10.1 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests==2.32.4 - Installed as dependency with another package
* requests-oauthlib==2.0.0 - Installed as dependency with another package (allauth authentication)
* setuptools==80.9.0 - Used to manage Python packages and dependencies during builds or installations
* six==1.17.0 - Installed as dependency with another package
* sqlparse==0.5.3 - Installed as dependency with another package
* tzdata==2025.2 - Installed as dependency with another package
* urllib3==1.26.20 - Installed as dependency with another package
* webencodings==0.5.1 - Required by bleach to handle web-safe text encoding formats
* whitenoise==5.3.0 - Used to serve static files directly without use of static resource provider like cloundinary


## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://the-wooden-spoon-cfb803cde318.herokuapp.com/)

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

### Media
* All the free images/hero image used on the site were gotten from https://www.pexels.com/


## Credits 

* My mentor [Gareth-McGirr](https://github.com/Gareth-McGirr/) for his insightful advice and encouragement.

* You Tube channel for Initial set up and way to navigate the apps [https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=2]