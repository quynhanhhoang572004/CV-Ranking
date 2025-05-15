grammar JSONMatcher;
program: json;
json: jsonObject | array;


multLine: (string COLON value) (COMMA (string COLON value))+;

multString: string (COMMA string)*;
jsonObject: OPEN_CURLY multLine CLOSE_CURLY;

value: string | number | array | jsonObject;

array: OPEN_SQUARE multValue? CLOSE_SQUARE;
multValue: value (COMMA value)*;

string: PARATHESIS ID+ PARATHESIS;
number: INT | FLOAT;


OPEN_CURLY: '{';
CLOSE_CURLY: '}';
OPEN_SQUARE: '[';
CLOSE_SQUARE: ']';
PARATHESIS: '"';
COMMA: ',';
COLON: ':';


INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
ID: ~[ \t\r\n"]+; 

WS: [ \t\r\n]+ -> skip ;
