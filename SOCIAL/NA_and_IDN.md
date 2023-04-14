# I have deleted the cases with NA in "if_grp_have_leader".
# I have fixed the mistake that un-consented cases were included in the previous analysis.
# Now with-leader group has a sample size of 101; without-leader of 116; 
# Now none of the items have NAs or "Don't know"s > 6, which is fairly acceptable.
# Results of factor analysis have changed slightly, while the factor structures remained. 
# I did a case-wise check for the NA and "Don't know" (value:6).
# Decisions were made case-wisely. The rule is if the NAs does not contradict 
# the logics of most of the respondent's other answers, the case will be kept and 
# the NAs will be imputed by with-in subgroup item median. 


#All the NAs were found in 3 cases from with-leader sub-group: index 6, 80, 153

## below is the answers of case 153. The respondent reported "the group had one 
## or more informal leader(s) ". Yet, he was not able to give any rating about 
## leader questions. 

## Decisions: This respondent's overall ratings for most items were below average;
## This corresponds to his no idea of leadership quality. It therefore is regarded
## as a reasonable case. The value of leader will be imputed by within-subgroup 
## median. 

Variable Value
index      153
i_leader0   NA
i_leader1   NA
i_leader2   NA
i_leader3   NA
i_skill0     3
i_skill1     2
i_skill2     2
i_skill3     2
i_skill4     4
i_orga0      3
i_orga1      3
i_orga2      4
i_orga3      2
i_orga4      2
i_comm0      4
i_comm1      4
i_comm2      4
i_comm3      2
i_iden0     NA
i_iden1      2
i_iden2      3
i_anom0      3
i_anom1      3
i_anom2      2
i_anom3      2
i_anom4      4


## below is the answers of case 80.  The respondent had one NA (i_anom1). 
## I don't regard it as an issue.  
## Decision: the NA will be imputed by within-subgroup median
Variable Value
index       80
i_leader0    4
i_leader1    4
i_leader2    4
i_leader3    4
i_skill0     4
i_skill1     3
i_skill2     2
i_skill3     2
i_skill4     4
i_orga0      5
i_orga1      2
i_orga2      5
i_orga3      2
i_orga4      5
i_comm0      5
i_comm1      4
i_comm2      3
i_comm3      3
i_iden0      5
i_iden1      4
i_iden2      5
i_anom0      1
i_anom1     NA
i_anom2      3
i_anom3      2
i_anom4      1

## below is the answers of case 6. The respondent had one NA (i_orga3). 
## I don't regard it as an issue.  

## Decision: the NA will be imputed by within-subgroup median

Variable Value
index        6
i_leader0    5
i_leader1    4
i_leader2    4
i_leader3    5
i_skill0     2
i_skill1     3
i_skill2     2
i_skill3     4
i_skill4     5
i_orga0      4
i_orga1      4
i_orga2     NA
i_orga3      2
i_orga4      1
i_comm0      4
i_comm1      5
i_comm2      4
i_comm3      4
i_iden0      4
i_iden1      2
i_iden2      4
i_anom0      1
i_anom1      5
i_anom2      2
i_anom3      4
i_anom4      1


############################################################################### 


#All the NAs were found in 2 cases from without-leader group: index 160 and 200

## below is the answers of case 160.  The respondent had skipped all leader items;
## Meanwhile, he skipped multiple-item organization questions; yet, answered the
## one-item organizaiton question (4 = Agree; positve wording)

## Decision: the respondent gave the lowest possible rating (negative) for these 
## two items: [1] " There was no large gap in avalanche assessment skills between 
## the group members"; [2] " All group members were equipped with standard 
## avalanche safety equipment (beacon, shovel, probe) and trained in the use of it".
## He does not seem to have social desirability bias in skipping the items. Answers
## to other items look pretty logical. The case will be kept and NAs will be imputed
## by within-group median.

Variable Value
index      160
i_leader0   NA
i_leader1   NA
i_leader2   NA
i_leader3   NA
i_skill0     3
i_skill1     2
i_skill2     1
i_skill3     4
i_skill4     1
i_orga0      4
i_orga1     NA
i_orga2     NA
i_orga3     NA
i_orga4     NA
i_comm0      4
i_comm1      4
i_comm2      4
i_comm3      4
i_iden0      4
i_iden1      4
i_iden2      5
i_anom0      1
i_anom1      5
i_anom2      2
i_anom3      1
i_anom4      4

