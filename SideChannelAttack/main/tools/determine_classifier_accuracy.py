#!/usr/bin/env python
# -*- coding: utf-8 -*-

from genericpath import isfile
import os
import glob

from determine_type_module import getBayesianType, getNearestNeighbourType, getHybridClassifierType

CLASSIFIERS = []
NN_CLASSIFIER_LABELS = []
i = 0

for f in glob.glob('classifier__uploadfile*'):
	CLASSIFIERS.append('classifier__uploadfile' + str(i) + '.json')
	NN_CLASSIFIER_LABELS.append('uploadfile' + str(i))
	i += 1

# CLASSIFIERS = ["classifier__uploadfile0.json","classifier__uploadfile1.json","classifier__uploadfile2.json","classifier__uploadfile3.json","classifier__uploadfile4.json","classifier__uploadfile5.json","classifier__uploadfile6.json"]
DATA_FOLDER = "TestData"

NN_CLASSIFIER = "nearest_neighbour_classifier.json"

# NN_CLASSIFIER_LABELS = ["uploadfile0","uploadfile1","uploadfile2","uploadfile3","uploadfile4","uploadfile5","uploadfile6"]

classifier_stats = {}
for classifier in CLASSIFIERS:
	classifier_stats[classifier] = {"TruePositive": 0, "FalsePositive": 0, "Undetected": 0, "total" : 0}

hybrid_classifier_stats = {}
for classifier in CLASSIFIERS:
	hybrid_classifier_stats[classifier] = {"TruePositive": 0, "FalsePositive": 0, "Undetected": 0, "total" : 0}

nn_classifier_stats = {}
for classifier in NN_CLASSIFIER_LABELS:
	nn_classifier_stats[classifier] = {"TruePositive": 0, "FalsePositive": 0, "Undetected": 0, "total" : 0}

#Test the classifier
for pcap_file in os.listdir(DATA_FOLDER):

	if 'uploadfile0' in pcap_file:
		ground_truth = CLASSIFIERS[0]
	elif 'uploadfile1' in pcap_file:
		ground_truth = CLASSIFIERS[1]
	elif 'uploadfile2' in pcap_file:
		ground_truth = CLASSIFIERS[2]
	elif 'uploadfile3' in pcap_file:
		ground_truth = CLASSIFIERS[3]
	elif 'uploadfile4' in pcap_file:
		ground_truth = CLASSIFIERS[4]
	elif 'uploadfile5' in pcap_file:
		ground_truth = CLASSIFIERS[5]
	elif 'uploadfile6' in pcap_file:
		ground_truth = CLASSIFIERS[6]
	elif 'uploadfile7' in pcap_file:
		ground_truth = CLASSIFIERS[7]
	elif 'uploadfile8' in pcap_file:
		ground_truth = CLASSIFIERS[8]
	elif 'uploadfile9' in pcap_file:
		ground_truth = CLASSIFIERS[9]

	
	#--- BEGIN Bayesian Classifier Tests ---#
	
	test_result = getBayesianType("{}/{}".format(DATA_FOLDER,pcap_file), CLASSIFIERS)
	#test_result = getHybridClassifierType("{}/{}".format(DATA_FOLDER,pcap_file), CLASSIFIERS, NN_CLASSIFIER_LABELS, NN_CLASSIFIER)
	
	for classifier in CLASSIFIERS:
		if ground_truth == classifier:
			#Did the classifier get it right?
			if test_result is None:
				classifier_stats[ground_truth]['Undetected'] = classifier_stats[ground_truth]['Undetected'] + 1
			elif test_result == ground_truth:
				classifier_stats[ground_truth]['TruePositive'] = classifier_stats[ground_truth]['TruePositive'] + 1
			else:
				classifier_stats[ground_truth]['FalsePositive'] = classifier_stats[ground_truth]['FalsePositive'] + 1
			
			classifier_stats[ground_truth]['total'] = classifier_stats[ground_truth]['total'] + 1
	
	# --- END Bayesian Classifier Tests ---#
	
	#--- BEGIN Nearest Neighbour Classifier Tests ---#
	test_result = getNearestNeighbourType("{}/{}".format(DATA_FOLDER,pcap_file),NN_CLASSIFIER)[0]
	#print "NN_TESTRESULT = {}".format(test_result[0])
	for classifier in nn_classifier_stats:
		if ground_truth == "classifier__{}.json".format(classifier):
			#Did the classifier get it right?
			print("Comparing classifier__{}.json to {}".format(test_result, ground_truth))
			if test_result is None:
				nn_classifier_stats[classifier]['Undetected'] = nn_classifier_stats[classifier]['Undetected'] + 1
			elif "classifier__{}.json".format(test_result) == ground_truth:
				nn_classifier_stats[classifier]['TruePositive'] = nn_classifier_stats[classifier]['TruePositive'] + 1
			else:
				nn_classifier_stats[classifier]['FalsePositive'] = nn_classifier_stats[classifier]['FalsePositive'] + 1
			
			nn_classifier_stats[classifier]['total'] = nn_classifier_stats[classifier]['total'] + 1
	#TODO
	
	#--- END Nearest Neighbour Classifier Tests ---#
	
	
	#--- BEGIN Hybrid Classifier Tests ---#
	
	test_result = getHybridClassifierType("{}/{}".format(DATA_FOLDER,pcap_file), CLASSIFIERS, NN_CLASSIFIER_LABELS, NN_CLASSIFIER)
	for classifier in CLASSIFIERS:
		if ground_truth == classifier:
			#Did the classifier get it right?
			if test_result is None:
				hybrid_classifier_stats[ground_truth]['Undetected'] = hybrid_classifier_stats[ground_truth]['Undetected'] + 1
			elif test_result == ground_truth:
				hybrid_classifier_stats[ground_truth]['TruePositive'] = hybrid_classifier_stats[ground_truth]['TruePositive'] + 1
			else:
				hybrid_classifier_stats[ground_truth]['FalsePositive'] = hybrid_classifier_stats[ground_truth]['FalsePositive'] + 1
			
			hybrid_classifier_stats[ground_truth]['total'] = hybrid_classifier_stats[ground_truth]['total'] + 1
	
	#--- END Hybrid Classifier Tests ---#
	
	#print ""	
	print("Tested with {}, should be {}, result was {}".format(pcap_file, ground_truth, test_result))
	print("")
	
	#nn_test_result = getNearestNeighbourType("{}/{}".format(DATA_FOLDER,pcap_file), NN_CLASSIFIER)
	#print "Nearest Neighbour Type was: {}".format(nn_test_result)

