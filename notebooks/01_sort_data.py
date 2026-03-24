import pandas as pd
import os
import shutil

# 1. حدد المسارات (تأكد إنها صحيحة)
base_path = os.getcwd()
csv_path = os.path.join(base_path, 'data', 'raw', 'train', '_annotations.csv')
images_dir = os.path.join(base_path, 'data', 'raw', 'train') # المجلد اللي فيه الـ 8000 صورة الأصلية
output_dir = os.path.join(base_path, 'data', 'processed', 'train')

# 2. قراءة ملف الإكسل
df = pd.read_csv(csv_path)
print(f"📊 ملف الإكسل فيه {len(df)} سطر.")

# 3. الفرز مع "عداد" للأخطاء
found_count = 0
missing_count = 0

for index, row in df.iterrows():
    category = str(row['class'])
    filename = row['filename']
    
    target_folder = os.path.join(output_dir, category)
    os.makedirs(target_folder, exist_ok=True)
    
    source = os.path.join(images_dir, filename)
    destination = os.path.join(target_folder, filename)
    
    if os.path.exists(source):
        shutil.copy(source, destination)
        found_count += 1
    else:
        missing_count += 1

print(f"✅ تم نسخ: {found_count} صورة.")
print(f"❌ صور لم يتم العثور عليها: {missing_count}")