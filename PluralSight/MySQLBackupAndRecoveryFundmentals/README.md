# Backup
**Introduction**
- mysqldump is a client utility that performs a locical backup
- mysqldump command generates SQL statements that can run to reproduce original schema objects and data
- Besides SQL Statement mysqldump command can also generate CSV, delimited text or XML format
**Note**
- For large scale backup and restore using a physical backup copy data files in their original format than can be restored quickly

```
mysqldump -h ${host} -u ${username} -p ${database} > ${fileoutput}.sql
mysqldump -h ${host} -u ${username} -p --database ${database1} ${database2} > ${fileoutput}.sql
mysqldump -h ${host} -u ${username} -p --all-database > ${fileoutput}.sql
mysqldump -h ${host} -u ${username} -p --database ${database} --table ${table} > ${fileoutput}.sql
```

**Options**
https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html

# Restore
**Introduction**
- A successful restore is equally valuable as a successful backup
- A disaster recovery strategy is never complete without test of a database restore
- Always test your backup by restoring it on a test server

```
mysql -h ${host} -u ${username} -p ${database} < ${fileinput}.sql
```

# Point in Time Recovery
- Point-in-time Recovery Using Event Positions
- Point-in-time Recovery Using Event Times
# Frequency of Backup
- Data Safety
- Take frequent backup at regular interval
# Location of backup
- Google Drive
- Dropbox
- Amazon Simple Storage Serive (S3)
- Remote Computers (FTP)
# Best time of the Day for Backup and Restore
- Nightly maintenance process
- Low database activity

