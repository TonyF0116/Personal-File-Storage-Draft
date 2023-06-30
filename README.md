# Personal-File-System

A personal file system, in which you can store and view pictures and other files. You can also create and edit simple excel and pdf files. 

The website implements SSO (Single Sign On) using JWT. Token stored in cookies has path attribute set for respective pages to simulate the SSO process on different websites.

Run with the following steps:

1. Run pip install -r requirements.txt
2. Modify database configurations in personal_file_storage/config.py
3. Navigate the terminal to folder 'Personal-File-Storage', which contains this 'README.md' (affect file storing directory)
4. Run app.py

To implement:
1. ~~Account Page~~
2. ~~JWT~~
3. Index Page
4. Pic
5. Edit Page(PDF/Excel) /Email
6. Swagger
7. Redis（excel templates）/Log
