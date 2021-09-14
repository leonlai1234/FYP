#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bayesian_classify_pcap_module import getBayesianStats
from nearest_neighbour_classify_module import getNearestNeighbourStats, getNearestDist

REMAP_BAYES_NN = {}
REMAP_BAYES_NN['classifier__uploadfile0.json'] = 'uploadfile0'
REMAP_BAYES_NN['classifier__uploadfile1.json'] = 'uploadfile1'
REMAP_BAYES_NN['classifier__uploadfile2.json'] = 'uploadfile2'
REMAP_BAYES_NN['classifier__uploadfile3.json'] = 'uploadfile3'
REMAP_BAYES_NN['classifier__uploadfile4.json'] = 'uploadfile4'
REMAP_BAYES_NN['classifier__uploadfile5.json'] = 'uploadfile5'
REMAP_BAYES_NN['classifier__uploadfile6.json'] = 'uploadfile6'
REMAP_BAYES_NN['classifier__uploadfile7.json'] = 'uploadfile7'
REMAP_BAYES_NN['classifier__uploadfile8.json'] = 'uploadfile8'
REMAP_BAYES_NN['classifier__uploadfile9.json'] = 'uploadfile9'

def getBayesianType(PCAP_FILE, classifiers_list):
	
	results_mapping = {}
	
	#Populate results_mapping
	for classifier in classifiers_list:
		results_mapping[classifier] = getBayesianStats(PCAP_FILE, classifier)
		#print "DEBUG {} = {}".format(classifier, results_mapping[classifier][2])
	
	#type_a_test_results = getBayesianStats(PCAP_FILE, TYPE_A_CLASSIFIER)
	#type_b_test_results = getBayesianStats(PCAP_FILE, TYPE_B_CLASSIFIER)
	
	
	#Find the greatest max_probability
	probs = []
	for classifier in classifiers_list:
		probs.append(results_mapping[classifier][0])
	
	max_prob = max(probs)
	
	#Find the classifier(s) that gives this max_probs
	has_max_prob = []
	for classifier in classifiers_list:
		if results_mapping[classifier][0] == max_prob:
			has_max_prob.append(classifier)
	
	#If there is only one element in has_max_prob then this is the predicted result
	if len(has_max_prob) == 1:
		return has_max_prob[0]
	
	#If there are multiple elements then find the one(s) with the highest max count
	max_count = 0
	for classifier in has_max_prob:
		if results_mapping[classifier][1] > max_count:
			max_count = results_mapping[classifier][1]
	
	highest_counts = []
	for classifier in has_max_prob:
		if results_mapping[classifier][1] == max_count:
			highest_counts.append(classifier)
	
	#If there is only one element in highest_counts then this is the predicted result
	if len(highest_counts) == 1:
		return highest_counts[0]
	else:
		return None


def getNearestNeighbourType(PCAP_FILE, classifier_file):
	return getNearestNeighbourStats(PCAP_FILE, classifier_file)


def getHybridClassifierType(PCAP_FILE, bayesian_classifiers_list, nn_classifier_labels, nearest_neighbour_classifier_file):
	bayesian_results_mapping = {}
	nn_results_mapping = {}
	hybrid_results_mapping = {}
	
	#Populate bayesian_results_mapping
	for classifier in bayesian_classifiers_list:
		bayesian_results_mapping[classifier] = getBayesianStats(PCAP_FILE, classifier)
	
	#Debug
	print("<BayesianClassification>")
	for classifier in bayesian_classifiers_list:
		print("\t{} --> {}".format(classifier, bayesian_results_mapping[classifier][0]))
	print("</BayesianClassification>")
	
	#Populate nn_results_mapping
	for classifier in nn_classifier_labels:
		nn_results_mapping[classifier] = getNearestDist(PCAP_FILE, classifier, nearest_neighbour_classifier_file)
	
	#Improve this...
	
	#For now...
	#Get the highest probability from Bayesian classification
	bayesian_choice = getBayesianType(PCAP_FILE, bayesian_classifiers_list)
	
	#Get the highest probability from Nearest Neighbour classification
	print("<NearestNeighbour>")
	for classifier in nn_classifier_labels:
		print("\t{} --> {}".format(classifier, nn_results_mapping[classifier]))
	print("</NearestNeighbour>")
	
	
	print("<Hybrid>")
	for bayes_classifier in bayesian_classifiers_list:
		bayes_prob = bayesian_results_mapping[bayes_classifier][0]
		nn_dist = nn_results_mapping[REMAP_BAYES_NN[bayes_classifier]]
		hybrid_result = float(bayes_prob) / float(nn_dist + 1)
		hybrid_results_mapping[bayes_classifier] = hybrid_result
		print("\t{} --> {}".format(REMAP_BAYES_NN[bayes_classifier], hybrid_result))
	print("</Hybrid>")
	
	max_hybrid_key = None
	max_hybrid_val = None
	for classifier in hybrid_results_mapping:
		if max_hybrid_key is None:
			max_hybrid_key = classifier
		if max_hybrid_val is None:
			max_hybrid_val = hybrid_results_mapping[classifier]
		
		if hybrid_results_mapping[classifier] > max_hybrid_val:
			max_hybrid_key = classifier
			max_hybrid_val = hybrid_results_mapping[classifier]
	
	return max_hybrid_key
	
	
