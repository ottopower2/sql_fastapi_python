BEGIN IMMEDIATE;

UPDATE customers
SET customer_id = 'a1fbc88172c00ba8bc7'
WHERE customer_id = '1106b8999e2fba1a1fbc88172c00ba8bc7'
  AND NOT EXISTS (
      SELECT 1
      FROM customers
      WHERE customer_id = 'a1fbc88172c00ba8bc7'
  );

COMMIT;
