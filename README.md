# mogilefs-client-python
<H4>
mogilefs ,looks like, has been decommissioned for many years. However, in my company, we are using it to store images. and we are trying 
to migrate those images  to other storage. this script is used to export all images(or files) to local drive.
</H4>
<H1>Usage:</H1>
python get_mogilefs_files.py -d images -t "172.18.56.2:7001,172.18.31.80:7001" -o '/root/mog-images'
<H1>Description:</H1>
-d or --domain  is the mogilefs domain <br>
-t or --trackers is the mogilefs trackers <br>
-o or --output-dir is the directory where you want to export files to <br>

<H4>Reference</H4>
https://github.com/AloneRoad/pymogile