## below is the answers of case 200. He had skipped multiple-item leader questions;
## Yet, he rated the one-item leader question (5 = strongly agree; positve wording)

## Decisions: to be made

index      200
i_leader0    5
i_leader1   NA
i_leader2   NA
i_leader3   NA
i_skill0     5
i_skill1     1
i_skill2     1
i_skill3     4
i_skill4     5
i_orga0      4
i_orga1      4
i_orga2      4
i_orga3      2
i_orga4      1
i_comm0      5
i_comm1      5
i_comm2      5
i_comm3      4
i_iden0      4
i_iden1      4
i_iden2      5
i_anom0     NA
i_anom1      5
i_anom2      4
i_anom3      2
i_anom4      3

############################################################################### 
############################################################################### 
############################################################################### 

#Below is the cases from with-leader group which has at least a "Don't know" (value 6) answer

## (note that the first row is case index number)
## except for case 82, I didn't observe much an issue. Case 82 gave 21 "Don't know" (value 6).

## Case 82 will be deleted. Other "Don't know" will be imputed by with-in subgroup median

                                    (*)
index       31   38   41   56   61   82   91  102  107   110   112   123   170   172   176   179   199   204   227   236   240   243
i_leader0    4    5    5    5    4    6    4    5    4     4     5     5     5     5     5     6     5     4     5     5     4     6
i_leader1    4    4    4    5    4    6    5    6    4     4     3     4     4     5     5     4     5     3     3     5     5     5
i_leader2    3    5    5    5    4    6    5    5    4     3     4     4     3     5     5     5     5     4     5     5     6     5
i_leader3    4    5    5    5    5    6    5    5    5     4     4     5     5     5     5     6     5     4     5     5     4     6
i_skill0     2    4    1    4    6    6    5    5    2     4     2     4     5     4     4     1     5     5     1     4     2     3
i_skill1     3    4    5    2    2    6    1    2    4     2     4     2     1     4     2     5     1     2     5     4     4     3
i_skill2     4    2    5    1    2    6    1    1    3     6     4     2     1     3     1     4     1     2     5     3     4     4
i_skill3     3    4    5    5    1    6    1    5    2     2     2     5     2     2     3     4     1     1     5     3     3     3
i_skill4     4    5    5    5    3    6    4    5    5     3     5     4     5     5     6     5     5     2     5     5     5     5
i_orga0      3    4    5    4    3    1    2    4    4     4     3     2     2     5     2     5     3     4     4     4     4     4
i_orga1      4    4    5    4    3    1    4    2    5     5     2     4     4     2     2     5     2     4     2     3     3     5
i_orga2      4    5    5    4    4    3    2    5    4     5     4     4     5     6     5     5     5     4     4     4     4     5
i_orga3      3    2    3    5    2    2    1    6    5     3     2     3     5     3     5     5     5     2     3     2     4     4
i_orga4      1    3    1    1    2    5    1    1    1     1     5     2     1     5     5     1     5     2     5     2     4     1
i_comm0      4    5    5    5    4    6    4    5    4     4     5     5     5     5     5     5     4     3     5     4     4     5
i_comm1      4    5    5    4    3    6    4    4    4     3     4     4     2     5     3     5     5     4     5     3     4     5
i_comm2      4    4    5    4    4    6    6    5    6     4     6     3     4     5     5     5     5     4     4     4     4     5
i_comm3      3    5    5    6    4    6    2    5    4     3     3     6     6     4     4     5     3     6     5     4     4     5
i_iden0      3    5    5    5    4    6    2    4    5     4     5     4     5     5     4     5     5     4     4     4     4     4
i_iden1      4    3    5    4    2    6    2    3    4     3     2     2     2     5     4     5     5     3     5     4     3     4
i_iden2      4    5    5    5    4    6    6    4    6     4     6     4     5     2     4     5     5     2     5     5     4     5
i_anom0      3    1    1    2    2    6    4    1    6     1     2     1     1     1     1     1     1     6     1     1     2     4
i_anom1      4    5    5    4    4    6    4    4    4     3     6     4     4     5     4     5     4     4     5     6     4     4
i_anom2      4    2    1    2    2    6    2    1    2     2     2     2     1     1     1     1     1     2     2     2     1     1
i_anom3      6    6    1    4    6    6    4    1    4     1     4     2     1     1     1     5     6     2     6     1     1     1
i_anom4      1    1    6    3    4    6    1    1    2     2     1     2     1     1     1     1     1     1     5     1     3     2

