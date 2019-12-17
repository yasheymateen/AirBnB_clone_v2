-- Prepares a MySQL server.
-- Creates a hbnb_dev_db database.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a hbnb_dev user.
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all PRIVILEGES to hbnb_dev.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
-- Grants all PRIVILEGES to hbnb_dev.
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
