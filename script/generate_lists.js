const fs = require('fs');
const path = require('path');

// Путь к папке с товарами
const productsDir = path.join(__dirname, '../products');
// Путь к папке, куда будут сохраняться списки
const outputDir = path.join(__dirname, 'js', '../products_lists');

// Создаём папку для списков, если её нет
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Читаем все категории (папки внутри products)
const categories = fs.readdirSync(productsDir);

// Для каждой категории генерируем список JSON-файлов
categories.forEach(category => {
    const categoryDir = path.join(productsDir, category);
    if (!fs.statSync(categoryDir).isDirectory()) return;

    const files = fs.readdirSync(categoryDir)
        .filter(f => f.endsWith('.json'))
        .map(f => f.replace('.json', ''))
        .sort((a, b) => a.localeCompare(b, 'ru'));

    const outputFile = path.join(outputDir, `${category}.js`);
    const outputContent = `const knownProducts = ${JSON.stringify(files)};`;
    fs.writeFileSync(outputFile, outputContent);
    console.log(`Сгенерирован список для категории: ${category}`);
});
