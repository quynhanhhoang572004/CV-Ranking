grammar cv_scan;

document: section+;
section: heading paragraph+;
heading: '#' TEXT NEWLINE;
paragraph: TEXT+;

TEXT: ~[\r\n#]+;
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip;
