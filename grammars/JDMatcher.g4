grammar JDMatcher;

program: jobDescription;

jobDescription: CONST_START requirePosition requireLevel requireTechnicalSkills DOT requireEducation
                (DOT requireLanguage)? (DOT requireExperience)? (DOT requireActivites)? (DOT requireReferences)?;

requirePosition: POSITION;
requireLevel: LEVEL;
requireTechnicalSkills: CONST_STACK requireTools SEMICOLON requireProLang SEMICOLON requireFrameworks SEMICOLON requireDB;
requireEducation: CONST_EDU requireMajor requireDegree? requireGPA?;
requireMajor: MAJOR;
requireDegree: DEGREE;
requireGPA: CONST_GPA COMPARATOR FLOAT;
requireLanguage: CONST_LANG LANGUAGE;
requireExperience: INT 'years of experience';
requireActivites: ID+;
requireReferences: ID+; 

requireTools: CONST_TOOL ID+;
requireProLang: CONST_PRO_LANG ID+;
requireFrameworks: CONST_FRAMEWORK ID+;
requireDB: CONST_DB ID+;


//Constants
CONST_START: 'we are looking for a/an ';
CONST_STACK: 'whose stack is: ';
CONST_EDU: 'education should be: ';
CONST_LANG: 'they should know ';
CONST_ACT: 'desired activities: '; 
CONST_EXP: 'candidate should have ';
CONST_REF: 'candidate should be referred from ';
CONST_TOOL: 'tools:';
CONST_PRO_LANG: 'programming languages: ';
CONST_FRAMEWORK: 'framework libraries: ';
CONST_DB: 'databases cloud services: ';
CONST_GPA: 'gpa';
DOT: '. ';
SEMICOLON: ';';

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
ID: [a-zA-Z_\-]+;
WS: [ \t\r\n]+ -> skip ;
