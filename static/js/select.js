 let faculties = { "BCT": { years: [1, 2, 3, 4], parts: ["I", "II"] }, "BEX": { years: [1, 2, 3, 4], parts: ["I", "II"] }, "BCE": { years: [1, 2, 3, 4], parts: ["I", "II"] } };
 let subjects = [
     {
         name: "DBMS",
         studiedIn: [{ faculty: "BCT", year: 3, part: "II" },{faculty:"BEX",year:3, part:"I"}],
     },
     {
         name: "Operating System",
         studiedIn: [{ faculty: "BCT", year: 3, part: "II" }],
     },
     {
         name: "Embedded System",
         studiedIn: [{ faculty: "BCT", year: 3, part: "II" }],
     },
     {
         name: "Physics",
         studiedIn: [{ faculty: "BCT", year: 1, part: "I" }, { faculty: "BEX", year: 1, part: "I" }, { faculty: "BCE", year: 1, part: "I" }],
     },
     {
         name: "Engineering Maths-I",
         studiedIn: [{ faculty: "BCE", year: 1, part: "I" }, { faculty: "BCT", year: 1, part: "I" }, { faculty: "BEX", year: 1, part: "I" }],
     }
     

 ]
 const updateSubjects = (faculty, year, part) => {
     let subjectSel = document.getElementById("subject");
     subjects.forEach(subject => {
         if (subject.studiedIn.find(_in => _in.faculty == faculty && _in.year == year && _in.part == part)) {
             subjectSel.options[subjectSel.options.length] = new Option(subject.name, subject.name);
         }
     });
 }
 window.onload = function () {
     var facultySel = document.getElementById("faculty");
     var yearSel = document.getElementById("year");
     var partSel = document.getElementById("part");
     var subjectSel = document.getElementById("subject");
     for (var x in faculties) {
         facultySel.options[facultySel.options.length] = new Option(x, x);
     }

     facultySel.onchange = function () {
         yearSel.innerHTML = "";
         partSel.innerHTML = "";
         subjectSel.innerHTML = "";
         yearSel.options[0] = new Option("Year", "");
         partSel.options[0] = new Option("Part", "");
         subjectSel.options[0] = new Option("Subject", "");
         //display correct values
         let years = faculties[facultySel.value].years;
         let parts = faculties[facultySel.value].parts;
         years.forEach(y => yearSel.options[yearSel.options.length] = new Option(y, y));
         parts.forEach(p => partSel.options[partSel.options.length] = new Option(p, p));
     }
     yearSel.onchange = function () {
         subjectSel.innerHTML = "";
         subjectSel.options[0] = new Option("Subject", "");
         if (partSel.value === "") return;
         //display correct values
         updateSubjects(facultySel.value, yearSel.value, partSel.value);
     }
     partSel.onchange = function () {
         subjectSel.innerHTML = "";
         subjectSel.options[0] = new Option("Subject", "");
         if (yearSel.value === "") return;
         //display correct values
         updateSubjects(facultySel.value, yearSel.value, partSel.value);
     }

 }