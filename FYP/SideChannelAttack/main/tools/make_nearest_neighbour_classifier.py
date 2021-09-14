#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Goes through all training data, and populates a JSON object with values
and labels corresponding to packet count and Google searched term.
"""

import os

from nearest_neighbour_classify_module import NearestNeighbourClassifier
from pcap_miner import get_total_packet_count


DATA_FOLDER = "TrainData"
JSON_NAME = "nearest_neighbour_classifier.json"

#Declare the classifier
nn_classifier = NearestNeighbourClassifier()

#Train the classifier
for pcap_file in os.listdir(DATA_FOLDER):
	
	if 'uploadfile0' in pcap_file:
		ground_truth = 'uploadfile0'
	elif 'uploadfile1' in pcap_file:
		ground_truth = 'uploadfile1'
	elif 'uploadfile2' in pcap_file:
		ground_truth = 'uploadfile2'
	elif 'uploadfile3' in pcap_file:
		ground_truth = 'uploadfile3'
	elif 'uploadfile4' in pcap_file:
		ground_truth = 'uploadfile4'
	elif 'uploadfile5' in pcap_file:
		ground_truth = 'uploadfile5'
	elif 'uploadfile6' in pcap_file:
		ground_truth = 'uploadfile6'
	elif 'uploadfile7' in pcap_file:
		ground_truth = 'uploadfile7'
	elif 'uploadfile8' in pcap_file:
		ground_truth = 'uploadfile8'
	elif 'uploadfile9' in pcap_file:
		ground_truth = 'uploadfile9'
	
	total_packets = get_total_packet_count("{}/{}".format(DATA_FOLDER, pcap_file))
	nn_classifier.learn(total_packets, ground_truth)


#Save the classifier
nn_classifier.save_learned_data(JSON_NAME)


	

