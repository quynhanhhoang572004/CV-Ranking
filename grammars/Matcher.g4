grammar Matcher;

matchBlock: 'match' '{' matchRule+ '}' ;

matchRule
    : requireRule
    | preferRule
    | scoreRule
    ;

requireRule: 'require' 'skill' STRING ;
preferRule: 'prefer' 'skill' STRING 'weight' INT ;
scoreRule: 'if' condition 'then' scoreAction ;

condition: IDENTIFIER '.' IDENTIFIER comparator value ;
scoreAction: 'score' ('+'|'-') INT ;

comparator: '==' | '>=' | '<=' ;
value: STRING | INT ;

STRING: '"' .*? '"' ;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;
INT: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
