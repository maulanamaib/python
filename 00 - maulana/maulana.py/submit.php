<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>pesanan</title>
</head>
<body>
    <?php
    require "conn.php";
    $nm_pelanggan = isset($_GET['nama']) ? $_GET['nama'] : "";
    $id_kasir = isset($_GET['kasir']) ? $_GET['kasir'] : "";
    $pilihmenu = mysqli_query($koneksi, "select * from menu");
    echo "
    <form action='pesanan.php?nama=$nm_pelanggan&kasir=$id_kasir' method='POST'>
    <label for='menu'>Pilih menu</label>
    <select name='menu' id='menu'>";
    while ($data = mysqli_fetch_array($pilihmenu)) {
        echo "<option value='$data[harga]'>$data[nama_menu] - $data[harga]</option>";
    }
    echo "</select><br>";
    echo "
        <label for='jumlah'>Input jumlah</label>
        <input type='number' name='jumlah'>";
    ?>
    <br>
    <input type="submit" name="submit">
    </form>
</body>
<?php
$id_pesanan = "";
$tgl = "";
$jumlah_item = isset($_POST["jumlah"]) ? $_POST["jumlah"] : '';
$harga = isset($_POST["menu"]) ? $_POST["menu"] : '';
$total_dibayar = ((int)$harga * (int)$jumlah_item);
if (isset($_POST["submit"])){
    $tambah = "INSERT INTO pesanan (id_pesanan,nm_pelanggan,tgl,total_dibayar,jumlah_item,id_kasir)
                values ('".$id_pesanan."','".$nm_pelanggan."','".$tgl."','".$total_dibayar."','".$jumlah_item."','".$id_kasir."')";
    $query = mysqli_query($koneksi,$tambah);
    echo "Total dibayar = $total_dibayar";

}
?>
</html>