# Vehicle Insider

#### Video Demo : https://youtu.be/3h3QAKogYhU


#### Description :



Vehicle Insider is a web application that addresses the need for simpler,easier and more insightful ways to rent a vehicle for your vacation on some of
the Greek islands.This idea was conceived by me as I am a local Greek Islander and see first hand the difficulties that tourists face while trying to find a reliable
car rental company.Vehicle Insider is here to help them,make their vacation unforgettable and also help them find the right car for the right price.


The project file is divided to the application.py file , the helpers.py which was in part from cs50 finance and the templates.I chose bootstrap for the menu bar
because of the requirement set by the exercise but also because of its simplicity and beauty.The navbar features some dropdowns leading to some static templates
so that the user can get some ideas about Greek destinations and vehicles that he may be interested in.


The website features a database with two tables, USERS and RENTALS.Functions in application.py give the proper queries for the insertion of elements in the database .
The register template uses some Textfields but most notably using the hexadecimal codes of countries flags and a simple script in javascript the app is capable of automatically inserting
to the PhoneNumber textfield the correct phone code of the country.

The rental template uses jQuery to implement datepickers and timepickers to the form.The format chosen for the datepicker is yy/mm/dd so that it can be compatible

with the database DATE format . The rest of it is mostly a pick from a list type of field with the known options from the menu .


The Layout template hosts the menubar . This template uses in html if else cases according to the user_id , so we can make login , logout , register, rent now buttons according to our needs.

The vehicles in the menu are , Mercedes vito and E class, Jeep Wrangler,Seat mii as a supermini and the VW polo.



The places offered to be visited are Karpathos , Rhodes , Heraklion, Santorini . All the destinations are Greek islands known for their beauty and attraction to tourists.
Karpathos and Rhodes are situated at the southeastern Aegean Sea, Heraklion and Santorini are situated at the center and southcentral of the Aegean.

Also for this project some other functions that were used in the finance problem were used , such as the apology.html template .

The logic behind the application.py file that serves as the backend part of the flask app is quiet similar to the logic behind the CS50 finance app.
With the app.route and function with the name of the template we get to redirect the links between the different templates of the site through the buttons and menu bars.
Also the functions register , login , rent all use the is_provided function to check if values are assigned to the fields of the template.Then most of the volume of the functions is taken 
from the sql queries which are quite big and the values should have the same name as the fields of the templates for it to work , now that was something that really took
me a lot and i mean a lot of time !!

The login function gets from the database the username that the user if trying to log into the app with (if it exists) and checks for the validity of the given password.Hash was used it this 
project so , Hash was also taken into consideration.After the user logs in , or registers , the menu changes , the register option disappears and  rent now is now an option.


The logout function is quite simple and frankly might have been the easiest to make , a simple clear command and the session times out and the user is returned to the index panel , logged out 
and with the options register and login.

The layout of the site is such that it gives to the visitor the opportunity to explore the destinations and think about the vehicles before registering for an account .
This helps him decide before creating just another account he wont ever use , just so he can browse freely the site.




