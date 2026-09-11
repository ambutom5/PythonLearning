create database gym_db;
use gym_db;

create table member(
id int auto_increment primary key,
name varchar(100) not null,
place varchar(100),
mobile varchar(15) unique,
plan enum("1month","2month","3month","6month","1year") default "1month",
fee int,
joined_on date);

select * from member;