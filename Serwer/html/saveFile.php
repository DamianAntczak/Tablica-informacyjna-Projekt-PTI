<?
if(!empty($_POST['data'])){
$data = $_POST['data'];
echo $data;
$path = $_SERVER['DOCUMENT_ROOT'].'/upload/tablica.txt';
echo $path;
$file = fopen($path, 'w+');
if($file === false){
	echo "nie mo¿na otworzyæ pliku";
	exit;
}
fwrite($file, $data);
fclose($file);
}
?>