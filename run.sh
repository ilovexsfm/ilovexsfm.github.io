rm data.json data.csv
rm idwk.xml

wget http://xsfm.co.kr/xml/idwk.xml
python3 search.py

git add .
git commit -m "running update script"
git push -u origin master
