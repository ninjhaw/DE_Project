## SQL Cheat Sheet:
# Basic SQL Commands:

```sql
-- Select all columns from a table
SELECT * FROM table_name;
```

```sql
-- Select specific columns
SELECT 
    column1, 
    column2 
FROM table_name;
```

```sql
-- Filter rows with a condition
SELECT * FROM table_name 
WHERE column_name = 'value';
```

```sql
-- Insert data into a table
INSERT INTO table_name (column1, column2) 
    VALUES ('value1', 'value2');
```

```sql
-- Update data in a table
UPDATE table_name 
SET column1 = 'new_value' 
WHERE column2 = 'old_value';
```

```sql
-- Delete data from a table
DELETE FROM table_name WHERE column_name = 'value';
```

# Aggregation Functions:
```sql
-- Count rows
SELECT COUNT(*) FROM table_name;
```
```sql
-- Calculate average
SELECT AVG(column_name) FROM table_name;
```
```sql
-- Find maximum value
SELECT MAX(column_name) FROM table_name;
```
```sql
-- Group by and aggregate
SELECT 
    column1, 
    COUNT(column2) 
FROM table_name 
GROUP BY column1;
```
# Joins
```sql
-- Inner join
SELECT * FROM table1 
INNER JOIN table2 
    ON table1.id = table2.id;
```
```sql
-- Left join
SELECT * FROM table1 
LEFT JOIN table2 
    ON table1.id = table2.id;
```
```sql
-- Right join
SELECT * FROM table1 
RIGHT JOIN table2 
    ON table1.id = table2.id;
```