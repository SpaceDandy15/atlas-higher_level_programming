-- 0-privileges.sql

-- Check privileges for user_0d_1
SELECT
    CONCAT('Grants for user_0d_1@localhost: ') AS 'Grants',
    IFNULL(GROUP_CONCAT(PRIVILEGE_TYPE SEPARATOR ', '), 'No grants found') AS 'Privileges'
FROM
    information_schema.user_privileges 
WHERE
    GRANTEE = "'user_0d_1'@'localhost'";

-- Check privileges for user_0d_2
SELECT
    CONCAT('Grants for user_0d_2@localhost: ') AS 'Grants',
    IFNULL(GROUP_CONCAT(PRIVILEGE_TYPE SEPARATOR ', '), 'No grants found') AS 'Privileges'
FROM
    information_schema.user_privileges 
WHERE
    GRANTEE = "'user_0d_2'@'localhost'";
