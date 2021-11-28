# D-B-PIC16B-TAX-Project

# Project Proposal

## Repository
[DC&LC Project Repository](https://github.com/CathrynChen8/D-B-PIC16B-TAX-Project)

## Abstract
Our project will focus on the analysis of the tax system in the United States in order to better understand tax systems and related economic conditions in the United States. Through analyzing data among different states in the U.S. with a 40 years time span, we want to know how tax policies influence employment, poverty rate, overall economic growth, and other factors. We will mainly use tax-related datasets from TAXSIM and current population survey data from the US Census Bureau, apply data cleaning and data-related skills to get the data we want, employ statistical and econometric analytical models and finally employ the interactive visualization to make it readable on webpage settings. 


## Planned Deliverables
The final presentation of the project will be in the form of a webpage, with clear and interesting interactive visualization after thorough statistical/economic analysis.

Full success for our project is a clear and useful interactive data visualization webpage that people can use criteria to select the data and graph they want. While traditional economics models focus on maximum utility and revenue, only considering labor supply. We want to create our own criteria that take some potential side-effects of progressive tax systems into account and calculate the optimal taxation using real-life data. The model should be well-developed using linear regression or econometric analysis and contain important and effective criteria that can help us to decide the optimal taxation. 

Partial success is that we developed plotly graphs that contain key data for analysis on the webpage. We calculate optimal taxation using the elasticity from the dataset instead of creating our own criteria and models. We present some notable relationships between tax systems and other selected factors, but not with a full model/regression.

## Resources Required
[NBER Taxsim](http://users.nber.org/~taxsim/) to gain general understanding of tax system and calculate federal and state taxes
This website contains many useful datasets, we highlight some important datasets that we may potentially use:

[Tables of representative households state income tax liability and marginal rates](http://users.nber.org/~taxsim/state-tax-rates)
contain state income tax data and marginal tax rate for the past 40 years

[Elasticity of the Income Tax](http://users.nber.org/~taxsim/elas/) to calculate optimal tax rate under the traditional model

[Maximum State tax rates](http://users.nber.org/~taxsim/state-rates/) contain marginal tax rate for a regression study

[Marginal Tax Rates by Factor Income](http://users.nber.org/~taxsim/marginal-tax-rates) to analyze inequality and calculate the optimal top income tax rate

[CPS](https://www.census.gov/programs-surveys/cps/data/datasets.html) data to access economic conditions in the state and measure income and employment status

## Tools and Skills Required
### Database management
We will first carefully choose and build datasets.
We will use basically the package NumPy, pandas, SQLite to build up our database and do data cleaning and data selection to get the variable we want. 
### Statistical regression
From the database after selection and cleaning, we will analyze the significance of the factor by developing statistical models to decide the criteria we want to build and understand more about the tax system and its potential effect through the process. We will use packages like sklearn and explore other packages for statistical and econometrics analysis.
### Complex visualization
We will use mainly plotly to get the final interactive graph on the webpage.
### Webpage
We will explore other packages that are not mentioned here if necessary.

## What You Will Learn
We will learn concrete skills about how to make advanced interactive graphs based on some criterias and selections. We will also learn more about building up web pages and statistical analysis of large databases. Meanwhile, we will also deepen our understanding of the tax system and economics.


## Risks
Since we will develop the model through learning and exploring data with so many resources available in hand, we may get lost in the sea of knowledge and spend too much time exploring. As a result, we may not have enough time for a desirable webpage presentation.

We neglect the transfers system in our analysis and hence may not obtain a desirable model and accurate results, since transfer systems do have a large impact and it has been changing in the past 40 years.

## Ethics
The tax system is actually complex with so much information needed to be considered. If we can build up a nice visualization and model, then all people who can access or want to understand about tax system will benefit from our webpage, since we provide a novel approach and direct visual presentation that can make it easier for people to know about the effect of the tax system with respect to both economic and their daily lives.

Possible harm may be produced by the bias and error of the model. Without other variables in control, this project should be stopped at the scope of historic data analysis. The conclusion may provide some insights but is not based on rigorous empirical research.

We believe that our webpage can act as an introductory reference to people who access it and provide them with a base, easier, and straight-forward tool to deepen understanding of the effect of different tax systems and probably further evoke interest in public policy. 

Assumptions:
- Providing clear interactive visualization, people will be interested more, explore more, and understand more about the tax system and economic policy.
- The world is a better place when the public get easier access to tools that help them understand policy and know more about the effect the policy brings.

## Tentative Timeline

Week 3-5 
- Research on existing theories and models
- Explore datasets and find suitable data
- Clean data and build draft database
- Build some basic interactive graphs

Week 6-7 
- Build some basic interactive graphs
- Finalize database
- Perform simple existing models
- Develop our own model

Week 8-10
- Optimized the final model and the criteria
- Build up the webpage
- Present our findings and visualizations onto the webpage
