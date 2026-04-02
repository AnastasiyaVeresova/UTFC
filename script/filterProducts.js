let filteredProducts = [];

function filterProducts() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase().trim();
    const min = parseInt(minHeightInput.value);
    const max = parseInt(maxHeightInput.value);
    const armrestFilters = Array.from(document.querySelectorAll('.armrest-filter:checked')).map(el => el.value);
    const mechanismFilters = Array.from(document.querySelectorAll('.mechanism-filter:checked')).map(el => el.value);
    const finishFilters = Array.from(document.querySelectorAll('.finish-filter:checked')).map(el => el.value);

    filteredProducts = validProducts.filter(product => {
        console.log("Проверяем товар:", product.unique_name);

        // Проверка по высоте
        const chairHeight = product.dimensions_details?.[0]?.chair_height;
        if (chairHeight) {
            const minHeight = parseInt(chairHeight.min) || 0;
            const maxHeight = parseInt(chairHeight.max) || minHeight;
            console.log("Высота:", minHeight, "-", maxHeight);
            if (maxHeight > max || minHeight < min) {
                console.log("Не прошёл по высоте:", product.unique_name);
                return false;
            }
        } else {
            console.log("Нет данных по высоте для товара:", product.unique_name);
        }



        // Проверка по подлокотникам
        if (armrestFilters.length > 0) {
            let armrestMatch = true; // Начинаем с true, так как нужно совпадение по всем выбранным
            armrestFilters.forEach(filter => {
                let filterMatch = false;
                const patterns = filter.split('|');
                patterns.forEach(pattern => {
                    const uniqueName = Array.isArray(product.unique_name) ? product.unique_name[0].toLowerCase() : product.unique_name.toLowerCase();
                    if (uniqueName.includes(pattern.toLowerCase())) {
                        filterMatch = true;
                    }
                });
                if (!filterMatch) {
                    armrestMatch = false; // Если хотя бы один фильтр не совпал, товар не подходит
                }
            });
            if (!armrestMatch) {
                console.log("Не прошёл по подлокотникам:", product.unique_name);
                return false;
            }
        }

        // Проверка по механизмам
        if (mechanismFilters.length > 0) {
            let mechanismMatch = true;
            mechanismFilters.forEach(filter => {
                let filterMatch = false;
                const patterns = filter.split('|');
                patterns.forEach(pattern => {
                    const uniqueName = Array.isArray(product.unique_name) ? product.unique_name[0].toLowerCase() : product.unique_name.toLowerCase();
                    if (uniqueName.includes(pattern.toLowerCase())) {
                        filterMatch = true;
                    }
                });
                if (!filterMatch) {
                    mechanismMatch = false;
                }
            });
            if (!mechanismMatch) {
                return false;
            }
        }

        // Проверка по исполнению
        if (finishFilters.length > 0) {
            let finishMatch = true;
            finishFilters.forEach(filter => {
                let filterMatch = false;
                const patterns = filter.split('|');
                patterns.forEach(pattern => {
                    const fieldsToCheck = [
                        product.unique_name?.[0]?.toLowerCase(),
                        product.namefile?.[0]?.toLowerCase(),
                        product.name?.[0]?.toLowerCase(),
                    ];
                    fieldsToCheck.forEach(field => {
                        if (field && field.includes(pattern.toLowerCase())) {
                            filterMatch = true;
                        }
                    });
                });
                if (!filterMatch) {
                    finishMatch = false;
                }
            });
            if (!finishMatch) {
                return false;
            }
        }

        return true;
    });


    // Обновляем видимость карточек
    const productCards = document.querySelectorAll('.product-card');
    let visibleProductsCount = 0;
    const oldMessage = document.querySelector('#products > p');
    if (oldMessage) oldMessage.remove();

    productCards.forEach(card => {
        const cardName = card.querySelector('a').textContent.trim().toLowerCase();
        const product = validProducts.find(p => {
            const pName = Array.isArray(p.unique_name) ? p.unique_name[0].trim().toLowerCase() : p.unique_name.trim().toLowerCase();
            return pName === cardName;

        });
        if (!product) {
            card.style.display = 'none';
            return;
        }

        const isFiltered = filteredProducts.some(p => {
            const pName = Array.isArray(p.unique_name) ? p.unique_name[0].toLowerCase() : p.unique_name.toLowerCase();
            return pName === cardName;
        });

        if (isFiltered) {
            card.style.display = 'inline-block';
            visibleProductsCount++;
        } else {
            card.style.display = 'none';
        }
    });

    if (visibleProductsCount === 0) {
        productsContainer.insertAdjacentHTML('beforeend', '<p>Товары не найдены. Попробуйте изменить условия фильтрации или поисковый запрос.</p>');
    }
    console.log(visibleProductsCount)
    console.log("Отфильтрованные", filteredProducts)

    // Перестроить график
    buildOverallChart(filteredProducts);
}
