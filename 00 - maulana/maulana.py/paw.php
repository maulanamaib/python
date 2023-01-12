<!DOCTYPE html>
<html>
<head>
	<title>output</title>
</head>
<body>
	<?php
		$nama = $_POST['nama'];
		echo 'Selamat datang '.$nama.' <br>';

		$tanggal = new DateTime($_POST['tanggal']);
    	$sekarang = new DateTime("today");
    	if ($tanggal > $sekarang) { 
    	$thn = "0";
    	}
    	$thn = $sekarang->diff($tanggal)->y;
    	echo "Umur anda adalah : ".$thn." tahun ";
	?>

</body>
</html>