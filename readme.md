# ReadME
This is a simple trade simulator web application developed using Python and Django that allows users to simulate trading stocks, cryptocurrencies, and other assets in a virtual environment. 
The app provides users with the ability to create an account, view their portfolio, and make trades with virtual money.
Also, this app is designed to simulate the trading of cryptocurrencies and containes some news from other sources as a blog.

## Features
- Registration and login system for users.
- Virtual trading simulation with real-time market data.
- Buy and sell assets (just some cryptocurrencies).
- User-friendly interface with clear trade information.

## Requirements
all the requirements about what do we need to clone and run the system is placed in other section.
please refer to [requirements section](./readme/requirements.md)

## Configuration
To run this project file "settings.ini" is required to be placed on root of the directory with following contents:
>[settings]\
DEBUG=True\
SECRET_KEY=YOURKEY\
ALLOWED_HOSTS =127.0.0.1,\

## Install 
1- Clone the repository to your local machine.
2- Create a virtual environment using the following command:
>[settings]\
virtualenv env \

3- Activate the virtual environment using the following command:
>[settings]\
source env/bin/activate \

4- do the requirements section manual
5- do the configuration section manual
6- Run the following command to set up the database:
>[settings]\
python manage.py migrate \

7- Start the development server using the following command:
>[settings]\
python manage.py migrate \

8- run server:
>[settings]\
python manage.py runserver

9- Open your web browser and navigate to http://localhost:8000/ to use the app.

## how to use
To use the app, users must first create an account and log in. 
Users can then make trades by selecting an asset to buy or sell, entering the quantity and price, and clicking the corresponding buy or sell button.
The app uses real-time market data from the Alpha Vantage API to simulate trading.

## Distinctiveness and Complexity
This app is designed to simulate a crypto broker. based on this you can make an account, login, logout, place buy and sell order.
modeling of trade is a bit complicate becasue the system not only have to control the existance of money and volume but also it requires to calculate the medium of trade each time.
and some times it has to calculate to the trade base on the existing of the amount and keep the rest of it for later trade. 

This project is different from the other projects and sufficiently distinct in cs50 web and it was complex to build.
- social media is used as a part of this project to show the ability to reuse previous projects! but the main topic is different
- this is not e-commerce project because some one should validate it but in this senario system has to get current price, compare with a list of orderes then do the transactions.
- it supports mobile version 
- it utilizes Django framework


## TODO
- show transactions
- bug fixes about transactions

## Credits
This project was developed by Amirhossein Mobayen as a personal project for finishing the CS50 Web development course.

## license 
The license for this trade simulator project is subject to the policies and agreements of CS50 Program.
