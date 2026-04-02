const fs = require('fs');
const path = require('path');

// Путь к папке с продуктами
const productsDir = 'C:\\Users\\UTFC\\Documents\\Downloads\\to\\products';

// Рекурсивно обходим папки
function walkDir(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            walkDir(fullPath); // Рекурсия для вложенных папок
        } else if (file.endsWith('.json')) {
            processJsonFile(fullPath);
        }
    });
}

// Обрабатываем JSON-файл
function processJsonFile(filePath) {
    try {
        const data = fs.readFileSync(filePath, 'utf8');
        let json = JSON.parse(data);

        // Удаляем unique_name, если оно уже есть
        if (json.unique_name) {
            delete json.unique_name;
        }

        // Генерируем unique_name
        let uniqueName = '';
        if (json.name && Array.isArray(json.name) && json.name.length > 0) {
            uniqueName = json.name[0];
        } else if (json.name && typeof json.name === 'string') {
            uniqueName = json.name;
        } else {
            uniqueName = path.basename(filePath, '.json');
        }

        // Очищаем от недопустимых символов
        uniqueName = uniqueName.replace(/[/\\:*?"<>|]/g, '_').trim();

        // Создаём новый объект с нужным порядком полей
        const newJson = {};
        for (const key in json) {
            newJson[key] = json[key];
            if (key === 'name') {
                newJson.unique_name = uniqueName;
            }
        }

        // Сохраняем обратно в файл с отступами
        fs.writeFileSync(filePath, JSON.stringify(newJson, null, 4), 'utf8');
        console.log(`Обновлено: ${filePath} (unique_name: ${uniqueName})`);
    } catch (err) {
        console.error(`Ошибка при обработке ${filePath}:`, err);
    }
}

// Запускаем обработку
walkDir(productsDir);
console.log('Готово!');
