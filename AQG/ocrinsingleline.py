# miner_text_generator.py
import io
import re
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from .models import Os,Dbms,Es,FilesAdmin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from msilib.schema import File 
import os
from django.conf import settings


def ocr_single(request):
    
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
                texts = split_text[i]
                patern=re.compile(r'(\d{1,3}\))\s+([a-zA-Z0-9.,:;?\'\-\|\\\s* ]+)+((\[\d\+\d)|(\[\d))')
                matches=patern.finditer(texts)

                for i in matches:
                    grp3=i.group(3)
                    grp3p=re.compile(r'\[(\d)+(\+)+(\d)')
                    grp3m=grp3p.finditer(grp3)
                    grp3pp=re.compile(r'(\[(\d)$)')
                    grp3mm=grp3pp.finditer(grp3)


                    for j in grp3m:
                        #group(1)=3#group(2)=+#group(3)=2
                        grp33=j.group(0)
                        if grp3==grp33:
                            qn_first=re.compile('(\d{1,3}\))\s+([a-zA-Z0-9,:;\'\-\\\| ]+\?(\.)?)')
                            qn_second=re.compile(r'(([a-zA-Z0-9,;:\'\\\|\-\ ]+)\.|\? )+(\s+\[\d\+\d)')
                            qn_first_match=qn_first.finditer(texts)
                            qn_second_match=qn_second.finditer(texts)
                            for i in qn_first_match:
                                Ques=(i.group(2))#first part question
                                marking=(j.group(1))#first part mark
                                if subject=='os':
                                    if Os.objects.filter(qn=Ques).exists():
                                        pass
                                    else:
                                        new_question =Os.objects.create(qn = Ques, mark = marking)
                                        new_question.save()

                                if subject=='dbms':
                                    if Dbms.objects.filter(qn=Ques).exists():
                                        pass
                                    else:
                                        new_question =Dbms.objects.create(qn = Ques, mark = marking)
                                        new_question.save()

                                if subject=='es':
                                    if Es.objects.filter(qn=Ques).exists():
                                        pass
                                    else:
                                        new_question =Es.objects.create(qn = Ques, mark = marking)
                                        new_question.save()

                            for i in qn_second_match:
                                Ques=(i.group(1))#second part question
                                marking=(j.group(3))#second part mark
                                if subject=='os':
                                    if Os.objects.filter(qn=Ques).exists():
                                        pass
                                    else:
                                        new_question =Os.objects.create(qn = Ques, mark = marking)
                                        new_question.save()

                                if subject=='dbms':
                                    if Dbms.objects.filter(qn=Ques).exists():
                                        pass
                                    else:
                                        new_question =Dbms.objects.create(qn = Ques, mark = marking)
                                        new_question.save()

                                if subject=='es':
                                    if Es.objects.filter(qn=Ques).exists():
                                        pass
                                    else:
                                        new_question =Es.objects.create(qn = Ques, mark = marking)
                                        new_question.save()
                                        


                    for j in grp3mm:
                        grp33=j.group(0)
                        if grp33==grp3:
                            Ques=(i.group(2))#sigle question 
                            marking=(j.group(2))#single question's mark
                            if subject=='os':
                                if Os.objects.filter(qn=Ques).exists():
                                    pass
                                else:
                                    new_question =Os.objects.create(qn = Ques, mark = marking)
                                    new_question.save() 

                            if subject=='dbms':
                                if Dbms.objects.filter(qn=Ques).exists():
                                    pass
                                else:
                                    new_question =Dbms.objects.create(qn = Ques, mark = marking)
                                    new_question.save()

                            if subject=='es':
                                if Es.objects.filter(qn=Ques).exists():
                                    pass
                                else:
                                    new_question =Es.objects.create(qn = Ques, mark = marking)
                                    new_question.save()


        with open('test.txt','w') as f:
            f.write(page)
            #print()


    filen=FilesAdmin.objects.get(id=1) 
 

    sub=FilesAdmin.objects.all()
    subs=[i for i in sub]
    for i in subs:
        subject=i.Subject
        subject.lower()
        # print(subject)
    
    text=extract_text(f'{filen}')
    return redirect(f'admin/AQG/{subject}')




