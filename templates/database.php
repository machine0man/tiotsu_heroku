<?php
$_hostname='localhost';
$_username='root';
$_password='';
if($_connection=pg_connect($_hostname,$_username,$_password)){
echo'connected to database';  // connecting to database
else
  echo'connection failed';
}
?>