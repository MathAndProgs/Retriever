from datasets import load_dataset

def load_ms_marco(split="train"):
    """
    Загружает датасет microsoft/ms_marco с Huggingface.

    Args:
        split (str): Сплит датасета для загрузки ("train", "validation", "test").

    Returns:
        dataset: Загруженный датасет.
    """
    dataset_name = "microsoft/ms_marco"
    try:
        dataset = load_dataset(dataset_name, split=split)
        print(f"Датасет '{dataset_name}' загружен успешно! Сплит: '{split}'")
        return dataset
    except Exception as e:
        print(f"Ошибка при загрузке датасета: {e}")