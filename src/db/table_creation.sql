CREATE TABLE IF NOT EXISTS word_count (
  document varchar(45) NOT NULL,
  word varchar(50) NOT NULL,
  count integer NOT NULL,
)



SELECT customer_id,
	rental_id,
	return_date
FROM
	rental
WHERE
	customer_id IN (1, 2)
ORDER BY
	return_date DESC;


select word sum(occurence)
from xxxx
group by word
where filename in ()