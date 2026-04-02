let isEditMode = false;

document.addEventListener('DOMContentLoaded', function() {
    // Получаем все необходимые элементы
    const editModeToggle = document.getElementById('editModeToggle');
    const addNewProductBtn = document.getElementById('addNewProduct');
    const productsContainer = document.getElementById('products');
    const addProductModal = document.getElementById('addProductModal');
    const closeModalBtn = document.querySelector('.close-modal');
    const addProductForm = document.getElementById('addProductForm');

    // Проверяем, что все элементы существуют
    if (!editModeToggle || !addNewProductBtn || !productsContainer || !addProductModal || !closeModalBtn || !addProductForm) {
        console.error("Ошибка: не найдены обязательные элементы DOM!");
        alert("Ошибка: не найдены обязательные элементы интерфейса. Проверьте HTML.");
        return;
    }

    // Переключение режима редактирования
    editModeToggle.addEventListener('click', function() {
        isEditMode = !isEditMode;
        if (isEditMode) {
            this.textContent = 'Выход из режима редактирования';
            this.classList.add('active');
            addNewProductBtn.style.display = 'inline-block';

            document.querySelectorAll('.product-card').forEach(card => {
                if (!card.querySelector('.edit-card-controls')) {
                    const controls = document.createElement('div');
                    controls.className = 'edit-card-controls';
                    controls.innerHTML = `
                        <button class="edit-product">Редактировать</button>
                        <button class="delete-product">Удалить</button>
                    `;
                    card.appendChild(controls);
                }
            });
        } else {
            this.textContent = 'Режим редактирования';
            this.classList.remove('active');
            addNewProductBtn.style.display = 'none';

            document.querySelectorAll('.edit-card-controls').forEach(controls => {
                controls.remove();
            });
        }
    });

    // Добавление нового товара
    addNewProductBtn.addEventListener('click', function() {
        if (!isEditMode) return;
        addProductModal.style.display = 'block';
    });

    // Закрытие модального окна
    closeModalBtn.addEventListener('click', function() {
        addProductModal.style.display = 'none';
    });

    // Закрытие по клику вне окна
    window.addEventListener('click', function(event) {
        if (event.target === addProductModal) {
            addProductModal.style.display = 'none';
        }
    });

    // Обработчики для кнопок редактирования/удаления
    productsContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-product')) {
            const card = e.target.closest('.product-card');
            const productName = card.querySelector('a').textContent;
            alert(`Редактирование товара: ${productName}`);
            // Здесь можно открыть модальное окно с формой редактирования
        }

        if (e.target.classList.contains('delete-product')) {
            if (confirm('Удалить этот товар?')) {
                const card = e.target.closest('.product-card');
                card.remove();
                // Здесь можно добавить логику удаления из базы/JSON
            }
        }
    });

    // Обработка формы добавления товара
    addProductForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Проверка обязательных полей
        const requiredFields = [
            'namefile', 'name_all', 'name', 'unique_name', 'vid', 'category', 'destiny'
        ];

        for (const field of requiredFields) {
            const fieldElement = document.getElementById(field);
            if (!fieldElement) {
                console.error(`Поле ${field} не найдено!`);
                alert(`Ошибка: поле ${field} не найдено!`);
                return;
            }
            if (!fieldElement.value.trim()) {
                alert(`Поле "${field}" обязательно для заполнения!`);
                fieldElement.focus();
                return;
            }
        }

        // Собираем данные из формы
        const newProduct = {
            namefile: [document.getElementById('namefile').value],
            name_all: [document.getElementById('name_all').value],
            name: [document.getElementById('name').value],
            unique_name: [document.getElementById('unique_name').value],
            vid: [document.getElementById('vid').value],
            category: [document.getElementById('category').value],
            destiny: [document.getElementById('destiny').value],
            technical_requirements: [
                document.getElementById('technical_requirements').value.split(',').map(item => item.trim()).filter(item => item)
            ],
            construction_and_materials: [{
                upholstery_materials: [document.getElementById('upholstery_materials').value],
                components: document.getElementById('components').value.split('\n').map(item => item.trim()).filter(item => item)
            }],
            dimensions_details: [{
                chair_height: {
                    min: document.getElementById('chair_height_min').value,
                    max: document.getElementById('chair_height_max').value
                }
            }],
            guarantee: [{
                period: document.getElementById('guarantee_period').value,
                max_load: document.getElementById('max_load').value
            }],
            images: [{
                vid_main: document.getElementById('vid_main_file').files[0] ? URL.createObjectURL(document.getElementById('vid_main_file').files[0]) : null,
                chair_view: document.getElementById('chair_view_file').files[0] ? URL.createObjectURL(document.getElementById('chair_view_file').files[0]) : null,
                box: document.getElementById('box_file').files[0] ? URL.createObjectURL(document.getElementById('box_file').files[0]) : null
            }],
            transportation: [{
                packaging: {
                    box_size: document.getElementById('box_size').value
                }
            }]
        };

        // Собираем FormData для отправки на сервер
 const formData = new FormData();
formData.append('product_data', JSON.stringify(newProduct));
// Добавляем файлы
const fileInputs = ['vid_main_file', 'chair_view_file', 'box_file'];
fileInputs.forEach(id => {
    const fileInput = document.getElementById(id);
    if (fileInput && fileInput.files[0]) {
        formData.append(id, fileInput.files[0]);
    }
});


        // Отправляем на сервер
        try {
            const response = await fetch('/api/upload_product', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

            const result = await response.json();
            if (result.success) {
                alert('Товар успешно добавлен!');
                addProductForm.reset(); // Очищаем форму
                addProductModal.style.display = 'none';
                window.location.reload();
            } else {
                alert('Ошибка: ' + (result.message || 'Неизвестная ошибка'));
            }
        } catch (error) {
            console.error('Ошибка загрузки:', error);
            alert('Ошибка загрузки: ' + error.message);
        }
    });

    // Предпросмотр изображения при выборе файла
    document.querySelectorAll('input[type="file"]').forEach(input => {
        input.addEventListener('change', function() {
            const previewId = `${this.id}_preview`;
            const preview = document.getElementById(previewId);
            if (!preview) {
                console.error(`Preview block ${previewId} not found!`);
                return;
            }
            preview.innerHTML = '';
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.style.maxWidth = '200px';
                    img.style.maxHeight = '200px';
                    preview.appendChild(img);
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    });
});