############################################################################### 

#Below is the cases from without-leader group which has at least a "Don't know" (value 6) answer

## (note that the first row is case index number)
## I didn't find any strong rowwise or columnwise paatern of "Dont't know".

## Decisions: All "Don't know" will be imputed by with-in subgroup median

index       18   20   46   55   66   77   86   89   93   121   137   141   147   157   163   165   168   183   189   193   201   221   260   264   268   272
i_skill0     4    1    6    2    4    3    1    2    4     5     2     4     2     2     3     4     3     6     4     2     4     1     3     2     3     4
i_skill1     2    5    4    4    2    5    4    4    2     1     4     2     3     2     4     4     2     5     2     4     3     5     3     4     4     2
i_skill2     2    4    4    3    4    2    5    4    2     1     5     1     4     2     4     3     3     5     2     3     4     5     3     2     2     2
i_skill3     2    5    3    5    5    4    5    5    4     4     5     2     4     4     2     5     2     5     2     2     3     5     2     2     5     2
i_skill4     4    5    4    5    3    5    5    5    2     4     5     2     5     5     3     5     1     5     4     4     6     5     2     5     5     5
i_orga0      4    4    4    5    3    5    4    5    4     4     4     4     5     2     4     3     3     4     3     4     4     5     4     4     4     4
i_orga1      2    4    3    5    1    2    5    3    4     2     4     4     5     4     4     5     4     5     4     3     2     5     4     4     5     3
i_orga2      4    5    4    5    4    5    5    5    4     4     3     5     4     4     4     5     5     5     4     6     3     5     4     4     5     5
i_orga3      2    3    6    6    1    6    3    3    2     2     3     2     4     5     3     2     4     1     2     2     1     3     3     6     6     5
i_orga4      5    1    4    1    5    1    1    4    1     5     2     1     1     4     1     1     2     1     1     1     4     6     2     1     1     4
i_comm0      5    5    4    5    2    5    3    5    4     4     4     3     4     5     4     3     4     5     2     4     4     5     4     5     4     4
i_comm1      4    4    4    5    1    2    2    5    4     5     4     4     4     3     5     4     3     5     4     3     5     5     4     5     4     4
i_comm2      6    5    4    5    2    5    4    5    4     5     4     3     5     4     3     4     5     5     3     4     5     5     4     5     5     6
i_comm3      6    5    6    5    2    3    2    5    6     4     4     6     4     5     6     2     4     5     6     4     4     5     6     4     4     4
i_iden0      4    5    4    5    1    5    4    5    4     4     4     4     5     4     3     4     3     4     3     4     3     5     4     5     4     5
i_iden1      2    4    2    4    2    5    4    4    2     4     4     4     5     2     4     4     3     2     2     2     3     3     4     2     3     2
i_iden2      4    5    4    4    1    5    2    5    4     4     4     4     5     4     4     4     5     5     6     4     4     5     4     4     4     5
i_anom0      2    1    2    1    5    1    6    1    2     3     2     2     1     2     3     6     3     1     3     6     2     1     2     1     1     1
i_anom1      3    4    4    5    6    5    3    4    4     4     4     6     6     6     4     6     6     5     6     4     5     5     4     4     5     4
i_anom2      1    1    2    1    6    1    2    2    2     2     6     2     2     1     2     2     2     1     2     2     2     1     2     2     1     2
i_anom3      1    6    2    1    3    1    1    1    1     6     2     1     1     5     3     1     1     1     1     1     1     1     2     2     1     1
i_anom4      1    3    4    1    5    1    1    6    4     1     2     1     1     1     5     5     4     2     1     4     1     1     2     2     1     4





