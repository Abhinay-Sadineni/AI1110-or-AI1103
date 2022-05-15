#code by sadineni abhinay
#cs21btech11055

#probabilities for A,B
P_A =(6.0/11)
P_B =(5.0/11)
P_AUB =(7.0/11)

#probability to occuring both events at same time
P_AB= P_A + P_B - P_AUB

#probability of  occurrence of A when B occurs
P_AGB =(P_AB/P_B)
#probability of  occurrence of B when A occurs
P_BGA =(P_AB/P_A)

print("probability to occuring both events is ",P_AB)
print("probability of  occurrence of A when B occurs ",P_AGB)
print("probability of  occurrence of B when A occurs ",P_BGA)

#end