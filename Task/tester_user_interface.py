import urllib.request
url = "http://comp2152.gblearn.com/2021/winter/a2_tester_user_interface.php"
tester_file = urllib.request.urlopen(url)

exec(tester_file.read())