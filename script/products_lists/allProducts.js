const knownProductsAllFiles = [
  {
    "name": "Айкью сн-710 пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Альт м-811 black pl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Альтаир в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Аляска ch-153 в хром хдп мб",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Аризона сн-400 бюджет в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Аризона ch-400 в хром хдп",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Артекс в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Астек б_п пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Астек гольф пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Астек пвм б_п",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Астек самба пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Астек eg б_п",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Астек eg гольф",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Астек eg самба",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Асти 4к",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Астон м-711 с подголовником белый пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Астон м-711 с подголовником черный пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Атлант в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Атлант в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Атлант в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Атлант в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Атлант в_п пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Атлант в_п пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Атлант в_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Афродита люкс со столиком хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Афродита люкс хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Аэро м-808 black pl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Бистро",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Бистро м",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Борн с-44 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Борн c-44 в хром мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Бостон сн-277 хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Бостон сн-277 хром топ-ган люкс",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Бостон хэви дьюти мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Бостон ch-277 пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Бруно ch-707",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Бэрри м-902 tg пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Бэрри м-902 tg хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Вальтер б_п пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Вальтер рондо пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Вальтер т-01 пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Ванесса",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Венус",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Венус м",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Венус м bl",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Венус м gr",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Венус ch",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Вермонт сн-151 в хром хдп мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Вермонт ch-151 в хром хдп",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Верона к-10 в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Верона к-10 в дерево мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Верона к-10 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Верона к-10 в хром мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Верона к-10 н_п дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Верона к-10 н_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Версаль",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Веста м-703 dark grey pl",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Гарвард сн-500 пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Гарвард сн-500 хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Гелакси к-49 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Гелакси к-49 в хром мб",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Гермес в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Гермес в хром",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Дакота ch-251 в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Дакота ch-251 в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Джуно дерево",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Джуно люкс дерево",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Директ лайт мс-040 в хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Директ лайт мс-040 н хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Директ лайт мс-040 н_п хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Директ люкс мс-040 в хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Дэли ch-503 белый пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Дэли ch-503 н_п хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Дэли ch-503 white ch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Идра бюджет в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Идра в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Идра в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Идра в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Идра н_п дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Идра н_п пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Изи сн-599 пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Изо",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо +",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо пластик",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо со столиком",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо bl",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо gr",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо_жтс",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Изо_жтс +",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Изо_жтс со столиком",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Изо-2",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Изо-3",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Йота м-805 black pl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Йота м-805 gray ch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Йота м-805 white ch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Кайман в топ-ган lux",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман комфорт ch-301 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман комфорт ch-301 в хром мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман комфорт ch-301 в bl",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман комфорт ch-301 н хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман комфорт ch-301 н_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман трио ch-303 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман трио ch-303 в хром мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман трио ch-303 н хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман трио ch-303 н_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 в хром мб",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 в bl",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 н хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 н bl",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 н_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Кайман ch-300 н_п bl",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Калифорния в cн-438 хром",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Калифорния ch-438 в бюджет пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Квадро м-807 black pl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Квадро м-807 white ch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Кембридж сн-502 н_п",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Кембридж сн-502 пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Кембридж ch-502 н_п хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Кендо к-41 в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Кендо к-41 в хром",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Кендо k-41 в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Клио с-101 нептун пвм хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Клуб",
    "category": "chair_visitors",
    "is_archive": true
  },
  {
    "name": "Клуб 4к",
    "category": "chair_visitors",
    "is_archive": true
  },
  {
    "name": "Клуб 4l",
    "category": "chair_visitors",
    "is_archive": true
  },
  {
    "name": "Клуб gts",
    "category": "chair_visitors",
    "is_archive": true
  },
  {
    "name": "Комо бюджет в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо н_п дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо н_п пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо н_п пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Комо н_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Компакт 4н складной",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Компакт люкс 4н складной",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Компакт люкс складной",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Компакт складной",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Комфорт б_п пластик",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Кора чёрный",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Кора ch",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Кремона 4к",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Кремона пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Кремона хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Куба сн-701",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Лайм хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Логика tg пластик",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Манго с-109 нептун люкс хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Марко",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Мартин б_п пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин гольф пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин люкс нептун хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин люкс т-01 пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин рондо пвм пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин рондо пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин самба пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Мартин т-01 пвм пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро б_п пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро гольф пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро люкс нептун хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро люкс т-01 пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро рондо пвм пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро рондо пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро самба пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Метро т-01 пвм пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Микс сн-696 н_п bl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Микс сн-696 н_п ch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Микс сн-696 пластик пиастра",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Микс сн-696 пластик tg",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Микс сн-696 хром tg",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Надир в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Надир в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Надир в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Надир в хром",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Неон",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Неон bl",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Нерон",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Оптима м-901 с подголовником черный пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Оптима м-901 черный пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Орегон сн-686 в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орегон сн-686 в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орион в дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орион в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орион в хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орион н_п дерево",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орион н_п пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Орион н_п хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Парма 4к",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Пилот в пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Пилот в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Пилот н пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Пилот н пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Пилот н_п пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Пилот н_п пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Премьер в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Премьер в пластик-люкс 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Престиж б_п овалина пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж б_п пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж гольф овалина пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж гольф пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж люкс",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Престиж нептун овалина хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж пвм",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Престиж самба овалина пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж самба пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж соната овалина пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж соната пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Престиж cpt",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Пронто сн-211 хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Профи м-900 black ppl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Профи м-900 grey pch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Рекорд м-878 белый пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Рекорд м-878 чёрный пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Рикс сн-577",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Ровер хэви дьюти сн-708",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Ройс м-704",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Самба",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Самба люкс gtp пиастра",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Самба люкс gtp пиастра столик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Самба люкс gtp tg",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Самба люкс gtp tg столик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Самба со столиком",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Самба gtp пиастра",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Самба gtp tg",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Сиена 4к",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Сириус с-102 нептун хром",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Сириус с-102 рондо пластик",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Сириус с-102 самба пластик",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Ситро м-804 black pl",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Ситро м-804 gray ch",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Ситро м-804 white ch",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Сн-710 айкью н пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Сн-710 айкью н_п",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Сн-710 айкью н_п bl",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Соло сн-601 пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Соло сн-601 хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Соло max сн-601 пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Соло max сн-601 хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "София",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "София со столиком",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Софт м-903 люкс хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Софт м-903 tg пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Софт м-903 tg хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Стандарт",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Стандарт gr",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Стар б_п овалина пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Стул кассира б_п eg со спинкой",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Стул кассира l б_п",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Стул кассира l б_п со спинкой",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Стэнфорд сн-501 т-01 пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Табурет кр",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Табурет кр bl",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Табурет кр ch",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Табурет пр",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Табурет пр bl",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Табурет пр ch",
    "category": "chair_cafe_and_bar",
    "is_archive": false
  },
  {
    "name": "Тесла сн-709 белый пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Тесла сн-709 чёрный пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Ультра нептун в хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Ультра нептун н хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Ультра рондо н пластик pl660",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Ультра рондо н хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Ультра т-01 н пластик pl660",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Фест к-11 н пластик",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Фигаро к13 н_п хром",
    "category": "chair_visitors",
    "is_archive": true
  },
  {
    "name": "Фигаро gts к13 пиастра хром",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Фигаро gts к13 tg хром",
    "category": "armchair_personal",
    "is_archive": true
  },
  {
    "name": "Форум",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Хэнди м-806 black pl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Хэнди м-806 gray ch",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Честер 4l хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Честер хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Честер gtp пиастра хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Честер gtp tg хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Честер gts пиастра хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Честер gts tg хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Чико 4l хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Шелл с-07",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Шелл софт",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Шелл gts с-21 белый",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Шелл gts с-21 софт хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Шелл gts с-21 хром",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Шелл gts с-21 черный",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Эльф в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Эльф н пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Энжел сн-800 белый н_п нео сн",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энжел сн-800 белый пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энжел сн-800 белый хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энжел сн-800 чёрный",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энжел сн-800 чёрный н_п нео bl",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энтер комби сн-320 гольф пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энтер сн-320 нептун хром",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Энтер сн-320 т-01 пластик",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Эрго б_п овалина пластик",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Эфир с-30 в пластик 727",
    "category": "armchair_rukovoditel",
    "is_archive": true
  },
  {
    "name": "Cильвия арм хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Cильвия хром",
    "category": "chair_visitors",
    "is_archive": false
  },
  {
    "name": "Epik а-001-mb",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik а-007-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik а-011-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik a-112-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik a-130-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik a-155-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik a-177-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik a-181-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik e-201-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik e-212-g",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik e-222-mb",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik k-400-ch",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik k-430-ch",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik p-521-sb",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Epik p-700",
    "category": "armchair_epik",
    "is_archive": false
  },
  {
    "name": "Kid's с-01",
    "category": "armchair_personal",
    "is_archive": false
  },
  {
    "name": "Utfc бремен м-123 алюминий",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Utfc канзас м-111 пластик хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Utfc киото м-250",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Utfc кофу м-231",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Utfc мориока м-242",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Utfc номи м-317",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Utfc номи м-317 с подголовником",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Utfc онтарио м-105 пластик хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Utfc онтарио м-405 н_п пластик хром",
    "category": "armchair_rukovoditel",
    "is_archive": false
  },
  {
    "name": "Utfc осака м-201",
    "category": "armchair_comfort",
    "is_archive": false
  },
  {
    "name": "Utfc санда м-207",
    "category": "armchair_comfort",
    "is_archive": false
  }
];