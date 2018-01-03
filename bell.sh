#! /bin/sh

echo -e \\a
sleep 0.5
echo -e \\a
sleep 0.5
echo -e \\a
sleep 0.5
echo -e \\a
sleep 0.5
echo -e \\a
sleep 0.5
echo -e \\a

echo "This is an email from Jenkins to inform you that the build has faild." | mail -s "Jenkins: Build Failed!" amvasudeva@gmail.com
  


