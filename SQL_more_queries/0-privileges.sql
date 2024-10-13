-- 0-privileges.sql

-- Check privileges for user_0d_1
SELECT * FROM information_schema.user_privileges 
WHERE GRANTEE = "'user_0d_1'@'localhost'";

-- Check privileges for user_0d_2
SELECT * FROM information_schema.user_privileges 
WHERE GRANTEE = "'user_0d_2'@'localhost'";
