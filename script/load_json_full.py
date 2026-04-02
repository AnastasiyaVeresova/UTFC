import json
from collections import defaultdict
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='merge_log.txt',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

def fix_urls(data):
    """Заменяет все /upload/ на https://utfc.ru/upload/ в словаре или списке"""
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str) and '/upload/' in v:
                data[k] = v.replace('/upload/', 'https://utfc.ru/upload/')
            else:
                fix_urls(v)
    elif isinstance(data, list):
        for item in data:
            fix_urls(item)
    return data

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Ошибка загрузки файла {file_path}: {e}")
        return []

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"Файл {file_path} успешно сохранён")
    except Exception as e:
        logger.error(f"Ошибка сохранения файла {file_path}: {e}")

def merge_children(kids):
    if not kids:
        return []
    merged = {}
    for kid in kids:
        try:
            for k, v in kid.items():
                if k not in merged:
                    merged[k] = v
                else:
                    if isinstance(merged[k], list):
                        if v not in merged[k]:
                            merged[k].append(v)
                    else:
                        if merged[k] != v:
                            merged[k] = [merged[k], v]
        except Exception as e:
            logger.error(f"Ошибка объединения данных ребёнка: {e}")
    return merged

def main():
    parents = load_json('export_file_tovar.json')
    children = load_json('export_file_offer.json')

    if not parents or not children:
        logger.error("Не удалось загрузить родителей или детей")
        return

    # Исправляем ссылки у родителей
    parents = fix_urls(parents)
    children = fix_urls(children)

    parent_to_children = defaultdict(list)
    for child in children:
        try:
            parent_id = child.get('IP_PROP34')
            if parent_id:
                parent_to_children[parent_id].append(child)
        except Exception as e:
            logger.error(f"Ошибка обработки ребёнка: {e}")

    result = []
    for parent in parents:
        try:
            parent_id = parent.get('IE_XML_ID')
            if parent_id in parent_to_children:
                unique_children = defaultdict(list)
                for child in parent_to_children[parent_id]:
                    try:
                        key = (child.get('IE_NAME'), child.get('IP_PROP35'))
                        unique_children[key].append(child)
                    except Exception as e:
                        logger.error(f"Ошибка группировки ребёнка: {e}")

                merged_children = []
                for key, kids in unique_children.items():
                    merged_children.append(merge_children(kids))

                result.append({
                    'parent': parent,
                    'children': merged_children
                })
        except Exception as e:
            logger.error(f"Ошибка обработки родителя {parent_id}: {e}")

    if result:
        save_json(result, 'merged_result.json')
    else:
        logger.error("Не удалось сформировать результат")

if __name__ == '__main__':
    main()
