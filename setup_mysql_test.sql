-- Prepares a MySQL test server.
-- Creates a hbnb_dev_db database.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a hbnb_dev user.
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all PRIVILEGES to hbnb_dev.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
-- Grants all PRIVILEGES to hbnb_dev.
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
