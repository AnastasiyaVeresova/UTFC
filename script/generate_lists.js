// const fs = require('fs');
// const path = require('path');

// // Путь к папке с товарами
// const productsDir = path.join(__dirname, '../products');
// // Путь к папке, куда будут сохраняться списки
// const outputDir = path.join(__dirname, 'js', '../products_lists');

// // Создаём папку для списков, если её нет
// if (!fs.existsSync(outputDir)) {
//     fs.mkdirSync(outputDir, { recursive: true });
// }

// // Читаем все категории (папки внутри products)
// const categories = fs.readdirSync(productsDir);

// // Для каждой категории генерируем список JSON-файлов
// categories.forEach(category => {
//     const categoryDir = path.join(productsDir, category);
//     if (!fs.statSync(categoryDir).isDirectory()) return;

//     const files = fs.readdirSync(categoryDir)
//         .filter(f => f.endsWith('.json'))
//         .map(f => f.replace('.json', ''))
//         .sort((a, b) => a.localeCompare(b, 'ru'));

//     const outputFile = path.join(outputDir, `${category}.js`);
//     const outputContent = `const knownProducts = ${JSON.stringify(files)};`;
//     fs.writeFileSync(outputFile, outputContent);
//     console.log(`Сгенерирован список для категории: ${category}`);
// });






// const fs = require('fs');
// const path = require('path');

// // Путь к папке с товарами
// const productsDir = path.join(__dirname, '../products');
// // Путь к папке, куда будут сохраняться списки
// const outputDir = path.join(__dirname, 'js', '../products_lists');

// // Создаём папку для списков, если её нет
// if (!fs.existsSync(outputDir)) {
//     fs.mkdirSync(outputDir, { recursive: true });
// }

// // Читаем все категории (папки внутри products)
// const categories = fs.readdirSync(productsDir);
// const allProducts = []; // Массив для всех продуктов

// // Для каждой категории генерируем список JSON-файлов
// categories.forEach(category => {
//     const categoryDir = path.join(productsDir, category);
//     if (!fs.statSync(categoryDir).isDirectory()) return;

//     const files = fs.readdirSync(categoryDir)
//         .filter(f => f.endsWith('.json'))
//         .map(f => f.replace('.json', ''))
//         .sort((a, b) => a.localeCompare(b, 'ru'));

//     allProducts.push(...files); // Добавляем продукты в общий массив

//     const outputFile = path.join(outputDir, `${category}.js`);
//     const outputContent = `const knownProducts = ${JSON.stringify(files)};`;
//     fs.writeFileSync(outputFile, outputContent);
//     console.log(`Сгенерирован список для категории: ${category}`);
// });

// // Сортируем и удаляем дубликаты из общего массива
// const uniqueAllProducts = [...new Set(allProducts)].sort((a, b) => a.localeCompare(b, 'ru'));

// // Создаём общий файл со всеми продуктами
// const allOutputFile = path.join(outputDir, 'allProducts.js');
// const allOutputContent = `const knownProductsAllFiles = ${JSON.stringify(uniqueAllProducts)};`;
// fs.writeFileSync(allOutputFile, allOutputContent);
// console.log('Сгенерирован общий список для всех категорий');




// const fs = require('fs');
// const path = require('path');

// // Путь к папке с товарами
// const productsDir = path.join(__dirname, '../products');
// // Путь к папке, куда будут сохраняться списки
// const outputDir = path.join(__dirname, 'js', '../products_lists');

// // Создаём папку для списков, если её нет
// if (!fs.existsSync(outputDir)) {
//     fs.mkdirSync(outputDir, { recursive: true });
// }

// // Читаем все категории (папки внутри products)
// const categories = fs.readdirSync(productsDir);
// const allProducts = []; // Массив для всех продуктов с категориями

// // Для каждой категории генерируем список JSON-файлов
// categories.forEach(category => {
//     const categoryDir = path.join(productsDir, category);
//     if (!fs.statSync(categoryDir).isDirectory()) return;

//     const files = fs.readdirSync(categoryDir)
//         .filter(f => f.endsWith('.json'))
//         .map(f => f.replace('.json', ''))
//         .sort((a, b) => a.localeCompare(b, 'ru'));

//     // Добавляем продукты в общий массив с указанием категории
//     files.forEach(name => {
//         allProducts.push({name, category});
//     });

//     const outputFile = path.join(outputDir, `${category}.js`);
//     const outputContent = `const knownProducts = ${JSON.stringify(files)};`;
//     fs.writeFileSync(outputFile, outputContent);
//     console.log(`Сгенерирован список для категории: ${category}`);
// });

// // Удаляем дубликаты (если есть товары с одинаковыми названиями в разных категориях)
// const uniqueAllProducts = Array.from(new Map(allProducts.map(item => [item.name, item])).values())
//     .sort((a, b) => a.name.localeCompare(b.name, 'ru'));

// // Создаём общий файл со всеми продуктами и их категориями
// const allOutputFile = path.join(outputDir, 'allProducts.js');
// const allOutputContent = `const knownProductsAllFiles = ${JSON.stringify(uniqueAllProducts)};`;
// fs.writeFileSync(allOutputFile, allOutputContent);
// console.log('Сгенерирован общий список для всех категорий с указанием категорий');


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

    const files = fs.readdirSync(categoryDir)
        .filter(f => f.endsWith('.json'))
        .map(f => f.replace('.json', ''))
        .sort((a, b) => a.localeCompare(b, 'ru'));

    // Добавляем продукты в общий массив с указанием категории
    files.forEach(name => {
        allProducts.push({name, category});
    });

    const outputFile = path.join(outputDir, `${category}.js`);
    const outputContent = `const knownProducts = ${JSON.stringify(files, null, 2)};`;
    fs.writeFileSync(outputFile, outputContent);
    console.log(`Сгенерирован список для категории: ${category}`);
});

// Удаляем дубликаты (если есть товары с одинаковыми названиями в разных категориях)
const uniqueAllProducts = Array.from(new Map(allProducts.map(item => [item.name, item])).values())
    .sort((a, b) => a.name.localeCompare(b.name, 'ru'));

// Создаём общий файл со всеми продуктами и их категориями, каждый объект на новой строке
const allOutputFile = path.join(outputDir, 'allProducts.js');
const allOutputContent = `const knownProductsAllFiles = ${JSON.stringify(uniqueAllProducts, null, 2)};`;
fs.writeFileSync(allOutputFile, allOutputContent);
console.log('Сгенерирован общий список для всех категорий с указанием категорий, каждый объект на новой строке');
