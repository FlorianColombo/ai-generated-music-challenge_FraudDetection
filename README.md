#AI generated music challenge | Fraud detection
## A repository containing the analysis of the votes for the Crowd AI challenge on AI music generation.\

Because the organizers observed statistics that did not make any sense during the evaluation. Because we discovered at the end of the contest that the submissions were easily identifiable through a unique identifier. We decided to run this Fraud detection analysis.

In this notebook is presented statistics demonstrating that votes made by several IP addresses were all in favor of only one or a few submissions. In addition, we show that these IP addresses are localized in well defined locations and always in favor of a group of participants.

Votes made by these IP addresses are removed from the pool and the scores are computed according to the updated log.