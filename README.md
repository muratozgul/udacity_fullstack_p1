rdb-fullstack
=============

Common code for the Relational Databases and Full Stack Fundamentals courses.  
Database can serve multiple tournaments.  
In order to register a player to a tournament, first create a player and a tournament.
Then register the player to the tournament. Use registered player id for matches.

### TO RUN TESTS:

##### Install virtualbox  
https://www.virtualbox.org/wiki/Downloads
##### Install vagrant  
https://www.vagrantup.com/downloads.html
##### Start and connect to vm
`vagrant up`  
`vagrant ssh`  
##### Create database "tournaments"
Navigate to tournament folder and launch PostgreSQL CLI   
`psql`  
Create database  
`create database tournaments;`  
Connect to tournaments  
`\c tournaments`  
##### Create tables & views
`\i tournament.sql`
##### Run tests
Exit psql CLI
`python tournament_test.py`