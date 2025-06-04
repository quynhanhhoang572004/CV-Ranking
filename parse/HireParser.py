<<<<<<< HEAD
# Generated from grammars/Hire.g4 by ANTLR 4.9.2
=======
# Generated from Hire.g4 by ANTLR 4.9.2
>>>>>>> 87c567f62372deea8f99ccea0a616120727943e7
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00af")
        buf.write("\u00f5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\3\2\5\2B\n\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5X\n\5\3\6\3\6\5\6\\\n\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7f\n\7\3\7\3\7\3\b\3\b\3\b\5\bm\n\b\3\b\5")
        buf.write("\bp\n\b\3\b\5\bs\n\b\3\b\5\bv\n\b\3\b\5\by\n\b\3\b\5\b")
        buf.write("|\n\b\3\b\5\b\177\n\b\3\b\5\b\u0082\n\b\3\b\5\b\u0085")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u009b\n\f")
        buf.write("\f\f\16\f\u009e\13\f\3\r\3\r\3\r\3\r\7\r\u00a4\n\r\f\r")
        buf.write("\16\r\u00a7\13\r\3\16\3\16\3\16\3\16\7\16\u00ad\n\16\f")
        buf.write("\16\16\16\u00b0\13\16\3\17\3\17\3\17\3\17\7\17\u00b6\n")
        buf.write("\17\f\17\16\17\u00b9\13\17\3\20\3\20\3\20\3\20\5\20\u00bf")
        buf.write("\n\20\3\20\5\20\u00c2\n\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u00d4\n\24\f\24\16\24\u00d7\13\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\6\26\u00df\n\26\r\26\16\26\u00e0\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\2\2 \2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2\13")
        buf.write("\3\2\3\34\3\2\35#\3\2$\'\3\2(.\3\2/C\3\2DW\3\2Xu\3\2v")
        buf.write("\u008a\3\2\u008b\u0091\2\u00f4\2A\3\2\2\2\4C\3\2\2\2\6")
        buf.write("H\3\2\2\2\bW\3\2\2\2\nY\3\2\2\2\f]\3\2\2\2\16i\3\2\2\2")
        buf.write("\20\u0088\3\2\2\2\22\u008b\3\2\2\2\24\u008e\3\2\2\2\26")
        buf.write("\u0096\3\2\2\2\30\u009f\3\2\2\2\32\u00a8\3\2\2\2\34\u00b1")
        buf.write("\3\2\2\2\36\u00ba\3\2\2\2 \u00c5\3\2\2\2\"\u00c8\3\2\2")
        buf.write("\2$\u00cb\3\2\2\2&\u00cf\3\2\2\2(\u00d8\3\2\2\2*\u00dc")
        buf.write("\3\2\2\2,\u00e2\3\2\2\2.\u00e4\3\2\2\2\60\u00e6\3\2\2")
        buf.write("\2\62\u00e8\3\2\2\2\64\u00ea\3\2\2\2\66\u00ec\3\2\2\2")
        buf.write("8\u00ee\3\2\2\2:\u00f0\3\2\2\2<\u00f2\3\2\2\2>B\5\n\6")
        buf.write("\2?B\5\4\3\2@B\5\6\4\2A>\3\2\2\2A?\3\2\2\2A@\3\2\2\2B")
        buf.write("\3\3\2\2\2CD\7\u00a4\2\2DE\7\u00a5\2\2EF\7\u00ac\2\2F")
        buf.write("G\7\u00a6\2\2G\5\3\2\2\2HI\7\u00a4\2\2IJ\7\u00a6\2\2J")
        buf.write("K\7\u00a7\2\2KL\5\b\5\2L\7\3\2\2\2MX\5\22\n\2NX\5\26\f")
        buf.write("\2OX\5\30\r\2PX\5\32\16\2QX\5\34\17\2RX\5\"\22\2SX\5$")
        buf.write("\23\2TX\5(\25\2UX\5&\24\2VX\5*\26\2WM\3\2\2\2WN\3\2\2")
        buf.write("\2WO\3\2\2\2WP\3\2\2\2WQ\3\2\2\2WR\3\2\2\2WS\3\2\2\2W")
        buf.write("T\3\2\2\2WU\3\2\2\2WV\3\2\2\2X\t\3\2\2\2Y[\5\f\7\2Z\\")
        buf.write("\5\16\b\2[Z\3\2\2\2[\\\3\2\2\2\\\13\3\2\2\2]^\7\u0092")
        buf.write("\2\2^_\7\u00a8\2\2_`\5\20\t\2`a\5\22\n\2ab\5\24\13\2b")
        buf.write("c\5\36\20\2ce\5(\25\2df\5&\24\2ed\3\2\2\2ef\3\2\2\2fg")
        buf.write("\3\2\2\2gh\7\u00a9\2\2h\r\3\2\2\2ij\7\u0093\2\2jl\7\u00a8")
        buf.write("\2\2km\5\26\f\2lk\3\2\2\2lm\3\2\2\2mo\3\2\2\2np\5\30\r")
        buf.write("\2on\3\2\2\2op\3\2\2\2pr\3\2\2\2qs\5\32\16\2rq\3\2\2\2")
        buf.write("rs\3\2\2\2su\3\2\2\2tv\5\34\17\2ut\3\2\2\2uv\3\2\2\2v")
        buf.write("x\3\2\2\2wy\5\"\22\2xw\3\2\2\2xy\3\2\2\2y{\3\2\2\2z|\5")
        buf.write("$\23\2{z\3\2\2\2{|\3\2\2\2|~\3\2\2\2}\177\5(\25\2~}\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080\u0082\5&\24")
        buf.write("\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\u0085\5*\26\2\u0084\u0083\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\7\u00a9")
        buf.write("\2\2\u0087\17\3\2\2\2\u0088\u0089\7\u0094\2\2\u0089\u008a")
        buf.write("\5,\27\2\u008a\21\3\2\2\2\u008b\u008c\7\u0095\2\2\u008c")
        buf.write("\u008d\5.\30\2\u008d\23\3\2\2\2\u008e\u008f\7\u0096\2")
        buf.write("\2\u008f\u0090\7\u00a8\2\2\u0090\u0091\5\26\f\2\u0091")
        buf.write("\u0092\5\30\r\2\u0092\u0093\5\32\16\2\u0093\u0094\5\34")
        buf.write("\17\2\u0094\u0095\7\u00a9\2\2\u0095\25\3\2\2\2\u0096\u0097")
        buf.write("\7\u009c\2\2\u0097\u009c\5\64\33\2\u0098\u0099\7\u00aa")
        buf.write("\2\2\u0099\u009b\5\64\33\2\u009a\u0098\3\2\2\2\u009b\u009e")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\27\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7\u009d\2")
        buf.write("\2\u00a0\u00a5\5\66\34\2\u00a1\u00a2\7\u00aa\2\2\u00a2")
        buf.write("\u00a4\5\66\34\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2")
        buf.write("\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\31\3")
        buf.write("\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7\u009e\2\2\u00a9")
        buf.write("\u00ae\58\35\2\u00aa\u00ab\7\u00aa\2\2\u00ab\u00ad\58")
        buf.write("\35\2\u00ac\u00aa\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\33\3\2\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b1\u00b2\7\u009f\2\2\u00b2\u00b7\5:\36\2\u00b3")
        buf.write("\u00b4\7\u00aa\2\2\u00b4\u00b6\5:\36\2\u00b5\u00b3\3\2")
        buf.write("\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\35\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\7\u0097\2\2\u00bb\u00bc\7\u00a8\2\2\u00bc\u00be\5 \21")
        buf.write("\2\u00bd\u00bf\5\"\22\2\u00be\u00bd\3\2\2\2\u00be\u00bf")
        buf.write("\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00c2\5$\23\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\7\u00a9\2\2\u00c4\37\3\2\2\2\u00c5\u00c6")
        buf.write("\7\u00a0\2\2\u00c6\u00c7\5\62\32\2\u00c7!\3\2\2\2\u00c8")
        buf.write("\u00c9\7\u00a1\2\2\u00c9\u00ca\5\60\31\2\u00ca#\3\2\2")
        buf.write("\2\u00cb\u00cc\7\u00a2\2\2\u00cc\u00cd\7\u00ab\2\2\u00cd")
        buf.write("\u00ce\7\u00ad\2\2\u00ce%\3\2\2\2\u00cf\u00d0\7\u0098")
        buf.write("\2\2\u00d0\u00d5\5<\37\2\u00d1\u00d2\7\u00aa\2\2\u00d2")
        buf.write("\u00d4\5<\37\2\u00d3\u00d1\3\2\2\2\u00d4\u00d7\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\'\3\2\2")
        buf.write("\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7\u009a\2\2\u00d9\u00da")
        buf.write("\7\u00ac\2\2\u00da\u00db\7\u00a3\2\2\u00db)\3\2\2\2\u00dc")
        buf.write("\u00de\7\u0099\2\2\u00dd\u00df\7\u00ae\2\2\u00de\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1+\3\2\2\2\u00e2\u00e3\t\2\2\2\u00e3")
        buf.write("-\3\2\2\2\u00e4\u00e5\t\3\2\2\u00e5/\3\2\2\2\u00e6\u00e7")
        buf.write("\t\4\2\2\u00e7\61\3\2\2\2\u00e8\u00e9\t\5\2\2\u00e9\63")
        buf.write("\3\2\2\2\u00ea\u00eb\t\6\2\2\u00eb\65\3\2\2\2\u00ec\u00ed")
        buf.write("\t\7\2\2\u00ed\67\3\2\2\2\u00ee\u00ef\t\b\2\2\u00ef9\3")
        buf.write("\2\2\2\u00f0\u00f1\t\t\2\2\u00f1;\3\2\2\2\u00f2\u00f3")
        buf.write("\t\n\2\2\u00f3=\3\2\2\2\27AW[elorux{~\u0081\u0084\u009c")
        buf.write("\u00a5\u00ae\u00b7\u00be\u00c1\u00d5\u00e0")
        return buf.getvalue()


