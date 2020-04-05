CREATE USER 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'dbpassword';
GRANT ALL PRIVILEGES ON * . * TO 'dbuser'@'%';
FLUSH PRIVILEGES;