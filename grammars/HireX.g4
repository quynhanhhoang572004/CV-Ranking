grammar HireX;

program: jd | showConditional;

//QUERIES COMMAND
showConditional: SHOW CV WITH condition;

condition: requireName | requireTools | requireProLang | requireFrameworks | requireDB
             | requireDegree | requireMajor | requireGPA | requireExperience | requireLanguage ;

//INPUT JD COMMAND
jd: requirements preferences?;

requirements: REQUIRE_SECTION OPEN_CURLY 
                requirePosition requireLevel requireTechnicalSkills 
                requireEducation requireExperience requireLanguage? CLOSE_CURLY;
preferences: PREFER_SECTION OPEN_CURLY requireTools? requireProLang? requireFrameworks? requireDB? 
             requireDegree? requireGPA?
             requireExperience? requireLanguage? 
             requireActivites? CLOSE_CURLY;

requirePosition: POSITION_LABEL position;
requireLevel: LEVEL_LABEL level;

requireTechnicalSkills: STACK_SECTION OPEN_CURLY requireTools requireProLang requireFrameworks requireDB CLOSE_CURLY;
requireTools: TOOL_LABEL tool (COMMA tool)*;
requireProLang: PROG_LANG_LABEL proLang (COMMA proLang)*;
requireFrameworks: FRAMEWORK_LABEL framework (COMMA framework)*;
requireDB: DATA_LABEL db (COMMA db)*;

requireEducation: EDU_SECTION OPEN_CURLY requireMajor requireDegree? requireGPA? CLOSE_CURLY;
requireMajor: MAJOR_LABEL major;
requireDegree: DEGREE_LABEL degree;
requireGPA: GPA_LABEL COMPARATOR FLOAT;

requireLanguage: LANG_LABEL lang (COMMA lang)*;

requireExperience: EXP_LABEL COMPARATOR INT YEARS;

requireActivites: ACTIVITY_LABEL ID+;

requireName: NAME_LABEL ID+;

//CONSTANTS
REQUIRE_SECTION: 'REQUIREMENTS'; 
PREFER_SECTION: 'PREFERENCES'; 
STACK_SECTION: 'stack';
EDU_SECTION: 'education';

POSITION_LABEL: 'position:';
LEVEL_LABEL: 'level:';
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
NAME_LABEL: 'name: ';

YEARS: 'years';
SHOW: 'show';
CV: 'CV' | 'cv';
WITH: 'with';
OPEN_CURLY: '{';
CLOSE_CURLY: '}';
COMMA: ',';


position: 'frontend developer' | 'backend developer' | 'full-stack developer' | 'software engineer' |
'ai engineer' | 'ml engineer' | 'data scientist' | 'data engineer' | 'data analyst' |
'qa/qc engineer' |'tester' | 'security engineer' | 'devops engineer' | 'cloud engineer' |
'network engineer' | 'embedded engineer' | 'mobile developer' | 'android developer' |'ios developer' |
'solution architect' | 'technical lead' | 'product manager' | 'scrum master' | 'game developer' |
'blockchain developer' | 'research engineer';

level: 'intern' | 'fresher' | 'junior' | 'medium' | 'senior' | 'director' | 'manager';
degree: 'bachelor' | 'engineering' | 'master' | 'phd';
major: 'computer science' | 'computer engineering' | 'network engineering' | 'data science'|
'artificial intelligence' | 'cybersecurity' | 'information systems';

tool: 'git' | 'docker' | 'kubernetes' | 'jenkins' | 'jira' | 'postman' | 'webpack' | 'npm' |
'yarn' | 'vscode' | 'intellij' | 'eclipse' | 'figma' | 'trello' | 'slack' | 'notion' |
 'aws cli' | 'gcp sdk' | 'azure cli' | 'terraform' | 'github actions';
proLang: 'python' | 'java' | 'c' | 'c++' | 'c#' | 'go' | 'rust' | 'javascript' | 'typescript' |
'ruby' | 'php' | 'swift' | 'kotlin' | 'scala' | 'r' | 'matlab' | 'bash' | 'sql' |
'haskell' | 'perl';
framework: 'pytorch' | 'tensorflow' | 'keras' | 'scikit-learn' | 'xgboost' | 'lightgbm' |
'opencv' | 'flask' | 'django' | 'spring' | 'express' | 'fastapi' |
'next.js' | 'nuxt.js' | 'react' | 'vue' | 'angular' | 'bootstrap' |
'laravel' | '.net' | 'asp.net' | 'electron' | 'flutter' | 'react native' |
<<<<<<< HEAD:grammars/Hire.g4
'node.js' | 'nestjs' | 'redux' | 'mui' | 'tailwindcss' | 'springboot';
=======
'node.js' | 'nestjs' | 'redux' | 'mui' | 'tailwindcss' | 'springboot'| 'pandas'| 'numpy';
>>>>>>> 669bff4db38c56335aeba01ab85b99207d85c14b:grammars/HireX.g4
db: 'mysql' | 'postgresql' | 'sqlite' | 'mongodb' | 'redis' | 'mariadb' |
'oracle' | 'sql server' | 'dynamodb' | 'cassandra' | 'elasticsearch' |
'aws' | 'azure' | 'gcp' | 'google cloud' | 'amazon web services' |
'firebase' | 'heroku' | 'digitalocean' | 'vercel' | 'netlify';

lang:'english' | 'japanese' | 'chinese' | 'korean'| 'german' | 'portugeese' | 'french';

COMPARATOR: '>' | '>=';
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
ID: [a-zA-Z_\-.]+;
WS: [ \t\r\n]+ -> skip ;