class HireParser ( Parser ):

    grammarFileName = "Hire.g4"

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
                     "'mui'", "'tailwindcss'", "'springboot'", "'mysql'", 
                     "'postgresql'", "'sqlite'", "'mongodb'", "'redis'", 
                     "'mariadb'", "'oracle'", "'sql server'", "'dynamodb'", 
                     "'cassandra'", "'elasticsearch'", "'aws'", "'azure'", 
                     "'gcp'", "'google cloud'", "'amazon web services'", 
                     "'firebase'", "'heroku'", "'digitalocean'", "'vercel'", 
                     "'netlify'", "'english'", "'japanese'", "'chinese'", 
                     "'korean'", "'german'", "'portugeese'", "'french'", 
                     "'REQUIREMENTS'", "'PREFERENCES'", "'position:'", "'level:'", 
                     "'stack'", "'education'", "'language:'", "'activities:'", 
                     "'experience:'", "'references:'", "'tools:'", "'programming languages:'", 
                     "'framework libraries:'", "'databases cloud services:'", 
                     "'major:'", "'degree:'", "'gpa:'", "'years'", "'show'", 
                     "'top'", "<INVALID>", "'with'", "'{'", "'}'", "','" ]

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
                      "REQUIRE_SECTION", "PREFER_SECTION", "POSITION_LABEL", 
                      "LEVEL_LABEL", "STACK_SECTION", "EDU_SECTION", "LANG_LABEL", 
                      "ACTIVITY_LABEL", "EXP_LABEL", "REF_LABEL", "TOOL_LABEL", 
                      "PROG_LANG_LABEL", "FRAMEWORK_LABEL", "DATA_LABEL", 
                      "MAJOR_LABEL", "DEGREE_LABEL", "GPA_LABEL", "YEARS", 
                      "SHOW", "TOP", "CV", "WITH", "OPEN_CURLY", "CLOSE_CURLY", 
                      "COMMA", "COMPARATOR", "INT", "FLOAT", "ID", "WS" ]

    RULE_program = 0
    RULE_showTop = 1
    RULE_showConditional = 2
    RULE_condition = 3
    RULE_jd = 4
    RULE_requirements = 5
    RULE_preferences = 6
    RULE_requirePosition = 7
    RULE_requireLevel = 8
    RULE_requireTechnicalSkills = 9
    RULE_requireTools = 10
    RULE_requireProLang = 11
    RULE_requireFrameworks = 12
    RULE_requireDB = 13
    RULE_requireEducation = 14
    RULE_requireMajor = 15
    RULE_requireDegree = 16
    RULE_requireGPA = 17
    RULE_requireLanguage = 18
    RULE_requireExperience = 19
    RULE_requireActivites = 20
    RULE_position = 21
    RULE_level = 22
    RULE_degree = 23
    RULE_major = 24
    RULE_tool = 25
    RULE_pro_lang = 26
    RULE_framework = 27
    RULE_db = 28
    RULE_lang = 29

    ruleNames =  [ "program", "showTop", "showConditional", "condition", 
                   "jd", "requirements", "preferences", "requirePosition", 
                   "requireLevel", "requireTechnicalSkills", "requireTools", 
                   "requireProLang", "requireFrameworks", "requireDB", "requireEducation", 
                   "requireMajor", "requireDegree", "requireGPA", "requireLanguage", 
                   "requireExperience", "requireActivites", "position", 
                   "level", "degree", "major", "tool", "pro_lang", "framework", 
                   "db", "lang" ]

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
    REQUIRE_SECTION=144
    PREFER_SECTION=145
    POSITION_LABEL=146
    LEVEL_LABEL=147
    STACK_SECTION=148
    EDU_SECTION=149
    LANG_LABEL=150
    ACTIVITY_LABEL=151
    EXP_LABEL=152
    REF_LABEL=153
    TOOL_LABEL=154
    PROG_LANG_LABEL=155
    FRAMEWORK_LABEL=156
    DATA_LABEL=157
    MAJOR_LABEL=158
    DEGREE_LABEL=159
    GPA_LABEL=160
    YEARS=161
    SHOW=162
    TOP=163
    CV=164
    WITH=165
    OPEN_CURLY=166
    CLOSE_CURLY=167
    COMMA=168
    COMPARATOR=169
    INT=170
    FLOAT=171
    ID=172
    WS=173

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
            return self.getTypedRuleContext(HireParser.JdContext,0)


        def showTop(self):
            return self.getTypedRuleContext(HireParser.ShowTopContext,0)


        def showConditional(self):
            return self.getTypedRuleContext(HireParser.ShowConditionalContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = HireParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.jd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.showTop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.showConditional()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowTopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(HireParser.SHOW, 0)

        def TOP(self):
            return self.getToken(HireParser.TOP, 0)

        def INT(self):
            return self.getToken(HireParser.INT, 0)

        def CV(self):
            return self.getToken(HireParser.CV, 0)

        def getRuleIndex(self):
            return HireParser.RULE_showTop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowTop" ):
                listener.enterShowTop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowTop" ):
                listener.exitShowTop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowTop" ):
                return visitor.visitShowTop(self)
            else:
                return visitor.visitChildren(self)




    def showTop(self):

        localctx = HireParser.ShowTopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_showTop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(HireParser.SHOW)
            self.state = 66
            self.match(HireParser.TOP)
            self.state = 67
            self.match(HireParser.INT)
            self.state = 68
            self.match(HireParser.CV)
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
            return self.getToken(HireParser.SHOW, 0)

        def CV(self):
            return self.getToken(HireParser.CV, 0)

        def WITH(self):
            return self.getToken(HireParser.WITH, 0)

        def condition(self):
            return self.getTypedRuleContext(HireParser.ConditionContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_showConditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowConditional" ):
                listener.enterShowConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowConditional" ):
                listener.exitShowConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowConditional" ):
                return visitor.visitShowConditional(self)
            else:
                return visitor.visitChildren(self)




    def showConditional(self):

        localctx = HireParser.ShowConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_showConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(HireParser.SHOW)
            self.state = 71
            self.match(HireParser.CV)
            self.state = 72
            self.match(HireParser.WITH)
            self.state = 73
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

        def requireLevel(self):
            return self.getTypedRuleContext(HireParser.RequireLevelContext,0)


        def requireTools(self):
            return self.getTypedRuleContext(HireParser.RequireToolsContext,0)


        def requireProLang(self):
            return self.getTypedRuleContext(HireParser.RequireProLangContext,0)


        def requireFrameworks(self):
            return self.getTypedRuleContext(HireParser.RequireFrameworksContext,0)


        def requireDB(self):
            return self.getTypedRuleContext(HireParser.RequireDBContext,0)


        def requireDegree(self):
            return self.getTypedRuleContext(HireParser.RequireDegreeContext,0)


        def requireGPA(self):
            return self.getTypedRuleContext(HireParser.RequireGPAContext,0)


        def requireExperience(self):
            return self.getTypedRuleContext(HireParser.RequireExperienceContext,0)


        def requireLanguage(self):
            return self.getTypedRuleContext(HireParser.RequireLanguageContext,0)


        def requireActivites(self):
            return self.getTypedRuleContext(HireParser.RequireActivitesContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = HireParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HireParser.LEVEL_LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.requireLevel()
                pass
            elif token in [HireParser.TOOL_LABEL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.requireTools()
                pass
            elif token in [HireParser.PROG_LANG_LABEL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.requireProLang()
                pass
            elif token in [HireParser.FRAMEWORK_LABEL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.requireFrameworks()
                pass
            elif token in [HireParser.DATA_LABEL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.requireDB()
                pass
            elif token in [HireParser.DEGREE_LABEL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.requireDegree()
                pass
            elif token in [HireParser.GPA_LABEL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.requireGPA()
                pass
            elif token in [HireParser.EXP_LABEL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.requireExperience()
                pass
            elif token in [HireParser.LANG_LABEL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 83
                self.requireLanguage()
                pass
            elif token in [HireParser.ACTIVITY_LABEL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 84
                self.requireActivites()
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
            return self.getTypedRuleContext(HireParser.RequirementsContext,0)


        def preferences(self):
            return self.getTypedRuleContext(HireParser.PreferencesContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_jd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJd" ):
                listener.enterJd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJd" ):
                listener.exitJd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJd" ):
                return visitor.visitJd(self)
            else:
                return visitor.visitChildren(self)




    def jd(self):

        localctx = HireParser.JdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_jd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.requirements()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.PREFER_SECTION:
                self.state = 88
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
            return self.getToken(HireParser.REQUIRE_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireParser.OPEN_CURLY, 0)

        def requirePosition(self):
            return self.getTypedRuleContext(HireParser.RequirePositionContext,0)


        def requireLevel(self):
            return self.getTypedRuleContext(HireParser.RequireLevelContext,0)


        def requireTechnicalSkills(self):
            return self.getTypedRuleContext(HireParser.RequireTechnicalSkillsContext,0)


        def requireEducation(self):
            return self.getTypedRuleContext(HireParser.RequireEducationContext,0)


        def requireExperience(self):
            return self.getTypedRuleContext(HireParser.RequireExperienceContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(HireParser.CLOSE_CURLY, 0)

        def requireLanguage(self):
            return self.getTypedRuleContext(HireParser.RequireLanguageContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_requirements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirements" ):
                listener.enterRequirements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirements" ):
                listener.exitRequirements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirements" ):
                return visitor.visitRequirements(self)
            else:
                return visitor.visitChildren(self)




    def requirements(self):

        localctx = HireParser.RequirementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_requirements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(HireParser.REQUIRE_SECTION)
            self.state = 92
            self.match(HireParser.OPEN_CURLY)
            self.state = 93
            self.requirePosition()
            self.state = 94
            self.requireLevel()
            self.state = 95
            self.requireTechnicalSkills()
            self.state = 96
            self.requireEducation()
            self.state = 97
            self.requireExperience()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.LANG_LABEL:
                self.state = 98
                self.requireLanguage()


            self.state = 101
            self.match(HireParser.CLOSE_CURLY)
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
            return self.getToken(HireParser.PREFER_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireParser.OPEN_CURLY, 0)

        def CLOSE_CURLY(self):
            return self.getToken(HireParser.CLOSE_CURLY, 0)

        def requireTools(self):
            return self.getTypedRuleContext(HireParser.RequireToolsContext,0)


        def requireProLang(self):
            return self.getTypedRuleContext(HireParser.RequireProLangContext,0)


        def requireFrameworks(self):
            return self.getTypedRuleContext(HireParser.RequireFrameworksContext,0)


        def requireDB(self):
            return self.getTypedRuleContext(HireParser.RequireDBContext,0)


        def requireDegree(self):
            return self.getTypedRuleContext(HireParser.RequireDegreeContext,0)


        def requireGPA(self):
            return self.getTypedRuleContext(HireParser.RequireGPAContext,0)


        def requireExperience(self):
            return self.getTypedRuleContext(HireParser.RequireExperienceContext,0)


        def requireLanguage(self):
            return self.getTypedRuleContext(HireParser.RequireLanguageContext,0)


        def requireActivites(self):
            return self.getTypedRuleContext(HireParser.RequireActivitesContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_preferences

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreferences" ):
                listener.enterPreferences(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreferences" ):
                listener.exitPreferences(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreferences" ):
                return visitor.visitPreferences(self)
            else:
                return visitor.visitChildren(self)




    def preferences(self):

        localctx = HireParser.PreferencesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_preferences)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(HireParser.PREFER_SECTION)
            self.state = 104
            self.match(HireParser.OPEN_CURLY)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.TOOL_LABEL:
                self.state = 105
                self.requireTools()


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.PROG_LANG_LABEL:
                self.state = 108
                self.requireProLang()


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.FRAMEWORK_LABEL:
                self.state = 111
                self.requireFrameworks()


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.DATA_LABEL:
                self.state = 114
                self.requireDB()


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.DEGREE_LABEL:
                self.state = 117
                self.requireDegree()


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.GPA_LABEL:
                self.state = 120
                self.requireGPA()


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.EXP_LABEL:
                self.state = 123
                self.requireExperience()


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.LANG_LABEL:
                self.state = 126
                self.requireLanguage()


            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.ACTIVITY_LABEL:
                self.state = 129
                self.requireActivites()


            self.state = 132
            self.match(HireParser.CLOSE_CURLY)
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
            return self.getToken(HireParser.POSITION_LABEL, 0)

        def position(self):
            return self.getTypedRuleContext(HireParser.PositionContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_requirePosition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirePosition" ):
                listener.enterRequirePosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirePosition" ):
                listener.exitRequirePosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirePosition" ):
                return visitor.visitRequirePosition(self)
            else:
                return visitor.visitChildren(self)




    def requirePosition(self):

        localctx = HireParser.RequirePositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_requirePosition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(HireParser.POSITION_LABEL)
            self.state = 135
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
            return self.getToken(HireParser.LEVEL_LABEL, 0)

        def level(self):
            return self.getTypedRuleContext(HireParser.LevelContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_requireLevel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireLevel" ):
                listener.enterRequireLevel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireLevel" ):
                listener.exitRequireLevel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireLevel" ):
                return visitor.visitRequireLevel(self)
            else:
                return visitor.visitChildren(self)




    def requireLevel(self):

        localctx = HireParser.RequireLevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_requireLevel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(HireParser.LEVEL_LABEL)
            self.state = 138
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
            return self.getToken(HireParser.STACK_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireParser.OPEN_CURLY, 0)

        def requireTools(self):
            return self.getTypedRuleContext(HireParser.RequireToolsContext,0)


        def requireProLang(self):
            return self.getTypedRuleContext(HireParser.RequireProLangContext,0)


        def requireFrameworks(self):
            return self.getTypedRuleContext(HireParser.RequireFrameworksContext,0)


        def requireDB(self):
            return self.getTypedRuleContext(HireParser.RequireDBContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(HireParser.CLOSE_CURLY, 0)

        def getRuleIndex(self):
            return HireParser.RULE_requireTechnicalSkills

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireTechnicalSkills" ):
                listener.enterRequireTechnicalSkills(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireTechnicalSkills" ):
                listener.exitRequireTechnicalSkills(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireTechnicalSkills" ):
                return visitor.visitRequireTechnicalSkills(self)
            else:
                return visitor.visitChildren(self)




    def requireTechnicalSkills(self):

        localctx = HireParser.RequireTechnicalSkillsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_requireTechnicalSkills)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(HireParser.STACK_SECTION)
            self.state = 141
            self.match(HireParser.OPEN_CURLY)
            self.state = 142
            self.requireTools()
            self.state = 143
            self.requireProLang()
            self.state = 144
            self.requireFrameworks()
            self.state = 145
            self.requireDB()
            self.state = 146
            self.match(HireParser.CLOSE_CURLY)
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
            return self.getToken(HireParser.TOOL_LABEL, 0)

        def tool(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireParser.ToolContext)
            else:
                return self.getTypedRuleContext(HireParser.ToolContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireParser.COMMA)
            else:
                return self.getToken(HireParser.COMMA, i)

        def getRuleIndex(self):
            return HireParser.RULE_requireTools

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireTools" ):
                listener.enterRequireTools(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireTools" ):
                listener.exitRequireTools(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireTools" ):
                return visitor.visitRequireTools(self)
            else:
                return visitor.visitChildren(self)




    def requireTools(self):

        localctx = HireParser.RequireToolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_requireTools)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(HireParser.TOOL_LABEL)
            self.state = 149
            self.tool()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireParser.COMMA:
                self.state = 150
                self.match(HireParser.COMMA)
                self.state = 151
                self.tool()
                self.state = 156
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
            return self.getToken(HireParser.PROG_LANG_LABEL, 0)

        def pro_lang(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireParser.Pro_langContext)
            else:
                return self.getTypedRuleContext(HireParser.Pro_langContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireParser.COMMA)
            else:
                return self.getToken(HireParser.COMMA, i)

        def getRuleIndex(self):
            return HireParser.RULE_requireProLang

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireProLang" ):
                listener.enterRequireProLang(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireProLang" ):
                listener.exitRequireProLang(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireProLang" ):
                return visitor.visitRequireProLang(self)
            else:
                return visitor.visitChildren(self)




    def requireProLang(self):

        localctx = HireParser.RequireProLangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_requireProLang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(HireParser.PROG_LANG_LABEL)
            self.state = 158
            self.pro_lang()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireParser.COMMA:
                self.state = 159
                self.match(HireParser.COMMA)
                self.state = 160
                self.pro_lang()
                self.state = 165
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
            return self.getToken(HireParser.FRAMEWORK_LABEL, 0)

        def framework(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireParser.FrameworkContext)
            else:
                return self.getTypedRuleContext(HireParser.FrameworkContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireParser.COMMA)
            else:
                return self.getToken(HireParser.COMMA, i)

        def getRuleIndex(self):
            return HireParser.RULE_requireFrameworks

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireFrameworks" ):
                listener.enterRequireFrameworks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireFrameworks" ):
                listener.exitRequireFrameworks(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireFrameworks" ):
                return visitor.visitRequireFrameworks(self)
            else:
                return visitor.visitChildren(self)




    def requireFrameworks(self):

        localctx = HireParser.RequireFrameworksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_requireFrameworks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(HireParser.FRAMEWORK_LABEL)
            self.state = 167
            self.framework()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireParser.COMMA:
                self.state = 168
                self.match(HireParser.COMMA)
                self.state = 169
                self.framework()
                self.state = 174
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
            return self.getToken(HireParser.DATA_LABEL, 0)

        def db(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireParser.DbContext)
            else:
                return self.getTypedRuleContext(HireParser.DbContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireParser.COMMA)
            else:
                return self.getToken(HireParser.COMMA, i)

        def getRuleIndex(self):
            return HireParser.RULE_requireDB

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireDB" ):
                listener.enterRequireDB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireDB" ):
                listener.exitRequireDB(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireDB" ):
                return visitor.visitRequireDB(self)
            else:
                return visitor.visitChildren(self)




    def requireDB(self):

        localctx = HireParser.RequireDBContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_requireDB)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(HireParser.DATA_LABEL)
            self.state = 176
            self.db()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireParser.COMMA:
                self.state = 177
                self.match(HireParser.COMMA)
                self.state = 178
                self.db()
                self.state = 183
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
            return self.getToken(HireParser.EDU_SECTION, 0)

        def OPEN_CURLY(self):
            return self.getToken(HireParser.OPEN_CURLY, 0)

        def requireMajor(self):
            return self.getTypedRuleContext(HireParser.RequireMajorContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(HireParser.CLOSE_CURLY, 0)

        def requireDegree(self):
            return self.getTypedRuleContext(HireParser.RequireDegreeContext,0)


        def requireGPA(self):
            return self.getTypedRuleContext(HireParser.RequireGPAContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_requireEducation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireEducation" ):
                listener.enterRequireEducation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireEducation" ):
                listener.exitRequireEducation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireEducation" ):
                return visitor.visitRequireEducation(self)
            else:
                return visitor.visitChildren(self)




    def requireEducation(self):

        localctx = HireParser.RequireEducationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_requireEducation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(HireParser.EDU_SECTION)
            self.state = 185
            self.match(HireParser.OPEN_CURLY)
            self.state = 186
            self.requireMajor()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.DEGREE_LABEL:
                self.state = 187
                self.requireDegree()


            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HireParser.GPA_LABEL:
                self.state = 190
                self.requireGPA()


            self.state = 193
            self.match(HireParser.CLOSE_CURLY)
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
            return self.getToken(HireParser.MAJOR_LABEL, 0)

        def major(self):
            return self.getTypedRuleContext(HireParser.MajorContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_requireMajor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireMajor" ):
                listener.enterRequireMajor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireMajor" ):
                listener.exitRequireMajor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireMajor" ):
                return visitor.visitRequireMajor(self)
            else:
                return visitor.visitChildren(self)




    def requireMajor(self):

        localctx = HireParser.RequireMajorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_requireMajor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(HireParser.MAJOR_LABEL)
            self.state = 196
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
            return self.getToken(HireParser.DEGREE_LABEL, 0)

        def degree(self):
            return self.getTypedRuleContext(HireParser.DegreeContext,0)


        def getRuleIndex(self):
            return HireParser.RULE_requireDegree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireDegree" ):
                listener.enterRequireDegree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireDegree" ):
                listener.exitRequireDegree(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireDegree" ):
                return visitor.visitRequireDegree(self)
            else:
                return visitor.visitChildren(self)




    def requireDegree(self):

        localctx = HireParser.RequireDegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_requireDegree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(HireParser.DEGREE_LABEL)
            self.state = 199
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
            return self.getToken(HireParser.GPA_LABEL, 0)

        def COMPARATOR(self):
            return self.getToken(HireParser.COMPARATOR, 0)

        def FLOAT(self):
            return self.getToken(HireParser.FLOAT, 0)

        def getRuleIndex(self):
            return HireParser.RULE_requireGPA

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireGPA" ):
                listener.enterRequireGPA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireGPA" ):
                listener.exitRequireGPA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireGPA" ):
                return visitor.visitRequireGPA(self)
            else:
                return visitor.visitChildren(self)




    def requireGPA(self):

        localctx = HireParser.RequireGPAContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_requireGPA)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(HireParser.GPA_LABEL)
            self.state = 202
            self.match(HireParser.COMPARATOR)
            self.state = 203
            self.match(HireParser.FLOAT)
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
            return self.getToken(HireParser.LANG_LABEL, 0)

        def lang(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HireParser.LangContext)
            else:
                return self.getTypedRuleContext(HireParser.LangContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HireParser.COMMA)
            else:
                return self.getToken(HireParser.COMMA, i)

        def getRuleIndex(self):
            return HireParser.RULE_requireLanguage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireLanguage" ):
                listener.enterRequireLanguage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireLanguage" ):
                listener.exitRequireLanguage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireLanguage" ):
                return visitor.visitRequireLanguage(self)
            else:
                return visitor.visitChildren(self)




    def requireLanguage(self):

        localctx = HireParser.RequireLanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_requireLanguage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(HireParser.LANG_LABEL)
            self.state = 206
            self.lang()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HireParser.COMMA:
                self.state = 207
                self.match(HireParser.COMMA)
                self.state = 208
                self.lang()
                self.state = 213
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
            return self.getToken(HireParser.EXP_LABEL, 0)

        def INT(self):
            return self.getToken(HireParser.INT, 0)

        def YEARS(self):
            return self.getToken(HireParser.YEARS, 0)

        def getRuleIndex(self):
            return HireParser.RULE_requireExperience

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireExperience" ):
                listener.enterRequireExperience(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireExperience" ):
                listener.exitRequireExperience(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireExperience" ):
                return visitor.visitRequireExperience(self)
            else:
                return visitor.visitChildren(self)




    def requireExperience(self):

        localctx = HireParser.RequireExperienceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_requireExperience)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(HireParser.EXP_LABEL)
            self.state = 215
            self.match(HireParser.INT)
            self.state = 216
            self.match(HireParser.YEARS)
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
            return self.getToken(HireParser.ACTIVITY_LABEL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HireParser.ID)
            else:
                return self.getToken(HireParser.ID, i)

        def getRuleIndex(self):
            return HireParser.RULE_requireActivites

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireActivites" ):
                listener.enterRequireActivites(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireActivites" ):
                listener.exitRequireActivites(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireActivites" ):
                return visitor.visitRequireActivites(self)
            else:
                return visitor.visitChildren(self)




    def requireActivites(self):

        localctx = HireParser.RequireActivitesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_requireActivites)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(HireParser.ACTIVITY_LABEL)
            self.state = 220 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 219
                self.match(HireParser.ID)
                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HireParser.ID):
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
            return HireParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPosition" ):
                return visitor.visitPosition(self)
            else:
                return visitor.visitChildren(self)




    def position(self):

        localctx = HireParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireParser.T__0) | (1 << HireParser.T__1) | (1 << HireParser.T__2) | (1 << HireParser.T__3) | (1 << HireParser.T__4) | (1 << HireParser.T__5) | (1 << HireParser.T__6) | (1 << HireParser.T__7) | (1 << HireParser.T__8) | (1 << HireParser.T__9) | (1 << HireParser.T__10) | (1 << HireParser.T__11) | (1 << HireParser.T__12) | (1 << HireParser.T__13) | (1 << HireParser.T__14) | (1 << HireParser.T__15) | (1 << HireParser.T__16) | (1 << HireParser.T__17) | (1 << HireParser.T__18) | (1 << HireParser.T__19) | (1 << HireParser.T__20) | (1 << HireParser.T__21) | (1 << HireParser.T__22) | (1 << HireParser.T__23) | (1 << HireParser.T__24) | (1 << HireParser.T__25))) != 0)):
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
            return HireParser.RULE_level

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLevel" ):
                listener.enterLevel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLevel" ):
                listener.exitLevel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLevel" ):
                return visitor.visitLevel(self)
            else:
                return visitor.visitChildren(self)




    def level(self):

        localctx = HireParser.LevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_level)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireParser.T__26) | (1 << HireParser.T__27) | (1 << HireParser.T__28) | (1 << HireParser.T__29) | (1 << HireParser.T__30) | (1 << HireParser.T__31) | (1 << HireParser.T__32))) != 0)):
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
            return HireParser.RULE_degree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDegree" ):
                listener.enterDegree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDegree" ):
                listener.exitDegree(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDegree" ):
                return visitor.visitDegree(self)
            else:
                return visitor.visitChildren(self)




    def degree(self):

        localctx = HireParser.DegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_degree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireParser.T__33) | (1 << HireParser.T__34) | (1 << HireParser.T__35) | (1 << HireParser.T__36))) != 0)):
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
            return HireParser.RULE_major

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMajor" ):
                listener.enterMajor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMajor" ):
                listener.exitMajor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMajor" ):
                return visitor.visitMajor(self)
            else:
                return visitor.visitChildren(self)




    def major(self):

        localctx = HireParser.MajorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_major)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HireParser.T__37) | (1 << HireParser.T__38) | (1 << HireParser.T__39) | (1 << HireParser.T__40) | (1 << HireParser.T__41) | (1 << HireParser.T__42) | (1 << HireParser.T__43))) != 0)):
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
            return HireParser.RULE_tool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTool" ):
                listener.enterTool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTool" ):
                listener.exitTool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTool" ):
                return visitor.visitTool(self)
            else:
                return visitor.visitChildren(self)




    def tool(self):

        localctx = HireParser.ToolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (HireParser.T__44 - 45)) | (1 << (HireParser.T__45 - 45)) | (1 << (HireParser.T__46 - 45)) | (1 << (HireParser.T__47 - 45)) | (1 << (HireParser.T__48 - 45)) | (1 << (HireParser.T__49 - 45)) | (1 << (HireParser.T__50 - 45)) | (1 << (HireParser.T__51 - 45)) | (1 << (HireParser.T__52 - 45)) | (1 << (HireParser.T__53 - 45)) | (1 << (HireParser.T__54 - 45)) | (1 << (HireParser.T__55 - 45)) | (1 << (HireParser.T__56 - 45)) | (1 << (HireParser.T__57 - 45)) | (1 << (HireParser.T__58 - 45)) | (1 << (HireParser.T__59 - 45)) | (1 << (HireParser.T__60 - 45)) | (1 << (HireParser.T__61 - 45)) | (1 << (HireParser.T__62 - 45)) | (1 << (HireParser.T__63 - 45)) | (1 << (HireParser.T__64 - 45)))) != 0)):
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


    class Pro_langContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HireParser.RULE_pro_lang

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPro_lang" ):
                listener.enterPro_lang(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPro_lang" ):
                listener.exitPro_lang(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPro_lang" ):
                return visitor.visitPro_lang(self)
            else:
                return visitor.visitChildren(self)




    def pro_lang(self):

        localctx = HireParser.Pro_langContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_pro_lang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            _la = self._input.LA(1)
            if not(((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (HireParser.T__65 - 66)) | (1 << (HireParser.T__66 - 66)) | (1 << (HireParser.T__67 - 66)) | (1 << (HireParser.T__68 - 66)) | (1 << (HireParser.T__69 - 66)) | (1 << (HireParser.T__70 - 66)) | (1 << (HireParser.T__71 - 66)) | (1 << (HireParser.T__72 - 66)) | (1 << (HireParser.T__73 - 66)) | (1 << (HireParser.T__74 - 66)) | (1 << (HireParser.T__75 - 66)) | (1 << (HireParser.T__76 - 66)) | (1 << (HireParser.T__77 - 66)) | (1 << (HireParser.T__78 - 66)) | (1 << (HireParser.T__79 - 66)) | (1 << (HireParser.T__80 - 66)) | (1 << (HireParser.T__81 - 66)) | (1 << (HireParser.T__82 - 66)) | (1 << (HireParser.T__83 - 66)) | (1 << (HireParser.T__84 - 66)))) != 0)):
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
            return HireParser.RULE_framework

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFramework" ):
                listener.enterFramework(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFramework" ):
                listener.exitFramework(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFramework" ):
                return visitor.visitFramework(self)
            else:
                return visitor.visitChildren(self)




    def framework(self):

        localctx = HireParser.FrameworkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_framework)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not(((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & ((1 << (HireParser.T__85 - 86)) | (1 << (HireParser.T__86 - 86)) | (1 << (HireParser.T__87 - 86)) | (1 << (HireParser.T__88 - 86)) | (1 << (HireParser.T__89 - 86)) | (1 << (HireParser.T__90 - 86)) | (1 << (HireParser.T__91 - 86)) | (1 << (HireParser.T__92 - 86)) | (1 << (HireParser.T__93 - 86)) | (1 << (HireParser.T__94 - 86)) | (1 << (HireParser.T__95 - 86)) | (1 << (HireParser.T__96 - 86)) | (1 << (HireParser.T__97 - 86)) | (1 << (HireParser.T__98 - 86)) | (1 << (HireParser.T__99 - 86)) | (1 << (HireParser.T__100 - 86)) | (1 << (HireParser.T__101 - 86)) | (1 << (HireParser.T__102 - 86)) | (1 << (HireParser.T__103 - 86)) | (1 << (HireParser.T__104 - 86)) | (1 << (HireParser.T__105 - 86)) | (1 << (HireParser.T__106 - 86)) | (1 << (HireParser.T__107 - 86)) | (1 << (HireParser.T__108 - 86)) | (1 << (HireParser.T__109 - 86)) | (1 << (HireParser.T__110 - 86)) | (1 << (HireParser.T__111 - 86)) | (1 << (HireParser.T__112 - 86)) | (1 << (HireParser.T__113 - 86)) | (1 << (HireParser.T__114 - 86)))) != 0)):
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
            return HireParser.RULE_db

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDb" ):
                listener.enterDb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDb" ):
                listener.exitDb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDb" ):
                return visitor.visitDb(self)
            else:
                return visitor.visitChildren(self)




    def db(self):

        localctx = HireParser.DbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_db)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            _la = self._input.LA(1)
            if not(((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (HireParser.T__115 - 116)) | (1 << (HireParser.T__116 - 116)) | (1 << (HireParser.T__117 - 116)) | (1 << (HireParser.T__118 - 116)) | (1 << (HireParser.T__119 - 116)) | (1 << (HireParser.T__120 - 116)) | (1 << (HireParser.T__121 - 116)) | (1 << (HireParser.T__122 - 116)) | (1 << (HireParser.T__123 - 116)) | (1 << (HireParser.T__124 - 116)) | (1 << (HireParser.T__125 - 116)) | (1 << (HireParser.T__126 - 116)) | (1 << (HireParser.T__127 - 116)) | (1 << (HireParser.T__128 - 116)) | (1 << (HireParser.T__129 - 116)) | (1 << (HireParser.T__130 - 116)) | (1 << (HireParser.T__131 - 116)) | (1 << (HireParser.T__132 - 116)) | (1 << (HireParser.T__133 - 116)) | (1 << (HireParser.T__134 - 116)) | (1 << (HireParser.T__135 - 116)))) != 0)):
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
            return HireParser.RULE_lang

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLang" ):
                listener.enterLang(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLang" ):
                listener.exitLang(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLang" ):
                return visitor.visitLang(self)
            else:
                return visitor.visitChildren(self)




    def lang(self):

        localctx = HireParser.LangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            _la = self._input.LA(1)
            if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HireParser.T__136 - 137)) | (1 << (HireParser.T__137 - 137)) | (1 << (HireParser.T__138 - 137)) | (1 << (HireParser.T__139 - 137)) | (1 << (HireParser.T__140 - 137)) | (1 << (HireParser.T__141 - 137)) | (1 << (HireParser.T__142 - 137)))) != 0)):
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





