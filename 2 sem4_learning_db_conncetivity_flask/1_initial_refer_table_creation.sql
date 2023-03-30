-- table is created using sql queries which are directly exectued

create table students1(

	student_id int,
	name varchar(100),
	city varchar(50),
	addr varchar(200),
	pin varchar(10),
	primary key (student_id),
	pointer real
	
);

select * from students1;


-- the below queries can be execute by firing from pg admin4 or from python program 

insert into students1 values(100,'name1','mumbai','addr1','pin1',9.8);
insert into students1 values(200,'name2','mumbai','addr2','pin2',8.5);

insert into students1 
        values(300,'name3','delhi','addr3','pin3',7.0),
              (400,'name4','kerala','addr4','pin4',8.9);
			  

update students1
set city='chennai' 
where student_id = 100


delete from students1
        where student_id = 400
		

