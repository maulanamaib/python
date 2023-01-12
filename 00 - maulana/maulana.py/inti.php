<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menampilkan Tabel Menu</title>
</head>
<body>
    <h1>form</h1>
    <form action="">
		<label for="nama">Nama</label>
		<input type="text" name="nama">
		<button type="submit">submit</button>
	</form>
    <br>
    <form>
        <label for ="tgl">tanggal </label>
        <input type="date" name="tanggal" required><br>
        <button type = "submit"> submit </button>
    </form>
    <br>
    <table border="1">
        <tr>
            <th>No</th>
            <th>Nama Menu</th>
            <th>Harga</th>
            <th>Status</th>
            <th>Kategori</th>
            <th>Aksi</>
        </tr>
        <?php 
        require "conn.php";
        if (isset($_GET['ttl_hlman'])){
			$ttl_hlman = $_GET['ttl_hlman'];
        }else{
			$ttl_hlman = 10;
        }
        $tabel_menu = "SELECT * FROM menu";
        $Data = mysqli_query($koneksi,$tabel_menu);
        $ttl_row = mysqli_num_rows($Data);
        $JumlahHal = ceil($ttl_row/$ttl_hlman);
        if(!isset($_GET['halaman'])){
            $halaman = 1;
        } else{
            $halaman = $_GET['halaman'];
        }
        $Awal = ($halaman - 1) * $ttl_hlman;
        $tabel_menu = "SELECT * FROM menu limit $Awal,$ttl_hlman";
        $Data = mysqli_query($koneksi,$tabel_menu);
        $no=1;
        if (isset($_GET["cari"])) {
            $Data = mysqli_query($koneksi, "SELECT * FROM menu WHERE nama_menu LIKE '%".$_GET['cari']."%'");
        }

        while ($muncul = mysqli_fetch_array($Data)){
            echo "
                <tr>
                <th>$no</th>
                <th>$muncul[nama_menu]</th>
                <th>$muncul[harga]</th>
                <th>$muncul[status]</th>
                <th>$muncul[kategori]</th>
                <th><a href= 'hapus.php?idmenu=$muncul[idmenu]'>Hapus Menu</a></th>
            </tr>
            ";
            $no++;
        }
        ?>
    </table>
    <br>
    <?php
 
        for ($halaman = 1;$halaman <= $JumlahHal; $halaman++){
            echo '<a href="index.php?halaman='. $halaman .'">'.$halaman.'</a>&nbsp';
        };

    ?>
    <br><br>
        <div>
            <th><a href="form_tambah.php">Tambah Menu</a></th>
        </div>
</body>
</html>