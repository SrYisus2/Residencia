<?php

$dbhost = "localhost"; // Nombre del host
$dbuser = "root"; // Nombre de usuario de la base de datos
$dbpass = ""; // Contraseña de la base de datos
$dbname = "remaga"; // Nombre de la base de datos

$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

echo "Conectado a la base de datos MySQL 'remaga' exitosamente.";
