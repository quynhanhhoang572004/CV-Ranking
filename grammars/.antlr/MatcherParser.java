// Generated from e:/CV-Ranking/grammars/Matcher.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MatcherParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, STRING=17, 
		IDENTIFIER=18, INT=19, WS=20;
	public static final int
		RULE_matchBlock = 0, RULE_matchRule = 1, RULE_requireRule = 2, RULE_preferRule = 3, 
		RULE_scoreRule = 4, RULE_condition = 5, RULE_scoreAction = 6, RULE_comparator = 7, 
		RULE_value = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"matchBlock", "matchRule", "requireRule", "preferRule", "scoreRule", 
			"condition", "scoreAction", "comparator", "value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'match'", "'{'", "'}'", "'require'", "'skill'", "'prefer'", "'weight'", 
			"'if'", "'then'", "'.'", "'score'", "'+'", "'-'", "'=='", "'>='", "'<='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "STRING", "IDENTIFIER", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Matcher.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MatcherParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MatchBlockContext extends ParserRuleContext {
		public List<MatchRuleContext> matchRule() {
			return getRuleContexts(MatchRuleContext.class);
		}
		public MatchRuleContext matchRule(int i) {
			return getRuleContext(MatchRuleContext.class,i);
		}
		public MatchBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matchBlock; }
	}

	public final MatchBlockContext matchBlock() throws RecognitionException {
		MatchBlockContext _localctx = new MatchBlockContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_matchBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(T__0);
			setState(19);
			match(T__1);
			setState(21); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(20);
				matchRule();
				}
				}
				setState(23); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 336L) != 0) );
			setState(25);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MatchRuleContext extends ParserRuleContext {
		public RequireRuleContext requireRule() {
			return getRuleContext(RequireRuleContext.class,0);
		}
		public PreferRuleContext preferRule() {
			return getRuleContext(PreferRuleContext.class,0);
		}
		public ScoreRuleContext scoreRule() {
			return getRuleContext(ScoreRuleContext.class,0);
		}
		public MatchRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matchRule; }
	}

	public final MatchRuleContext matchRule() throws RecognitionException {
		MatchRuleContext _localctx = new MatchRuleContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_matchRule);
		try {
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				requireRule();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				setState(28);
				preferRule();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(29);
				scoreRule();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RequireRuleContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(MatcherParser.STRING, 0); }
		public RequireRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireRule; }
	}

	public final RequireRuleContext requireRule() throws RecognitionException {
		RequireRuleContext _localctx = new RequireRuleContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_requireRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(T__3);
			setState(33);
			match(T__4);
			setState(34);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PreferRuleContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(MatcherParser.STRING, 0); }
		public TerminalNode INT() { return getToken(MatcherParser.INT, 0); }
		public PreferRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preferRule; }
	}

	public final PreferRuleContext preferRule() throws RecognitionException {
		PreferRuleContext _localctx = new PreferRuleContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_preferRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(T__5);
			setState(37);
			match(T__4);
			setState(38);
			match(STRING);
			setState(39);
			match(T__6);
			setState(40);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScoreRuleContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public ScoreActionContext scoreAction() {
			return getRuleContext(ScoreActionContext.class,0);
		}
		public ScoreRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scoreRule; }
	}

	public final ScoreRuleContext scoreRule() throws RecognitionException {
		ScoreRuleContext _localctx = new ScoreRuleContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_scoreRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(T__7);
			setState(43);
			condition();
			setState(44);
			match(T__8);
			setState(45);
			scoreAction();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(MatcherParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(MatcherParser.IDENTIFIER, i);
		}
		public ComparatorContext comparator() {
			return getRuleContext(ComparatorContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(IDENTIFIER);
			setState(48);
			match(T__9);
			setState(49);
			match(IDENTIFIER);
			setState(50);
			comparator();
			setState(51);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScoreActionContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MatcherParser.INT, 0); }
		public ScoreActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scoreAction; }
	}

	public final ScoreActionContext scoreAction() throws RecognitionException {
		ScoreActionContext _localctx = new ScoreActionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_scoreAction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(T__10);
			setState(54);
			_la = _input.LA(1);
			if ( !(_la==T__11 || _la==T__12) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(55);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparatorContext extends ParserRuleContext {
		public ComparatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparator; }
	}

	public final ComparatorContext comparator() throws RecognitionException {
		ComparatorContext _localctx = new ComparatorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_comparator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 114688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(MatcherParser.STRING, 0); }
		public TerminalNode INT() { return getToken(MatcherParser.INT, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_la = _input.LA(1);
			if ( !(_la==STRING || _la==INT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014>\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0016\b\u0000"+
		"\u000b\u0000\f\u0000\u0017\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u001f\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0000\u0000\t\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0000\u0003\u0001\u0000\f\r\u0001\u0000\u000e\u0010\u0002\u0000"+
		"\u0011\u0011\u0013\u00137\u0000\u0012\u0001\u0000\u0000\u0000\u0002\u001e"+
		"\u0001\u0000\u0000\u0000\u0004 \u0001\u0000\u0000\u0000\u0006$\u0001\u0000"+
		"\u0000\u0000\b*\u0001\u0000\u0000\u0000\n/\u0001\u0000\u0000\u0000\f5"+
		"\u0001\u0000\u0000\u0000\u000e9\u0001\u0000\u0000\u0000\u0010;\u0001\u0000"+
		"\u0000\u0000\u0012\u0013\u0005\u0001\u0000\u0000\u0013\u0015\u0005\u0002"+
		"\u0000\u0000\u0014\u0016\u0003\u0002\u0001\u0000\u0015\u0014\u0001\u0000"+
		"\u0000\u0000\u0016\u0017\u0001\u0000\u0000\u0000\u0017\u0015\u0001\u0000"+
		"\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u0019\u0001\u0000"+
		"\u0000\u0000\u0019\u001a\u0005\u0003\u0000\u0000\u001a\u0001\u0001\u0000"+
		"\u0000\u0000\u001b\u001f\u0003\u0004\u0002\u0000\u001c\u001f\u0003\u0006"+
		"\u0003\u0000\u001d\u001f\u0003\b\u0004\u0000\u001e\u001b\u0001\u0000\u0000"+
		"\u0000\u001e\u001c\u0001\u0000\u0000\u0000\u001e\u001d\u0001\u0000\u0000"+
		"\u0000\u001f\u0003\u0001\u0000\u0000\u0000 !\u0005\u0004\u0000\u0000!"+
		"\"\u0005\u0005\u0000\u0000\"#\u0005\u0011\u0000\u0000#\u0005\u0001\u0000"+
		"\u0000\u0000$%\u0005\u0006\u0000\u0000%&\u0005\u0005\u0000\u0000&\'\u0005"+
		"\u0011\u0000\u0000\'(\u0005\u0007\u0000\u0000()\u0005\u0013\u0000\u0000"+
		")\u0007\u0001\u0000\u0000\u0000*+\u0005\b\u0000\u0000+,\u0003\n\u0005"+
		"\u0000,-\u0005\t\u0000\u0000-.\u0003\f\u0006\u0000.\t\u0001\u0000\u0000"+
		"\u0000/0\u0005\u0012\u0000\u000001\u0005\n\u0000\u000012\u0005\u0012\u0000"+
		"\u000023\u0003\u000e\u0007\u000034\u0003\u0010\b\u00004\u000b\u0001\u0000"+
		"\u0000\u000056\u0005\u000b\u0000\u000067\u0007\u0000\u0000\u000078\u0005"+
		"\u0013\u0000\u00008\r\u0001\u0000\u0000\u00009:\u0007\u0001\u0000\u0000"+
		":\u000f\u0001\u0000\u0000\u0000;<\u0007\u0002\u0000\u0000<\u0011\u0001"+
		"\u0000\u0000\u0000\u0002\u0017\u001e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}