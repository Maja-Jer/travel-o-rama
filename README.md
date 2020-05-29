# Introduction

`Travel-o-Rama`(https://travel-o-rama.herokuapp.com/) was created by Maja Jercic, to serve all the travellers to organise and save their trip infprmation in one place.

As a bit of wanderlust myself, I was always looking for an app where I could have all the details of my trips, reservation codes, places to visit, restaurants to go and try  delicious local food in and any experiences that would be a must-see. After Google Trips has been retired, I have struggled to find an app that would sasify my needs, so this was a perfct opportunity to build it myself. The goal for this page is to allow everyone to save their own trips and use them as a single reference when sightseeing, instead of swapping between multiple apps at the same time.

# UX
## Goals

### Visitor Goals

The central target audience for Trip_O-Rama are:
- Traveller, no age limit
- English-speaking (for the beginning)

User goals are:
- Have one app in which all the trip details can be saved
- Be able to access, add, edit and delete the information quickly an easily, without needing to open multiple apps and website to get the information

Why does it meet the goals?
- It's simple, intuitive
- After google Trips have been retired I haven't been able to find an app the has all of the funtionalities that I needed in one place
- The design of this site fits the conventions of similar sites, and lays out the information in a user friendly and accessible way
- The app allows adding new trips, new trip categories, editing the ones that have already been saved and deleting trips for better organisation

### Business Goals

In an advanced version, some businesses could use Travel-O-Rama:
- Airlines
- Flight search engines
- Rent-a-cars companies
- accommodation platforms, like Booking.com or Airbnb
- Local restaurants, based on the trip location
- Hotels, based on the trip location
- Local agencies, offering local experiences, based on the trip location

Business user goals are:
- A well thought-out, well designed, user-friendly platform that will benefit my business to advertise on.
- A user interface that is user-friendly for me to input my data easily and efficiently.
- Value for money (for now the app is a student project, but I would like to build on this app and start using it, so I would like to ad this goal now.)

### Travel-O-Rama Goals

- Provide an easy-to use and effective app for travellers to stay organised during the trip and find information about a specific trip
- So that I can learn and practice frontend and backend programming for the first time. To combine the use of HTML, CSS, Bootstrap and JavaScript with Python, MongoDB, Flask and Jinja
- While a student project for now, the future goal is to implement more features and have it used by friends and family at the beginning to test it. Down the line, the plan is to include ads  by different businesses and have the app ready for a more wide-spread use.

## User stories
### Visitor Stories

As a Travel-O-Rama user, I expect/want/need to:
- To find what I am looking for easily , I want the layout of the site to make sense so I am not confused or put off using it.
- The options that I have need to be laid out in an intuitive way that is easy for me to navigate and digest, so I don't have trouble finding functionalities I need
- To be able to acces my trips easily and be able to edit or delete it without complications
- As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices.
- As a user, I expect my trips to be saved, updated and deleted as I go through the steps to do so

### Business Stories

On the business side of things, I want/expect/need:
- To be able to access existing entries and that data to be editable on the app. (I plan on building a log-in page in the future, so user will have access to their own database of trip that are editable)
- To create, edit and delete entries
- A user interface that is simple and easy to use, laid out in a logical way with clear steps 
- To be able to create, edit and delete entries in the page
- A user interface that is simple and easy to use, that is laid out in a logical way with clear indications where necessary about the type and format of the data I need to provide.

## Design Choices

Travel-o-Rama has an overall friendly feel with emphasis on providing ands finisng information in a bite-size, easy format. The following design choices were made with that in mind:
The background is white and non-imposing

**Fonts**

- I have kept `Segoue UI`that is default for Materialize as it is easy to read and it complements the styling of the page. Also, it is very easy to read when using smaller screens and that is another reason why i chose to stary with this Fonts

**Colour scheme**

I have kept the colour scheme to the shades of blue as it has a relaxing effect on the users viewing the page. I have found that in multiple research, and I'm linking one [here](https://www.verywellmind.com/the-color-psychology-of-blue-2795815)
Shades of blue used:
0D4F8B for the fonts in h4 and trip.html for the list of saved trips
00B2EE for the navbar background as it provides a nice contrast to the white font colour of the navbar

Materialise colours for the buttons in trips.html:
red lighten-1 for the Delete button
cyan for the edit button, add trip button in addtrip.html and add category in addcategory.html

## Wireframes

There are the wifreames built with `Balsamiq`(https://balsamiq.com/)

I have created the wireframes for all 3 pages. The page is planned to look the same on all screen sizes (excluding the responsivness of the buttons on trips.html)
- Home
- Add a Trip
- Add categories

The wireframes are hosted in a google doc and anyone with the `link`(https://docs.google.com/document/d/1VeDi4zn4yRVsI5jna1Ylv9NS7TKhib07MXxNQAs9W8k/edit?usp=sharing) can access the document

# Features

## Existing features

###Navbar

- The logo is on the top left side
- On the right hand side we have: Home, Add a trip, Add categories
- The navbar is collapsed into a burger icon on small screens.

###Home page

**Home page features** 

- the list of saved trips which allows the user to edit or delete the saved trip
- a collapsible which opens up to show more details saved when adding a trip
- when editing a trip, a page opens up which looks exactly like Add a Trip, but it already has the details of the trip already saved and ready for editing. to complete the editing process, the user needs to click on a button at the bottom of the page that allows him to save the edited changes. At that moment the home page reflects the updates
- when deleting a trip, it is enough to click on the Delete button of a trip the User wants to delete

###Add a trip

When opening "Add a trip page", the user sees a list of options they can write the information about their trip.

**Add a trip features**

- Trip category, something that will be looked into with more detail on how to filter trips and their views in a future version of the app. Because of that it doesn't show in the Trips page for now
- Trip location
- Reservation code for the accommodation
- Check in date
- Check-out date
- option to choose if the trip is happening now
- option to save the sights
- Option to save the restaurants to visit during the trip
- Option to save the experinces the traveller is interesting to try out
- Button which saves the trip upon clicking on it

### Add a Category

For this page I never planned on having a delete function as I didn't feel like it was something to be used for now, but I might reconsider and implement it in the future

**Add a Category features**

- a small icon and a line on to which the users can add a name of a trip category they wish to use for future trips
- a button that saves a category and allows it to be selected in the database and can be selected when adding a trip

##Features left to implement

- Register and Log in Page
- Filter according to trip categories
- Deleting categories

# Information architecture

## Databae choices

I have decided to use MongoDB as the objects are easily accessed for the purposes of this project

### Data storage types

The types of data stored in MongoDB for this project are:

- ObjectId
- Strings

### Data structure

Travel-o-Rama database has 2 collections:

- categories
- trips

**Categories collection**

| Title         | Key in DB      | Data type  |
| ------------- | -------------  | ---------- |
|  categories   | category_name  | string     |

**Trips collection**
| Title                          | Key in DB      | Data type  |
| ------------------------------ | -------------  | ---------- |
|  Choose your trip type         | trip_name      | string     |
|  Where are you travelling?     | trip_name      | string     |
|  Reservation Code              | transport_code | string     |
|  Is now                        | is_now         | string     |
|  Check-In                      | check_in       | string     |
|  Check-Out                     | check_out      | string     |
|  Sights to visit               | sights         | string     |
|  Restaurants to try            | restaurants    | string     |
|  Things to experience          | category_name  | string     |

# Technologies used
## Tools

- `Gitpod`(https://gitpod.io/) is the IDE used for developing this project.
- Git to handle version control.
- `MongoDB Atlas`(https://cloud.mongodb.com) is the database for this project
- `GitHub`(https://github.com) to store and share all project code remotely.
- `Am I responsive?`(http://ami.responsivedesign.is) to create the images in this readme file of each page displayed on different screen sizes.

## Libraries

- JQuery to simplify DOM manipulation.
- Materialize to simplify the structure of the website and make the website responsive easily.
- PyMongo to make communication between Python and MongoDB possible.
- Flask to construct and render pages.
- Jinja to simplify displaying data from the backend of this project smoothly and effectively in html.

## Languages
This project uses HTML, CSS and Python programming languages.

# Testing
## Desktop testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes

**Navbar**

- Click on the logo to test, confirm it takes the user to the home page.
- Click the Home link, confirm it takes the user to the home page.
- Click the add a trip link, confirm it takes the user to the add a trip page.
- Click the Add a category link, confirm it takes the user to the add a categopry page page.

**Home page**
- open the collapsible to confirm it shows additional trip details
- click on Delete button to delete the trip
- click on edit button to go to edit trip page, where we have to be able to edit trip details which will in turn save on the home page after Edit trip button has been clicked

**Add a Trip page**
- type in the information in every section of the trip
- click on a button Add a trip at the bottom of the page and then go to Home page to confirm the new trip has been saved

**Add a category page**
- click on adda a category line and write the name of the new category the suer wants to save
- click on add a category button to save the new category
- go to Add a trip to test if the new category saved


## Tablet and mobile testing
All steps below were repeated to test mobile and tablet specific elements on my Huawei phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design waw also tested in the Chrome Developer Tools device simulators on all options and orientations.

**Navbar**

- Click on the logo to test, confirm it takes the user to the home page.
- Click the Home link, confirm it takes the user to the home page.
- Click the add a trip link, confirm it takes the user to the add a trip page.
- Click the Add a category link, confirm it takes the user to the add a categopry page page.

**Home page**
- open the collapsible to confirm it shows additional trip details
- click on Delete button to delete the trip
- click on edit button to go to edit trip page, where we have to be able to edit trip details which will in turn save on the home page after Edit trip button has been clicked

**Add a Trip page**
- type in the information in every section of the trip
- click on a button Add a trip at the bottom of the page and then go to Home page to confirm the new trip has been saved

**Add a category page**
- click on adda a category line and write the name of the new category the suer wants to save
- click on add a category button to save the new category
- go to Add a trip to test if the new category saved


# Deployment
## How to run locally?

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

- An IDE such as GitPod
The following must be installed on your machine or implemented in the iDE if it's an online one like GitPod:

- PIP
- Python 3
- Git

An account at MongoDB Atlas or MongoDB running locally on your machine.
How to set up your Mongo Atlas account `here`(https://docs.atlas.mongodb.com/).

### Instructions
- Save a copy of the github repository located at https://github.com/Maja-Jer/travel-o-rama by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```git clone https://github.com/Maja-Jer/travel-o-rama```

- Follow instructions in your IDE how to open such funtionalities

## Heroku Deployment

To deploy Travel-o-Rama to Heroku, take the following steps:

- Create a **requirements.txt** file using the terminal **command pip freeze > requirements.txt**.

- Create a Procfile with the terminal command **echo web: python app.py > Procfile**.

- **git add** and **git commit** the new requirements and Procfile and then git push the project to GitHub.

- Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

- From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

- Confirm the linking of the heroku app to the correct GitHub repository.

- In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

- Set the following config vars:
Debug: false 
Mongo URI: mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
port: 5000
Secret_key: <your password>

To get you MONGO_URI read the MongoDB Atlas documentation `here`(https://docs.atlas.mongodb.com/) 

In the heroku dashboard, click "Deploy".

In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

The site is now successfully deployed.

## Bugs I was unable to fix

In Edit trips, the system doesn't save the edited checkin and check out dates, as well as the experinces. I have checked the code multiple times, with students from Ci and tutors and we were unable to understand what is the readon. DB collection documents names are identical to the code, but we weren't able to find a solution. That is something i will have to look into in the future if I want to expand this application

I was unable to find a way to override Materialize's default font size in labels in trips collapsibles. I would manage to do it when testing in Inspect code, but when i would copy that code in the style.css, it wouldn't work. I have left the code I tried to use in the file and commented it

# Credits

I used Materialize as a library and I have used the code from there to build the form, icons, buttons, navbar. i have specified in the code  more details
I was influenced by the Task Manager project in our CI course and I have adapted it to suit my needs.

# Acknowledgements

Getting to this project has been a struggle, dealing with the impact of the Corona virus and losing my job, so the motivation to continue with the Python modules has been fleeting, but with the help of my fellow students I have managed to see this project through, even though I am aware it needs improvements. Submitting has been been an accomplishment in itself
Thank you to everyone in Code Institute that helped me in any way while building this site:
dickv_mentor for his feedback and suggestions how to improve my project.
IgorB-lead for listening and helping out, even last minute
Anthony for encouraging me all the time and just being in my corner and pushing me
tutors
My small group of Croatian students
The entire Slack community for just being there, encouraging and helping

# Disclaimer

The content of this website is educational purposes only.