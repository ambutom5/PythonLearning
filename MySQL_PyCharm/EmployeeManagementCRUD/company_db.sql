show databases;
create database company_db;
use company_db;

create table employee(
id int auto_increment primary key,
name varchar(100) not null,
place varchar(100),
mobile varchar(15) unique,
email varchar(100),
department varchar(100),
salary int,
joining_date date);

select * from employee;
