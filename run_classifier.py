import analyzer_pkg.user_analyzer

def run_classifier (user_name, user_description):

	dictionary = analyzer_pkg.user_analyzer.dictionary_parser('analyzer_pkg/language_data/user_dictionary.txt')
	lexicon = analyzer_pkg.user_analyzer.lexicon_generator('analyzer_pkg/language_data/user_grammar.txt', dictionary)
	string_twitter_queries = analyzer_pkg.user_analyzer.string_twitter_queriesParser('analyzer_pkg/language_data/string_twitter_queries.txt')
	
	result = analyzer_pkg.user_analyzer.user_analyzer(
		user_name,
		user_description, 
		string_twitter_queries, 
		lexicon
	)

	return result[1]