print("Bayesian Classifier Performance")
avg_tpr = 0.0
avg_fpr = 0.0
avg_ndr = 0.0
for classifier in classifier_stats:
	avg_tpr += float(classifier_stats[classifier]['TruePositive']) / float(classifier_stats[classifier]['total'])
	avg_fpr += float(classifier_stats[classifier]['FalsePositive']) / float(classifier_stats[classifier]['total'])
	avg_ndr += float(classifier_stats[classifier]['Undetected']) / float(classifier_stats[classifier]['total'])
	print("{}: True Positive rate = {}/{}, False Positive rate = {}/{}, Non-detection rate = {}/{}".format(classifier, classifier_stats[classifier]['TruePositive'], classifier_stats[classifier]['total'], classifier_stats[classifier]['FalsePositive'], classifier_stats[classifier]['total'], classifier_stats[classifier]['Undetected'], classifier_stats[classifier]['total']))
avg_tpr = (avg_tpr / len(classifier_stats)) * 100
avg_fpr = (avg_fpr / len(classifier_stats)) * 100
avg_ndr = (avg_ndr / len(classifier_stats)) * 100
print("Average True Positive rate = {}%".format(avg_tpr))
print("Average False Positive rate = {}%".format(avg_fpr))
print("Average Non-detection rate = {}%".format(avg_ndr))

print("")

avg_tpr = 0.0
avg_fpr = 0.0
avg_ndr = 0.0
print("Nearest Neighbour Classifier Performance")
for classifier in nn_classifier_stats:
	avg_tpr += float(nn_classifier_stats[classifier]['TruePositive']) / float(nn_classifier_stats[classifier]['total'])
	avg_fpr += float(nn_classifier_stats[classifier]['FalsePositive']) / float(nn_classifier_stats[classifier]['total'])
	avg_ndr += float(nn_classifier_stats[classifier]['Undetected']) / float(nn_classifier_stats[classifier]['total'])
	print("{}: True Positive rate = {}/{}, False Positive rate = {}/{}, Non-detection rate = {}/{}".format(classifier, nn_classifier_stats[classifier]['TruePositive'], nn_classifier_stats[classifier]['total'], nn_classifier_stats[classifier]['FalsePositive'], nn_classifier_stats[classifier]['total'], nn_classifier_stats[classifier]['Undetected'], nn_classifier_stats[classifier]['total']))
avg_tpr = (avg_tpr / len(nn_classifier_stats)) * 100
avg_fpr = (avg_fpr / len(nn_classifier_stats)) * 100
avg_ndr = (avg_ndr / len(nn_classifier_stats)) * 100
print("Average True Positive rate = {}%".format(avg_tpr))
print("Average False Positive rate = {}%".format(avg_fpr))
print("Average Non-detection rate = {}%".format(avg_ndr))

print("")

avg_tpr = 0.0
avg_fpr = 0.0
avg_ndr = 0.0
print("Hybrid Classifier Performance")
for classifier in hybrid_classifier_stats:
	avg_tpr += float(hybrid_classifier_stats[classifier]['TruePositive']) / float(hybrid_classifier_stats[classifier]['total'])
	avg_fpr += float(hybrid_classifier_stats[classifier]['FalsePositive']) / float(hybrid_classifier_stats[classifier]['total'])
	print("{}: True Positive rate = {}/{}, False Positive rate = {}/{}, Non-detection rate = {}/{}".format(classifier, hybrid_classifier_stats[classifier]['TruePositive'], hybrid_classifier_stats[classifier]['total'], hybrid_classifier_stats[classifier]['FalsePositive'], hybrid_classifier_stats[classifier]['total'], hybrid_classifier_stats[classifier]['Undetected'], hybrid_classifier_stats[classifier]['total']))
avg_tpr = (avg_tpr / len(hybrid_classifier_stats)) * 100
avg_fpr = (avg_fpr / len(hybrid_classifier_stats)) * 100
avg_ndr = (avg_ndr / len(hybrid_classifier_stats)) * 100
print("Average True Positive rate = {}%".format(avg_tpr))
print("Average False Positive rate = {}%".format(avg_fpr))
print("Average Non-detection rate = {}%".format(avg_ndr))
