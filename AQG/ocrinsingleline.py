# miner_text_generator.py
import io
import re
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from .models import Question,Osquestion
from django.contrib.auth.models import User


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
           
            text = fake_file_handle.getvalue()
            yield text
   
            # close open handles
            converter.close()
            fake_file_handle.close()
   
def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        split_text=page.split("]")
        # print(split_text)
        x = len(split_text)
        for i in range(0,x):
            mlist = split_text[i]
            pattern = re.compile(r'(\d{1,3})\)\s+([A-Za-z0-9.,;\"\s?]+)\s+\[(\d{1,2})\s*')
            matches = pattern.finditer(mlist)
            for match in matches:
                # print(match.group(3))
                Ques = match.group(2)
                marking = match.group(3)
                if Question.objects.filter(qn=Ques).exists():
                    pass
                else:
                    new_question = Question.objects.create(qn = Ques, mark = marking)
                    new_question.save()

    with open('test.txt','w') as f:
        f.write(page)
        #print()


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
           
            text = fake_file_handle.getvalue()
            yield text
   
            # close open handles
            converter.close()
            fake_file_handle.close()
   
def extract_texts(pdf_path):
    for page in extract_text_by_page(pdf_path):
        split_text=page.split("]")
        # print(split_text)
        x = len(split_text)
        for i in range(0,x):
            mlist = split_text[i]
            pattern = re.compile(r'(\d{1,3})\)\s+([A-Za-z0-9.,;\"\s?]+)\s+\[(\d{1,2})\s*')
            matches = pattern.finditer(mlist)
            for match in matches:
                # print(match.group(3))
                Ques = match.group(2)
                marking = match.group(3)
                if Osquestion.objects.filter(qn=Ques).exists():
                    pass
                else:
                    new_question = Osquestion.objects.create(qn = Ques, mark = marking)
                    new_question.save()

    with open('ostest.txt','w') as f:
        f.write(page)
       
text=extract_text('test.pdf')
textos = extract_texts('ostest.pdf')







