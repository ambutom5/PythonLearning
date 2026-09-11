create database blood_db;
use blood_db;

create table donor(
	id int auto_increment primary key,
	name varchar(100) not null,
	blood_group enum("A+","A-","B+","B-","AB+","AB-","O+","O-") default "A+",
	phone varchar(15) unique,
	city varchar(100),
	last_donation date
);

show tables;
select * from donor;