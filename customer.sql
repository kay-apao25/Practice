create table customer(
    customer_id serial primary key,
    customer_name text,
);


--HOW TO USE:
-- SELECT loadCustomerData(1);

create or replace function loadCustomerData(in int, out int, out text) 
	returns setof record as

$$ 
    select customer_id, customer_name from customer
				where customer_id = $1;
$$
 
	language 'sql';


--HOW TO USE:
-- SELECT addCustomer('Air');

create or replace function addCustomer(p_customer_name) 
returns text as

$$
declare
  v_customer_id int; 
begin
  select into v_customer_id customer_id from customer
	where customer_name = p_customer_name;
  
  if v_customer_id isnull then
   insert into customer(customer_name) 
					values
					(p_customer_name)
  returning 'Ok';
  else
  	update customer
  	set customer_name = p_customer_name
  		where customer_id = v_customer_id
  return 'Updated';
  end if;

end;
$$

    language 'plpgsql';