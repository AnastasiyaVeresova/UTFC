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
const allProducts = []; // Массив для всех продуктов с категориями

// Для каждой категории генерируем список JSON-файлов
categories.forEach(category => {
    const categoryDir = path.join(productsDir, category);
    if (!fs.statSync(categoryDir).isDirectory()) return;

    // Собираем обычные товары (не из escape)
    const normalFiles = fs.readdirSync(categoryDir)
        .filter(f => f.endsWith('.json') && !f.includes('escape'))
        .map(f => f.replace('.json', ''))
        .sort((a, b) => a.localeCompare(b, 'ru'));

    // Добавляем обычные товары в общий массив
    normalFiles.forEach(name => {
        allProducts.push({ name, category, is_archive: false });
    });

    // Проверяем наличие папки escape
    const escapeDir = path.join(categoryDir, 'escape');
    if (fs.existsSync(escapeDir) && fs.statSync(escapeDir).isDirectory()) {
        const escapeFiles = fs.readdirSync(escapeDir)
            .filter(f => f.endsWith('.json'))
            .map(f => f.replace('.json', ''))
            .sort((a, b) => a.localeCompare(b, 'ru'));

        // Добавляем товары из escape в общий массив с флагом is_archive: true
        escapeFiles.forEach(name => {
            allProducts.push({ name, category, is_archive: true });
        });
    }

    // Создаём файл для категории (только обычные товары)
    const outputFile = path.join(outputDir, `${category}.js`);
    const outputContent = `const knownProducts = ${JSON.stringify(normalFiles, null, 2)};`;
    fs.writeFileSync(outputFile, outputContent);
    console.log(`Сгенерирован список для категории: ${category}`);
});

// Удаляем дубликаты (если есть товары с одинаковыми названиями в разных категориях)
const uniqueAllProducts = Array.from(new Map(allProducts.map(item => [item.name, item])).values())
    .sort((a, b) => a.name.localeCompare(b.name, 'ru'));

// Создаём общий файл со всеми продуктами и их категориями
const allOutputFile = path.join(outputDir, 'allProducts.js');
const allOutputContent = `const knownProductsAllFiles = ${JSON.stringify(uniqueAllProducts, null, 2)};`;
fs.writeFileSync(allOutputFile, allOutputContent);
console.log('Сгенерирован общий список для всех категорий с указанием категорий и флага is_archive');
