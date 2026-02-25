const knownProductsAllFiles = [
  {
    "name": "Айкью сн-710 н пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Айкью сн-710 пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Альт м-811 black pl",
    "category": "armchair_comfort"
  },
  {
    "name": "Альтаир в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Аляска ch-153 в хром хдп мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Аризона сн-400 бюджет в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Аризона ch-400 в хром хдп",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Артекс в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Астек б_п пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Астек гольф пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Астек пвм б_п",
    "category": "armchair_personal"
  },
  {
    "name": "Астек самба пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Астек eg б_п",
    "category": "armchair_personal"
  },
  {
    "name": "Астек eg гольф",
    "category": "armchair_personal"
  },
  {
    "name": "Астек eg самба",
    "category": "armchair_personal"
  },
  {
    "name": "Асти 4к",
    "category": "chair_visitors"
  },
  {
    "name": "Астон м-711 с подголовником белый пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Астон м-711 с подголовником черный пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Атлант в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Атлант в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Атлант в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Атлант в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Атлант в_п пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Атлант в_п пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Атлант в_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Афродита люкс со столиком хром",
    "category": "chair_visitors"
  },
  {
    "name": "Афродита люкс хром",
    "category": "chair_visitors"
  },
  {
    "name": "Аэро м-808 black pl",
    "category": "armchair_comfort"
  },
  {
    "name": "Бистро",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Бистро м",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Борн с-44 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Борн c-44 в хром мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Бостон сн-277 хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Бостон СН-277 хром Топ-Ган Люкс",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Бостон Хэви Дьюти МБ",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Бостон ch-277 пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Бруно ch-707",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Бэрри м-902 tg пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Бэрри м-902 tg хром",
    "category": "armchair_personal"
  },
  {
    "name": "Вальтер б_п пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Вальтер рондо пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Вальтер т-01 пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Ванесса",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Венус",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Венус м",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Вермонт сн-151 в хром хдп мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Вермонт ch-151 в хром хдп",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Верона к-10 в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Верона к-10 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Верона к-10 в хром мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Верона к-10 н_п дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Верона к-10 н_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Версаль",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Веста м-703 dark grey pl",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Гарвард сн-500 пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Гарвард сн-500 хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Гелакси к-49 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Гелакси к-49 в хром мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Гермес в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Гермес в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Дакота ch-251 в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Дакота ch-251 в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Джуно дерево",
    "category": "chair_visitors"
  },
  {
    "name": "Джуно люкс дерево",
    "category": "chair_visitors"
  },
  {
    "name": "Директ лайт мс-040 в хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Директ лайт мс-040 н хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Директ лайт мс-040 н_п хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Директ люкс мс-040 в хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Дэли ch-503 белый пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Дэли ch-503 н_п хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Дэли ch-503 white ch",
    "category": "armchair_comfort"
  },
  {
    "name": "Идра бюджет в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Идра в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Идра в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Идра в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Идра н_п дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Идра н_п пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Изи сн-599 пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Изо",
    "category": "chair_visitors"
  },
  {
    "name": "Изо +",
    "category": "chair_visitors"
  },
  {
    "name": "Изо пластик",
    "category": "chair_visitors"
  },
  {
    "name": "Изо со столиком",
    "category": "chair_visitors"
  },
  {
    "name": "Изо_жтс",
    "category": "armchair_personal"
  },
  {
    "name": "Изо_жтс +",
    "category": "armchair_personal"
  },
  {
    "name": "Изо_жтс со столиком",
    "category": "armchair_personal"
  },
  {
    "name": "Изо-2",
    "category": "chair_visitors"
  },
  {
    "name": "Изо-3",
    "category": "chair_visitors"
  },
  {
    "name": "Йота м-805 black pl",
    "category": "armchair_comfort"
  },
  {
    "name": "Йота м-805 gray ch",
    "category": "armchair_comfort"
  },
  {
    "name": "Йота м-805 white ch",
    "category": "armchair_comfort"
  },
  {
    "name": "Кайман в топ-ган lux",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман комфорт ch-301 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман комфорт ch-301 в хром мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман комфорт ch-301 н хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман комфорт ch-301 н_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман трио ch-303 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман трио ch-303 в хром мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман трио ch-303 н хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман трио ch-303 н_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман ch-300 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман ch-300 в хром мб",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман ch-300 н хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кайман ch-300 н_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Калифорния в cн-438 хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Калифорния ch-438 в бюджет пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Квадро м-807 black pl",
    "category": "armchair_comfort"
  },
  {
    "name": "Квадро м-807 white ch",
    "category": "armchair_comfort"
  },
  {
    "name": "Кембридж сн-502 н_п",
    "category": "armchair_comfort"
  },
  {
    "name": "Кембридж сн-502 пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Кембридж ch-502 н_п хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Кендо к-41 в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кендо к-41 в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Кендо k-41 в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Клио с-101 нептун пвм хром",
    "category": "armchair_personal"
  },
  {
    "name": "Клуб",
    "category": "chair_visitors"
  },
  {
    "name": "Клуб 4к",
    "category": "chair_visitors"
  },
  {
    "name": "Клуб 4l",
    "category": "chair_visitors"
  },
  {
    "name": "Клуб gts",
    "category": "chair_visitors"
  },
  {
    "name": "Комо бюджет в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо н_п дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо н_п пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо н_п пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Комо н_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Компакт 4н складной",
    "category": "chair_visitors"
  },
  {
    "name": "Компакт люкс 4н складной",
    "category": "chair_visitors"
  },
  {
    "name": "Компакт люкс складной",
    "category": "chair_visitors"
  },
  {
    "name": "Компакт складной",
    "category": "chair_visitors"
  },
  {
    "name": "Комфорт б_п пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Кора чёрный",
    "category": "chair_visitors"
  },
  {
    "name": "Кремона 4к",
    "category": "chair_visitors"
  },
  {
    "name": "Кремона пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Кремона хром",
    "category": "armchair_personal"
  },
  {
    "name": "Куба сн-701",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Лайм хром",
    "category": "chair_visitors"
  },
  {
    "name": "Логика tg пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Манго с-109 нептун люкс хром",
    "category": "armchair_personal"
  },
  {
    "name": "Марко",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Мартин б_п пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин гольф пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин люкс нептун хром",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин люкс т-01 пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин рондо пвм пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин рондо пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин самба пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Мартин т-01 пвм пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро б_п пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро гольф пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро люкс нептун хром",
    "category": "armchair_personal"
  },
  {
    "name": "Метро люкс т-01 пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро рондо пвм пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро рондо пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро самба пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Метро т-01 пвм пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Микс сн-696 н_п bl",
    "category": "armchair_comfort"
  },
  {
    "name": "Микс сн-696 н_п ch",
    "category": "armchair_comfort"
  },
  {
    "name": "Микс сн-696 пластик пиастра",
    "category": "armchair_comfort"
  },
  {
    "name": "Микс сн-696 пластик tg",
    "category": "armchair_comfort"
  },
  {
    "name": "Микс сн-696 хром tg",
    "category": "armchair_comfort"
  },
  {
    "name": "Надир в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Надир в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Надир в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Надир в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Неон",
    "category": "chair_visitors"
  },
  {
    "name": "Нерон",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Оптима м-901 с подголовником черный пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Оптима м-901 черный пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Орегон сн-686 в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орегон сн-686 в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орион в дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орион в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орион в хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орион н_п дерево",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орион н_п пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Орион н_п хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Парма 4к",
    "category": "chair_visitors"
  },
  {
    "name": "Пилот в пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Пилот в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Пилот н пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Пилот н пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Пилот н_п пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Пилот н_п пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Премьер в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Премьер в пластик-люкс 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Престиж б_п овалина пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж б_п пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж гольф овалина пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж гольф пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж люкс",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж нептун овалина хром",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж пвм",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж самба овалина пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж самба пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж соната овалина пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж соната пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Престиж cpt",
    "category": "armchair_personal"
  },
  {
    "name": "Пронто сн-211 хром",
    "category": "armchair_personal"
  },
  {
    "name": "Профи м-900 black ppl",
    "category": "armchair_comfort"
  },
  {
    "name": "Профи м-900 grey pch",
    "category": "armchair_comfort"
  },
  {
    "name": "Рекорд м-878 белый пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Рекорд м-878 чёрный пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Рикс сн-577",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Ровер хэви дьюти сн-708",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Ройс м-704",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Самба",
    "category": "chair_visitors"
  },
  {
    "name": "Самба люкс gtp пиастра",
    "category": "armchair_personal"
  },
  {
    "name": "Самба люкс gtp пиастра столик",
    "category": "armchair_personal"
  },
  {
    "name": "Самба люкс gtp tg",
    "category": "armchair_personal"
  },
  {
    "name": "Самба люкс gtp tg столик",
    "category": "armchair_personal"
  },
  {
    "name": "Самба со столиком",
    "category": "chair_visitors"
  },
  {
    "name": "Самба gtp пиастра",
    "category": "armchair_personal"
  },
  {
    "name": "Самба gtp tg",
    "category": "armchair_personal"
  },
  {
    "name": "Сиена 4к",
    "category": "chair_visitors"
  },
  {
    "name": "Сириус с-102 нептун хром",
    "category": "armchair_personal"
  },
  {
    "name": "Сириус с-102 рондо пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Сириус с-102 самба пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Ситро м-804 black pl",
    "category": "armchair_personal"
  },
  {
    "name": "Ситро м-804 gray ch",
    "category": "armchair_personal"
  },
  {
    "name": "Ситро м-804 white ch",
    "category": "armchair_personal"
  },
  {
    "name": "СН-710 Айкью Н_п",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Соло сн-601 пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Соло сн-601 хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "София",
    "category": "chair_visitors"
  },
  {
    "name": "София со столиком",
    "category": "chair_visitors"
  },
  {
    "name": "Софт м-903 люкс хром",
    "category": "armchair_personal"
  },
  {
    "name": "Софт м-903 tg пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Софт м-903 tg хром",
    "category": "armchair_personal"
  },
  {
    "name": "Стандарт",
    "category": "chair_visitors"
  },
  {
    "name": "Стар б_п овалина пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Стул кассира б_п eg со спинкой",
    "category": "armchair_personal"
  },
  {
    "name": "Стул кассира l б_п",
    "category": "armchair_personal"
  },
  {
    "name": "Стул кассира l б_п со спинкой",
    "category": "armchair_personal"
  },
  {
    "name": "Стэнфорд сн-501 т-01 пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Табурет кр",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Табурет пр",
    "category": "chair_cafe_and_bar"
  },
  {
    "name": "Тесла сн-709 белый пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Тесла сн-709 чёрный пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Ультра нептун в хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Ультра нептун н хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Ультра рондо н пластик pl660",
    "category": "armchair_comfort"
  },
  {
    "name": "Ультра рондо н хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Ультра т-01 н пластик pl660",
    "category": "armchair_comfort"
  },
  {
    "name": "Фест к-11 н пластик",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Фигаро к13 н_п хром",
    "category": "chair_visitors"
  },
  {
    "name": "Фигаро gts к13 пиастра хром",
    "category": "armchair_personal"
  },
  {
    "name": "Фигаро gts к13 tg хром",
    "category": "armchair_personal"
  },
  {
    "name": "Форум",
    "category": "chair_visitors"
  },
  {
    "name": "Хэнди м-806 black pl",
    "category": "armchair_comfort"
  },
  {
    "name": "Хэнди м-806 gray ch",
    "category": "armchair_comfort"
  },
  {
    "name": "Честер 4l хром",
    "category": "chair_visitors"
  },
  {
    "name": "Честер хром",
    "category": "chair_visitors"
  },
  {
    "name": "Честер gtp пиастра хром",
    "category": "armchair_personal"
  },
  {
    "name": "Честер gtp tg хром",
    "category": "armchair_personal"
  },
  {
    "name": "Честер gts пиастра хром",
    "category": "armchair_personal"
  },
  {
    "name": "Чико 4l хром",
    "category": "chair_visitors"
  },
  {
    "name": "Шелл с-07",
    "category": "chair_visitors"
  },
  {
    "name": "Шелл софт",
    "category": "chair_visitors"
  },
  {
    "name": "Шелл gts с-21 белый",
    "category": "armchair_personal"
  },
  {
    "name": "Шелл gts с-21 хром",
    "category": "armchair_personal"
  },
  {
    "name": "Шелл gts с-21 черный",
    "category": "armchair_personal"
  },
  {
    "name": "Эльф в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Эльф н пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Энжел сн-800 белый н_п нео сн",
    "category": "armchair_comfort"
  },
  {
    "name": "Энжел сн-800 белый пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Энжел сн-800 белый хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Энжел сн-800 чёрный",
    "category": "armchair_comfort"
  },
  {
    "name": "Энжел сн-800 чёрный н_п нео bl",
    "category": "armchair_comfort"
  },
  {
    "name": "Энтер комби сн-320 гольф пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Энтер сн-320 нептун хром",
    "category": "armchair_comfort"
  },
  {
    "name": "Энтер сн-320 т-01 пластик",
    "category": "armchair_comfort"
  },
  {
    "name": "Эрго б_п овалина пластик",
    "category": "armchair_personal"
  },
  {
    "name": "Эфир с-30 в пластик 727",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Cильвия арм хром",
    "category": "chair_visitors"
  },
  {
    "name": "Cильвия хром",
    "category": "chair_visitors"
  },
  {
    "name": "Epik а-001-mb",
    "category": "armchair_epik"
  },
  {
    "name": "Epik а-007-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik а-011-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik a-112-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik a-130-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik a-155-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik a-177-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik a-181-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik e-201-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik e-212-g",
    "category": "armchair_epik"
  },
  {
    "name": "Epik e-222-mb",
    "category": "armchair_epik"
  },
  {
    "name": "Epik k-400-ch",
    "category": "armchair_epik"
  },
  {
    "name": "Epik k-430-ch",
    "category": "armchair_epik"
  },
  {
    "name": "Epik p-521-sb",
    "category": "armchair_epik"
  },
  {
    "name": "Epik p-700",
    "category": "armchair_epik"
  },
  {
    "name": "Kid's с-01",
    "category": "armchair_personal"
  },
  {
    "name": "UTFC Бремен М-123 алюминий",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "UTFC Канзас М-111 пластик хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Utfc киото м-250",
    "category": "armchair_comfort"
  },
  {
    "name": "Utfc кофу м-231",
    "category": "armchair_comfort"
  },
  {
    "name": "Utfc мориока м-242",
    "category": "armchair_comfort"
  },
  {
    "name": "Utfc номи м-317",
    "category": "armchair_comfort"
  },
  {
    "name": "UTFC Онтарио М-105 пластик хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "UTFC Онтарио М-405 Н_п пластик хром",
    "category": "armchair_rukovoditel"
  },
  {
    "name": "Utfc осака м-201",
    "category": "armchair_comfort"
  },
  {
    "name": "Utfc санда м-207",
    "category": "armchair_comfort"
  }
];