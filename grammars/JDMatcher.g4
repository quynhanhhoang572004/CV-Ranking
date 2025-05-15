grammar JDMatcher;

program: listCV | jd | show_X_best | showConditional;

listCV: LIST_CV POSITION;

showConditional: SHOW_CV_WITH (requirePosition | requireLevel 
             | requireTools | requireProLang | requireFrameworks | requireDB
             | requireDegree | requireGPA | requireExperience | requireLanguage
             | requireActivites | requireReferences);

show_X_best: SHOW_TOP INT BEST_FOR POSITION;

jd: requirements (preferences)?;
requirements: REQUIRE_SECTION OPEN_CURLY 
                requirePosition requireLevel requireTechnicalSkills 
                requireEducation requireExperience requireLanguage? 
                requireActivites? requireReferences? CLOSE_CURLY;
preferences: PREFER_SECTION OPEN_CURLY requireTools? requireProLang? requireFrameworks? requireDB?
             requireDegree? requireGPA?
             requireExperience? requireLanguage? 
             requireActivites? requireReferences? CLOSE_CURLY;


//Compulsory

requirePosition: POSITION_LABEL POSITION;
requireLevel: LEVEL_LABEL LEVEL;
requireTechnicalSkills: STACK_SECTION OPEN_CURLY requireTools requireProLang requireFrameworks? requireDB? CLOSE_CURLY;
requireTools: TOOL_LABEL ID+;
requireProLang: PROG_LANG_LABEL ID+;
requireFrameworks: FRAMEWORK_LABEL ID+;
requireDB: DATA_LABEL ID+;
requireEducation: EDU_SECTION OPEN_CURLY requireMajor requireDegree? requireGPA? CLOSE_CURLY;
requireMajor: MAJOR_LABEL MAJOR;
requireDegree: DEGREE_LABEL DEGREE;
requireGPA: GPA_LABEL COMPARATOR FLOAT;
requireExperience: EXP_LABEL INT 'years';


//Optional

requireLanguage: LANG_LABEL LANGUAGE;
requireActivites: ACTIVITY_LABEL ID+;
requireReferences: REF_LABEL ID+; 


//Constants:

LIST_CV: 'list all CVs for job';
SHOW_TOP: 'show top';
SHOW_CV_WITH: 'show CV with';
BEST_FOR: 'best CV for';

REQUIRE_SECTION: 'REQUIREMENTS'; 
PREFER_SECTION: 'PREFERENCES'; 
POSITION_LABEL: 'position:';
LEVEL_LABEL: 'level:';
STACK_SECTION: 'stack';
EDU_SECTION: 'education';
LANG_LABEL: 'language:';
ACTIVITY_LABEL: 'activities:'; 
EXP_LABEL: 'experience:';
REF_LABEL: 'references:';
TOOL_LABEL: 'tools:';
PROG_LANG_LABEL: 'programming languages:';
FRAMEWORK_LABEL: 'framework libraries:';
DATA_LABEL: 'databases cloud services:';
MAJOR_LABEL: 'major:';
DEGREE_LABEL: 'degree:';
GPA_LABEL: 'gpa:';

OPEN_CURLY: '{';
CLOSE_CURLY: '}';


//Variables 
POSITION: 
'frontend developer' | 'backend developer' | 'full-stack developer' | 'software engineer' |
'ai engineer' | 'ml engineer' | 'data scientist' | 'data engineer' | 'data analyst' |
'qa/qc engineer' |'tester' | 'security engineer' | 'devops engineer' | 'cloud engineer' |
'network engineer' | 'embedded engineer' | 'mobile developer' | 'android developer' |'ios developer' |
'solution architect' | 'technical lead' | 'product manager' | 'scrum master' | 'game developer' |
'blockchain developer' | 'research engineer';

LEVEL: 'intern' | 'fresher' | 'junior' | 'medium' | 'senior' | 'director' | 'manager';

DEGREE: 'bachelor' | 'engineering' | 'master' | 'phd';

MAJOR: 'computer science' | 'computer engineering' | 'network engineering' | 'data science'|
'artificial intelligence' | 'cybersecurity' | 'information systems';

COMPARATOR: '>' | '>=';

LANGUAGE:'english' | 'japanese' | 'chinese' | 'korean'| 'german' | 'portugeese' | 'french';

INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
ID: ~[ \t\r\n{}]+; 
WS: [ \t\r\n]+ -> skip ;

