#This file is an update of the Q6 question and Q11.

#Q6 Plot all non-chain restaurants in each borrough
#Approach: First we created a series that included only borroughs and unique restaurants,we derived this series from 
#the unique restaurant dataframe from problem 2. Then I filtered out all the missing borrough values by dropping them.
#I then created a mask and applied it to the dataframe that we removed the missing values from. So at this point only 
#non_chain restaurants should show. Once applied, the dataframe became a series, so i converted it back to a series so
#that it could be merged. Then i used value counts on the boroughs and plotted it


rest_borrough = uniqueRestaurants[['DBA','BORO']]

#filter number of non-chain restaurant
non_chainMask = (numberOfEach < 2)
non_chain = numberOfEach[non_chainMask]

non_chain_df = DataFrame(non_chain.index)

non_chain_df.columns = ['Restaurants']#name a column in the new dataframe

#here I merge the dataframes and apply the value_counts to it
merged_df = pd.merge(non_chain_df, rest_borrough,\
left_on='Restaurants' , right_on='DBA', suffixes =['_non_chain','_rest'])

#Drop the missing boro
mask_missing = (merged_df['BORO'] == 'Missing')
merged_df.ix[mask_missing, 'BORO'] = np.nan # This sets the value to NaN
	
nonchain_valuecounts = merged_df['BORO'].value_counts()
	
nonchain_valuecounts.plot(kind = "bar")

#vc = non_chain_df["BORO"].value_counts()
#print nonchain_valuecounts
#print rest_borrough

#Q11 What are the most common violations in each borough?
#APPROACH: I first assigned a dummy column to each inspection for counting purpose.
#Then I cleared out the data by substituting all missing BORO with NaN. Finally use pivot table to organize 
#the number of each type of violations by borough and listed the top violation with the function .idxmax().
	
	df['count'] = 1 # dumpy value
	
	vioBoro = df[['VIOLATION DESCRIPTION','BORO','count']]
	
	#most = vioBoro['VIOLATION DESCRIPTION'].value_counts()
	#print most[:5]

	mask_missing = (vioBoro['BORO'] == 'Missing')
	vioBoro.ix[mask_missing, 'BORO'] = np.nan # This sets the value to NaN

	violations = pd.pivot_table(vioBoro,
                         index='VIOLATION DESCRIPTION',
                         columns='BORO',
                         values='count',
                         aggfunc=sum, #what do I do with the data if there is a collision
                         fill_value=0) #fill non-existed violation with 0.
	
	topVio = violations.idxmax()
	

	print topVio