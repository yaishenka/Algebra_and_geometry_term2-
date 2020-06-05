from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import os
from io import BytesIO

def compile_files():
    sources_dir = 'src/'
    compiled_dir = 'compiled/'
    file_list = os.listdir(sources_dir)

    for task_number in file_list:
        if 'DS_Store' in task_number: # Костыль
            continue

        sources = os.listdir(sources_dir + task_number)
        sources.sort()
        new_task_file = PdfFileWriter()
        for source_file_name in sources:
            if 'DS_Store' in source_file_name:
                continue
            buf = BytesIO()
            img = Image.open(sources_dir + task_number + '/' + source_file_name)
            img.convert("RGB").save(buf, format="pdf")
            # once image is PDF, it can be appended
            new_task_file.addPage(PdfFileReader(buf).getPage(0))
        outputStream = open(compiled_dir + task_number  + ' билет'+ '.pdf', "wb")
        new_task_file.write(outputStream)
        outputStream.close()

if os.environ.get('TRAVIS_COMMIT_MESSAGE') is None or 'Travis build' not in os.environ['TRAVIS_COMMIT_MESSAGE']:
    compile_files()



