# Generated from grammars\HireX.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00b1")
        buf.write("\u00f6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\5\2A\n\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4R\n\4\3\5\3\5\5")
        buf.write("\5V\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6`\n\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\5\7g\n\7\3\7\5\7j\n\7\3\7\5\7m\n\7\3\7")
        buf.write("\5\7p\n\7\3\7\5\7s\n\7\3\7\5\7v\n\7\3\7\5\7y\n\7\3\7\5")
        buf.write("\7|\n\7\3\7\5\7\177\n\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\7\13\u0095\n\13\f\13\16\13\u0098\13\13\3\f\3\f\3\f\3")
        buf.write("\f\7\f\u009e\n\f\f\f\16\f\u00a1\13\f\3\r\3\r\3\r\3\r\7")
        buf.write("\r\u00a7\n\r\f\r\16\r\u00aa\13\r\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u00b0\n\16\f\16\16\16\u00b3\13\16\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u00b9\n\17\3\17\5\17\u00bc\n\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\7\23\u00ce\n\23\f\23\16\23\u00d1\13\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\6\25\u00da\n\25\r\25\16")
        buf.write("\25\u00db\3\26\3\26\6\26\u00e0\n\26\r\26\16\26\u00e1\3")
        buf.write("\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\2\2 \2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<\2\13\3\2\3\34\3\2\35#\3\2$\'\3\2(.\3\2/C\3\2DW\3\2")
        buf.write("Xw\3\2x\u008c\3\2\u008d\u0093\2\u00f5\2@\3\2\2\2\4B\3")
        buf.write("\2\2\2\6Q\3\2\2\2\bS\3\2\2\2\nW\3\2\2\2\fc\3\2\2\2\16")
        buf.write("\u0082\3\2\2\2\20\u0085\3\2\2\2\22\u0088\3\2\2\2\24\u0090")
        buf.write("\3\2\2\2\26\u0099\3\2\2\2\30\u00a2\3\2\2\2\32\u00ab\3")
        buf.write("\2\2\2\34\u00b4\3\2\2\2\36\u00bf\3\2\2\2 \u00c2\3\2\2")
        buf.write("\2\"\u00c5\3\2\2\2$\u00c9\3\2\2\2&\u00d2\3\2\2\2(\u00d7")
        buf.write("\3\2\2\2*\u00dd\3\2\2\2,\u00e3\3\2\2\2.\u00e5\3\2\2\2")
        buf.write("\60\u00e7\3\2\2\2\62\u00e9\3\2\2\2\64\u00eb\3\2\2\2\66")
        buf.write("\u00ed\3\2\2\28\u00ef\3\2\2\2:\u00f1\3\2\2\2<\u00f3\3")
        buf.write("\2\2\2>A\5\b\5\2?A\5\4\3\2@>\3\2\2\2@?\3\2\2\2A\3\3\2")
        buf.write("\2\2BC\7\u00a7\2\2CD\7\u00a8\2\2DE\7\u00a9\2\2EF\5\6\4")
        buf.write("\2F\5\3\2\2\2GR\5*\26\2HR\5\24\13\2IR\5\26\f\2JR\5\30")
        buf.write("\r\2KR\5\32\16\2LR\5 \21\2MR\5\36\20\2NR\5\"\22\2OR\5")
        buf.write("&\24\2PR\5$\23\2QG\3\2\2\2QH\3\2\2\2QI\3\2\2\2QJ\3\2\2")
        buf.write("\2QK\3\2\2\2QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2Q")
        buf.write("P\3\2\2\2R\7\3\2\2\2SU\5\n\6\2TV\5\f\7\2UT\3\2\2\2UV\3")
        buf.write("\2\2\2V\t\3\2\2\2WX\7\u0094\2\2XY\7\u00aa\2\2YZ\5\16\b")
        buf.write("\2Z[\5\20\t\2[\\\5\22\n\2\\]\5\34\17\2]_\5&\24\2^`\5$")
        buf.write("\23\2_^\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\u00ab\2\2b\13")
        buf.write("\3\2\2\2cd\7\u0095\2\2df\7\u00aa\2\2eg\5\24\13\2fe\3\2")
        buf.write("\2\2fg\3\2\2\2gi\3\2\2\2hj\5\26\f\2ih\3\2\2\2ij\3\2\2")
        buf.write("\2jl\3\2\2\2km\5\30\r\2lk\3\2\2\2lm\3\2\2\2mo\3\2\2\2")
        buf.write("np\5\32\16\2on\3\2\2\2op\3\2\2\2pr\3\2\2\2qs\5 \21\2r")
        buf.write("q\3\2\2\2rs\3\2\2\2su\3\2\2\2tv\5\"\22\2ut\3\2\2\2uv\3")
        buf.write("\2\2\2vx\3\2\2\2wy\5&\24\2xw\3\2\2\2xy\3\2\2\2y{\3\2\2")
        buf.write("\2z|\5$\23\2{z\3\2\2\2{|\3\2\2\2|~\3\2\2\2}\177\5(\25")
        buf.write("\2~}\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081")
        buf.write("\7\u00ab\2\2\u0081\r\3\2\2\2\u0082\u0083\7\u0098\2\2\u0083")
        buf.write("\u0084\5,\27\2\u0084\17\3\2\2\2\u0085\u0086\7\u0099\2")
        buf.write("\2\u0086\u0087\5.\30\2\u0087\21\3\2\2\2\u0088\u0089\7")
        buf.write("\u0096\2\2\u0089\u008a\7\u00aa\2\2\u008a\u008b\5\24\13")
        buf.write("\2\u008b\u008c\5\26\f\2\u008c\u008d\5\30\r\2\u008d\u008e")
        buf.write("\5\32\16\2\u008e\u008f\7\u00ab\2\2\u008f\23\3\2\2\2\u0090")
        buf.write("\u0091\7\u009e\2\2\u0091\u0096\5\64\33\2\u0092\u0093\7")
        buf.write("\u00ac\2\2\u0093\u0095\5\64\33\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\25\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\7\u009f")
        buf.write("\2\2\u009a\u009f\5\66\34\2\u009b\u009c\7\u00ac\2\2\u009c")
        buf.write("\u009e\5\66\34\2\u009d\u009b\3\2\2\2\u009e\u00a1\3\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\27\3")
        buf.write("\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\u00a0\2\2\u00a3")
        buf.write("\u00a8\58\35\2\u00a4\u00a5\7\u00ac\2\2\u00a5\u00a7\58")
        buf.write("\35\2\u00a6\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\31\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\7\u00a1\2\2\u00ac\u00b1\5:\36\2\u00ad")
        buf.write("\u00ae\7\u00ac\2\2\u00ae\u00b0\5:\36\2\u00af\u00ad\3\2")
        buf.write("\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\33\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5")
        buf.write("\7\u0097\2\2\u00b5\u00b6\7\u00aa\2\2\u00b6\u00b8\5\36")
        buf.write("\20\2\u00b7\u00b9\5 \21\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00bc\5\"\22\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00be\7\u00ab\2\2\u00be\35\3\2\2\2\u00bf\u00c0")
        buf.write("\7\u00a2\2\2\u00c0\u00c1\5\62\32\2\u00c1\37\3\2\2\2\u00c2")
        buf.write("\u00c3\7\u00a3\2\2\u00c3\u00c4\5\60\31\2\u00c4!\3\2\2")
        buf.write("\2\u00c5\u00c6\7\u00a4\2\2\u00c6\u00c7\7\u00ad\2\2\u00c7")
        buf.write("\u00c8\7\u00af\2\2\u00c8#\3\2\2\2\u00c9\u00ca\7\u009a")
        buf.write("\2\2\u00ca\u00cf\5<\37\2\u00cb\u00cc\7\u00ac\2\2\u00cc")
        buf.write("\u00ce\5<\37\2\u00cd\u00cb\3\2\2\2\u00ce\u00d1\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0%\3\2\2")
        buf.write("\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\7\u009c\2\2\u00d3\u00d4")
        buf.write("\7\u00ad\2\2\u00d4\u00d5\7\u00ae\2\2\u00d5\u00d6\7\u00a6")
        buf.write("\2\2\u00d6\'\3\2\2\2\u00d7\u00d9\7\u009b\2\2\u00d8\u00da")
        buf.write("\7\u00b0\2\2\u00d9\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc)\3\2\2\2\u00dd")
        buf.write("\u00df\7\u00a5\2\2\u00de\u00e0\7\u00b0\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2+\3\2\2\2\u00e3\u00e4\t\2\2\2\u00e4")
        buf.write("-\3\2\2\2\u00e5\u00e6\t\3\2\2\u00e6/\3\2\2\2\u00e7\u00e8")
        buf.write("\t\4\2\2\u00e8\61\3\2\2\2\u00e9\u00ea\t\5\2\2\u00ea\63")
        buf.write("\3\2\2\2\u00eb\u00ec\t\6\2\2\u00ec\65\3\2\2\2\u00ed\u00ee")
        buf.write("\t\7\2\2\u00ee\67\3\2\2\2\u00ef\u00f0\t\b\2\2\u00f09\3")
        buf.write("\2\2\2\u00f1\u00f2\t\t\2\2\u00f2;\3\2\2\2\u00f3\u00f4")
        buf.write("\t\n\2\2\u00f4=\3\2\2\2\30@QU_filorux{~\u0096\u009f\u00a8")
        buf.write("\u00b1\u00b8\u00bb\u00cf\u00db\u00e1")
        return buf.getvalue()


