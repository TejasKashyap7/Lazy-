# Our dictionary
region={

    'North_India':['Haryana','Himachal Pradesh','Punjab','Rajasthan',' Chandigarh','Delhi','Kashmir ','Jammu','Ladakh'],
    'East_India':['Bihar','West Bengal','Bihar','Assam','Arunachal Pradesh','Nagaland','Sikkim ','Tripura'],
    'North_East':['Mizoram','manipur','Meghalaya'],
    'South_India':['Andhra Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu','Telangana','Puducherry','Lakshdweep','Andaman and Nicobar Island'],
    'West_India':['Gujarat','Maharashtra','Goa','Dadar and Nagar haveli','Daman and Diu']
}

# Inputs
#state=input()


#   Region Finder
def region_finder(state):
    '''
    This function is used to define in which area is the state/Union Teratory you are entring is in
    '''
    list_regions=region.keys()
    for regions in list_regions: # region.keys = list of regions
        list_state=region.get(regions)
        if state in list_state:
            return(regions)
        else :
            continue

#print(region_finder(list_regions,state))