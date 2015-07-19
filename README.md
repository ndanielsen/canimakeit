#Data Exploration for DDL Incubator Group 4

##Problem

Distill economic data from BLS and various public sources, combined with user input about income and spending to simply answer a simple question: 
 
“Can I make it in this city?”


###Research Questions

Can we make a prediction on if someone can 'make it' if they move to DC (or any other large city)?

What is making it in DC? Can we define making it or is it defined by user preferences?

Does 'making it' require a certain income threshold or budget breakdown for different locations (zip code, neighborhood) depending on the persons gross household income and/or household size?

Can we recommend or predict where the best place is for a person to live based on a combination of their resources, quality of life preferences and other information/ preferences?

What are the strongest dependant variables (ie. costs for housing, grocery or insurance; or perhaps walkability score?) that feed into 'making it' or not? 

Can we predict if 'making it' will change over time due to inflation or other changes in consumer prices?


###Hypothesis

I hypothesize that by using open data sources (open and user-given) and by using widely accepted models for 'making it', we will find that a ratio of housing price to net-income, cost/ease of the work commute, and ability to save are the greatest determinants of making it.    


###Value Proposition

We can give users a realistic picture of the total costs of living in a certain area and give them guidance on if they can make it or not - in short term and long term. 



###Strategy for Analysis

**For the DC Market:**

Segment - Divide and segment publically available consumer expenditure data into demographic groups (young singles under 25 and 25+, married without kids etc)

Location - Break down all data in DC by Ward, Zip code and/or neighboorhood


**Output**

Attempt to create a model (min, mean, max) of consumer purchasing power by segment and location in DC 

With this model, can we complement this model with additional information to give users a more realistic understanding of 'can they make it'?



##Data Sources

**Seed Data**

Bureau of Labor Statistics Data
[Consumer Expenditure (CE) tabular data](http://www.bls.gov/cex/tables.htm)
[CE microdata](http://www.bls.gov/cex/pumdhome.htm)
[Component CPI price indexes by elementary item and area](http://www.bls.gov/cpi/data.htm)

Can we find more data out there on this?

**Complementary Data**

[Craigs List's Apartment Listings](http://washingtondc.craigslist.org/search/apa?)

[Zillow API](http://www.zillow.com/howto/api/APIOverview.htm)


**Data Feature Backlog**

Mint Intergration






##Already Invented Features (To refactor and not reinvent wheels)


###Craigslist

Craigslist Apartment Crawler
[Craig's List Apartment Crawler](https://github.com/Madrox/CraigsLister)

[craigsuck: A Craigslist RSS poller](https://github.com/jbrukh/craigsuck)


###Zillow API

[PyZillow](https://github.com/hanneshapke/pyzillow)



###Mint API
[a screen-scraping API for Mint.com](https://github.com/mrooney/mintapi)