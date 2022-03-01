
# from fpdf import FPDF
# # from .views import getdata





# subject=input("Enter a subject:")
# full_marks=input("Enter a full marks")
# pass_marks=input("Enter a pass marks")

# #grpA=["What is dbms?","Whai is advantage of database?","What is relational algebra?"]


# # grpB=["How can you store data?","Write shorts notes on following.","Explain advance database management system."]

# grpA=getdata.grpA
# grpA=getdata.grpB


# with open('question_pattern.txt','w') as f:
#     firstline="             HIMALAYA COLLEGE OF ENGINEERING    \n "
#     secondline="                   Chaysal-9,Lalitpur  \n"
#     thirdline="             \n"
#     fourthline="Students are requested to give an answer in their own words\n\n"
#     fifthline=f"Subject:{subject}\n"
#     sixline=f"Full Marks:{full_marks}\n"
#     sevenline=f"Pass Marks:{pass_marks}\n\n\n"
#     f.write(firstline)
#     f.write(secondline)
#     f.write(thirdline)
#     f.write(fourthline)
#     f.write(fifthline)
#     f.write(sixline)
#     f.write(sevenline)
#     f.write("               Group 'A' (marks=2)           \n\n")

#     i=0
#     for A in grpA:
#         i=i+1
#         f.write(f"{i}."+A)
#         f.write("\n")
#     f.write("\n")

    

#     f.write("               Group 'B' (marks=4)           \n\n")
#     i=0
#     for B in grpB:
#         i=i+1
#         f.write(f"{i}."+B)
#         f.write("\n")
#     f.write('\n')


#     f.write("                Thank You!!")

# pdf=FPDF()
# pdf.add_page()
# pdf.set_font("Times",size=20)
# file=open("question_pattern.txt",'r')
# for i in file:
#     pdf.cell(100,10,txt=i,ln=1,align='c')

# pdf.output("samplequestion.pdf")