# Fix 500 error when GET http methodf is requested to Apache web server

exec {'replace':
   provider => shell,
   command => 'sed -i "s/phpp/php/g" /var/www/html/wp-setting.php'
}
