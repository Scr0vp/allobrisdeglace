-- ALLO BRISE DE GLACE — migration MariaDB 001 : table des demandes de contact
-- Usage : mysql -u root -p < deploy/mariadb/001_create_leads.sql
-- Remplacez MOT_DE_PASSE_FORT avant exécution.

CREATE DATABASE IF NOT EXISTS allobrisdeglace CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'allobrisdeglace'@'localhost' IDENTIFIED BY 'MOT_DE_PASSE_FORT';
GRANT ALL PRIVILEGES ON allobrisdeglace.* TO 'allobrisdeglace'@'localhost';
FLUSH PRIVILEGES;

USE allobrisdeglace;

CREATE TABLE IF NOT EXISTS leads (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  nom VARCHAR(120) NOT NULL,
  prenom VARCHAR(120) NOT NULL,
  telephone VARCHAR(32) NOT NULL,
  email VARCHAR(190) NOT NULL,
  region VARCHAR(60) NOT NULL,
  type_vehicule VARCHAR(120) NOT NULL,
  immatriculation VARCHAR(20) DEFAULT NULL,
  service VARCHAR(80) NOT NULL,
  message TEXT NOT NULL,
  consentement_rgpd TINYINT(1) NOT NULL DEFAULT 0,
  page_source VARCHAR(500) DEFAULT NULL,
  ip_address VARCHAR(45) DEFAULT NULL,
  user_agent VARCHAR(300) DEFAULT NULL,
  email_status ENUM('pending','sent','failed') NOT NULL DEFAULT 'pending',
  email_sent_at DATETIME(6) DEFAULT NULL,
  INDEX idx_leads_created_at (created_at),
  INDEX idx_leads_email_status (email_status),
  INDEX idx_leads_region (region)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
