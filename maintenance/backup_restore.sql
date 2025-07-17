-- ========================================
-- PostgreSQL Backup and Restore Script
-- ========================================

-- ✅ BACKUP:
-- pg_dump -U postgres -d hospital_db -F c -f hospital_db.backup

-- 🧨 DROP DATABASE (simulate disaster):
-- dropdb -U postgres hospital_db

-- 🧱 RECREATE DATABASE:
-- createdb -U postgres hospital_db

-- 🔁 RESTORE FROM BACKUP:
-- pg_restore -U postgres -d hospital_db hospital_db.backup
