<?php
header('Content-Type: application/json');

// Папки для загрузки
$uploadDir = '../img/armchair_personal/';
$boxUploadDir = '../img/boxes/';

// Проверяем и создаем папки
if (!file_exists($uploadDir)) mkdir($uploadDir, 0777, true);
if (!file_exists($boxUploadDir)) mkdir($boxUploadDir, 0777, true);

// Проверяем, что пришли данные
if (empty($_POST['product_data'])) {
    echo json_encode(['success' => false, 'message' => 'Нет данных о товаре.']);
    exit;
}

// Декодируем JSON
$productData = json_decode($_POST['product_data'], true);
if (json_last_error() !== JSON_ERROR_NONE) {
    echo json_encode(['success' => false, 'message' => 'Ошибка декодирования JSON.']);
    exit;
}

// Обрабатываем файлы
$files = [
    'vid_main_file' => $uploadDir,
    'chair_view_file' => $uploadDir,
    'dimensions_file' => $uploadDir,
    'box_file' => $boxUploadDir
];
$filePaths = [];

foreach ($files as $inputName => $dir) {
    if (isset($_FILES[$inputName]) && $_FILES[$inputName]['error'] === UPLOAD_ERR_OK) {
        $ext = pathinfo($_FILES[$inputName]['name'], PATHINFO_EXTENSION);
        $filename = uniqid() . '.' . $ext;
        $destination = $dir . $filename;
        if (move_uploaded_file($_FILES[$inputName]['tmp_name'], $destination)) {
            $filePaths[$inputName] = $destination;
        } else {
            echo json_encode(['success' => false, 'message' => "Не удалось сохранить файл $inputName."]);
            exit;
        }
    }
}

// Формируем ответ
$productData['images'] = [
    [
        'vid_main' => $filePaths['vid_main_file'] ?? '',
        'chair_view' => $filePaths['chair_view_file'] ?? '',
        'dimensions' => $filePaths['dimensions_file'] ?? '',
        'box' => $filePaths['box_file'] ?? ''
    ]
];

// Сохраняем JSON в файл
$jsonFilename = '../products/armchair_personal/' . $productData['unique_name'][0] . '.json';
if (file_put_contents($jsonFilename, json_encode($productData, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT))) {
    echo json_encode(['success' => true, 'message' => 'Товар добавлен!']);
} else {
    echo json_encode(['success' => false, 'message' => 'Не удалось сохранить JSON-файл.']);
}
?>
