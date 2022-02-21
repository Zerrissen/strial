import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
from pyfiglet import Figlet # pip install pyfiglet
from colorama import init # pip install colorama
from os import system

############
#Print Menu#
############
def printMenu():
    system("cls")
    f = Figlet(font="big")
    print(f"{MAGENTA}"+f.renderText("STrial"))
    print("v1.0.0\nCreated by Nathan Hines")
    print(f"{RED}\nTHIS IS CURRENTLY A WORK IN PROGRESS")
    print(f"{RED}TRIAL COMPLETION CRITERIA IS LIMITED TO:")
    print(f"{RED}ALL OUTCOMES OCCURING ONCE {WHITE}or{RED} REACHING MAX TRIAL FREQUENCY\n")
    print(f"{YELLOW}THIS PROGRAM WAS MADE FOR STATISTICAL USE. IF YOU ARE UNAWARE OF HOW TO USE THIS PROGRAM OR WANT DOCUMENTATION, VISIT:{WHITE} ")

#######Constants#########
# Colors for print
WHITE = "\x1b[1;37;40m"
GREEN = "\x1b[1;32;40m"
YELLOW = "\x1b[1;33;40m"
RED = "\x1b[1;31;40m"
MAGENTA = "\x1b[1;35;40m"
init(autoreset=True)
printMenu()

#######Inputs#########
# Outside createOutcomes() as unchanged (no point using global)
print(f"\n[{GREEN}+{WHITE}] How many trials do you want to run?\n{YELLOW}Input: ", end="")
trialCount = int(input())
print(f"\n[{GREEN}+{WHITE}] What is the maximum outcome frequency?\n{YELLOW}Input: ", end="")
frequencyCount = int(input())
print(f"\n[{GREEN}+{WHITE}] How many outcomes are there?\n{YELLOW}Input: ", end="")
outcomeCount = int(input())

#######Integers#########
currentTrial = 0
successCount = 0 # Globally accessed
totalFreq = 0 # Globally accessed

#######Arrays#########
outcomeNames = [] # Stores names of possible outcomes
outcomeProbabilities = [] # Stores chances of outcomes occuring
outcomes = [] # Stores resulting outcomes from trial
trialFreqArr = [] # Stores no. of times outcome has occured

########################################
#Name all outcomes/assign probabilities#
########################################
def createOutcomes(outcomeCount, outcomeNames, outcomeProbabilities, trialFreqArr):
	while True: # Continues to loop until current input given
		try:
			print(f"\n[{GREEN}+{WHITE}] What do you want to call the " + str(outcomeCount) + f" outcomes?\n[{GREEN}+{WHITE}] Please separate with spaces.\n{YELLOW}Input: ", end="")
			names = input()
			names = names.split()
		except ValueError: # Incase input cannot be parsed
			print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}Invalid input. Try again.")
		if len(names) < outcomeCount:
			print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}not enough outcomes given. Please try again.\n{RED}[-] Required: {WHITE}" + str(outcomeCount) + f"\n[{RED}-{WHITE}] Given: {WHITE}" + str(len(names)))
			continue # Restart the loop
		elif len(names) > outcomeCount:
			print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}too many outcomes given. Please try again.\n{RED}[-] Required: {WHITE}" + str(outcomeCount) + f"\n[{RED}-{WHITE}] Given: {WHITE}" + str(len(names)))
			continue # Restart the loop
		else:
			break # Stop the loop
	for i in names:
		outcomeNames.append(i)
		trialFreqArr.append(0)

	countProb = float(0) # Current probability total
	probLeft = float(1) # Probability amount left
	while probLeft > 0: # Total prob must be 1
		for i in range(len(outcomeNames)):
			if i == len(outcomeNames)-1: # Auto assign last prob, reduces error potential
				print(f"[{GREEN}+{WHITE}] Auto assigning remain probability.")
				outcomeProbabilities.append(probLeft)
				countProb += probLeft
				probLeft -= probLeft
			else: # Choose your own probs for outcomes
				while True:
					try:
						print(f"\n[{GREEN}+{WHITE}] What probability would you like to assign to outcome " + str(outcomeNames[i]) + f"?\n[{GREEN}+{WHITE}] Max probability: " + str(probLeft) + f"\n{YELLOW}Input: ", end="")
						askProb = float(input())
					except ValueError:
						print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}Invalid input. Try again.")
						continue # Restart the loop
					if askProb < 0:
						print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}Input less than 0. Try again.")
						continue # Restart the loop
					elif askProb >= probLeft:
						print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}Input too high. Try again.")
						continue # Restart the loop
					elif askProb == 0:
						print(f"[{RED}-{WHITE}] {RED}Error: {WHITE}Input cannot equal 0. Try again.")
						continue # Restart the loop
					else:
						break # Stop the loop
				countProb = float(countProb) + askProb
				probLeft -= askProb
				outcomeProbabilities.append(askProb)
	return outcomeNames

######################
#Run individual trial#
######################
def runTrials(outcomes, frequencyCount, outcomeNames, outcomeProbabilities, trialFreqArr):
	currentFreq = 0
	global successCount
	global totalFreq
	outcomes = []
	while currentFreq < frequencyCount:
		i = np.intersect1d(outcomeNames, outcomes)
		if len(i) < 5:
			addOutcome = np.random.choice(a=outcomeNames, p=outcomeProbabilities)
			outcomes.append(addOutcome)
		currentFreq += 1
	if len(i) == 5:
		successCount += 1
	totalFreq += len(outcomes)
	trialFreq = len(outcomes)
	print(f"[{GREEN}+{WHITE}] Trial Frequency: {WHITE}" + str(trialFreq))

	for i in range(len(outcomeNames)):
		outcomeOccuranceCount = outcomes.count(outcomeNames[i])
		print(f"[{GREEN}+{WHITE}] Times " + outcomeNames[i] + f" occurs: {WHITE}" + str(outcomeOccuranceCount))
		trialFreqArr[i] = trialFreqArr[i] + outcomeOccuranceCount
	system("cls")
	#print(f"{GREEN}"+str(trialFreqArr))

########################################
#Process data collected from all trials#
########################################
def processData(outcomeNames, trialFreqArr, trialCount):
	global totalFreq
	print(f"[{GREEN}+{WHITE}] There is a " + str(successCount) + f"{GREEN}/{WHITE}" + str(trialCount) + " chance of meeting criteria.")
	plt.figure(1) # Bar graph
	plt.bar(outcomeNames, trialFreqArr)
	plt.title("Occurrences of Outcomes")
	plt.ylabel("No. of Occurrences")
	plt.xlabel("Outcomes")

	plt.figure(2) # Bar graph
	plt.bar(("Success", "Failure"), (successCount, trialCount-successCount))
	plt.title("Number of Successes vs Failures")
	plt.ylabel("No. of Successes")

	successPercent = successCount / trialCount * 100
	failurePercent = 100 - successPercent
	percentages = [successPercent, failurePercent]
	plt.figure(3) # Pie chart
	plt.pie(percentages, labels=["Success","Failure"], autopct='%1.1f%%')

	mean = totalFreq/trialCount # Mean number of generated numbers before trial complete
	print(f"[{GREEN}+{WHITE}] Mean: {WHITE}" + str(mean))

	plt.show()

if __name__ == '__main__':
	createOutcomes(outcomeCount, outcomeNames, outcomeProbabilities, trialFreqArr)
	while currentTrial < trialCount:
		runTrials(outcomes, frequencyCount, outcomeNames, outcomeProbabilities, trialFreqArr)
		currentTrial += 1
	processData(outcomeNames, trialFreqArr, trialCount)
	system("pause")