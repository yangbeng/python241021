import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 파일별 확장자 리스트
image_extensions = ['.jpg', '.jpeg']
data_extensions = ['.csv', '.xlsx']
docs_extensions = ['.txt', '.doc', '.pdf']
archive_extensions = ['.zip']

# 폴더가 없으면 생성
os.makedirs(image_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 다운로드 폴더 내 파일 이동
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    
    # 파일일 경우만 처리
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()  # 확장자 소문자로 변환

        # 이미지 파일 이동
        if file_ext in image_extensions:
            shutil.move(file_path, os.path.join(image_folder, filename))
        
        # 데이터 파일 이동
        elif file_ext in data_extensions:
            shutil.move(file_path, os.path.join(data_folder, filename))

        # 문서 파일 이동
        elif file_ext in docs_extensions:
            shutil.move(file_path, os.path.join(docs_folder, filename))

        # 압축 파일 이동
        elif file_ext in archive_extensions:
            shutil.move(file_path, os.path.join(archive_folder, filename))

print("파일 이동이 완료되었습니다.")
