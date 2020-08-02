<?php
$type= $_GET['T'];
$htmlDOC='<!DOCTYPE html>
<html lang="en">

<head>
    <title>SIH Demo</title>
    <script src="assests/plotly.js"></script>
    <script src="assests/jquery.min.js"></script>
</head>

<body>
<center>
<a href="https://dps-sih.herokuapp.com/index.php?T=VC">
<button>Variable Color</button>
</a>
<a href="https://dps-sih.herokuapp.com/index.php?T=VS">
<button>Variable Size</button>
</a>
</center>
<div style="height: 95vh">
   <div id="myDiv" style="height: inherit"/>
</div>
    <div id="myDiv">
        <!-- Plotly chart will be drawn inside this DIV -->
    </div>
    <script src="scattermapbox-Green-Variable-Size.js"></script>';
if($type=="VS"){
$htmlDOC=$htmlDOC.'<script src="scattermapbox-Green-Variable-Size.js"></script>';
}elseif ($type=="VC") {
    $htmlDOC=$htmlDOC.'<script src="scattermapbox-RYG-constant-size.js"></script>';
}elseif ($type=="NCSS") {
    $htmlDOC=$htmlDOC.'<script src="scattermapbox-Network-Variable-Color_Signal-Variable-size.js"></script>';
}
$htmlDOC=$htmlDOC.'
</body>
</html>';
echo $htmlDOC;
?>