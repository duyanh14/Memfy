<?php

include_once 'Request.php';
include_once 'Router.php';
include_once 'database.php';

$router = new Router(new Request);

$router->post('/api/application', function($request) {

	$database_host = 'localhost';
	$database_user = 'zjrfpnjq_memfy';
	$database_password = 'duyanh123a';
	$database_name = 'zjrfpnjq_memfy';

	$database = new database($database_host, $database_user, $database_password, $database_name);
	
	$hardware = $_POST['hardware'];
	
	$result = $database->query('SELECT * FROM hardware WHERE id = ?', array($hardware));
	if (!$result->numRows()) {
		$result = $database->query('INSERT INTO hardware (id,date) VALUES (?,?)', array($hardware, time()));
		if (!$result->affectedRows()) {
		}
	}
	
	$result = $database->query('INSERT INTO hardware_active (hardware,date,ip) VALUES (?,?,?)', array($hardware, time(), get_client_ip()));
	if (!$result->numRows()) {
	}
	
	$result = $database->query('SELECT * FROM banner WHERE disable = 0 ORDER BY date DESC')->fetchAll();
	
	$banner = [];
	
	foreach ($result as $rs) {
		array_push($banner, [
			'id' => $rs['id'],
			'image' => $rs['image'],
			'url' => $rs['url'],
		]);
	}
	
	$data = [
		'banner' => $banner
	];
	
	header('Content-Type: application/json; charset=utf-8');
	
	echo json_encode($data);
});

function get_client_ip() {
    $ipaddress = '';
    if (isset($_SERVER['HTTP_CLIENT_IP']))
        $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
    else if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_X_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED'];
    else if(isset($_SERVER['HTTP_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_FORWARDED'];
    else if(isset($_SERVER['REMOTE_ADDR']))
        $ipaddress = $_SERVER['REMOTE_ADDR'];
    else
        $ipaddress = 'UNKNOWN';
    return $ipaddress;
}

?>