import datetime
import logging
from pathlib import Path

logging.basicConfig(
    filename='hb_test.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def analyze_heartbeats(file_path):
    print(f"Спроба відкрити файл: {file_path}")
    if not file_path.exists():
        print(f"ПОМИЛКА: Файл не знайдено за шляхом: {file_path}")
        return

    prev_time = None
    processed_lines = 0
    warnings_count = 0
    errors_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                # Шукаємо час після слова "Timestamp" у кожному рядку
                parts = line.split()
                time_str = None
                for i in range(len(parts) - 1):
                    if parts[i] == "Timestamp":
                        time_str = parts[i+1]
                        break
                
                if not time_str:
                    continue
                
                processed_lines += 1
                # Парсимо час у форматі HH:MM:SS
                current_time = datetime.datetime.strptime(time_str, "%H:%M:%S")

                if prev_time is not None:
                    diff = (current_time - prev_time).total_seconds()
                    
                    if diff < 0:
                        diff += 86400

                    # Перевірка згідно з вимогами:
                    # 1. > 31 та <= 33 -> WARNING
                    if 31 < diff <= 33:
                        msg = f"Line {line_num}: Heartbeat gap is {diff}s (між {prev_time.time()} та {current_time.time()}) - WARNING"
                        logging.warning(msg)
                        print(f"[WARNING] {msg}")
                        warnings_count += 1
                    # 2. > 33 -> ERROR
                    elif diff > 33:
                        msg = f"Line {line_num}: Heartbeat gap is {diff}s (між {prev_time.time()} та {current_time.time()}) - ERROR"
                        logging.error(msg)
                        print(f"[ERROR] {msg}")
                        errors_count += 1

                prev_time = current_time
            except Exception as e:
                print(f"Помилка парсингу на рядку {line_num}: {e}")
                continue

    print("\n--- Аналіз завершено ---")
    print(f"Опрацьовано сигналів (Timestamp): {processed_lines}")
    print(f"Знайдено WARNING (31-33с): {warnings_count}")
    print(f"Знайдено ERROR (>33с): {errors_count}")
    

if __name__ == "__main__":
    base_dir = Path(__file__).parent
    log_file = base_dir / "hblog.txt" 
    analyze_heartbeats(log_file)