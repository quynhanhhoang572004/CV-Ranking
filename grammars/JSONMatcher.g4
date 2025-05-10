grammar JSONMatcher;
program: json;
json: jsonObject | array;

jsonObject: OPEN_CURLY multLine? CLOSE_CURLY;

array: OPEN_SQUARE multString? CLOSE_SQUARE;

multLine: line (COMMA line)*;
line: string COLON (string | number | array | jsonObject);

multString: string (COMMA string)*;
string: PARATHESIS ID+ PARATHESIS;
OPEN_CURLY: '{';
CLOSE_CURLY: '}';
OPEN_SQUARE: '[';
CLOSE_SQUARE: ']';
PARATHESIS: '"';
COMMA: ',';
COLON: ':';


number: INT | FLOAT;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
ID: ~[ \t\r\n"]+; 

WS: [ \t\r\n]+ -> skip ;
