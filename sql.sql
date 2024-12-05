select c.login, COUNT(DISTINCT o.track)
from "Couriers" as c
left join "Orders" as o
on c.id = o."courierId"
where o."inDelivery" = True
group by c.login;


SELECT o.track,
case
    when o.finished = true then 2
    when o."cancelled" = true then -1
    when o."inDelivery" = true then 1
	else 0
    end as status
FROM "Orders" as o;

