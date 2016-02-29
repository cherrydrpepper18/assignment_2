#Q12 What are the most common violations per borough, 
		#after normalizing for the relative abundance of each violation?
	
	# Step 1: Get overall frequencies
	frequency = df['VIOLATION CODE'].dropna().value_counts()

 	# Step 2: Create a new column that records total frquency

	totalFreq = frequency[df['VIOLATION CODE'].dropna()]
	print totalFreq

	df['normalize'] = df['count']/totalFreq
    '''⬆️⬆️⬆️Here is the problem ⬆️⬆️⬆️'''
	#Create a pivot table with the percentage column and the Boro column
	norm_vioBoro = df[['VIOLATION DESCRIPTION','BORO','normalize']]
	norm_violations = pd.pivot_table(norm_vioBoro,
                         index='VIOLATION DESCRIPTION',
                         columns='BORO',
                         values='normalize',
                         aggfunc=sum, #what do I do with the data if there is a collision
                         fill_value=0) #fill non-existed violation with 0.
	topVio = norm_violations.idxmax()


	#violationFrequency = DataFrame(frequency) #convert it to a data frame
	

	''' Unused code
	#normalized = violations['count'].map(normalize)

	#df['type total'] = df.map(addcol(df,frequency))

	#print df[['VIOLATION DESCRIPTION','type total']]
	
	norm_vioBoro = df[['VIOLATION DESCRIPTION','BORO','count_norm']]

	#print norm_vioBoro['BORO'].sum()
	
	#most = vioBoro['VIOLATION DESCRIPTION'].value_counts()
	#print most[:5]

	mask_missing = (norm_vioBoro['BORO'] == 'Missing')
	norm_vioBoro.ix[mask_missing, 'BORO'] = np.nan # This sets the value to NaN



	
	violations = pd.pivot_table(norm_vioBoro,
                         index='VIOLATION DESCRIPTION',
                         columns='BORO',
                         values='count_norm',
                         aggfunc=sum, #what do I do with the data if there is a collision
                         fill_value=0) #fill non-existed violation with 0.
	
	

	#noise_mask = orig_data['Complaint Type'].map(noisy)

	#violations.div(frequency)
	#print violations[:3]

	#Normalize
def normalize(x,violationFrequency):
	per = float(x/violationFrequency)
	result = '%.2f'%per*100 + '%'
	return result



def addcol(x,frequency):
	if df[df['VIOLATION CODE'] == frequency.index]:
		return frequency.values




	'''