create table cd(
    cd_id serial primary key,
    cd_name text,
    rent_status text
);


--HOW TO USE:
-- SELECT loadCdData(1);

create or replace function loadCdData(in int, out int, out text, out text) 
	returns setof record as

$$ 
    select cd_id, cd_name, rent_status from cd
				where cd_id = $1;
$$
 
	language 'sql';


--HOW TO USE:
-- SELECT addCd('Twila Paris Hits', 'No');

create or replace function addCd(p_customer_name, p_rent_status) 
returns text as

$$
declare
  v_cd_id int; 
begin
  select into v_cd_id cd_id from cd
	where cd_name = p_cd_name;
  
  if v_cd_id isnull then
   insert into cd(cd_name, rent_status) 
					values
					(p_customer_name, p_rent_status)
  returning 'Ok';
  else
  	update cd
  	set cd_name = p_cd_name, rent_status = p_rent_status
  		where cd_id = v_cd_id
  return 'Updated';
  end if;

end;
$$

    language 'plpgsql';


--HOW TO USE:
-- SELECT addCd('Twila Paris Hits', 'No');

create or replace function addCd(p_customer_name, p_rent_status) 
returns text as

$$
declare
  v_cd_id int; 
begin
  select into v_cd_id cd_id from cd
  where cd_name = p_cd_name;
  
  if v_cd_id isnull then
   insert into cd(cd_name, rent_status) 
          values
          (p_customer_name, p_rent_status)
  returning 'Ok';
  else
    update cd
    set cd_name = p_cd_name, rent_status = p_rent_status
      where cd_id = v_cd_id
  return 'Updated';
  end if;

end;
$$

    language 'plpgsql';