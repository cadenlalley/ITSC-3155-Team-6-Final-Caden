# Petpals - University of North Carolina at Charlotte - Software Engineering (ITSC 3155)

Petpals is a project that was created in the Software Engineering course at the University of North Carolina at Charlotte. The feature I (Caden Lalley) worked the most on was the Direct Messaging system which was created using Websockets and JavaScript. I also worked on some backend route logic and the frontend for the DM page.

## Contributors
* [Cody Liske](https://github.com/cliske94)
* [Jacob Harland](https://github.com/JacobHarland)
* [Ethan Pinto](https://github.com/EthanPintoA)
* [Wendy Dushanin](https://github.com/wDushanin)
* [Ryan Braswell](https://github.com/braswellry67)
* [Caden Lalley (me)](https://github.com/cadenlalley)

## Demo
https://petpals.clalley.dev

## Setup
1. Clone and change directory into project directory
2. Install requirements by running this command: `pip install -r requirements.txt`
3. Copy the `.env.sample` file into a file named `.env`
4. Setup your MySQL database with the name `petpals`
5. Run the SQL scripts ending in 'dummydata' in the `/sql` directory to populate your DB with dummy data.
6. Setup email for email service
7. Populate your `.env` file with values relevant to your environment


## Run the Server
Run the command: `flask run` to start Petpal's webserver 
