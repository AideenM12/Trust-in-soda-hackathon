# Contents
- [Site Name](#site-name)
- [Collaborators](#collaborators)
- [UX](#ux)
  - [Strategy](#strategy)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
- [Scope](#scope)
    - [_Planned Features_](#planned-features)
- [Structure](#structure)
  - [Existing Features](#existing-features)
    - [Features on all pages:](#features-on-all-pages)
    - [Home page features:](#home-page-features)
    - [Login page features:](#login-page-features)
    - [Sign-Up page features:](#sign-up-page-features)
    - [Profile page features:](#profile-page-features)
    - [Logout features:](#logout-features)
    - [404 Page](#404-page)
    - [500 Page](#500-page)
    - [Features exclusive to Admin:](#features-exclusive-to-admin)
  - [Features left to implement](#features-left-to-implement)
  - [Design](#design)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Skeleton](#skeleton)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Sitemap](#sitemap)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deployment Steps](#deployment-steps)
    - [Set environment variables:](#set-environment-variables)
    - [Enable automatic deployment:](#enable-automatic-deployment)
    - [Connect app to Github Repository](#connect-app-to-github-repository)
    - [Making a clone to run locally](#making-a-clone-to-run-locally)
    - [How to Fork the respository.](#how-to-fork-the-respository)
  - [Credits](#credits)
    - [Media](#media)
    - [Content](#content)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

# Site Name

# Collaborators

* [Scott](https://github.com/Ryagg)

* [Jon](https://github.com/jpg6453)

* [Aideen](https://github.com/AideenM12)

* [Mateusz](https://github.com/mateuszniechwiej)

* [Steve](https://github.com/SteveKennyUK)

![Website MockUp](static/doc-images/mockup.png)

The live website can be viewed [here](https://trust-in-soda-hackathon.herokuapp.com/)


# UX

## Strategy

### Project Goals




**The Ideal User of this site:**

  

### User Stories

* As a first-time user I want to know the main purpose of the site immediately upon arriving on the site.
* As a first-time user I want the site UX to be intuitive for ease of use. 
* As a returning user, I want to be able to register with the site and create my own profile which I can log in to at any time.
* As a returning user, I want to be able to add ....
* As a returning user, I want to be able to edit/delete any contribution I have made to the site. 
* As a user I want the site to be responsive to all devices.
* As a user I want to be able to contact the admin with any queries or suggestions I may have.


# Scope 

### _Planned Features_

1. Responsive website with a navigation menu and website title.
2. Login functionality
3. Registration functionality
4. Logout functionality
5. MongoDB database to store username and user needs.
6. Profile Page
7. Edit profile functionality
8. Allow user to submit a form with information about them disabilities
9. Receive form submission confirmation 
10. Ability for users to select an alternative color scheme


| -   | Planned Feature                                                     | Importance | Viability/Feasibility |
| --- | ------------------------------------------------------------------ | ---------- | --------------------- |
| 1   | Responsive website with a navigation menu and website title                                             | 5          | 4                     |
| 2   | Login functionality                                   | 4          | 4                     |
| 3   | Registration functionality      | 4          | 4                     |
| 4   | Logout functionality            | 4          | 5                     |
| 5   | MongoDB database to store username and user needs.                                           | 4          | 4                     |
| 6   | Profile Page                         | 4          | 5                     |
| 7   | Edit profile functionality                     | 4          | 5                     |
| 8   | Allow user to fill a form with information about them disabilities and send it to ther admint  | 5          | 4                     |
9   | Receive form submission confirmation  | 4          | 4                     |
10  | Alternative color scheme              | 2           | 4

# Structure

## Existing Features

### Features on all pages:
* Navbar
* Footer
* Social Media Icons


### Home page features:
* Alternative color scheme:
Users can choose between the default theme and an alternative theme. The theme selection is saved to local storage and applied on all pages.





### Login page features:

 
* A Log in form is presented to the user which asks for their username and password which are validated by the login route handler. An image of the login form can be seen below.



### Sign-Up page features:


* A register form is presented to the user which asks for their username, email address and password which are validated by the sign route handler. The password must be declared twice to ensure it matches or else the user will be notified that their passwords do not match. This is done to ensure that the user has input a password that they are familiar with and can remember and to avoid any possible typos that could hinder the user from signing in in the future. An image of the registration form can be seen below.



### Profile page features:






### Logout features:
* The log out button removes the user's session cookie from the app using the pop method and redirects the user to the login page.

### 404 Page
* A 404 Page has been created in order to deal with user errors in navigation or invalid search data in order to assist the user in returning to the home page. All navigation features are present on the 404 page as well as a button labeled 'home' in order to easily redirect the user back to the relevant page.



### 500 Page 
* A 500 page has been created to deal with any potential internal server errors.



### Features exclusive to Admin:

* Only the Admin can edit/delete all articles content on the site, otherwise the content must belong to the session user in order for it to be edited or deleted. 



## Features left to implement






## Design

### Colors

* The colors of this site were chosen for contrast. They also should not be a distraction for the user. For the alternative theme we chose a blue hue because blue is the richest color across all types of colour blindness. For text color we chose white for maximum contrast with the background. 

This palette was created on the [Coolors Website](https://coolors.co).




### Typography



* Both fonts were found on [Google Fonts](https://fonts.google.com/)



### Imagery





## Skeleton

### Wireframes

* The wireframes were created using [Balsamiq wireframes](https://balsamiq.com/)

* The wireframe mockup links can be found below:

* [Home Page Wireframes for Desktop](static/doc-images/wireframes/home-page-desktop.png)

* [Home Page Wireframes for Mobile](static/doc-images/wireframes/home-page-mobile.png)

* [Contact Page Wireframes](static/doc-images/wireframes/TIS-contact-wireframe.pdf)

* [Register Page Wireframes]()

* [Profile Page Wireframes](static/doc-images/wireframes/TIS-Hackathon-Profile-Page.pdf)

* [Login Page Wireframes for Desktop](static/doc-images/wireframes/login-desktop.png)

* [Login Page Wireframes for Mobile](static/doc-images/wireframes/login-mobile.png)

* [Requirements Page Wireframes for Desktop and Mobile](static/doc-images/wireframes/disabilities-1.png)

* [Disabilities Subcategories Page Wireframes for Desktop and Mobile](static/doc-images/wireframes/disabilities-2.png)





### Database Schema



* The site contains  collections which are stored in MongoDB. The users collection stores the user's username and password which enables the user to create an account and have a profile page. 


### Sitemap
* The sitemap was created using [Balsamiq wireframes](https://balsamiq.com/)

!!!The path is wrong and the file can't be found!!!
* A link to the [Sitemap can be found here](assets/documentation/wireframes/MS3-sitemap-wireframe.pdf)

## Technologies Used
- This project is primarily built using HTML5 semantic markup, CSS stylesheets, Javascript, Python, Flask and MongoDB.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask was used as the main python framework in the building of this project.
- [jQuery](https://jquery.com/)
    - This framework was used to create some of the site's interactive functions.
- [Gitpod](https://gitpod.io)
    - This project was built using Gitpod as the IDE.
- [Github](https://github.com/)
    - Github was used for online version control and storing files and documents.
- [Heroku](https://id.heroku.com/)
    - Heroku was used as a cloud based platform to deploy this site.
- [Google fonts](https://fonts.google.com/) 
    - The font styles used on this website were chosen from Google fonts.
    !!! Did we use that? !!!
- [Materializecss](https://materializecss.com/)
   - Various aspects of this website were structured using Materialize.
   - Materialize was used to make this website responsive
- [Fontawesome](https://fontawesome.com/)
    - The icons used on this page were found in Fontawesome.
- [MongoDB](https://www.mongodb.com/)
    - MongoDB Atlas was used as the database for the creation of this project.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Jinja was used for templating.
- [flask-paginate](https://pythonhosted.org/Flask-paginate/)
    - flask-paginate was used to create the site's pagination links.
- [Balsamiq](https://balsamiq.com/)
    - The wireframes and sitemap for this project were created using Balsamiq.
 - [Freeformatter- CSS beautifier](https://www.freeformatter.com/css-beautifier.html)
    - This was used to format the CSS stylesheet.
- [Freeformatter- HTML formatter](https://www.freeformatter.com/html-formatter.html)
    - This was used to format each HTML page
- [PEP8online](http://pep8online.com/)
    - PEP8 online was used to make sure all python code was pep8 compliant.
- [Google DevTools](https://developers.google.com/web/tools/chrome-devtools) 
    - Google Dev Tools was extensively used throughout the project for various styling and testing purposes. Its lighthouse feature was used as one of the main testing tools for this project.
- [EmailJS](https://www.emailjs.com/)
    - The contact-form was created using EmailJS following a code institute tutorial.
- [CSS-Tricks](https://css-tricks.com/)
    - This was used as a general reference resource.
- [Favicon.io](https://favicon.io/) 
    - This was used to create the site's favicon.
- [Am I Responsive](http://ami.responsivedesign.is/)
    - This was used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.
- [Beautifier.io](https://beautifier.io/)
    - Beautifier.io was used to format all javascript files in this project.
- [Dbdiagram.io](https://dbdiagram.io/home)
    - Dbdiagram.io was used to create the Database Schema presented in this document.
- [Coolors.co](https://coolors.co/)
    - Coolors.co was used to create the project's color palette.
- [StackOverflow](https://stackoverflow.com/)
    - Stack Overflow was used as a general reference resource.
- [Looka](https://looka.com/)
	- Looka was used to create the website logo.     
- [TinyPNG](https://tinypng.com/)
	- Tiny PNG was used for image compression.    

## Testing
Testing information can be found here in the separate [TESTING.md file](TESTING.md)

## Deployment
This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like MotherFolklore. 

This project was deployed using Heroku and stored in GitHub.

Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:
1. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

2. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

3. Push these files to GitHub.
Once those steps are done, the website can be deployed in Heroku using the steps listed below:

### Deployment Steps

1. Log into Heroku.
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.

### Set environment variables:

Navigate to the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (the name of the database that is being used for the project)
4. key: MONGO_URI, value:
 * This can be found in MongoDB by navigating  to the clusters section of your MongoDB account.
 * Click the cluster where the database is located.
 * Click the connect button.
 * Select the connect you application button.
 *  Copy the link provided to your application and ensure you have substituted the password and dbname with the correct values).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).


### Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.


### Connect app to Github Repository

1. Click the deploy tab and connect to GitHub.
2. Type the name of the repository into the search bar presented.
3. Click the Code dropdown button next to the green Gitpod button.
4. When the correct repository displays click the connect button.



### Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/AideenM12/Trust-in-soda-hackathon).
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone' and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

### How to Fork the respository.

1. Log into GitHub.
2. In Github go to (https://github.com/AideenM12/Trust-in-soda-hackathon).
3. In the top right hand corner click "Fork".

## Credits

### Media
- [Favicon image](https://github.com/AideenM12/Trust-in-soda-hackathon/tree/main/static/doc-images/favicon) by <a href="https://www.pngwing.com/en/free-png-ynqbo">pngwing.com</a>


### Content


### Code


### Acknowledgements

