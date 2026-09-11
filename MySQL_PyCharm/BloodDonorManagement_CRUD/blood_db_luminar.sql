use luminar;

create table donor(
	id int auto_increment primary key,
    name varchar(100) not null,
    blood_group enum("A+","A-","B+","B-","AB+","AB-","O+","O-") default "A+",
    phone varchar(15),
    city varchar(100),
    last_donation date);
    
select * from donor;
delete from donor where id = 4;

    