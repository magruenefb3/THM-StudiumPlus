select count(*) as rentals, 
DATE_FORMAT(rental_date, "%d-%m-%Y") as 'date' 
from rental group by DATE_FORMAT(rental_date, "%d.%m.%Y");