class HireXParser ( Parser ):

    grammarFileName = "HireX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'frontend developer'", "'backend developer'", 
                     "'full-stack developer'", "'software engineer'", "'ai engineer'", 
                     "'ml engineer'", "'data scientist'", "'data engineer'", 
                     "'data analyst'", "'qa/qc engineer'", "'tester'", "'security engineer'", 
                     "'devops engineer'", "'cloud engineer'", "'network engineer'", 
                     "'embedded engineer'", "'mobile developer'", "'android developer'", 
                     "'ios developer'", "'solution architect'", "'technical lead'", 
                     "'product manager'", "'scrum master'", "'game developer'", 
                     "'blockchain developer'", "'research engineer'", "'intern'", 
                     "'fresher'", "'junior'", "'medium'", "'senior'", "'director'", 
                     "'manager'", "'bachelor'", "'engineering'", "'master'", 
                     "'phd'", "'computer science'", "'computer engineering'", 
                     "'network engineering'", "'data science'", "'artificial intelligence'", 
                     "'cybersecurity'", "'information systems'", "'git'", 
                     "'docker'", "'kubernetes'", "'jenkins'", "'jira'", 
                     "'postman'", "'webpack'", "'npm'", "'yarn'", "'vscode'", 
                     "'intellij'", "'eclipse'", "'figma'", "'trello'", "'slack'", 
                     "'notion'", "'aws cli'", "'gcp sdk'", "'azure cli'", 
                     "'terraform'", "'github actions'", "'python'", "'java'", 
                     "'c'", "'c++'", "'c#'", "'go'", "'rust'", "'javascript'", 
                     "'typescript'", "'ruby'", "'php'", "'swift'", "'kotlin'", 
                     "'scala'", "'r'", "'matlab'", "'bash'", "'sql'", "'haskell'", 
                     "'perl'", "'pytorch'", "'tensorflow'", "'keras'", "'scikit-learn'", 
                     "'xgboost'", "'lightgbm'", "'opencv'", "'flask'", "'django'", 
                     "'spring'", "'express'", "'fastapi'", "'next.js'", 
                     "'nuxt.js'", "'react'", "'vue'", "'angular'", "'bootstrap'", 
                     "'laravel'", "'.net'", "'asp.net'", "'electron'", "'flutter'", 
                     "'react native'", "'node.js'", "'nestjs'", "'redux'", 
                     "'mui'", "'tailwindcss'", "'springboot'", "'pandas'", 
                     "'numpy'", "'mysql'", "'postgresql'", "'sqlite'", "'mongodb'", 
                     "'redis'", "'mariadb'", "'oracle'", "'sql server'", 
                     "'dynamodb'", "'cassandra'", "'elasticsearch'", "'aws'", 
                     "'azure'", "'gcp'", "'google cloud'", "'amazon web services'", 
                     "'firebase'", "'heroku'", "'digitalocean'", "'vercel'", 
                     "'netlify'", "'english'", "'japanese'", "'chinese'", 
                     "'korean'", "'german'", "'portugeese'", "'french'", 
                     "'REQUIREMENTS'", "'PREFERENCES'", "'stack'", "'education'", 
                     "'position:'", "'level:'", "'language:'", "'activities:'", 
                     "'experience:'", "'references:'", "'tools:'", "'programming languages:'", 
                     "'framework libraries:'", "'databases cloud services:'", 
                     "'major:'", "'degree:'", "'gpa:'", "'name: '", "'years'", 
                     "'show'", "<INVALID>", "'with'", "'{'", "'}'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "REQUIRE_SECTION", "PREFER_SECTION", 
                      "STACK_SECTION", "EDU_SECTION", "POSITION_LABEL", 
                      "LEVEL_LABEL", "LANG_LABEL", "ACTIVITY_LABEL", "EXP_LABEL", 
                      "REF_LABEL", "TOOL_LABEL", "PROG_LANG_LABEL", "FRAMEWORK_LABEL", 
                      "DATA_LABEL", "MAJOR_LABEL", "DEGREE_LABEL", "GPA_LABEL", 
                      "NAME_LABEL", "YEARS", "SHOW", "CV", "WITH", "OPEN_CURLY", 
                      "CLOSE_CURLY", "COMMA", "COMPARATOR", "INT", "FLOAT", 
                      "ID", "WS" ]

    RULE_program = 0
    RULE_showConditional = 1
    RULE_condition = 2
    RULE_jd = 3
    RULE_requirements = 4
    RULE_preferences = 5
    RULE_requirePosition = 6
    RULE_requireLevel = 7
    RULE_requireTechnicalSkills = 8
    RULE_requireTools = 9
    RULE_requireProLang = 10
    RULE_requireFrameworks = 11
    RULE_requireDB = 12
    RULE_requireEducation = 13
    RULE_requireMajor = 14
    RULE_requireDegree = 15
    RULE_requireGPA = 16
    RULE_requireLanguage = 17
    RULE_requireExperience = 18
    RULE_requireActivites = 19
    RULE_requireName = 20
    RULE_position = 21
    RULE_level = 22
    RULE_degree = 23
    RULE_major = 24
    RULE_tool = 25
    RULE_proLang = 26
    RULE_framework = 27
    RULE_db = 28
    RULE_lang = 29

    ruleNames =  [ "program", "showConditional", "condition", "jd", "requirements", 
                   "preferences", "requirePosition", "requireLevel", "requireTechnicalSkills", 
                   "requireTools", "requireProLang", "requireFrameworks", 
                   "requireDB", "requireEducation", "requireMajor", "requireDegree", 
                   "requireGPA", "requireLanguage", "requireExperience", 
                   "requireActivites", "requireName", "position", "level", 
                   "degree", "major", "tool", "proLang", "framework", "db", 
                   "lang" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    T__79=80
    T__80=81
    T__81=82
    T__82=83
    T__83=84
    T__84=85
    T__85=86
    T__86=87
    T__87=88
    T__88=89
    T__89=90
    T__90=91
    T__91=92
    T__92=93
    T__93=94
    T__94=95
    T__95=96
    T__96=97
    T__97=98
    T__98=99
    T__99=100
    T__100=101
    T__101=102
    T__102=103
    T__103=104
    T__104=105
    T__105=106
    T__106=107
    T__107=108
    T__108=109
    T__109=110
    T__110=111
    T__111=112
    T__112=113
    T__113=114
    T__114=115
    T__115=116
    T__116=117
    T__117=118
    T__118=119
    T__119=120
    T__120=121
    T__121=122
    T__122=123
    T__123=124
    T__124=125
    T__125=126
    T__126=127
    T__127=128
    T__128=129
    T__129=130
    T__130=131
    T__131=132
    T__132=133
    T__133=134
    T__134=135
    T__135=136
    T__136=137
    T__137=138
    T__138=139
    T__139=140
    T__140=141
    T__141=142
    T__142=143
    T__143=144
    T__144=145
    REQUIRE_SECTION=146
    PREFER_SECTION=147
    STACK_SECTION=148
    EDU_SECTION=149
    POSITION_LABEL=150
    LEVEL_LABEL=151
    LANG_LABEL=152
    ACTIVITY_LABEL=153
    EXP_LABEL=154
    REF_LABEL=155
    TOOL_LABEL=156
    PROG_LANG_LABEL=157
    FRAMEWORK_LABEL=158
    DATA_LABEL=159
    MAJOR_LABEL=160
    DEGREE_LABEL=161
    GPA_LABEL=162
    NAME_LABEL=163
    YEARS=164
    SHOW=165
    CV=166
    WITH=167
    OPEN_CURLY=168
    CLOSE_CURLY=169
    COMMA=170
    COMPARATOR=171
    INT=172
    FLOAT=173
    ID=174
    WS=175

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def jd(self):
            return self.getTypedRuleContext(HireXParser.JdContext,0)


        def showConditional(self):
            return self.getTypedRuleContext(HireXParser.ShowConditionalContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_program




    def program(self):

        localctx = HireXParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HireXParser.REQUIRE_SECTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.jd()
                pass
            elif token in [HireXParser.SHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.showConditional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(HireXParser.SHOW, 0)

        def CV(self):
            return self.getToken(HireXParser.CV, 0)

        def WITH(self):
            return self.getToken(HireXParser.WITH, 0)

        def condition(self):
            return self.getTypedRuleContext(HireXParser.ConditionContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_showConditional




    def showConditional(self):

        localctx = HireXParser.ShowConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_showConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(HireXParser.SHOW)
            self.state = 65
            self.match(HireXParser.CV)
            self.state = 66
            self.match(HireXParser.WITH)
            self.state = 67
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requireName(self):
            return self.getTypedRuleContext(HireXParser.RequireNameContext,0)


        def requireTools(self):
            return self.getTypedRuleContext(HireXParser.RequireToolsContext,0)


        def requireProLang(self):
            return self.getTypedRuleContext(HireXParser.RequireProLangContext,0)


        def requireFrameworks(self):
            return self.getTypedRuleContext(HireXParser.RequireFrameworksContext,0)


        def requireDB(self):
            return self.getTypedRuleContext(HireXParser.RequireDBContext,0)


        def requireDegree(self):
            return self.getTypedRuleContext(HireXParser.RequireDegreeContext,0)


        def requireMajor(self):
            return self.getTypedRuleContext(HireXParser.RequireMajorContext,0)


        def requireGPA(self):
            return self.getTypedRuleContext(HireXParser.RequireGPAContext,0)


        def requireExperience(self):
            return self.getTypedRuleContext(HireXParser.RequireExperienceContext,0)


        def requireLanguage(self):
            return self.getTypedRuleContext(HireXParser.RequireLanguageContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_condition




    def condition(self):

        localctx = HireXParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HireXParser.NAME_LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.requireName()
                pass
            elif token in [HireXParser.TOOL_LABEL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.requireTools()
                pass
            elif token in [HireXParser.PROG_LANG_LABEL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.requireProLang()
                pass
            elif token in [HireXParser.FRAMEWORK_LABEL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.requireFrameworks()
                pass
            elif token in [HireXParser.DATA_LABEL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.requireDB()
                pass
            elif token in [HireXParser.DEGREE_LABEL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.requireDegree()
                pass
            elif token in [HireXParser.MAJOR_LABEL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.requireMajor()
                pass
            elif token in [HireXParser.GPA_LABEL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.requireGPA()
                pass
            elif token in [HireXParser.EXP_LABEL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 77
                self.requireExperience()
                pass
            elif token in [HireXParser.LANG_LABEL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 78
                self.requireLanguage()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirements(self):
            return self.getTypedRuleContext(HireXParser.RequirementsContext,0)


        def preferences(self):
            return self.getTypedRuleContext(HireXParser.PreferencesContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_jd




    def jd(self):

        localctx = HireXParser.JdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_jd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.requirements()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.PREFER_SECTION:
                self.state = 82
                self.preferences()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIRE_SECTION(self):
            return self.getToken(HireXParser.REQUIRE_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireXParser.OPEN_CURLY, 0)

        def requirePosition(self):
            return self.getTypedRuleContext(HireXParser.RequirePositionContext,0)


        def requireLevel(self):
            return self.getTypedRuleContext(HireXParser.RequireLevelContext,0)


        def requireTechnicalSkills(self):
            return self.getTypedRuleContext(HireXParser.RequireTechnicalSkillsContext,0)


        def requireEducation(self):
            return self.getTypedRuleContext(HireXParser.RequireEducationContext,0)


        def requireExperience(self):
            return self.getTypedRuleContext(HireXParser.RequireExperienceContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(HireXParser.CLOSE_CURLY, 0)

        def requireLanguage(self):
            return self.getTypedRuleContext(HireXParser.RequireLanguageContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_requirements




    def requirements(self):

        localctx = HireXParser.RequirementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_requirements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(HireXParser.REQUIRE_SECTION)
            self.state = 86
            self.match(HireXParser.OPEN_CURLY)
            self.state = 87
            self.requirePosition()
            self.state = 88
            self.requireLevel()
            self.state = 89
            self.requireTechnicalSkills()
            self.state = 90
            self.requireEducation()
            self.state = 91
            self.requireExperience()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.LANG_LABEL:
                self.state = 92
                self.requireLanguage()


            self.state = 95
            self.match(HireXParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreferencesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFER_SECTION(self):
            return self.getToken(HireXParser.PREFER_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireXParser.OPEN_CURLY, 0)

        def CLOSE_CURLY(self):
            return self.getToken(HireXParser.CLOSE_CURLY, 0)

        def requireTools(self):
            return self.getTypedRuleContext(HireXParser.RequireToolsContext,0)


        def requireProLang(self):
            return self.getTypedRuleContext(HireXParser.RequireProLangContext,0)


        def requireFrameworks(self):
            return self.getTypedRuleContext(HireXParser.RequireFrameworksContext,0)


        def requireDB(self):
            return self.getTypedRuleContext(HireXParser.RequireDBContext,0)


        def requireDegree(self):
            return self.getTypedRuleContext(HireXParser.RequireDegreeContext,0)


        def requireGPA(self):
            return self.getTypedRuleContext(HireXParser.RequireGPAContext,0)


        def requireExperience(self):
            return self.getTypedRuleContext(HireXParser.RequireExperienceContext,0)


        def requireLanguage(self):
            return self.getTypedRuleContext(HireXParser.RequireLanguageContext,0)


        def requireActivites(self):
            return self.getTypedRuleContext(HireXParser.RequireActivitesContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_preferences




    def preferences(self):

        localctx = HireXParser.PreferencesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_preferences)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(HireXParser.PREFER_SECTION)
            self.state = 98
            self.match(HireXParser.OPEN_CURLY)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.TOOL_LABEL:
                self.state = 99
                self.requireTools()


            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.PROG_LANG_LABEL:
                self.state = 102
                self.requireProLang()


            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.FRAMEWORK_LABEL:
                self.state = 105
                self.requireFrameworks()


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.DATA_LABEL:
                self.state = 108
                self.requireDB()


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.DEGREE_LABEL:
                self.state = 111
                self.requireDegree()


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.GPA_LABEL:
                self.state = 114
                self.requireGPA()


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.EXP_LABEL:
                self.state = 117
                self.requireExperience()


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.LANG_LABEL:
                self.state = 120
                self.requireLanguage()


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.ACTIVITY_LABEL:
                self.state = 123
                self.requireActivites()


            self.state = 126
            self.match(HireXParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirePositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITION_LABEL(self):
            return self.getToken(HireXParser.POSITION_LABEL, 0)

        def position(self):
            return self.getTypedRuleContext(HireXParser.PositionContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_requirePosition




    def requirePosition(self):

        localctx = HireXParser.RequirePositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_requirePosition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(HireXParser.POSITION_LABEL)
            self.state = 129
            self.position()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireLevelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEVEL_LABEL(self):
            return self.getToken(HireXParser.LEVEL_LABEL, 0)

        def level(self):
            return self.getTypedRuleContext(HireXParser.LevelContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_requireLevel




    def requireLevel(self):

        localctx = HireXParser.RequireLevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_requireLevel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(HireXParser.LEVEL_LABEL)
            self.state = 132
            self.level()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireTechnicalSkillsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACK_SECTION(self):
            return self.getToken(HireXParser.STACK_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireXParser.OPEN_CURLY, 0)

        def requireTools(self):
            return self.getTypedRuleContext(HireXParser.RequireToolsContext,0)


        def requireProLang(self):
            return self.getTypedRuleContext(HireXParser.RequireProLangContext,0)


        def requireFrameworks(self):
            return self.getTypedRuleContext(HireXParser.RequireFrameworksContext,0)


        def requireDB(self):
            return self.getTypedRuleContext(HireXParser.RequireDBContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(HireXParser.CLOSE_CURLY, 0)

        def getRuleIndex(self):
            return HireXParser.RULE_requireTechnicalSkills




    def requireTechnicalSkills(self):

        localctx = HireXParser.RequireTechnicalSkillsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_requireTechnicalSkills)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(HireXParser.STACK_SECTION)
            self.state = 135
            self.match(HireXParser.OPEN_CURLY)
            self.state = 136
            self.requireTools()
            self.state = 137
            self.requireProLang()
            self.state = 138
            self.requireFrameworks()
            self.state = 139
            self.requireDB()
            self.state = 140
            self.match(HireXParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireToolsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOL_LABEL(self):
            return self.getToken(HireXParser.TOOL_LABEL, 0)

        def tool(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireXParser.ToolContext)
            else:
                return self.getTypedRuleContext(HireXParser.ToolContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.COMMA)
            else:
                return self.getToken(HireXParser.COMMA, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireTools




    def requireTools(self):

        localctx = HireXParser.RequireToolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_requireTools)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(HireXParser.TOOL_LABEL)
            self.state = 143
            self.tool()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireXParser.COMMA:
                self.state = 144
                self.match(HireXParser.COMMA)
                self.state = 145
                self.tool()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireProLangContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROG_LANG_LABEL(self):
            return self.getToken(HireXParser.PROG_LANG_LABEL, 0)

        def proLang(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireXParser.ProLangContext)
            else:
                return self.getTypedRuleContext(HireXParser.ProLangContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.COMMA)
            else:
                return self.getToken(HireXParser.COMMA, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireProLang




    def requireProLang(self):

        localctx = HireXParser.RequireProLangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_requireProLang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(HireXParser.PROG_LANG_LABEL)
            self.state = 152
            self.proLang()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireXParser.COMMA:
                self.state = 153
                self.match(HireXParser.COMMA)
                self.state = 154
                self.proLang()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireFrameworksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRAMEWORK_LABEL(self):
            return self.getToken(HireXParser.FRAMEWORK_LABEL, 0)

        def framework(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireXParser.FrameworkContext)
            else:
                return self.getTypedRuleContext(HireXParser.FrameworkContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.COMMA)
            else:
                return self.getToken(HireXParser.COMMA, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireFrameworks




    def requireFrameworks(self):

        localctx = HireXParser.RequireFrameworksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_requireFrameworks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(HireXParser.FRAMEWORK_LABEL)
            self.state = 161
            self.framework()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireXParser.COMMA:
                self.state = 162
                self.match(HireXParser.COMMA)
                self.state = 163
                self.framework()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireDBContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_LABEL(self):
            return self.getToken(HireXParser.DATA_LABEL, 0)

        def db(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireXParser.DbContext)
            else:
                return self.getTypedRuleContext(HireXParser.DbContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.COMMA)
            else:
                return self.getToken(HireXParser.COMMA, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireDB




    def requireDB(self):

        localctx = HireXParser.RequireDBContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_requireDB)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(HireXParser.DATA_LABEL)
            self.state = 170
            self.db()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireXParser.COMMA:
                self.state = 171
                self.match(HireXParser.COMMA)
                self.state = 172
                self.db()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireEducationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EDU_SECTION(self):
            return self.getToken(HireXParser.EDU_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireXParser.OPEN_CURLY, 0)

        def requireMajor(self):
            return self.getTypedRuleContext(HireXParser.RequireMajorContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(HireXParser.CLOSE_CURLY, 0)

        def requireDegree(self):
            return self.getTypedRuleContext(HireXParser.RequireDegreeContext,0)


        def requireGPA(self):
            return self.getTypedRuleContext(HireXParser.RequireGPAContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_requireEducation




    def requireEducation(self):

        localctx = HireXParser.RequireEducationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_requireEducation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(HireXParser.EDU_SECTION)
            self.state = 179
            self.match(HireXParser.OPEN_CURLY)
            self.state = 180
            self.requireMajor()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.DEGREE_LABEL:
                self.state = 181
                self.requireDegree()


            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireXParser.GPA_LABEL:
                self.state = 184
                self.requireGPA()


            self.state = 187
            self.match(HireXParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireMajorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAJOR_LABEL(self):
            return self.getToken(HireXParser.MAJOR_LABEL, 0)

        def major(self):
            return self.getTypedRuleContext(HireXParser.MajorContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_requireMajor




    def requireMajor(self):

        localctx = HireXParser.RequireMajorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_requireMajor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(HireXParser.MAJOR_LABEL)
            self.state = 190
            self.major()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireDegreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEGREE_LABEL(self):
            return self.getToken(HireXParser.DEGREE_LABEL, 0)

        def degree(self):
            return self.getTypedRuleContext(HireXParser.DegreeContext,0)


        def getRuleIndex(self):
            return HireXParser.RULE_requireDegree




    def requireDegree(self):

        localctx = HireXParser.RequireDegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_requireDegree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(HireXParser.DEGREE_LABEL)
            self.state = 193
            self.degree()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireGPAContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GPA_LABEL(self):
            return self.getToken(HireXParser.GPA_LABEL, 0)

        def COMPARATOR(self):
            return self.getToken(HireXParser.COMPARATOR, 0)

        def FLOAT(self):
            return self.getToken(HireXParser.FLOAT, 0)

        def getRuleIndex(self):
            return HireXParser.RULE_requireGPA




    def requireGPA(self):

        localctx = HireXParser.RequireGPAContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_requireGPA)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(HireXParser.GPA_LABEL)
            self.state = 196
            self.match(HireXParser.COMPARATOR)
            self.state = 197
            self.match(HireXParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireLanguageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LANG_LABEL(self):
            return self.getToken(HireXParser.LANG_LABEL, 0)

        def lang(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireXParser.LangContext)
            else:
                return self.getTypedRuleContext(HireXParser.LangContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.COMMA)
            else:
                return self.getToken(HireXParser.COMMA, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireLanguage




    def requireLanguage(self):

        localctx = HireXParser.RequireLanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_requireLanguage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(HireXParser.LANG_LABEL)
            self.state = 200
            self.lang()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireXParser.COMMA:
                self.state = 201
                self.match(HireXParser.COMMA)
                self.state = 202
                self.lang()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireExperienceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXP_LABEL(self):
            return self.getToken(HireXParser.EXP_LABEL, 0)

        def COMPARATOR(self):
            return self.getToken(HireXParser.COMPARATOR, 0)

        def INT(self):
            return self.getToken(HireXParser.INT, 0)

        def YEARS(self):
            return self.getToken(HireXParser.YEARS, 0)

        def getRuleIndex(self):
            return HireXParser.RULE_requireExperience




    def requireExperience(self):

        localctx = HireXParser.RequireExperienceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_requireExperience)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(HireXParser.EXP_LABEL)
            self.state = 209
            self.match(HireXParser.COMPARATOR)
            self.state = 210
            self.match(HireXParser.INT)
            self.state = 211
            self.match(HireXParser.YEARS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireActivitesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIVITY_LABEL(self):
            return self.getToken(HireXParser.ACTIVITY_LABEL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.ID)
            else:
                return self.getToken(HireXParser.ID, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireActivites




    def requireActivites(self):

        localctx = HireXParser.RequireActivitesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_requireActivites)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(HireXParser.ACTIVITY_LABEL)
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 214
                self.match(HireXParser.ID)
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HireXParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME_LABEL(self):
            return self.getToken(HireXParser.NAME_LABEL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HireXParser.ID)
            else:
                return self.getToken(HireXParser.ID, i)

        def getRuleIndex(self):
            return HireXParser.RULE_requireName




    def requireName(self):

        localctx = HireXParser.RequireNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_requireName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(HireXParser.NAME_LABEL)
            self.state = 221 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 220
                self.match(HireXParser.ID)
                self.state = 223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HireXParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_position




    def position(self):

        localctx = HireXParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireXParser.T__0) | (1 << HireXParser.T__1) | (1 << HireXParser.T__2) | (1 << HireXParser.T__3) | (1 << HireXParser.T__4) | (1 << HireXParser.T__5) | (1 << HireXParser.T__6) | (1 << HireXParser.T__7) | (1 << HireXParser.T__8) | (1 << HireXParser.T__9) | (1 << HireXParser.T__10) | (1 << HireXParser.T__11) | (1 << HireXParser.T__12) | (1 << HireXParser.T__13) | (1 << HireXParser.T__14) | (1 << HireXParser.T__15) | (1 << HireXParser.T__16) | (1 << HireXParser.T__17) | (1 << HireXParser.T__18) | (1 << HireXParser.T__19) | (1 << HireXParser.T__20) | (1 << HireXParser.T__21) | (1 << HireXParser.T__22) | (1 << HireXParser.T__23) | (1 << HireXParser.T__24) | (1 << HireXParser.T__25))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LevelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_level




    def level(self):

        localctx = HireXParser.LevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_level)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireXParser.T__26) | (1 << HireXParser.T__27) | (1 << HireXParser.T__28) | (1 << HireXParser.T__29) | (1 << HireXParser.T__30) | (1 << HireXParser.T__31) | (1 << HireXParser.T__32))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DegreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_degree




    def degree(self):

        localctx = HireXParser.DegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_degree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireXParser.T__33) | (1 << HireXParser.T__34) | (1 << HireXParser.T__35) | (1 << HireXParser.T__36))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MajorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_major




    def major(self):

        localctx = HireXParser.MajorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_major)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireXParser.T__37) | (1 << HireXParser.T__38) | (1 << HireXParser.T__39) | (1 << HireXParser.T__40) | (1 << HireXParser.T__41) | (1 << HireXParser.T__42) | (1 << HireXParser.T__43))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_tool




    def tool(self):

        localctx = HireXParser.ToolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (HireXParser.T__44 - 45)) | (1 << (HireXParser.T__45 - 45)) | (1 << (HireXParser.T__46 - 45)) | (1 << (HireXParser.T__47 - 45)) | (1 << (HireXParser.T__48 - 45)) | (1 << (HireXParser.T__49 - 45)) | (1 << (HireXParser.T__50 - 45)) | (1 << (HireXParser.T__51 - 45)) | (1 << (HireXParser.T__52 - 45)) | (1 << (HireXParser.T__53 - 45)) | (1 << (HireXParser.T__54 - 45)) | (1 << (HireXParser.T__55 - 45)) | (1 << (HireXParser.T__56 - 45)) | (1 << (HireXParser.T__57 - 45)) | (1 << (HireXParser.T__58 - 45)) | (1 << (HireXParser.T__59 - 45)) | (1 << (HireXParser.T__60 - 45)) | (1 << (HireXParser.T__61 - 45)) | (1 << (HireXParser.T__62 - 45)) | (1 << (HireXParser.T__63 - 45)) | (1 << (HireXParser.T__64 - 45)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProLangContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_proLang




    def proLang(self):

        localctx = HireXParser.ProLangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_proLang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not(((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (HireXParser.T__65 - 66)) | (1 << (HireXParser.T__66 - 66)) | (1 << (HireXParser.T__67 - 66)) | (1 << (HireXParser.T__68 - 66)) | (1 << (HireXParser.T__69 - 66)) | (1 << (HireXParser.T__70 - 66)) | (1 << (HireXParser.T__71 - 66)) | (1 << (HireXParser.T__72 - 66)) | (1 << (HireXParser.T__73 - 66)) | (1 << (HireXParser.T__74 - 66)) | (1 << (HireXParser.T__75 - 66)) | (1 << (HireXParser.T__76 - 66)) | (1 << (HireXParser.T__77 - 66)) | (1 << (HireXParser.T__78 - 66)) | (1 << (HireXParser.T__79 - 66)) | (1 << (HireXParser.T__80 - 66)) | (1 << (HireXParser.T__81 - 66)) | (1 << (HireXParser.T__82 - 66)) | (1 << (HireXParser.T__83 - 66)) | (1 << (HireXParser.T__84 - 66)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FrameworkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_framework




    def framework(self):

        localctx = HireXParser.FrameworkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_framework)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not(((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & ((1 << (HireXParser.T__85 - 86)) | (1 << (HireXParser.T__86 - 86)) | (1 << (HireXParser.T__87 - 86)) | (1 << (HireXParser.T__88 - 86)) | (1 << (HireXParser.T__89 - 86)) | (1 << (HireXParser.T__90 - 86)) | (1 << (HireXParser.T__91 - 86)) | (1 << (HireXParser.T__92 - 86)) | (1 << (HireXParser.T__93 - 86)) | (1 << (HireXParser.T__94 - 86)) | (1 << (HireXParser.T__95 - 86)) | (1 << (HireXParser.T__96 - 86)) | (1 << (HireXParser.T__97 - 86)) | (1 << (HireXParser.T__98 - 86)) | (1 << (HireXParser.T__99 - 86)) | (1 << (HireXParser.T__100 - 86)) | (1 << (HireXParser.T__101 - 86)) | (1 << (HireXParser.T__102 - 86)) | (1 << (HireXParser.T__103 - 86)) | (1 << (HireXParser.T__104 - 86)) | (1 << (HireXParser.T__105 - 86)) | (1 << (HireXParser.T__106 - 86)) | (1 << (HireXParser.T__107 - 86)) | (1 << (HireXParser.T__108 - 86)) | (1 << (HireXParser.T__109 - 86)) | (1 << (HireXParser.T__110 - 86)) | (1 << (HireXParser.T__111 - 86)) | (1 << (HireXParser.T__112 - 86)) | (1 << (HireXParser.T__113 - 86)) | (1 << (HireXParser.T__114 - 86)) | (1 << (HireXParser.T__115 - 86)) | (1 << (HireXParser.T__116 - 86)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_db




    def db(self):

        localctx = HireXParser.DbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_db)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HireXParser.T__117 - 118)) | (1 << (HireXParser.T__118 - 118)) | (1 << (HireXParser.T__119 - 118)) | (1 << (HireXParser.T__120 - 118)) | (1 << (HireXParser.T__121 - 118)) | (1 << (HireXParser.T__122 - 118)) | (1 << (HireXParser.T__123 - 118)) | (1 << (HireXParser.T__124 - 118)) | (1 << (HireXParser.T__125 - 118)) | (1 << (HireXParser.T__126 - 118)) | (1 << (HireXParser.T__127 - 118)) | (1 << (HireXParser.T__128 - 118)) | (1 << (HireXParser.T__129 - 118)) | (1 << (HireXParser.T__130 - 118)) | (1 << (HireXParser.T__131 - 118)) | (1 << (HireXParser.T__132 - 118)) | (1 << (HireXParser.T__133 - 118)) | (1 << (HireXParser.T__134 - 118)) | (1 << (HireXParser.T__135 - 118)) | (1 << (HireXParser.T__136 - 118)) | (1 << (HireXParser.T__137 - 118)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LangContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireXParser.RULE_lang




    def lang(self):

        localctx = HireXParser.LangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not(((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (HireXParser.T__138 - 139)) | (1 << (HireXParser.T__139 - 139)) | (1 << (HireXParser.T__140 - 139)) | (1 << (HireXParser.T__141 - 139)) | (1 << (HireXParser.T__142 - 139)) | (1 << (HireXParser.T__143 - 139)) | (1 << (HireXParser.T__144 - 139)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





