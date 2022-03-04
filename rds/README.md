Go to Server and try to connect with the database using 

```psql -h <database-endpoint> -U postgres -W -d nodejs_demo enter the password when asked```

Create a table using the below SQL script, this table will be used by the nodejs we have deployed to insert and retrieve the data

```
create table if not exists employee(
id SERIAL,
name varchar(50),
job varchar(40),
department varchar(40),
salary int,
hire_date date,
PRIMARY KEY (id));
```

Insert into table
```
INSERT INTO employee(id, name, job, department, salary, hire_date)
VALUES (12345, 'Darshan', 'Dev', 'IT', 10000,'4-3-2022');
```
