<?php
include'database.php';
// Strings must be escaped to prevent SQL injection attack. 
$Name = pg_escape_string($_GET['Name'], $db); 
$Geolocationcore = pg_escape_string($_GET['Geolocation'], $db); 
$hash = $_GET['hash']; 
$secretKey="mySecretKey"; 
$real_hash = md5($name . $score . $secretKey); 
if($real_hash == $hash) { 
    // Send variables for the MySQL database class. 
    $query = "insert into scores values (NULL, '$name', '$score');"; 
    $result = pg_query($query) or die('Query failed: ' . mysql_error()); 
	} 
?>